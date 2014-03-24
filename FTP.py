import sublime
import sublime_plugin
import ftplib
import webbrowser
import threading
import urllib
import os
import tempfile
import datetime
import time
import json
import os
import sys
import hashlib
from pprint import pprint
import difflib

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

def debug(message):
    if debug_enabled:
        print('[%s][FTP.DEBUG]: %s' % (time.strftime('%Y-%m-%dT%H:%M:%S'), message))


debug_enabled = True
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
            if name[:1] == '.':
                continue
            server = os.path.join(configPath, name)
            try:
                serverConfigFile = open(server)
                data = sublime.decode_value(serverConfigFile.read())
                serverConfigFile.close()
            except Exception as e:
                debug('could not load config file(%s): %s' % (server, e))
                continue

            self.servers.append([name, '%s://%s@%s:%s' % (data['type'].lower(), data['user'], data['host'], data['port'] if 'port' in data else 21)])

        return self.servers


class FtpBrowseCommand(sublime_plugin.WindowCommand):
    def run(self, server=None, stop_at_connect=False):

        startup_path = None

        if server == None:
            current_view = self.window.active_view()
            current_view_settings = current_view.settings()

            if not current_view_settings.has('ftp_site'):
                return self.window.run_command('ftp_connect')

            server = current_view_settings.get('ftp_site')
            startup_path = os.path.dirname(current_view_settings.get('ftp_path'))

        if server not in connections:
            configFile = os.path.join(sublime.packages_path(), 'User', 'sftp_servers', server)

            try:
                with open(configFile) as f:
                    configData = sublime.decode_value(f.read())
            except Exception:
                debug('there was an error opening the config file: %s' % configFile)
                return

            configObj = {'server': server, 'config': configData, 'ftp': ftplib.FTP()}

            configObj['ftp'].connect(configData['host'], int(configData['port'] if 'port' in configData else 21))
            configObj['ftp'].login(configData['user'], configData['password'])

            connections[server] = configObj

        self.conn = connections[server]

        self.current_path = None
        self.current_attrs = None

        sublime.status_message('Connected to %s' % self.conn['server']);

        if stop_at_connect == True:
            return

        self.find(startup_path if startup_path != None else '');

    def find(self, path, attrs=None):

        self.current_path = path
        self.current_attrs = attrs

        path = os.path.join(attrs['parent'] if attrs != None and 'parent' in attrs else '', path)

        debug('retrieving path: %s attrs %s' % (path, attrs))

        if attrs != None and 'action' in attrs:
            if attrs['action'] == 'goto':
                print('show goto panel')
            if attrs['action'] == 'options':
                print('show options')
            return

        if attrs and attrs['type'] != 'dir':
            return self.file_actions(path, attrs)
            #return self.download(path, attrs)

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
            elif index == 0:
                return self.goto()
            elif index == 1:
                return self.folder_actions()

            [name, attrs] = items[index];
            if name == '..':
                return this.find(os.path.dirname(attrs['parent']))
            this.find(name, attrs)

        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action), 1)

    def download(self, path, attrs):
        debug('downloading remote file from quick panel: %s' % path)
        name = os.path.basename(path)
        local_path = os.path.join(tempfile.mkdtemp('-sublime-ftp'), self.conn['server'], attrs['parent'])
        os.makedirs(local_path, 0o777, True)
        local_path = os.path.join(local_path, name)

        with open(local_path, 'wb') as f:
            self.conn['ftp'].retrbinary('RETR %s' % path, f.write)

        new_view = sublime.active_window().open_file(local_path)
        view_settings = new_view.settings()
        view_settings.set('ftp_path', path)
        view_settings.set('ftp_site', self.conn['server'])
        # sublime.set_timeout(lambda: , 1)

    def goto(self):
        pass

    def file_actions(self, path, attrs):
        this = self
        def action(index):
            if index == -1:#exit
                return
            elif index == 2:#download
                return this.download(path, attrs)
            elif index == 3:#rename
                pass
            elif index == 4:#chmod
                pass
            elif index == 5:#delete(with confirm)
                pass
            else: # return back
                return this.find(os.path.dirname(attrs['parent']))

        path = os.path.join(self.current_attrs['parent'] if self.current_attrs != None and 'parent' in self.current_attrs else '', self.current_path)

        menu = ['%s:/%s' % (self.conn['config']['host'], path), u'\u2022 Back', u'\u2022 Edit', u'\u2022 Rename', u'\u2022 Chmod', u'\u2022 Delete']
        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action, selected_index=2), 1)

    def folder_actions(self):

        def action(index):
            if index == 1:
                self.find(self.current_path, self.current_attrs)

        path = os.path.join(self.current_attrs['parent'] if self.current_attrs != None and 'parent' in self.current_attrs else '', self.current_path)

        menu = ['%s:/%s' % (self.conn['config']['host'], path), u'\u2022 Back', u'\u2022 New File', u'\u2022 New Folder', u'\u2022 Rename', u'\u2022 Chmod', u'\u2022 Delete']
        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action), 1)

