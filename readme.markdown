# Sublime FTP Plugin
Because the rest of them suck

### About
This plugin was created to solve some of the missing features wanted in the popular SFTP package. The goal of this project is simple; create a fast, easy to use, ftp plugin thats open source. This project also aims to be a drop-in replacement for SFTP one day. It still has a way to go but progress is being made.

### Manual Installation
___
1. To install this plugin download the latest version of sublime here: http://www.sublimetext.com/3
2. In Sublime 3, navigate through the menu to Sublime > Preferences > Browse Packages... this will your Sublime Packages folder
3. Download the most recent version of this plugin via Git or the "Download Zip" button and extract (or clone) it to your Packages folder
4. Rename the folder to "FTP" all caps, so the configs can be read correctly
5. Restart Sublime and you're ready to go!

> I will eventually add this package to package control when its been a little more battle-tested

### Currently Working Functionality
___
- Connecting to FTP (SFTP and FTPS will come later, maybe even other protocols like webdav, etc. too)
- Creating, editing, deleting and connecting to servers
- Downloading, creating, renaming, deleting and chmod-ing files/folders
- Overwrite protection with hash checking (that works!)
- Display diff of remote and local file before overwriting
- Key bindings
- Settings (most of them, more to come)
- Menu items
- Status while connecting/peforming operations
- Hide files or folders that match regex
- Re-downloading/loading of current file
- Asyncronous functions (most of them)
- Diffing remote and currently open tab (from quick panel)
- Duplicate files

### Functionality in Development
___
- Output panel information
- Prompt for password (if user doesnt want to store it in config)
- Save new server config in actual config directory

### Todo
___
- cant delete empty directory
- create ability to cancel current operation
- optionally show folder/file info/permissions on a row
- Handle symlink files and folders correctly
- Disconnect from server when not in use using "quit" method on wrapper
- Prevent uploading of a file that is already uploading (quick double save fix)
- Verify config file settings
- Disallow certain operations on root folder, such as rename, delete, etc.
- On rename of file also change local versions name
- Implement folder syncing for easier file management (optionally ignoring regexs in config)

> Notes: This code needs some *MAJOR* refactoring as this was once just a proof-of-concept so you might see partially rebuilt classes from time to time

### License
___
[MIT](http://opensource.org/licenses/MIT) &copy; Alex Galletti