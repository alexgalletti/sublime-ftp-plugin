# Sublime FTP Plugin
Because the rest of them suck ass

### Installation

1. To install this plugin download the latest version of sublime here: http://www.sublimetext.com/3
2. In Sublime 3, navigate through the menu to Sublime > Preferences > Browse Packages... this will your Sublime Packages folder
3. Download the most recent version of this plugin via Git or the "Download Zip" button and extract (or clone) it to your Packages folder
4. Rename the folder to "FTP" all caps, so the configs can be read correctly
5. Restart Sublime and you're ready to go!


### Currently Working Functionality
- Connecting to FTP (SFTP will come later, maybe even other protocols too)
- Creating, editing and connecting to sites
- Downloading, creating, renaming and deleting files
- Overwrite protection (that works!)
- Key bindings
- Menu items
- Status while connecting/peforming operations
- Connection progress
- Settings file should actually use and pull in settings
- Chmod files/folders
- Hide hidden files or items that match regex
- Re-downloading of current file

### Functionality in Development
- Diffing remote and currently open tab (from quick panel)
- Output panel information
- Prompt for password (if user doesnt want to store it in config)
- Asyncronous functions
- Save new server config in actual config directory

### Todo
- Handle symlink files and folders correctly
- Disconnect from server when not in use using "quit" method on wrapper
- Prevent uploading of a file that is already uploading (quick double save fix)
- Verify config file settings
- Disallow certain operations on root folder, such as rename, delete, etc.
- On rename of file also change local versions name
- Implement folder syncing for easier file management
- For folder syncing create option for downloading all code/text files, optionally ignoring regexs in config

> Notes: This code needs some *MAJOR* refactoring as this was once just a proof-of-concept so you might see partially rebuilt classes from time to time

### Documentation

Official: http://www.sublimetext.com/docs/3/api_reference.html
Non-Official: http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/extensibility/plugins.html