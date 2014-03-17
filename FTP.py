import sublime
import sublime_plugin
import ftplib
import webbrowser
import threading
import urllib
import os

from pprint import pprint

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

class FtpCommand(sublime_plugin.WindowCommand):
    def run(self):

        self.ftp = ftplib.FTP('bluechipdigital.com')
        self.ftp.login('digital', 'SExO@![I[[ce')

        ftplist = self.find('');

    def find(self, path, attrs=None):
        pprint(['DEBUG: finding', path, attrs])
        if attrs and attrs['type'] != 'dir':
            return self.download(path, attrs)

        ftplist = self.ftp.mlsd(path, ["type", "size", "perm"])

        menu = []
        items = []

        for [name, attrs] in ftplist:
            attrs['parent'] = path
            if name != '.':
                if (path == '/' or path == '') and name == '..':
                    continue
                if attrs['type'] == 'dir':
                    name = name + '/'
                menu.append(name)
                items.append([name, attrs])

        this = self

        def action(index):
            [name, attrs] = items[index];
            #pprint({'name': name, 'attrs': attrs, 'index': index})
            if name == '..':
                return this.find(os.path.basename(attrs['parent']))
            this.find(name, attrs)

        sublime.set_timeout(lambda: self.window.show_quick_panel(menu, action), 5)

    def download(self, path, attrs):
        fullpath = os.path.join(attrs['parent'], path)
        pprint('downloading %s' % fullpath)
        name = os.path.basename(path)
        tempfile = os.path.join(sublime.cache_path(), name)
        fh = open(tempfile, 'wb')
        self.ftp.retrbinary('RETR %s' % fullpath, fh.write)
        pprint('opening file')
        sublime.active_window().open_file(tempfile)

class FtpReadmeCommand(sublime_plugin.WindowCommand):
    def run(self):
        webbrowser.open("http://git.bluechipdigital.com/blue-chip/sublime-ftp-plugin", 2, True)

class PrefixrApiCall(threading.Thread):
    def __init__(self, sel, string, timeout):
        self.sel = sel
        self.original = string
        self.timeout = timeout
        self.result = None
        threading.Thread.__init__(self)