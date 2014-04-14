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

`
startup time: 0.493802
first paint time: 0.509802
launching: /C/Program Files/Sublime Text 3/plugin_host.exe
loaded 850 snippets
reloading plugin Default.block
reloading plugin Default.comment
reloading plugin Default.copy_path
reloading plugin Default.delete_word
reloading plugin Default.detect_indentation
reloading plugin Default.duplicate_line
reloading plugin Default.echo
reloading plugin Default.exec
reloading plugin Default.fold
reloading plugin Default.font
reloading plugin Default.goto_line
reloading plugin Default.history_list
reloading plugin Default.indentation
reloading plugin Default.kill_ring
reloading plugin Default.mark
reloading plugin Default.new_templates
reloading plugin Default.open_file_settings
reloading plugin Default.open_in_browser
reloading plugin Default.pane
reloading plugin Default.paragraph
reloading plugin Default.paste_from_history
reloading plugin Default.save_on_focus_lost
reloading plugin Default.scroll
reloading plugin Default.set_unsaved_view_name
reloading plugin Default.side_bar
reloading plugin Default.sort
reloading plugin Default.swap_line
reloading plugin Default.switch_file
reloading plugin Default.symbol
reloading plugin Default.transform
reloading plugin Default.transpose
reloading plugin Default.trim_trailing_white_space
reloading plugin CSS.css_completions
reloading plugin Diff.diff
reloading plugin HTML.encode_html_entities
reloading plugin HTML.html_completions
reloading plugin Alignment.Alignment
reloading plugin BracketHighlighter.bh_core
reloading plugin BracketHighlighter.bh_plugin
reloading plugin BracketHighlighter.bh_remove
reloading plugin BracketHighlighter.bh_swapping
reloading plugin BracketHighlighter.bh_wrapping
reloading plugin BracketHighlighter.ure
reloading plugin DocBlockr.__init__
reloading plugin DocBlockr.jsdocs
reloading plugin Emmet.emmet-plugin
reloading plugin Git.add
reloading plugin Git.annotate
reloading plugin Git.commit
reloading plugin Git.diff
reloading plugin Git.flow
reloading plugin Git.git
reloading plugin Git.history
reloading plugin Git.repo
reloading plugin Git.stash
reloading plugin Git.status
reloading plugin Git.statusbar
reloading plugin LineEndings.LineEndings
reloading plugin Package Control.Package Control
reloading plugin FTP.FTP
reloading plugin SFTP.SFTP
plugins loaded
PyV8: Creating new thread
Emmet: Creating thread
Emmet: Loading https://api.github.com/repos/emmetio/pyv8-binaries/contents
Emmet: You have the most recent PyV8 binary
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpltyoi6-sublime-ftp\inter.realtechniques.com\public_html\administrator\components\com_virtuemart\html\checkout_register_form.php created: 080c6044a5e7da64bd46635364f1aad1
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmp7cbdf8-sublime-ftp\inter.realtechniques.com\public_html\components\com_virtuemart\themes\default\templates\basket\basket_b2c.html.php created: 06408a1d1b79534fca4f52b718a64b7c
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmplrte2x-sublime-ftp\inter.realtechniques.com\public_html\components\com_virtuemart\themes\default\templates\browse\browse_1.php created: 613b41a61c8778a3372fae1432fa692f
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpslld8t-sublime-ftp\inter.realtechniques.com\public_html\components\com_virtuemart\themes\default\templates\browse\includes\browse_notables.tpl.php created: 6f0da9ad7450e8c39a89ae55c8dfda7a
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpzy7okd-sublime-ftp\inter.realtechniques.com\public_html\administrator\components\com_virtuemart\html\shop_browse_queries.php created: c7fba9152b3c109f4217aa79f17786ea
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmp29gasy-sublime-ftp\inter.realtechniques.com\public_html\administrator\components\com_virtuemart\html\shop.product_details.php created: 17de48a88eac410f1225389b36cc62d6
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpq_kj1s-sublime-ftp\inter.realtechniques.com\public_html\administrator\components\com_virtuemart\classes\ps_product_type.php created: b8da668463518e45a4647f188ccf39b3
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpuo489f-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\data_export.php created: b47d90b8e0bdfb1e9bbbc25824e7570b
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmptj47g7-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\loop.php created: be3eaeee1f071c97cf95d74249dded44
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmp1ncdl9-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php created: d507bfc9909dc7da599ae765ad94ab40
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpyi7hip-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\components\com_virtuemart\themes\default\templates\product_details\includes\video_mapping.php created: b5864acf208201711ea49b126ff727e2
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php created: 90de5ef478f261d85eaf0ccbca72201c
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpkxhz52-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\templates\nc_multivmenu\css\template.css created: 1e07a8fca826592dd3b920f90f5bd4c6
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpdj6nh_-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\components\com_virtuemart\themes\default\templates\product_details\includes\addtocart_form.tpl.php created: d16b9e41c5a9c2a46c15f8b1d9da6fd3
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmp3j2et5-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\templates\nc_multivmenu\js\local.js created: 3cab059ffe404bdc11e83e1942216dce
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmp6vdivw-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\templates\nc_multivmenu\js\accordion.js created: 63bc40e3ec6dcca3a636be641cbf09e7
[2014-04-10T17:06:21][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpzi4gb0-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\components\com_virtuemart\themes\default\templates\product_details\flypage.tpl.php created: 9e24cbad914662044fa0801e3d7c243d
Writing file /c/users/vtruba~1/appdata/local/temp/tmpo_w_yb-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php with encoding UTF-8 (atomic)
[2014-04-10T17:06:27][FTP.DEBUG]: executing ftp command CONNECT
*get* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n'
*get* '220-You are user number 4 of 50 allowed.\n'
*get* '220-Local time is now 17:05. Server port: 21.\n'
*get* '220-This is a private system - No anonymous login\n'
*get* '220-IPv6 connections are also welcome on this server.\n'
*get* '220 You will be disconnected after 15 minutes of inactivity.\n'
*resp* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n220-You are user number 4 of 50 allowed.\n220-Local time is now 17:05. Server port: 21.\n220-This is a private system - No anonymous login\n220-IPv6 connections are also welcome on this server.\n220 You will be disconnected after 15 minutes of inactivity.'
*cmd* 'USER realintl'
*put* 'USER realintl\r\n'
*get* '331 User realintl OK. Password required\n'
*resp* '331 User realintl OK. Password required'
*cmd* 'PASS ************'
*put* 'PASS ************\r\n'
*get* '230 OK. Current restricted directory is /\n'
*resp* '230 OK. Current restricted directory is /'
[2014-04-10T17:06:27][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-10T17:06:27][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-10T17:06:27][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-10T17:06:27][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
Package Control: No updated packages
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-10T17:06:27][FTP.DEBUG]: executing ftp command RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,112,78)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,112,78)'
*cmd* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php'
*put* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.9 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.9 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 74.06 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 74.06 Mbytes per second'
[2014-04-10T17:06:27][FTP.DEBUG]: comparing hashes on remote(5ec6d0cb8d89c955832fced741eacb51) to local(5ec6d0cb8d89c955832fced741eacb51)
[2014-04-10T17:06:27][FTP.DEBUG]: executing ftp command STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,195,101)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,195,101)'
*cmd* 'STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php'
*put* 'STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.175 seconds (measured here), 86.47 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.175 seconds (measured here), 86.47 Kbytes per second'
[2014-04-10T17:06:28][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpo_w_yb-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\components\com_virtuemart\themes\default\templates\product_details\flypage_resp.tpl.php) remote(/public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpo_w_yb-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php with encoding UTF-8 (atomic)
[2014-04-10T17:06:35][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-10T17:06:35][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-10T17:06:35][FTP.DEBUG]: executing ftp command RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,82,193)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,82,193)'
*cmd* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php'
*put* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 15.2 kbytes to download\n'
*resp* '150-Accepted data connection\n150 15.2 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 97.31 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 97.31 Mbytes per second'
[2014-04-10T17:06:36][FTP.DEBUG]: comparing hashes on remote(380029681f414231f79bd9e87789b152) to local(380029681f414231f79bd9e87789b152)
[2014-04-10T17:06:36][FTP.DEBUG]: executing ftp command STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,251,78)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,251,78)'
*cmd* 'STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php'
*put* 'STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.176 seconds (measured here), 86.09 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.176 seconds (measured here), 86.09 Kbytes per second'
[2014-04-10T17:06:36][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpo_w_yb-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\components\com_virtuemart\themes\default\templates\product_details\flypage_resp.tpl.php) remote(/public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php)
Writing file /C/users/vtruba~1/appdata/local/temp/sublime-sftp-browse-1397165991/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-10T17:09:55][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-10T17:09:55][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-10T17:09:55][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,58,97)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,58,97)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.5 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.5 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 65.92 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 65.92 Mbytes per second'
[2014-04-10T17:09:55][FTP.DEBUG]: hash for /public_html/pre_scripts/readctltodb.php created: 89c9eae0763ca4d0a2a3e883bb1c3ffd
Reloading /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T09:03:34][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:03:34][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
[2014-04-11T09:03:34][FTP.DEBUG]: exception while testing connection to inter.realtechniques.com: [WinError 10054] An existing connection was forcibly closed by the remote host
[2014-04-11T09:03:34][FTP.DEBUG]: executing ftp command QUIT
*cmd* 'QUIT'
*put* 'QUIT\r\n'
[2014-04-11T09:03:34][FTP.DEBUG]: exception while quitting FTP protocol: [WinError 10054] An existing connection was forcibly closed by the remote host
[2014-04-11T09:03:34][FTP.DEBUG]: executing ftp command CONNECT
*get* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n'
*get* '220-You are user number 1 of 50 allowed.\n'
*get* '220-Local time is now 09:02. Server port: 21.\n'
*get* '220-This is a private system - No anonymous login\n'
*get* '220-IPv6 connections are also welcome on this server.\n'
*get* '220 You will be disconnected after 15 minutes of inactivity.\n'
*resp* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n220-You are user number 1 of 50 allowed.\n220-Local time is now 09:02. Server port: 21.\n220-This is a private system - No anonymous login\n220-IPv6 connections are also welcome on this server.\n220 You will be disconnected after 15 minutes of inactivity.'
*cmd* 'USER realintl'
*put* 'USER realintl\r\n'
*get* '331 User realintl OK. Password required\n'
*resp* '331 User realintl OK. Password required'
*cmd* 'PASS ************'
*put* 'PASS ************\r\n'
*get* '230 OK. Current restricted directory is /\n'
*resp* '230 OK. Current restricted directory is /'
[2014-04-11T09:03:35][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,88,132)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,88,132)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.5 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.5 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.032 seconds (measured here), 444.97 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.032 seconds (measured here), 444.97 Kbytes per second'
[2014-04-11T09:03:36][FTP.DEBUG]: comparing hashes on remote(89c9eae0763ca4d0a2a3e883bb1c3ffd) to local(89c9eae0763ca4d0a2a3e883bb1c3ffd)
[2014-04-11T09:03:36][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,150,5)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,150,5)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 1.063 seconds (measured here), 13.61 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 1.063 seconds (measured here), 13.61 Kbytes per second'
[2014-04-11T09:03:38][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T09:04:14][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:04:14][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T09:04:14][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,206,134)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,206,134)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.5 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.5 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 135.57 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 135.57 Mbytes per second'
[2014-04-11T09:04:14][FTP.DEBUG]: comparing hashes on remote(57e59528d745e76e8f448db4b46f5425) to local(57e59528d745e76e8f448db4b46f5425)
[2014-04-11T09:04:14][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,200,126)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,200,126)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.175 seconds (measured here), 82.78 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.175 seconds (measured here), 82.78 Kbytes per second'
[2014-04-11T09:04:14][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T09:10:21][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:10:21][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T09:10:21][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,81,179)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,81,179)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.5 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.5 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 130.96 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 130.96 Mbytes per second'
[2014-04-11T09:10:22][FTP.DEBUG]: comparing hashes on remote(97c9634510b225cc58655df8e7e57691) to local(97c9634510b225cc58655df8e7e57691)
[2014-04-11T09:10:22][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,99,254)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,99,254)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.393 seconds (measured here), 36.84 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.393 seconds (measured here), 36.84 Kbytes per second'
[2014-04-11T09:10:23][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpzi4gb0-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php with encoding UTF-8 (atomic)
[2014-04-11T09:26:15][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:26:15][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '421 Timeout - try typing a little faster next time\n'
*resp* '421 Timeout - try typing a little faster next time'
[2014-04-11T09:26:15][FTP.DEBUG]: exception while testing connection to inter.realtechniques.com: 421 Timeout - try typing a little faster next time
[2014-04-11T09:26:15][FTP.DEBUG]: executing ftp command QUIT
*cmd* 'QUIT'
*put* 'QUIT\r\n'
*get* ''
[2014-04-11T09:26:15][FTP.DEBUG]: exception while quitting FTP protocol:
[2014-04-11T09:26:15][FTP.DEBUG]: executing ftp command CONNECT
*get* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n'
*get* '220-You are user number 1 of 50 allowed.\n'
*get* '220-Local time is now 09:24. Server port: 21.\n'
*get* '220-This is a private system - No anonymous login\n'
*get* '220-IPv6 connections are also welcome on this server.\n'
*get* '220 You will be disconnected after 15 minutes of inactivity.\n'
*resp* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n220-You are user number 1 of 50 allowed.\n220-Local time is now 09:24. Server port: 21.\n220-This is a private system - No anonymous login\n220-IPv6 connections are also welcome on this server.\n220 You will be disconnected after 15 minutes of inactivity.'
*cmd* 'USER realintl'
*put* 'USER realintl\r\n'
*get* '331 User realintl OK. Password required\n'
*resp* '331 User realintl OK. Password required'
*cmd* 'PASS ************'
*put* 'PASS ************\r\n'
*get* '230 OK. Current restricted directory is /\n'
*resp* '230 OK. Current restricted directory is /'
[2014-04-11T09:26:15][FTP.DEBUG]: executing ftp command RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,33,79)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,33,79)'
*cmd* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php'
*put* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 20.8 kbytes to download\n'
*resp* '150-Accepted data connection\n150 20.8 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.111 seconds (measured here), 188.16 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.111 seconds (measured here), 188.16 Kbytes per second'
[2014-04-11T09:26:16][FTP.DEBUG]: comparing hashes on remote(9e24cbad914662044fa0801e3d7c243d) to local(9e24cbad914662044fa0801e3d7c243d)
[2014-04-11T09:26:16][FTP.DEBUG]: executing ftp command STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,214,27)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,214,27)'
*cmd* 'STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php'
*put* 'STOR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.195 seconds (measured here), 74.96 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.195 seconds (measured here), 74.96 Kbytes per second'
[2014-04-11T09:26:16][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpzi4gb0-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\components\com_virtuemart\themes\default\templates\product_details\flypage.tpl.php) remote(/public_html/components/com_virtuemart/themes/default/templates/product_details/flypage.tpl.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T09:49:11][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:49:11][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '421 Timeout - try typing a little faster next time\n'
*resp* '421 Timeout - try typing a little faster next time'
[2014-04-11T09:49:11][FTP.DEBUG]: exception while testing connection to inter.realtechniques.com: 421 Timeout - try typing a little faster next time
[2014-04-11T09:49:11][FTP.DEBUG]: executing ftp command QUIT
*cmd* 'QUIT'
*put* 'QUIT\r\n'
*get* ''
[2014-04-11T09:49:11][FTP.DEBUG]: exception while quitting FTP protocol:
[2014-04-11T09:49:11][FTP.DEBUG]: executing ftp command CONNECT
*get* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n'
*get* '220-You are user number 1 of 50 allowed.\n'
*get* '220-Local time is now 09:47. Server port: 21.\n'
*get* '220-This is a private system - No anonymous login\n'
*get* '220-IPv6 connections are also welcome on this server.\n'
*get* '220 You will be disconnected after 15 minutes of inactivity.\n'
*resp* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n220-You are user number 1 of 50 allowed.\n220-Local time is now 09:47. Server port: 21.\n220-This is a private system - No anonymous login\n220-IPv6 connections are also welcome on this server.\n220 You will be disconnected after 15 minutes of inactivity.'
*cmd* 'USER realintl'
*put* 'USER realintl\r\n'
*get* '331 User realintl OK. Password required\n'
*resp* '331 User realintl OK. Password required'
*cmd* 'PASS ************'
*put* 'PASS ************\r\n'
*get* '230 OK. Current restricted directory is /\n'
*resp* '230 OK. Current restricted directory is /'
[2014-04-11T09:49:11][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,79,47)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,79,47)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.5 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.5 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 70.35 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 70.35 Mbytes per second'
[2014-04-11T09:49:11][FTP.DEBUG]: comparing hashes on remote(151e8b38efc33680c531eb9c0e824220) to local(151e8b38efc33680c531eb9c0e824220)
[2014-04-11T09:49:11][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,13,131)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,13,131)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.178 seconds (measured here), 82.44 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.178 seconds (measured here), 82.44 Kbytes per second'
[2014-04-11T09:49:12][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T09:51:29][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:51:29][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T09:51:30][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,52,143)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,52,143)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.7 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.7 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 114.82 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 114.82 Mbytes per second'
[2014-04-11T09:51:30][FTP.DEBUG]: comparing hashes on remote(42e74a80a811b5f343300506f1ad74a8) to local(42e74a80a811b5f343300506f1ad74a8)
[2014-04-11T09:51:30][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,80,44)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,80,44)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.176 seconds (measured here), 85.21 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.176 seconds (measured here), 85.21 Kbytes per second'
[2014-04-11T09:51:30][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T09:51:35][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:51:35][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T09:51:35][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,235,57)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,235,57)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 15.0 kbytes to download\n'
*resp* '150-Accepted data connection\n150 15.0 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 128.23 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 128.23 Mbytes per second'
[2014-04-11T09:51:35][FTP.DEBUG]: comparing hashes on remote(8154e7cfa63c5db53cc54685039b4594) to local(8154e7cfa63c5db53cc54685039b4594)
[2014-04-11T09:51:35][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,240,242)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,240,242)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.175 seconds (measured here), 84.42 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.175 seconds (measured here), 84.42 Kbytes per second'
[2014-04-11T09:51:36][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T09:51:46][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T09:51:46][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T09:51:46][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,74,90)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,74,90)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.8 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.8 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 71.45 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 71.45 Mbytes per second'
[2014-04-11T09:51:46][FTP.DEBUG]: comparing hashes on remote(38e05aae5b19aee308d33d1bf63ee3c0) to local(38e05aae5b19aee308d33d1bf63ee3c0)
[2014-04-11T09:51:46][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,44,24)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,44,24)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.176 seconds (measured here), 84.02 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.176 seconds (measured here), 84.02 Kbytes per second'
[2014-04-11T09:51:47][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T10:03:27][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T10:03:27][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:03:27][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,232,165)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,232,165)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.7 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.7 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 135.75 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 135.75 Mbytes per second'
[2014-04-11T10:03:27][FTP.DEBUG]: comparing hashes on remote(7cbee70f6d3f7ecf5819576516cde307) to local(7cbee70f6d3f7ecf5819576516cde307)
[2014-04-11T10:03:27][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,59,102)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,59,102)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.176 seconds (measured here), 84.18 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.176 seconds (measured here), 84.18 Kbytes per second'
[2014-04-11T10:03:27][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpfa7p9w-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/pre_scripts/readctltodb.php with encoding UTF-8 (atomic)
[2014-04-11T10:17:45][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T10:17:45][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:17:45][FTP.DEBUG]: executing ftp command RETR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,97,202)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,97,202)'
*cmd* 'RETR /public_html/pre_scripts/readctltodb.php'
*put* 'RETR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 14.8 kbytes to download\n'
*resp* '150-Accepted data connection\n150 14.8 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 122.55 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 122.55 Mbytes per second'
[2014-04-11T10:17:45][FTP.DEBUG]: comparing hashes on remote(5884900c9c5e974aff58c5efd7a1c977) to local(5884900c9c5e974aff58c5efd7a1c977)
[2014-04-11T10:17:45][FTP.DEBUG]: executing ftp command STOR /public_html/pre_scripts/readctltodb.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,147,60)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,147,60)'
*cmd* 'STOR /public_html/pre_scripts/readctltodb.php'
*put* 'STOR /public_html/pre_scripts/readctltodb.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.193 seconds (measured here), 76.75 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.193 seconds (measured here), 76.75 Kbytes per second'
[2014-04-11T10:17:46][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpfa7p9w-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\pre_scripts\readctltodb.php) remote(/public_html/pre_scripts/readctltodb.php)
[2014-04-11T10:23:21][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T10:23:21][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:23:21][FTP.DEBUG]: executing ftp command MLSD /public_html/components/com_virtuemart/themes/default/templates/product_details meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,153,249)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,153,249)'
*cmd* 'MLSD /public_html/components/com_virtuemart/themes/default/templates/product_details'
*put* 'MLSD /public_html/components/com_virtuemart/themes/default/templates/product_details\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 12 matches total\n'
*resp* '226-Options: -a -l \n226 12 matches total'
[2014-04-11T10:23:22][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:23:24][FTP.DEBUG]: executing ftp command CONNECT
*get* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n'
*get* '220-You are user number 6 of 50 allowed.\n'
*get* '220-Local time is now 10:21. Server port: 21.\n'
*get* '220-This is a private system - No anonymous login\n'
*get* '220-IPv6 connections are also welcome on this server.\n'
*get* '220 You will be disconnected after 15 minutes of inactivity.\n'
*resp* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n220-You are user number 6 of 50 allowed.\n220-Local time is now 10:21. Server port: 21.\n220-This is a private system - No anonymous login\n220-IPv6 connections are also welcome on this server.\n220 You will be disconnected after 15 minutes of inactivity.'
*cmd* 'USER realtech'
*put* 'USER realtech\r\n'
*get* '331 User realtech OK. Password required\n'
*resp* '331 User realtech OK. Password required'
*cmd* 'PASS ************'
*put* 'PASS ************\r\n'
*get* '230 OK. Current restricted directory is /\n'
*resp* '230 OK. Current restricted directory is /'
[2014-04-11T10:23:25][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:23:25][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:23:25][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:23:25][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:23:25][FTP.DEBUG]: executing ftp command MLSD / meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,211,203)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,211,203)'
*cmd* 'MLSD /'
*put* 'MLSD /\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 32 matches total\n'
*resp* '226-Options: -a -l \n226 32 matches total'
[2014-04-11T10:23:27][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:23:27][FTP.DEBUG]: executing ftp command MLSD /public_html meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,57,210)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,57,210)'
*cmd* 'MLSD /public_html'
*put* 'MLSD /public_html\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 96 matches total\n'
*resp* '226-Options: -a -l \n226 96 matches total'
[2014-04-11T10:23:29][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:23:29][FTP.DEBUG]: executing ftp command MLSD /public_html/facebook meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,151,27)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,151,27)'
*cmd* 'MLSD /public_html/facebook'
*put* 'MLSD /public_html/facebook\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 6 matches total\n'
*resp* '226-Options: -a -l \n226 6 matches total'
[2014-04-11T10:23:31][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:23:31][FTP.DEBUG]: executing ftp command MLSD /public_html/facebook/0164 meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,171,70)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,171,70)'
*cmd* 'MLSD /public_html/facebook/0164'
*put* 'MLSD /public_html/facebook/0164\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 9 matches total\n'
*resp* '226-Options: -a -l \n226 9 matches total'
[2014-04-11T10:23:35][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:23:36][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/ajax.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,252,142)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,252,142)'
*cmd* 'RETR /public_html/facebook/0164/ajax.php'
*put* 'RETR /public_html/facebook/0164/ajax.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 4.74 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 4.74 Mbytes per second'
[2014-04-11T10:23:36][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\ajax.php created: 11e88fd242669e6579c5422642ef4daa
[2014-04-11T10:25:01][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:25:01][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:25:01][FTP.DEBUG]: executing ftp command MLSD /public_html/facebook/0164 meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,114,202)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,114,202)'
*cmd* 'MLSD /public_html/facebook/0164'
*put* 'MLSD /public_html/facebook/0164\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 9 matches total\n'
*resp* '226-Options: -a -l \n226 9 matches total'
[2014-04-11T10:25:03][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:25:03][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/index.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,104,26)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,104,26)'
*cmd* 'RETR /public_html/facebook/0164/index.php'
*put* 'RETR /public_html/facebook/0164/index.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 4.1 kbytes to download\n'
*resp* '150-Accepted data connection\n150 4.1 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 53.61 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 53.61 Mbytes per second'
[2014-04-11T10:25:04][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\index.php created: 2821d84f8f95fffcebc50b8f49c314f6
Writing file /c/users/vtruba~1/appdata/local/temp/tmpw411ax-sublime-ftp/Real Techniques (realtechniques.com)/public_html/facebook/0164/index.php with encoding UTF-8 (atomic)
[2014-04-11T10:25:48][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:25:48][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:25:48][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/index.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,199,49)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,199,49)'
*cmd* 'RETR /public_html/facebook/0164/index.php'
*put* 'RETR /public_html/facebook/0164/index.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 4.1 kbytes to download\n'
*resp* '150-Accepted data connection\n150 4.1 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 40.05 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 40.05 Mbytes per second'
[2014-04-11T10:25:48][FTP.DEBUG]: comparing hashes on remote(2821d84f8f95fffcebc50b8f49c314f6) to local(2821d84f8f95fffcebc50b8f49c314f6)
[2014-04-11T10:25:48][FTP.DEBUG]: executing ftp command STOR /public_html/facebook/0164/index.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,207,250)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,207,250)'
*cmd* 'STOR /public_html/facebook/0164/index.php'
*put* 'STOR /public_html/facebook/0164/index.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.115 seconds (measured here), 35.25 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.115 seconds (measured here), 35.25 Kbytes per second'
[2014-04-11T10:25:49][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\index.php) remote(/public_html/facebook/0164/index.php)
[2014-04-11T10:29:04][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:29:04][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:29:04][FTP.DEBUG]: executing ftp command MLSD /public_html/facebook/0164 meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,225,53)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,225,53)'
*cmd* 'MLSD /public_html/facebook/0164'
*put* 'MLSD /public_html/facebook/0164\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 9 matches total\n'
*resp* '226-Options: -a -l \n226 9 matches total'
[2014-04-11T10:29:06][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:29:06][FTP.DEBUG]: executing ftp command MLSD /public_html/facebook/0164/css meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,62,89)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,62,89)'
*cmd* 'MLSD /public_html/facebook/0164/css'
*put* 'MLSD /public_html/facebook/0164/css\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 3 matches total\n'
*resp* '226-Options: -a -l \n226 3 matches total'
[2014-04-11T10:29:07][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:29:07][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/css/style.css
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,122,61)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,122,61)'
*cmd* 'RETR /public_html/facebook/0164/css/style.css'
*put* 'RETR /public_html/facebook/0164/css/style.css\r\n'
*get* '150-Accepted data connection\n'
*get* '150 5.0 kbytes to download\n'
*resp* '150-Accepted data connection\n150 5.0 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 118.63 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 118.63 Mbytes per second'
[2014-04-11T10:29:08][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\css\style.css created: 8dfc935c6f494048be67eaf7f4578cf6
Writing file /c/users/vtruba~1/appdata/local/temp/tmpw411ax-sublime-ftp/Real Techniques (realtechniques.com)/public_html/facebook/0164/css/style.css with encoding UTF-8 (atomic)
[2014-04-11T10:29:16][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:29:16][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:29:16][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/css/style.css
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,218,143)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,218,143)'
*cmd* 'RETR /public_html/facebook/0164/css/style.css'
*put* 'RETR /public_html/facebook/0164/css/style.css\r\n'
*get* '150-Accepted data connection\n'
*get* '150 5.0 kbytes to download\n'
*resp* '150-Accepted data connection\n150 5.0 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 51.27 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 51.27 Mbytes per second'
[2014-04-11T10:29:16][FTP.DEBUG]: comparing hashes on remote(8dfc935c6f494048be67eaf7f4578cf6) to local(8dfc935c6f494048be67eaf7f4578cf6)
[2014-04-11T10:29:16][FTP.DEBUG]: executing ftp command STOR /public_html/facebook/0164/css/style.css
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,227,91)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,227,91)'
*cmd* 'STOR /public_html/facebook/0164/css/style.css'
*put* 'STOR /public_html/facebook/0164/css/style.css\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.116 seconds (measured here), 42.81 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.116 seconds (measured here), 42.81 Kbytes per second'
[2014-04-11T10:29:17][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\css\style.css) remote(/public_html/facebook/0164/css/style.css)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpw411ax-sublime-ftp/Real Techniques (realtechniques.com)/public_html/facebook/0164/index.php with encoding UTF-8 (atomic)
[2014-04-11T10:30:15][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:30:15][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:30:15][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/index.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,105,63)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,105,63)'
*cmd* 'RETR /public_html/facebook/0164/index.php'
*put* 'RETR /public_html/facebook/0164/index.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 4.1 kbytes to download\n'
*resp* '150-Accepted data connection\n150 4.1 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 60.09 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 60.09 Mbytes per second'
[2014-04-11T10:30:15][FTP.DEBUG]: comparing hashes on remote(6684990b2d42cc0a727b0c4fc02f4853) to local(6684990b2d42cc0a727b0c4fc02f4853)
[2014-04-11T10:30:15][FTP.DEBUG]: executing ftp command STOR /public_html/facebook/0164/index.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,4,211)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,4,211)'
*cmd* 'STOR /public_html/facebook/0164/index.php'
*put* 'STOR /public_html/facebook/0164/index.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.115 seconds (measured here), 35.46 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.115 seconds (measured here), 35.46 Kbytes per second'
[2014-04-11T10:30:15][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\index.php) remote(/public_html/facebook/0164/index.php)
[2014-04-11T10:30:35][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:30:35][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:30:35][FTP.DEBUG]: executing ftp command MLSD /public_html/facebook/0164 meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,149,43)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,149,43)'
*cmd* 'MLSD /public_html/facebook/0164'
*put* 'MLSD /public_html/facebook/0164\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 9 matches total\n'
*resp* '226-Options: -a -l \n226 9 matches total'
[2014-04-11T10:30:38][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:30:38][FTP.DEBUG]: executing ftp command MLSD /public_html/facebook/0164/js meta: ['type', 'size', 'perm']
*cmd* 'OPTS MLST type;size;perm;'
*put* 'OPTS MLST type;size;perm;\r\n'
*get* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;\n'
*resp* '200  MLST OPTS type;size;sizd;modify;UNIX.mode;UNIX.uid;UNIX.gid;unique;'
*cmd* 'TYPE A'
*put* 'TYPE A\r\n'
*get* '200 TYPE is now ASCII\n'
*resp* '200 TYPE is now ASCII'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,100,227)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,100,227)'
*cmd* 'MLSD /public_html/facebook/0164/js'
*put* 'MLSD /public_html/facebook/0164/js\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-Options: -a -l \n'
*get* '226 3 matches total\n'
*resp* '226-Options: -a -l \n226 3 matches total'
[2014-04-11T10:30:39][FTP.DEBUG]: ftpbrowse.list.action called
[2014-04-11T10:30:39][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/js/scripts.js
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,162,166)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,162,166)'
*cmd* 'RETR /public_html/facebook/0164/js/scripts.js'
*put* 'RETR /public_html/facebook/0164/js/scripts.js\r\n'
*get* '150-Accepted data connection\n'
*get* '150 13.4 kbytes to download\n'
*resp* '150-Accepted data connection\n150 13.4 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 85.66 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 85.66 Mbytes per second'
[2014-04-11T10:30:39][FTP.DEBUG]: hash for c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\js\scripts.js created: 470e19675e362eac5dddb35e21c58ea2
Writing file /c/users/vtruba~1/appdata/local/temp/tmpw411ax-sublime-ftp/Real Techniques (realtechniques.com)/public_html/facebook/0164/js/scripts.js with encoding UTF-8 (atomic)
[2014-04-11T10:30:49][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:30:49][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:30:49][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/js/scripts.js
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,87,13)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,87,13)'
*cmd* 'RETR /public_html/facebook/0164/js/scripts.js'
*put* 'RETR /public_html/facebook/0164/js/scripts.js\r\n'
*get* '150-Accepted data connection\n'
*get* '150 13.4 kbytes to download\n'
*resp* '150-Accepted data connection\n150 13.4 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 124.79 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 124.79 Mbytes per second'
[2014-04-11T10:30:49][FTP.DEBUG]: comparing hashes on remote(470e19675e362eac5dddb35e21c58ea2) to local(470e19675e362eac5dddb35e21c58ea2)
[2014-04-11T10:30:49][FTP.DEBUG]: executing ftp command STOR /public_html/facebook/0164/js/scripts.js
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,241,60)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,241,60)'
*cmd* 'STOR /public_html/facebook/0164/js/scripts.js'
*put* 'STOR /public_html/facebook/0164/js/scripts.js\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.175 seconds (measured here), 76.78 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.175 seconds (measured here), 76.78 Kbytes per second'
[2014-04-11T10:30:50][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\js\scripts.js) remote(/public_html/facebook/0164/js/scripts.js)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpw411ax-sublime-ftp/Real Techniques (realtechniques.com)/public_html/facebook/0164/ajax.php with encoding UTF-8 (atomic)
[2014-04-11T10:40:00][FTP.DEBUG]: testing connection ftp://realtech@realtechniques.com:21/
[2014-04-11T10:40:00][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T10:40:00][FTP.DEBUG]: executing ftp command RETR /public_html/facebook/0164/ajax.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,137,242)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,137,242)'
*cmd* 'RETR /public_html/facebook/0164/ajax.php'
*put* 'RETR /public_html/facebook/0164/ajax.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.000 seconds (measured here), 7.10 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.000 seconds (measured here), 7.10 Mbytes per second'
[2014-04-11T10:40:00][FTP.DEBUG]: comparing hashes on remote(11e88fd242669e6579c5422642ef4daa) to local(11e88fd242669e6579c5422642ef4daa)
[2014-04-11T10:40:00][FTP.DEBUG]: executing ftp command STOR /public_html/facebook/0164/ajax.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (198,154,236,99,13,88)\n'
*resp* '227 Entering Passive Mode (198,154,236,99,13,88)'
*cmd* 'STOR /public_html/facebook/0164/ajax.php'
*put* 'STOR /public_html/facebook/0164/ajax.php\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.057 seconds (measured here), 12.20 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.057 seconds (measured here), 12.20 Kbytes per second'
[2014-04-11T10:40:00][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpw411ax-sublime-ftp\Real Techniques (realtechniques.com)\public_html\facebook\0164\ajax.php) remote(/public_html/facebook/0164/ajax.php)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
indexing [queue 43]: no files were indexed out of the 1 queued, abandoning crawl
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
indexing [queue 68]: no files were indexed out of the 2 queued, abandoning crawl
Writing file /C/xampp/htdocs/roots/up/app/controllers/CrawlerController.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/routes.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/controllers/CrawlerController.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/controllers/CrawlerController.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/models/Crawl.php with encoding UTF-8 (atomic)
indexing [queue 99]: no files were indexed out of the 1 queued, abandoning crawl
indexing [queue 100]: no files were indexed out of the 1 queued, abandoning crawl
Writing file /C/xampp/htdocs/roots/up/app/models/Crawl.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
indexing [queue 124]: no files were indexed out of the 1 queued, abandoning crawl
indexing [queue 130]: no files were indexed out of the 1 queued, abandoning crawl
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/models/Crawl.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/controllers/CrawlerController.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/list.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/list.blade.php with encoding UTF-8 (atomic)
indexing [queue 158]: no files were indexed out of the 1 queued, abandoning crawl
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/models/Crawl.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/controllers/CrawlerController.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/models/Crawl.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/list.blade.php with encoding UTF-8 (atomic)
indexing [queue 183]: no files were indexed out of the 1 queued, abandoning crawl
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/database/migrations/2014_04_07_155933_add_crawl_table.php with encoding UTF-8 (atomic)
indexing [queue 198]: no files were indexed out of the 1 queued, abandoning crawl
ReadDirectoryChangesW fails with ERROR_ACCESS_DENIED
Reloading /C/xampp/htdocs/roots/up/app/commands/CrawlerCommand.php
Reloading /C/xampp/htdocs/roots/up/app/routes.php
Reloading /C/xampp/htdocs/roots/up/app/controllers/CrawlerController.php
Reloading /C/xampp/htdocs/roots/up/app/commands/CrawlJob.php
Reloading /C/xampp/htdocs/roots/up/app/models/Crawl.php
Reloading /C/xampp/htdocs/roots/up/app/config/queue.php
Reloading /C/xampp/htdocs/roots/up/assets/css/style.css
Reloading /C/xampp/htdocs/roots/up/app/views/layout.blade.php
Reloading /C/xampp/htdocs/roots/up/app/lib/simple_html_dom.php
Reloading /C/xampp/htdocs/roots/up/app/models/Site.php
Reloading /C/xampp/htdocs/roots/up/app/database/migrations/2014_04_07_155933_add_crawl_table.php
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/list.blade.php with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/crawler/show.blade.php with encoding UTF-8 (atomic)
Writing file /C/Windows/System32/drivers/etc/hosts with encoding UTF-8 (atomic)
Writing file /C/Windows/System32/drivers/etc/hosts with encoding UTF-8 (atomic)
Writing file /C/xampp/htdocs/roots/up/app/views/site/export/ftp_sublime.blade.php with encoding UTF-8 (atomic)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpkxhz52-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/templates/nc_multivmenu/css/template.css with encoding UTF-8 (atomic)
[2014-04-11T14:35:39][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T14:35:39][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '421 Timeout - try typing a little faster next time\n'
*resp* '421 Timeout - try typing a little faster next time'
[2014-04-11T14:35:39][FTP.DEBUG]: exception while testing connection to inter.realtechniques.com: 421 Timeout - try typing a little faster next time
[2014-04-11T14:35:39][FTP.DEBUG]: executing ftp command QUIT
*cmd* 'QUIT'
*put* 'QUIT\r\n'
*get* ''
[2014-04-11T14:35:39][FTP.DEBUG]: exception while quitting FTP protocol:
[2014-04-11T14:35:39][FTP.DEBUG]: executing ftp command CONNECT
*get* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n'
*get* '220-You are user number 1 of 50 allowed.\n'
*get* '220-Local time is now 14:33. Server port: 21.\n'
*get* '220-This is a private system - No anonymous login\n'
*get* '220-IPv6 connections are also welcome on this server.\n'
*get* '220 You will be disconnected after 15 minutes of inactivity.\n'
*resp* '220---------- Welcome to Pure-FTPd [privsep] [TLS] ----------\n220-You are user number 1 of 50 allowed.\n220-Local time is now 14:33. Server port: 21.\n220-This is a private system - No anonymous login\n220-IPv6 connections are also welcome on this server.\n220 You will be disconnected after 15 minutes of inactivity.'
*cmd* 'USER realintl'
*put* 'USER realintl\r\n'
*get* '331 User realintl OK. Password required\n'
*resp* '331 User realintl OK. Password required'
*cmd* 'PASS ************'
*put* 'PASS ************\r\n'
*get* '230 OK. Current restricted directory is /\n'
*resp* '230 OK. Current restricted directory is /'
[2014-04-11T14:35:40][FTP.DEBUG]: executing ftp command RETR /public_html/templates/nc_multivmenu/css/template.css
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,18,28)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,18,28)'
*cmd* 'RETR /public_html/templates/nc_multivmenu/css/template.css'
*put* 'RETR /public_html/templates/nc_multivmenu/css/template.css\r\n'
*get* '150-Accepted data connection\n'
*get* '150 46.9 kbytes to download\n'
*resp* '150-Accepted data connection\n150 46.9 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.058 seconds (measured here), 0.79 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.058 seconds (measured here), 0.79 Mbytes per second'
[2014-04-11T14:35:40][FTP.DEBUG]: comparing hashes on remote(1e07a8fca826592dd3b920f90f5bd4c6) to local(1e07a8fca826592dd3b920f90f5bd4c6)
[2014-04-11T14:35:40][FTP.DEBUG]: executing ftp command STOR /public_html/templates/nc_multivmenu/css/template.css
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,167,119)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,167,119)'
*cmd* 'STOR /public_html/templates/nc_multivmenu/css/template.css'
*put* 'STOR /public_html/templates/nc_multivmenu/css/template.css\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.352 seconds (measured here), 133.24 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.352 seconds (measured here), 133.24 Kbytes per second'
[2014-04-11T14:35:41][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpkxhz52-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\templates\nc_multivmenu\css\template.css) remote(/public_html/templates/nc_multivmenu/css/template.css)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpkxhz52-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/templates/nc_multivmenu/css/template.css with encoding UTF-8 (atomic)
[2014-04-11T14:47:04][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T14:47:04][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T14:47:04][FTP.DEBUG]: executing ftp command RETR /public_html/templates/nc_multivmenu/css/template.css
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,188,31)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,188,31)'
*cmd* 'RETR /public_html/templates/nc_multivmenu/css/template.css'
*put* 'RETR /public_html/templates/nc_multivmenu/css/template.css\r\n'
*get* '150-Accepted data connection\n'
*get* '150 46.9 kbytes to download\n'
*resp* '150-Accepted data connection\n150 46.9 kbytes to download'
*get* '226-File successfully transferred\n'
*get* '226 0.058 seconds (measured here), 0.78 Mbytes per second\n'
*resp* '226-File successfully transferred\n226 0.058 seconds (measured here), 0.78 Mbytes per second'
[2014-04-11T14:47:04][FTP.DEBUG]: comparing hashes on remote(d7cbd98a7221744c7986abe96ee92002) to local(d7cbd98a7221744c7986abe96ee92002)
[2014-04-11T14:47:04][FTP.DEBUG]: executing ftp command STOR /public_html/templates/nc_multivmenu/css/template.css
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,221,54)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,221,54)'
*cmd* 'STOR /public_html/templates/nc_multivmenu/css/template.css'
*put* 'STOR /public_html/templates/nc_multivmenu/css/template.css\r\n'
*get* '150 Accepted data connection\n'
*resp* '150 Accepted data connection'
*get* '226-File successfully transferred\n'
*get* '226 0.350 seconds (measured here), 133.94 Kbytes per second\n'
*resp* '226-File successfully transferred\n226 0.350 seconds (measured here), 133.94 Kbytes per second'
[2014-04-11T14:47:05][FTP.DEBUG]: uploading file complete local(c:\users\vtruba~1\appdata\local\temp\tmpkxhz52-sublime-ftp\Real Techniques International (inter.realtechniques.com)\public_html\templates\nc_multivmenu\css\template.css) remote(/public_html/templates/nc_multivmenu/css/template.css)
Writing file /c/users/vtruba~1/appdata/local/temp/tmpo_w_yb-sublime-ftp/Real Techniques International (inter.realtechniques.com)/public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php with encoding UTF-8 (atomic)
[2014-04-11T14:48:25][FTP.DEBUG]: testing connection ftp://realintl@inter.realtechniques.com:21/
[2014-04-11T14:48:25][FTP.DEBUG]: executing ftp command NOOP
*cmd* 'NOOP'
*put* 'NOOP\r\n'
*get* '200 Zzz...\n'
*resp* '200 Zzz...'
[2014-04-11T14:48:25][FTP.DEBUG]: executing ftp command RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php
*cmd* 'TYPE I'
*put* 'TYPE I\r\n'
*get* '200 TYPE is now 8-bit binary\n'
*resp* '200 TYPE is now 8-bit binary'
*cmd* 'PASV'
*put* 'PASV\r\n'
*get* '227 Entering Passive Mode (142,4,24,154,242,46)\n'
*resp* '227 Entering Passive Mode (142,4,24,154,242,46)'
*cmd* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php'
*put* 'RETR /public_html/components/com_virtuemart/themes/default/templates/product_details/flypage_resp.tpl.php\r\n'
*get* '150-Accepted data connection\n'
*get* '150 15.1 kbytes to download\n'
*resp* '150-Accepted data connection\n150 15.1 kbytes to download'
`