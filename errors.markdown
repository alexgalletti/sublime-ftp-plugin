### Errors to fix

`
[2014-04-09T16:43:57][FTP.DEBUG]: executing ftp command MLSD /public_html/news/wp-content/themes/bcblog meta: ['type', 'size', 'perm']
[2014-04-09T16:44:02][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-09T16:44:07][FTP.DEBUG]: executing ftp command NOOP
[2014-04-09T16:44:07][FTP.DEBUG]: exception while testing connection to bcpatientrecruitment.com: 421 Timeout - try typing a little faster next time
[2014-04-09T16:44:07][FTP.DEBUG]: executing ftp command QUIT
[2014-04-09T16:44:07][FTP.DEBUG]: exception while quitting FTP protocol:
[2014-04-09T16:44:07][FTP.DEBUG]: executing ftp command CONNECT
[2014-04-09T16:44:16][FTP.DEBUG]: error trying to connect to bcpatientrecruitment.com: [Errno 60] Operation timed out
[2014-04-09T16:44:16][FTP.DEBUG]: executing ftp command MLSD /public_html/components/com_jumi/files meta: ['type', 'size', 'perm']
Exception in thread Thread-2058:
Traceback (most recent call last):
  File "X/threading.py", line 639, in _bootstrap_inner
  File "X/threading.py", line 596, in run
  File "/Users/alexgalletti/Library/Application Support/Sublime Text 3/Packages/FTP/FTP.py", line 335, in list
    listing = sorted(list(listing), key=lambda i: 0 if i[1]['type'] == 'dir' else 1)
  File "X/ftplib.py", line 545, in mlsd
  File "X/ftplib.py", line 258, in sendcmd
  File "X/ftplib.py", line 192, in putcmd
  File "X/ftplib.py", line 187, in putline
AttributeError: 'NoneType' object has no attribute 'sendall'
`