class RemoteSync(sublime_plugin.EventListener):
    def on_post_save_async(self, view):
        view_settings = view.settings()
        if not view_settings.has('ftp_site'):
            return

        site = view_settings.get('ftp_site', False)

        # (re)connect to the remote server so we can save quickly
        # TODO: use some type of connection manager class, this seems really hacky :S
        view.window().run_command('ftp_browse', {'server': site, 'stop_at_connect': True})

        if site in connections:
            local_file_path = view.file_name()
            local_md5_hash = view_settings.get('ftp_hash', False)
            remote_file_path = view_settings.get('ftp_path')

            # should check if the user even wants to compare hashes, because then we dont need this check
            # TODO: check user configurable option for overwrite protection
            # TODO: also needs to check if file even still exists
            tmp = tempfile.SpooledTemporaryFile(1024**2*5) # 5MB file before writing to disk
            connections[site]['ftp'].retrbinary('RETR %s' % remote_file_path, tmp.write)
            tmp.seek(0)
            remote_md5_hash = md5_for_file(tmp)

            f = open(local_file_path, 'rb')

            def action(index):
                if index == 0: # confirm overite
                    view.settings().set('ftp_hash', md5_for_file(f))
                    connections[site]['ftp'].storbinary('STOR %s' % remote_file_path, f)
                    debug('uploading file complete: local(%s) remote(%s)' % (local_file_path, remote_file_path))
                elif index == 2: # show diff of new and old file
                    def decode(s):
                        return s.decode('ascii')
                    def resetlines(s):
                        return s.strip('\n') + '\n'

                    diff = difflib.unified_diff(list(map(decode, tmp.readlines())), list(map(decode, f.readlines())), 'remote', 'local')
                    view.window().run_command('ftp_create_buffer', {'name': '%s.diff' % os.path.basename(local_file_path), 'data': ''.join([resetlines(str(x)) for x in diff]), 'syntax': 'Packages/Diff/Diff.tmLanguage'})
                    debug('displaying diff file for %s' % local_file_path)
                else:
                    debug('save operation aborted for %s' % local_file_path)

                tmp.close()
                f.close()

            menu_overwrite = ['Overwrite Remote File', 'The file on the server has changed since first download']
            menu_cancel = ['Cancel', 'Abort this operation, no changes will be uploaded']
            menu_diff = ['Diff With Remote File', 'Show changes between this file and the remote one']

            debug('comparing hashes on remote(%s) to local(%s)' % (remote_md5_hash, local_md5_hash))

            if remote_md5_hash != local_md5_hash:
                sublime.set_timeout(lambda: view.window().show_quick_panel([menu_overwrite, menu_cancel, menu_diff], action), 1)
            else:
                action(0)

    def on_load_async(self, view):
        view_settings = view.settings()
        if not view_settings.has('ftp_site'):
            return

        path = view.file_name()
        site = view_settings.get('ftp_site')

        # (re)connect to the remote server so we can save quickly
        # TODO: use some type of connection manager class, this seems really hacky :S
        view.window().run_command('ftp_browse', {'server': site, 'stop_at_connect': True})

        # generate an md5 hash regardless if we need it or not, it's async after all
        if site in connections:
            with open(path, 'rb') as f:
                md5_hash = md5_for_file(f)
            view.settings().set('ftp_hash', md5_hash)
            debug('hash for %s created: %s' % (path, md5_hash))


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