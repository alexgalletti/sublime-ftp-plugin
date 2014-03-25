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
import subprocess
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

def noop(*arg):
    pass

def debug(message):
    if debug_enabled:
        print('[%s][FTP.DEBUG]: %s' % (time.strftime('%Y-%m-%dT%H:%M:%S'), message))

# Sublime output panel example
# window = sublime.active_window()
# output_panel = window.create_output_panel('ftp')
# output.run_command('erase_view')
# output.run_command('append', {'characters': 'mytext'})
# window.run_command('show_panel', {'panel': 'output.ftp'})

global_settings = sublime.load_settings('FTP.sublime-settings')

debug_enabled = global_settings.get('debug', False)

connections = {}

class ConnectionWrapper(object):
    def __init__(self, protocol):
        super(ConnectionWrapper, self).__init__()
        self.protocol = protocol


class ConnectionManager(object):

    active_connections = {}

    def connect(self, config_name):
        servers = self.getServers()

        if config_name not in servers:
            return False

        connection = ConnectionWrapper('FTP')
        connection.setConfig(servers[config_name])
        self.set(config_name, connection)

        return self.get(config_name)

    def set(self, key, value):
        self.active_connections[key] = value

    def get(self, config_name):
        if config_name in active_connections:
            return active_connections[config_name]
        return self.connect(config_name)

    def getServers(self):
        return os.listdir(os.path.join(sublime.packages_path(), 'User', 'sftp_servers'))

Manager = ConnectionManager()

class FtpConnectCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.servers = []
        sublime.set_timeout(lambda: self.window.show_quick_panel(self.getServers(), self.menuAction), 1)

    def menuAction(self, index):
        if index == -1:
            return
        elif index == 0:
            self.window.run_command('ftp_create_server')
            return

        self.window.run_command('ftp_browse', {'server': self.servers[index][0]})

    def getServers(self):

        files = Manager.getServers()

        self.servers.append(['Setup New Server...', 'Opens a config template for a new server'])

        for name in files:
            if name[:1] == '.':
                continue
            server = os.path.join(os.path.join(sublime.packages_path(), 'User', 'sftp_servers'), name)
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

        for x in sublime.active_window().views():
            settings = x.settings()
            if os.path.basename(x.file_name()) == os.path.basename(path) and settings.has('ftp_site') and settings.get('ftp_site') == self.conn['server']:
                debug('remote file is already downloaded, re-focusing')
                return sublime.active_window().focus_view(x)

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

    def rename(self, path, attrs):
        this = self

        def done(name):
            target = os.path.join(os.path.dirname(path), name)
            debug('renaming %s to %s' % (path, target))
            this.conn['ftp'].rename(path, target)
        def cancel():
            if attrs['type'] == 'dir':
                this.folder_actions(path, attrs)
            else:
                this.file_actions(path, attrs)

        sublime.active_window().show_input_panel('Rename', os.path.basename(path), done, noop, cancel)

    def delete(self, path, attrs):
        yes = sublime.ok_cancel_dialog('Are you sure you want to delete the remote file %s? This action can not be reversed!' % path, 'Delete')
        if yes:
            debug('deleting %s from server' % path)
            self.conn['ftp'].delete(path)
            sublime.set_timeout(lambda: self.find(os.path.dirname(path)), 1)
        else:
            sublime.set_timeout(lambda: self.file_actions(path, attrs), 1)

    def createFile(self, path, attrs):
        this = self
        def done(name):
            target = os.path.join(path, name)
            debug('creating new file %s' % target)
            if not this.checkExists(path, target):
                this.conn['ftp'].storbinary('STOR %s' % target, tempfile.SpooledTemporaryFile(0))
            else:
                debug('can not create %s, a file with that name already exists' % target)
        def cancel():
            this.folder_actions(path, attrs)

        sublime.active_window().show_input_panel('Create New File', 'untitled', done, noop, cancel)

    def createFolder(self, path, attrs):
        this = self
        def done(name):
            target = os.path.join(path, name)
            debug('creating new folder %s' % target)
            if not this.checkExists(path, target):
                this.conn['ftp'].mkd(target)
            else:
                debug('can not create %s, a folder with that name already exists' % target)
        def cancel():
            this.folder_actions(path, attrs)

        sublime.active_window().show_input_panel('Create New Folder', 'untitled', done, noop, cancel)

    # really dont think this works :S
    def checkExists(self, path, lookingfor):
        lookingfor = os.path.basename(lookingfor)
        names = self.conn['ftp'].mlsd(path)
        for [name, attr] in names:
            if path == lookingfor:
                return True
        return False

    def goto(self):
        pass

    def file_actions(self, path, attrs):
        this = self
        def action(index):
            if index == 2:#download
                return this.download(path, attrs)
            elif index == 3:#rename
                return this.rename(path, attrs)
            elif index == 4:#chmod
                pass
            elif index == 5:#duplicate
                pass
            elif index == 6:#diff with current tab
                pass
            elif index == 7:#delete(with confirm)
                this.delete(path, attrs)
            else: # return back
                return this.find(os.path.dirname(attrs['parent']))

        path = os.path.join(self.current_attrs['parent'] if self.current_attrs != None and 'parent' in self.current_attrs else '', self.current_path)

        menu = ['%s:/%s' % (self.conn['config']['host'], path), u'\u2022 Back', u'\u2022 Edit', u'\u2022 Rename', u'\u2022 Chmod', u'\u2022 Duplicate', u'\u2022 Diff with Current Tab', u'\u2022 Delete']
        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action, selected_index=2), 1)

    def folder_actions(self):

        this = self;

        def action(index):
            if index == 1:
                this.find(this.current_path, this.current_attrs)
            elif index == 2:
                this.createFile(this.current_path, this.current_attrs)
            elif index == 3:
                this.createFolder(this.current_path, this.current_attrs)
            elif index == 4:
                this.rename(this.current_path, this.current_attrs)
            elif index == 5:#chmod
                pass
            elif index == 6:#delete(with confirm)
                pass
                #this.delete(this.current_path)

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
                    #TODO: check diff with external diff tool if speficied in config
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