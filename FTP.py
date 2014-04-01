import sublime
import sublime_plugin
import ftplib
import webbrowser
import threading
import os
import tempfile
import datetime
import time
import json
import os
import sys
import hashlib
import subprocess
import difflib
import posixpath
import re
import collections
from pprint import pprint
from functools import wraps

panel_open = False
output_panel = None

# Sublime output panel example
# output.run_command('erase_view')
# output.run_command('append', {'characters': 'mytext'})
# window.run_command('show_panel', {'panel': 'output.ftp'})

global_settings = sublime.load_settings('FTP.sublime-settings')

connections = {}

progress_i = 0
progress_dir = 1

# Some utilities that should probably be split out into a module
def run_async(func):
    @wraps(func)
    def async_func(*args, **kwargs):
        func_hl = threading.Thread(target = func, args = args, kwargs = kwargs)
        func_hl.start()
        return func_hl
    return async_func

def md5_for_file(f, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    f.seek(0)
    return md5.hexdigest()

def format_server(c):
    return ('%s://%s@%s:%s%s' % (c['type'], c['user'], c['host'], c['port'] if 'port' in c else 21, c['remote_path'] if 'remote_path' in c else '/')).lower()

def debug(message):
    global output_panel
    if output_panel == None:
            output_panel = sublime.active_window().create_output_panel('ftp')

    if global_settings.get('debug', False):
        string = '[%s][FTP.DEBUG]: %s' % (time.strftime('%Y-%m-%dT%H:%M:%S'), message)
        print(string)
        output_panel.run_command('append', {'characters': string + '\n'})

@run_async
def progress(view):
    settings = view.settings()
    if(settings.has('ftp_working')):
        global progress_i
        global progress_dir
        # This animates a little activity indicator in the status area
        before = progress_i % 8
        after = (7) - before
        if not after:
            progress_dir = -1
        if not before:
            progress_dir = 1
        progress_i += progress_dir
        view.set_status('ftp', 'FTP Working [%s=%s]' % (' ' * before, ' ' * after))
        sublime.set_timeout(lambda: progress(view), 100)
        return

    view.erase_status('ftp')
    sublime.status_message(settings.get('ftp_status'))
    settings.erase('ftp_progress')

def monitor(argument):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            view = sublime.active_window().active_view()
            settings = view.settings()
            settings.set('ftp_working', True)
            settings.set('ftp_status', 'FTP Info: %s' % argument)
            progress(view)
            result = function(*args, **kwargs)
            settings.erase('ftp_working')
            return result
        return wrapper
    return real_decorator

# Default connection wrapper, should eventually be a base class to implement other connection types
class Connection(object):

    def __init__(self, protocol):
        self.protocol = protocol
        self.handler = ftplib.FTP()
        self.config = None

    def setConfig(self, config):
        self.config = config

    def getConfig(self):
        return self.config

    @monitor('connected to server')
    def connect(self):
        debug('executing ftp command CONNECT')
        self.handler.connect(self.config['host'], int(self.config['port'] if 'port' in self.config else 21), int(self.config['timeout']) if 'timeout' in self.config else None)
        self.handler.login(self.config['user'] if 'user' in self.config else self.config['username'], self.config['pass'] if 'pass' in self.config else self.config['password'])

    def test(self):
        debug('executing ftp command NOOP')
        try:
            self.handler.voidcmd('NOOP')
        except Exception as e:
            debug('exception while testing %s protocol: %s' % (self.protocol, str(e)))
            self.quit()
            self.handler = ftplib.FTP() # TODO: check, does this seem right? reinitialization right here and now????
            self.connect()
        return True

    def quit(self):
        debug('executing ftp command QUIT')
        try:
            self.handler.quit()
        except Exception as e:
            debug('exception while quitting %s protocol: %s' % (self.protocol, e))

    @monitor('listing directory')
    def list(self, path, meta=['type', 'size', 'perm']):
        debug('executing ftp command MLSD %s meta: %s' % (path, meta))
        return self.handler.mlsd(path, meta)

    @monitor('downloaded file')
    def get(self, path, f):
        debug('executing ftp command RETR %s' % path)
        return self.handler.retrbinary('RETR %s' % path, f.write)

    @monitor('uploaded file')
    def put(self, path, f):
        debug('executing ftp command STOR %s' % path)
        return self.handler.storbinary('STOR %s' % path, f)

    def touch(self, path):
        return self.put(path, tempfile.SpooledTemporaryFile(0))

    @monitor('changed permissions')
    def chmod(self, path, mode):
        debug('executing ftp command CHMOD %s %s' % (mode, path))
        return self.handler.sendcmd('CHMOD %s %s' % (mode, path))

    @monitor('renamed target')
    def rename(self, source, target):
        debug('executing ftp command RENAME %s %s' % (source, target))
        return self.handler.rename(source, target)

    @monitor('deleted file')
    def delete(self, path):
        debug('executing ftp command DELETE %s' % path)
        return self.handler.delete(path)

    def exists(self, path):
        debug('executing ftp command SIZE %s' % path)
        try:
            return self.handler.size(path) != None
        except Exception as e:
            return False

    @monitor('created directory')
    def mkdir(self, path):
        debug('executing ftp command MKD %s' % path)
        return self.handler.mkd(path)

    @monitor('removed directory')
    def rmdir(self, path):
        debug('executing ftp command RMD %s' % path)
        return self.handler.rmd(path)

class ConnectionManager(object):

    active_connections = {}

    def connect(self, name):
        connections = self.getConnections()

        if name not in connections:
            return False

        connection = Connection('FTP')
        connection.setConfig(connections[name])

        try:
            connection.connect()
        except Exception as e:
            debug('error trying to connect to %s: %s' % (connection.getConfig()['host'], str(e)))
            return False

        self.set(name, connection)

        return self.get(name)

    def set(self, key, value):
        self.active_connections[key] = value

    def get(self, name):
        connection = self.active_connections[name] if name in self.active_connections else self.connect(name)
        connection.test()
        return connection

    def getConnections(self):
        connections = {}
        directory = os.path.join(sublime.packages_path(), 'User', global_settings.get('configs_folder')) # TODO: change path to just 'servers', or maybe read from both?
        for name in os.listdir(directory):
            if name[:1] == '.':
                continue

            json = None

            with open(os.path.join(directory, name)) as f:
                try:
                    json = sublime.decode_value(f.read())
                except Exception as e:
                    debug('could not load config file(%s): %s' % (name, e))
                    continue
            json['name'] = name
            connections[name] = json
        return collections.OrderedDict(sorted(connections.items(), key=lambda k: k))

# Manages all connections and handles all wrappers and such
connection_manager = ConnectionManager()

class FtpConnectCommand(sublime_plugin.WindowCommand):

    menu_items = []

    def run(self):
        sublime.set_timeout_async(lambda: self.window.show_quick_panel(self.menu(), self.action), 1)

    def action(self, index):
        if index == -1:
            return
        elif index == 0:
            self.window.run_command('ftp_create_server')
            return

        self.window.run_command('ftp_browse', {'name': self.menu_items[index][0]})

    def menu(self):
        self.menu_items = [['Setup New Connection...', 'Opens a config template for a new connection']]
        connections = connection_manager.getConnections()

        for name in connections:
            self.menu_items.append([name, format_server(connections[name])])

        return self.menu_items


class FtpBrowseCommand(sublime_plugin.WindowCommand):

    connection = None
    current_path = None

    def run(self, name=None, stop_at_connect=False, startup_path=None):

        if name == None:
            current_view = self.window.active_view()
            current_view_settings = current_view.settings()

            if not current_view_settings.has('ftp_site'):
                return self.window.run_command('ftp_connect')

            name = current_view_settings.get('ftp_site')
            startup_path = posixpath.dirname(current_view_settings.get('ftp_path'))

        self.connection = connection_manager.get(name)

        if not self.connection:
            sublime.status_message('Error connecting to %s, check configuration' % name)
            return

        config = self.connection.getConfig()

        sublime.status_message('Connected to %s successfully' % name)
        self.list(startup_path if startup_path != None else (config['remote_path'] if 'remote_path' in config else '/'))

    def is_visible(self):
        return self.window.active_view().settings().has('ftp_site')

    def list(self, path):

        path = posixpath.normpath(path)

        self.current_path = path

        menu_items = []
        file_items = []

        # special menu items
        menu_items.append('%s:%s' % (self.connection.getConfig()['host'], path))
        file_items.append(['goto', {'type': 'goto'}])
        menu_items.append(u'\u2022 Folder Actions')
        file_items.append(['actions', {'type': 'actions'}])

        if path != '/':
            menu_items.append('   ..')
            file_items.append(['back', {'type': 'back'}])

        config = self.connection.getConfig()

        listing = self.connection.list(path)

        if listing:
            regex = config['hidden_formats'] if 'hidden_formats' in config else global_settings.get('hidden_formats', False)

            if regex:
                regex = re.compile(regex, re.I)

            if config['folders_first'] if 'folders_first' in config else global_settings.get('folders_first', False):
                listing = sorted(list(listing), key=lambda i: 0 if i[1]['type'] == 'dir' else 1)

            for [name, attrs] in listing:
                if name == '.' or name == '..' or (regex and regex.match(name)):
                    continue

                file_items.append([name, attrs])
                attrs['fullpath'] = posixpath.join(path, name)
                menu_items.append('   ' + name + ('/' if attrs['type'] == 'dir' else ''))

        this = self

        def action(index):
            debug('ftpbrowse.list.action called')
            if index == -1:
                return

            [name, attrs] = file_items[index]

            if attrs['type'] == 'dir':
                path = posixpath.dirname(attrs['fullpath']) if name == '..' else attrs['fullpath']
                return this.list(path)
            else:
                if attrs['type'] == 'goto':
                    return this.goto(this.current_path)
                elif attrs['type'] == 'actions':
                    return this.folder(this.current_path)
                elif attrs['type'] == 'back':
                    return this.list(posixpath.dirname(this.current_path))
                else:
                    return this.file(attrs['fullpath'])

        sublime.set_timeout_async(lambda: self.window.show_quick_panel(menu_items, action), 1)

    def folder(self, path):
        debug('ftpbrowse.folder called')
        this = self

        def action(index):
            if index < 2:
                return this.list(path)
            elif index == 2:
                return this.create(path)
            elif index == 3:
                return this.create(path, True)
            elif index == 4:
                return this.rename(path, True)
            elif index == 5:
                return this.chmod(path)
            elif index == 6:
                return this.delete(path, True)

        menu = ['%s:%s' % (self.connection.getConfig()['host'], path), u'\u2022 Back', u'\u2022 New File', u'\u2022 New Folder', u'\u2022 Rename', u'\u2022 Chmod', u'\u2022 Delete']
        sublime.set_timeout_async(lambda: self.window.show_quick_panel(menu, action), 1)

    def file(self, path):
        this = self

        def action(index):
            if index < 2: # TODO: when the first item (current path info) is selected, allow goto navigation to another file instead of just returning back
                return this.list(posixpath.dirname(path))
            elif index == 2:
                return this.edit(path)
            elif index == 3:
                return this.rename(path)
            elif index == 4:
                return this.chmod(path)
            elif index == 5:
                return this.duplicate(path)
            elif index == 6:
                return this.diff(path)
            elif index == 7:
                return this.delete(path)

        menu = ['%s:%s' % (self.connection.getConfig()['host'], path), u'\u2022 Back', u'\u2022 Edit', u'\u2022 Rename', u'\u2022 Chmod', u'\u2022 Duplicate', u'\u2022 Diff with Current Tab', u'\u2022 Delete']
        sublime.set_timeout_async(lambda: self.window.show_quick_panel(menu, action, selected_index=2), 1)

    @run_async
    def edit(self, path):

        config = self.connection.getConfig()

        for x in sublime.active_window().views():
            settings = x.settings()
            # TODO: if user tries to download the file again and local copy differs from remote show diff?
            if settings.has('ftp_site') and settings.get('ftp_site') == config['name'] and settings.get('ftp_path') == path:
                debug('remote file is already downloaded, re-focusing')
                return sublime.active_window().focus_view(x)

        name = posixpath.basename(path)
        directory = os.path.dirname(path)

        local_path = os.path.join(tempfile.mkdtemp('-sublime-ftp'), config['name'], directory.lstrip('/').lstrip('\\'))
        os.makedirs(local_path, 0o777, True)
        local_path = os.path.join(local_path, name)

        with open(local_path, 'wb') as f:
            self.connection.get(path, f)

        new_view = sublime.active_window().open_file(local_path)
        view_settings = new_view.settings()
        view_settings.set('ftp_path', path)
        view_settings.set('ftp_site', config['name'])

    def rename(self, path, folder=False):
        # TODO: rename should also rename the local file if its downloaded, and also re-open the quick panel to the previous state when done
        # TODO: possibly create a keybind for renaming files so navigation through the quick panel isnt needed
        this = self

        def done(name):
            if not name or name == '' or name == posixpath.basename(path):
                return cancel()
            target = posixpath.join(posixpath.dirname(path), name)
            debug('renaming %s to %s' % (path, target))
            this.connection.rename(path, target)

        def cancel():
            if folder:
                this.folder(path)
            else:
                this.file(path)

        sublime.set_timeout_async(lambda: sublime.active_window().show_input_panel('Rename', posixpath.basename(path), done, None, cancel), 1)

    def chmod(self, folder=False):
        this = self

        def done(mode):
            if not mode or mode == '': # or mode == current_mode: # TODO: get current mode for file/folder
                return cancel()
            debug('setting chmod of file %s to %s' % (path, mode))
            this.connection.chmod(path, mode)

        def cancel():
            if folder:
                this.folder(path)
            else:
                this.file(path)

        sublime.set_timeout_async(lambda: sublime.active_window().show_input_panel('New Permissons', '0644', done, None, cancel), 1)

    def duplicate(self):
        pass

    def diff(self):
        pass

    def goto(self, path):
        this = self

        def done(to):
            if not to or to == '':
                return this.list(path)
            debug('navigating from user input to %s' % to)
            this.list(to)

        sublime.set_timeout_async(lambda: sublime.active_window().show_input_panel('Go to Path', path, done, None, lambda: this.list(path)), 1)

    def delete(self, path, folder=False):
        # TODO: close local file view if file is removed on server
        if sublime.ok_cancel_dialog('Are you sure you want to delete the remote file %s? This action can not be reversed!' % path, 'Delete'):
            debug('deleting %s from server' % path)
            getattr(self.connection, 'delete' if folder == False else 'rmdir')(path)
            sublime.set_timeout_async(lambda: self.list(posixpath.dirname(path)), 1)
        else:
            sublime.set_timeout_async(lambda: self.file(path), 1)

    def create(self, path, folder=False):
        this = self

        def done(name):
            target = posixpath.join(path, name)
            debug('creating new %s %s' % ('folder' if folder else 'file', target))
            if not this.connection.exists(target):
                if folder:
                    this.connection.mkdir(target)
                else:
                    with tempfile.SpooledTemporaryFile(0) as f:
                        this.connection.put(target, f)

                if global_settings.get('open_new_files', False):
                    this.edit(target)
                else:
                    this.list(path)
            else:
                debug('can not create %s, a file or directory with that name already exists' % target)
                this.list(path)

        sublime.set_timeout_async(lambda: sublime.active_window().show_input_panel('Create New %s' % ('Folder' if folder else 'File'), 'untitled', done, None, lambda: this.folder(path)), 1)

class FtpEventListner(sublime_plugin.EventListener):

    def on_post_save_async(self, view):
        view_settings = view.settings()
        if not view_settings.has('ftp_site'):
            return

        site = view_settings.get('ftp_site', False)

        connection = connection_manager.get(site)

        if not connection:
            debug('failed to get connection information for %s' % site)
            return

        local_file_path = view.file_name()
        local_md5_hash = view_settings.get('ftp_hash', False)
        remote_file_path = view_settings.get('ftp_path')

        # TODO: should check if the user even wants to compare hashes, because then we dont need this check
        # TODO: check user configurable option for overwrite protection
        # TODO: also needs to check if file even still exists on server
        tmp = tempfile.SpooledTemporaryFile(1024**2*5) # 5MB file before writing to disk
        connection.get(remote_file_path, tmp)
        tmp.seek(0)
        remote_md5_hash = md5_for_file(tmp)

        f = open(local_file_path, 'rb')

        def action(index):
            if index == 0: # confirm overite
                view_settings.set('ftp_hash', md5_for_file(f))
                connection.put(remote_file_path, f)
                debug('uploading file complete local(%s) remote(%s)' % (local_file_path, remote_file_path))
            elif index == 2: # show diff of remote and local file
                debug('displaying diff file for %s' % local_file_path)

                # if global_settings.has('diff_command'):
                #     try:
                #         subprocess.Popen(str(global_settings.get('diff_command')) % (local_file_path, remote_file_path))
                #     except Exception as e:
                #         debug('failed run diff program: %s' % e)
                #     return

                def decode(s):
                    return s.decode('ascii')

                diff = difflib.unified_diff(list(map(decode, tmp.readlines())), list(map(decode, f.readlines())), 'remote', 'local')
                view.window().run_command('ftp_create_buffer', {'name': '%s.diff' % os.path.basename(local_file_path), 'data': ''.join([(str(x).strip('\n') + '\n') for x in diff]), 'syntax': 'Packages/Diff/Diff.tmLanguage'})
            else:
                debug('save operation aborted for %s' % local_file_path)

            tmp.close()
            f.close()

        menu_overwrite = ['Overwrite Remote File', 'The file on the server has changed since first download']
        menu_cancel = ['Cancel', 'Abort this operation, no changes will be uploaded']
        menu_diff = ['Diff With Remote File', 'Show changes between this file and the remote one']

        debug('comparing hashes on remote(%s) to local(%s)' % (remote_md5_hash, local_md5_hash))
        if local_md5_hash and remote_md5_hash != local_md5_hash:
            sublime.set_timeout(lambda: view.window().show_quick_panel([menu_overwrite, menu_cancel, menu_diff], action), 1)
        else:
            action(0)

    def on_load_async(self, view):
        view_settings = view.settings()
        if not view_settings.has('ftp_site'):
            return

        path = view.file_name()

        with open(path, 'rb') as f:
            md5_hash = md5_for_file(f)
        view.settings().set('ftp_hash', md5_hash)
        debug('hash for %s created %s' % (path, md5_hash))

class FtpFileInfoCommand(sublime_plugin.TextCommand):

    def run(self):
        pass

    def is_visible(self):
        return self.view.settings().has('ftp_site')


class FtpFileDownloadCommand(sublime_plugin.TextCommand):

    @run_async
    def run(self, edit):
        view_settings = self.view.settings()
        if not view_settings.has('ftp_site'):
            return

        site = view_settings.get('ftp_site', False)

        connection = connection_manager.get(site)

        if not connection:
            debug('failed to get connection information for %s' % site)
            return

        if self.view.is_dirty():
            overwrite = sublime.ok_cancel_dialog('Are you sure you want to overwrite your local changes for %s?' % os.path.basename(self.view.file_name()), 'Overwrite')
        else:
            overwrite = True

        if overwrite:
            with open(self.view.file_name(), 'wb') as f:
                connection.get(view_settings.get('ftp_path'), f)
        #self.view.replace(edit, sublime.Region(0, self.view.size()), )

    def is_visible(self):
        return self.view.settings().has('ftp_site')


class FtpReadmeCommand(sublime_plugin.WindowCommand):

    def run(self):
        webbrowser.open("http://git.bluechipdigital.com/blue-chip/sublime-ftp-plugin", 2, True)

class FtpTogglePanelCommand(sublime_plugin.WindowCommand):

    def run(self):
        window = sublime.active_window()
        if hasattr(self, 'panel_open') and self.panel_open:
            window.run_command('hide_panel', {'panel': 'output.ftp'})
        else:
            window.run_command('show_panel', {'panel': 'output.ftp'})
        self.panel_open = not self.panel_open if hasattr(self, 'panel_open') else True

class FtpEditServerCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.menu = []
        connections = connection_manager.getConnections()
        for i in connections:
            self.menu.append([connections[i]['name'], format_server(connections[i])])

        sublime.set_timeout(lambda: sublime.active_window().show_quick_panel(self.menu, self.action), 1)

    def action(self, index):
        if index != -1:
            new_file = sublime.active_window().open_file(os.path.join(sublime.packages_path(), 'User', global_settings.get('configs_folder'), self.menu[index][0]))
            new_file.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')

class FtpDeleteServerCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.menu = []
        connections = connection_manager.getConnections()
        for i in connections:
            self.menu.append([connections[i]['name'], format_server(connections[i])])

        sublime.set_timeout(lambda: sublime.active_window().show_quick_panel(self.menu, self.action), 1)

    def action(self, index):
        if index != -1:
            if sublime.ok_cancel_dialog('Are you sure you want to delete the server %s? This action can not be undone.' % self.menu[index][0], 'Delete') == True:
                os.remove(os.path.join(sublime.packages_path(), 'User', global_settings.get('configs_folder'), self.menu[index][0]))

class FtpCreateServerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        new_file = sublime.active_window().new_file()
        new_file.set_name('untitled')
        new_file.set_syntax_file('Packages/JavaScript/JSON.tmLanguage')
        with open(os.path.join(sublime.packages_path(), 'FTP', 'FTP.default-config'), 'r') as f:
            new_file.insert(edit, 0, f.read())
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