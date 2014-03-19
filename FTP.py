import sublime
import sublime_plugin
import ftplib
import webbrowser
import threading
import urllib
import os
import tempfile
import datetime
import json
import os
import sys
from pprint import pprint



def splitpath(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

def md5_for_file(f, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.digest()

# rips out the temp directory and plugin directory leaving the info we want
def segmentPath(path):
    segments = splitpath(path)
    goodsegments = None
    for i, v in enumerate(segments):
        if 'sublime-ftp-plugin' in v:
            goodsegments = segments[i+1:]
            break
    return goodsegments

def dump(obj):
    '''return a printable representation of an object for debugging'''
    newobj=obj
    if '__dict__' in dir(obj):
        newobj=obj.__dict__
        if ' object at ' in str(obj) and not newobj.has_key('__type__'):
            newobj['__type__']=str(obj)
        for attr in newobj:
            newobj[attr]=dump(newobj[attr])
    pprint(newobj)

connections = {}

class FtpConnectCommand(sublime_plugin.WindowCommand):
    def run(self):

        self.servers = []

        sublime.set_timeout(lambda: self.window.show_quick_panel(self.getServers(), self.menuAction), 1)

    def menuAction(self, index):
        if index == -1:
            return

        if index == 0:
            self.window.run_command('ftp_new_server_config')
            return

        self.window.run_command('ftp_browse', {'server': self.servers[index][0]})

    def getServers(self):

        configPath = os.path.join(sublime.packages_path(), 'User', 'sftp_servers')

        configFiles = os.listdir(configPath)

        self.servers.append(['Setup New Server...', 'Opens a config template for a new server'])

        for name in configFiles:
            server = os.path.join(configPath, name)
            json_data = open(server)
            data = sublime.decode_value(json_data.read())
            json_data.close()

            self.servers.append([name, '%s://%s@%s:%s' % (data['type'].lower(), data['user'], data['host'], data['port'] if 'port' in data else 21)])

        return self.servers


class FtpBrowseCommand(sublime_plugin.WindowCommand):
    def run(self, server=None):

        startup_path = None

        if server == None:
            current_file_path = self.window.active_view().file_name()

            datapath = segmentPath(os.path.dirname(current_file_path))

            if datapath != None:
                server = datapath[:1][0]
                try:
                    startup_path = os.path.join(*(datapath[1:]))
                except Exception:
                    print('error setting starup path, defaulting to nothing')
            else:
                return self.window.run_command('ftp_connect')

        if server not in connections:
            configFile = os.path.join(sublime.packages_path(), 'User', 'sftp_servers', server)

            try:
                json_data = open(configFile)
            except Exception:
                print('there was an error opening the config file: %s' % configFile)
                return

            configData = sublime.decode_value(json_data.read())
            json_data.close()

            configObj = {}

            configObj['server'] = server
            configObj['config'] = configData

            configObj['ftp'] = ftplib.FTP()
            configObj['ftp'].connect(configData['host'], int(configData['port'] if 'port' in configData else 21))
            configObj['ftp'].login(configData['user'], configData['password'])

            connections[server] = configObj

        self.conn = connections[server]

        # sublime.status_message('Establishing connection to %s' % self.site);

        sublime.status_message('Connected to %s' % self.conn['server']);

        ftplist = self.find(startup_path if startup_path != None else '');

    def find(self, path, attrs=None):

        path = os.path.join(attrs['parent'] if attrs != None and 'parent' in attrs else '', path)
        pprint(['DEBUG: finding', path, attrs])

        if attrs != None and 'action' in attrs:
            if attrs['action'] == 'goto':
                print('show goto panel')
            if attrs['action'] == 'options':
                print('show options')
            return

        if attrs and attrs['type'] != 'dir':
            return self.download(path, attrs)

        ftplist = self.conn['ftp'].mlsd(path, ["type", "size", "perm"])

        menu = []
        items = []

        # special menu items
        menu.append('%s:/%s' % (self.conn['config']['host'], path))
        items.append(['goto', {'action': 'goto'}])
        menu.append(u'\u2022 Folder actions')
        items.append(['options', {'action': 'options'}])

        for [name, attrs] in ftplist:
            attrs['parent'] = path
            if name != '.':
                if (path == '/' or path == '') and name == '..':
                    continue

                if attrs['type'] == 'dir' and name != '..':
                    name = name + '/'
                menu.append('  ' + name)
                items.append([name, attrs])

        this = self

        def action(index):
            if index == -1:
                return

            [name, attrs] = items[index];
            #pprint({'name': name, 'attrs': attrs, 'index': index})
            if name == '..':
                return this.find(os.path.basename(attrs['parent']))
            this.find(name, attrs)

        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action), 1)

    def download(self, path, attrs):
        pprint('downloading %s' % path)
        name = os.path.basename(path)

        temppath = os.path.join(tempfile.mkdtemp('-sublime-ftp-plugin'), self.conn['server'], attrs['parent'])

        os.makedirs(temppath, 0o777, True)

        temppath = os.path.join(temppath, name)

        fh = open(temppath, 'wb')
        self.conn['ftp'].retrbinary('RETR %s' % path, fh.write)

        sublime.set_timeout(lambda: sublime.active_window().open_file(temppath), 1)


class RemoteSync(sublime_plugin.EventListener):

    # needs to check connection before attempting to store the binary
    def on_post_save(self, view):
        filepath = view.file_name()

        datapath = segmentPath(filepath)

        site = datapath[:1][0]

        try:
            realpath = os.path.join(*(datapath[1:]))
        except Exception:
            print('error saving file on save')
            return None

        fh = open(filepath, 'rb')

        if site in connections:
            connections[site]['ftp'].storbinary('STOR %s' % realpath, fh)
            pprint('file saved')
        else:
            pprint('file being saved does not belong to a site')

class FtpReadmeCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open("http://git.bluechipdigital.com/blue-chip/sublime-ftp-plugin", 2, True)

# sample class, not used
class PrefixrApiCall(threading.Thread):

    def __init__(self, sel, string, timeout):
        self.sel = sel
        self.original = string
        self.timeout = timeout
        self.result = None
        threading.Thread.__init__(self)

class FtpNewServerConfigCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        new_file = sublime.active_window().new_file()
        new_file.set_name('untitled')
        new_file.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')

        new_config = """{
    // sftp, ftp or ftps
    "type": "sftp",

    // hostname or ip address
    "host": "example.com",

    // user and password credentials
    "user": "username",
    "password": "password",

    // optional port, default is 21
    //"port": "21",

    // startup path, defailt is /
    //"remote_path": "/public_html",

    // permissions for new files/directories
    //"file_permissions": "664",
    //"dir_permissions": "775",

    // seconds to wait before aborting
    //"connect_timeout": 30,

    // some other optional options

    //"keepalive": 120,
    //"ftp_passive_mode": true,
}"""

        new_file.insert(edit, 0, new_config)
        new_file.sel().clear()
        new_file.sel().add(sublime.Region(0))