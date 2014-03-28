# Sublime FTP Plugin
Because the rest of them suck ass

## Currently Working Functionality
- Connecting to FTP (SFTP will come later, maybe even other protocols too)
- Creating, editing and connecting to sites
- Downloading, creating, renaming and deleting files
- Overwrite protection (that works!)
- Key bindings
- Menu items

## Functionality in Development
- Diffing remote and currently open tab (from quick panel)
- Chmod files/folders
- Settings file should actually use and pull in settings
- Output panel information
- Asyncronous functions
- Connection progress
- Prompt for password (if user doesnt want to store it in config)
- Save new server config in actual config directory

## Todo
- Status while connecting/peforming operations
- Verify config file settings
- Disallow certain operations on root folder, such as rename, delete, etc.
- On rename of file also change local versions name
- Implement folder syncing for dreamweaver like file management
- For folder syncing create option for downloading all code/text files, optionally ignoring regexs in config

> Notes: This code needs some *MAJOR* refactoring as this was once just a proof-of-concept so you might see partially rebuilt classes from time to time

### Documentation

Official: http://www.sublimetext.com/docs/3/api_reference.html
Non-Official: http://sublime-text-unofficial-documentation.readthedocs.org/en/latest/extensibility/plugins.html