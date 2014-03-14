import sublime
import sublime_plugin
import ftplib
import webbrowser
import threading
import urllib

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

        ftplist = self.find('');

    def find(self, path, attrs=None):
        # pprint(['attrs', attrs])
        if attrs and attrs['type'] != 'dir':
            return pprint('path is not a directory')

        ftp = ftplib.FTP('bluechipdigital.com')
        ftp.login('digital', 'SExO@![I[[ce')
        ftplist = ftp.mlsd(path, ["type", "size", "perm"])

        menu = []
        items = []

        for [name, attrs] in ftplist:
            if name != '.':
                menu.append(name)
                items.append([name, attrs])

        this = self

        def action(index):
            [name, attrs] = items[index];
            # pprint({'name': name, 'attrs': attrs, 'index': index})
            this.find(name, attrs)

        self.window.show_quick_panel(menu, action)

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