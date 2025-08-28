# Python File Management System
This project is a simple command-line file management system implemented in Python, originally developed as part of the JetBrains Academy curriculum (Python Developer Track). It allows users to perform various file and directory operations such as listing files, changing directories, removing files, moving files, creating directories, and copying files. The system is designed to be user-friendly and efficient, providing essential functionalities for managing files and directories.

## Features

- **List Files and Directories**: Users can list all files and directories in the current working directory. Options are available to display file sizes in different formats.
- **Change Directory**: Navigate through directories using the `cd` command, including the ability to move up one level.
- **Remove Files and Directories**: Delete files or entire directories with the `rm` command, including support for wildcard file extensions.
- **Move Files**: Move or rename files and directories using the `mv` command, with prompts to confirm overwriting existing files.
- **Create Directories**: Easily create new directories with the `mkdir` command.
- **Copy Files**: Copy files to a specified location, with checks to prevent overwriting existing files unless confirmed by the user.

## Usage

To use the file management system, run the script in a Python environment. The following commands are available:

- `ls`: List files and directories.
- `cd <directory>`: Change to the specified directory.
- `rm <file/directory>`: Remove the specified file or directory.
- `mv <old_name> <new_name>`: Move or rename a file or directory.
- `mkdir <directory_name>`: Create a new directory.
- `cp <source> <destination>`: Copy a file to the specified destination.
- `pwd`: Print the current working directory.
- `break`: Exit the program.

## Implementation Details

The program utilizes the following Python modules:

- `os`: For interacting with the operating system, including file and directory operations.
- `shutil`: For high-level file operations such as copying and moving files.
- `glob`: For file pattern matching.

## Future Enhancements

- Implement additional file search functionalities.
- Add support for file permissions and attributes.
- Enhance the user interface for better usability.







