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
import hashlib
from pprint import pprint
import difflib

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
    # return md5.digest()
    f.seek(0)
    return md5.hexdigest()

# rips out the temp directory and plugin directory leaving the info we want
def segmentPath(path):
    segments = splitpath(path)
    goodsegments = None
    for i, v in enumerate(segments):
        if 'sublime-ftp-plugin' in v:
            goodsegments = segments[i+1:]
            break
    return goodsegments

connections = {}

class FtpConnectCommand(sublime_plugin.WindowCommand):
    def run(self):

        self.servers = []

        sublime.set_timeout(lambda: self.window.show_quick_panel(self.getServers(), self.menuAction), 1)

    def menuAction(self, index):
        if index == -1:
            return

        if index == 0:
            self.window.run_command('ftp_create_server')
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
    def run(self, server=None, stop_at_connect=False):

        startup_path = None

        if server == None:
            current_file_path = self.window.active_view().file_name()

            datapath = segmentPath(os.path.dirname(current_file_path))

            if datapath != None:
                try:
                    server = datapath[:1][0]
                    startup_path = os.path.join(*(datapath[1:]))
                except Exception:
                    print('error setting starup path, defaulting to nothing')
                    return
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

        self.current_path = None
        self.current_attrs = None

        # sublime.status_message('Establishing connection to %s' % self.site);

        sublime.status_message('Connected to %s' % self.conn['server']);

        if stop_at_connect == True:
            return False

        ftplist = self.find(startup_path if startup_path != None else '');

    def find(self, path, attrs=None):

        self.current_path = path
        self.current_attrs = attrs

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

            if index == 0:
                return self.goto()

            if index == 1:
                return self.folder_actions()

            [name, attrs] = items[index];
            #pprint({'name': name, 'attrs': attrs, 'index': index})
            if name == '..':
                return this.find(os.path.dirname(attrs['parent']))
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

        fh.close()

        sublime.set_timeout(lambda: sublime.active_window().open_file(temppath), 1)

    def goto(self):
        pass

    def file_actions(self):
        menu = [u'\u2022 Back', u'\u2022 Edit', u'\u2022 Rename', u'\u2022 Chmod', u'\u2022 Delete']
        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action), 1)

    def folder_actions(self):

        def action(index):
            if index == 1:
                self.find(self.current_path, self.current_attrs)

        path = os.path.join(self.current_attrs['parent'] if self.current_attrs != None and 'parent' in self.current_attrs else '', self.current_path)

        menu = ['%s:/%s' % (self.conn['config']['host'], path), u'\u2022 Back', u'\u2022 New File', u'\u2022 New Folder', u'\u2022 Rename', u'\u2022 Chmod', u'\u2022 Delete']
        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action), 1)

class RemoteSync(sublime_plugin.EventListener):

    # needs to check connection before attempting to store the binary
    def on_post_save_async(self, view):
        filepath = view.file_name()

        datapath = segmentPath(filepath)

        site = None

        try:
            site = datapath[:1][0]
            realpath = os.path.join(*(datapath[1:]))
        except Exception:
            # remove this message
            # print('error saving file on save, realpath could not be found')
            return None

        fh = open(filepath, 'rb')

        view.window().run_command('ftp_browse', {'server': site, 'stop_at_connect': True})

        if site in connections:

            local_md5_hash = view.settings().get('hash', False)

            tempfh = tempfile.SpooledTemporaryFile(1024*1024*5) #5MB file before writing to disk
            connections[site]['ftp'].retrbinary('RETR %s' % realpath, tempfh.write)

            tempfh.seek(0)

            remote_md5_hash = md5_for_file(tempfh)

            def action(index):
                if index == 0: # confirm overite
                    new_md5_hash = md5_for_file(fh)
                    # print('hash for %s created: %s' % (filepath, new_md5_hash))
                    view.settings().set('hash', new_md5_hash)
                    connections[site]['ftp'].storbinary('STOR %s' % realpath, fh)
                    # print('file saved')
                    print('upload complete')
                elif index == 2: # show diff of new and old file
                    def convert(s):
                        return s.decode('ascii')

                    def setnewlines(s):
                        return s.strip('\n') + '\n'

                    diff = difflib.unified_diff(list(map(convert, tempfh.readlines())), list(map(convert, fh.readlines())), 'remote', 'local')
                    diff = ''.join([setnewlines(str(x)) for x in diff])
                    view.window().run_command('ftp_create_buffer', {'name': '%s.diff' % os.path.basename(filepath), 'data': diff, 'syntax': 'Packages/Diff/Diff.tmLanguage'})
                    print('showing diff')
                else:
                    print('save operation aborted')

                tempfh.close()
                fh.close()

            menu_overwrite = ['Overwrite Remote File', 'The file on the server has changed since first download']
            menu_cancel = ['Cancel', 'Abort this operation, no changes will be uploaded']
            menu_diff = ['Diff With Remote File', 'Show changes between this file and the remote one']

            print('comparing hashes on server(%s) to local(%s)' % (remote_md5_hash, local_md5_hash))

            if remote_md5_hash != local_md5_hash:
                sublime.set_timeout(lambda: view.window().show_quick_panel([menu_overwrite, menu_cancel, menu_diff], action), 1)
            else:
                action(0)

    def on_load_async(self, view):
        path = view.file_name()
        datapath = segmentPath(path)
        site = None

        try:
            site = datapath[:1][0]
            realpath = os.path.join(*(datapath[1:]))
        except Exception:
            # remove this message
            # print('error saving file on save, realpath could not be found')
            return None

        view.window().run_command('ftp_browse', {'server': site, 'stop_at_connect': True})

        if site in connections:
            fh = open(path, 'rb')
            md5_hash = md5_for_file(fh)
            fh.close()
            print('hash for %s created: %s' % (path, md5_hash))
            view.settings().set('hash', md5_hash)


class FtpReadmeCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open("http://git.bluechipdigital.com/blue-chip/sublime-ftp-plugin", 2, True)

class FtpEditServerCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.ok_cancel_dialog('edit server')

class FtpDeleteServerCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.ok_cancel_dialog('delete server')

class FtpCreateServerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        new_file = sublime.active_window().new_file()
        new_file.set_name('untitled')
        new_file.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')
        f = open(os.path.join(sublime.packages_path(), 'FTP', 'FTP.default-config'), 'r')
        new_file.insert(edit, 0, f.read())
        f.close()
        new_file.sel().clear()
        new_file.sel().add(sublime.Region(0))

class FtpCreateBufferCommand(sublime_plugin.TextCommand):
    def run(self, edit, name='untitled', data='', syntax=''):
        new_file = sublime.active_window().new_file()
        new_file.set_name(name)
        new_file.set_syntax_file(syntax)
        new_file.insert(edit, 0, data)
        new_file.sel().clear()
        new_file.sel().add(sublime.Region(0))

# example thread class, not used
# class PrefixrApiCall(threading.Thread):
#     def __init__(self, sel, string, timeout):
#         self.sel = sel
#         self.original = string
#         self.timeout = timeout
#         self.result = None
#         threading.Thread.__init__(self)