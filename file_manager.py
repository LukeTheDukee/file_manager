import os
import shutil
import glob
from shutil import SameFileError

# run the user's program in our generated folders
# os.chdir("module/root_folder")


def list_f_and_dir(options):
    folders_and_files = os.listdir()
    file_list = []
    directory_list = []

    for item in folders_and_files:
        if "." in item:
            file_list.append(item)
        else:
            directory_list.append(item)

    # Print directories first
    for directory in directory_list:
        print(directory)

    # Handle file listing based on options
    if len(options) < 2:
        for file in file_list:
            print(file)
    elif options[1] == "-l":
        for file in file_list:
            print(f"{file} {os.path.getsize(file)}")
    elif options[1] == "-lh":
        for file in file_list:
            size = os.path.getsize(file)
            if size < 1024:
                print(f"{file} {size}B")
            elif size < 1024**2:
                print(f"{file} {size // 1024}KB")
            elif size < 1024**3:
                print(f"{file} {size // (1024**2)}MB")
            else:
                print(f"{file} {size // (1024**3)}GB")


def manipulate_directory(option):
    if len(option) < 2:
        print("Invalid command")  # Handle missing path
        return

    path = input_command[1]
    try:
        if path == "..":
            os.chdir("..")  # Go up one directory
            print(os.getcwd())
        else:
            os.chdir(path)  # Change to the specified directory
            print(os.getcwd())
    except FileNotFoundError:
        print("Invalid path")  # Handle invalid path


def prompt_user(file):
    print(
        f"{file} already exists in this directory. Replace? (y/n): ", end="", flush=True
    )
    user_input = input()
    return user_input


def remove_file(option):
    if len(option) < 2:
        print("Specify the file or directory")  # Handle missing path
        return

    path = option[1]

    # Find all files matching the extension in cwd and delete them
    if option[1].startswith("."):
        special_paths = glob.glob(f"*{path}")

        if not special_paths:
            print(f"File extension {path} not found in this directory")
        else:
            for file in special_paths:
                full_path = os.path.join(os.getcwd(), file)
                if os.path.isfile(full_path):
                    os.remove(full_path)
        return

    if not os.path.isdir(path):
        print("No such file or directory")
        return
    else:
        shutil.rmtree(path)

    if not os.path.isfile(path):
        print("No such file or directory")
        return
    else:
        os.remove(path)


def move_file(option):
    if len(option) != 3:
        print(
            "Specify the current name of the file or directory and the new location and/or name"
        )  # Handle missing path
        return

    old_name = input_command[1]
    new_name = input_command[2]

    path = option[1]

    if option[1].startswith("."):
        special_paths = glob.glob(f"*{path}")

        if not special_paths:
            print(f"File extension {path} not found in this directory")
            return

        for file in special_paths:
            full_path = os.path.join(os.path.abspath(option[2]), file)
            if os.path.isfile(full_path):
                while True:
                    answer = prompt_user(file)
                    if answer == "y":
                        os.remove(full_path)
                        # Copy the file after removing the existing one
                        shutil.copy(os.path.join(os.getcwd(), file), full_path)
                        break  # Exit the loop after copying
                    elif answer == "n":
                        break  # Exit the loop and skip copying this file
            else:
                # Copy the file if it doesn't already exist
                shutil.copy(os.path.join(os.getcwd(), file), full_path)
        return

    if os.path.isfile(new_name):
        print("The file or directory already exists")
        return

    try:
        shutil.move(old_name, new_name)
    except FileNotFoundError:
        print("No such file or directory")


def make_directory(option):
    if len(option) < 2:
        # Handle missing path
        print("Specify the name of the directory to be made")
        return

    path = option[1]

    if os.path.isdir(path):
        print("The directory already exists")
        return
    else:
        os.mkdir(path)


def copy_file(option):
    if len(option) < 3:
        print(
            "\nSpecify the file which should be copied and the target directory/name."
        )
        return

    path = option[1]
    target_directory = option[2]

    if option[1].startswith("."):
        special_paths = glob.glob(f"*{path}")

        if not special_paths:
            print(f"File extension {path} not found in this directory")
            return

        for file in special_paths:
            full_path = os.path.join(target_directory, file)

            if os.path.isfile(full_path):
                answer = prompt_user(file)
                while True:
                    if answer.lower() == "y":
                        os.remove(full_path)
                        # Copy the file after removing the existing one
                        shutil.copy(os.path.join(os.getcwd(), file), full_path)
                        break  # Exit the loop after copying
                    elif answer.lower() == "n":
                        break  # Exit the loop and skip copying this file
                    else:
                        answer = prompt_user(file)
            else:
                # Copy the file if it doesn't already exist
                shutil.copy(os.path.join(os.getcwd(), file), full_path)
        return

    if not (os.path.isdir(option[1]) or os.path.isfile(option[1])):
        print("No such file or directory")
        return
    elif len(option) != 3:
        print(
            "Specify the current name of the file or directory and the new location and/or name"
        )
        return
    else:
        try:
            shutil.copy(option[1], option[2])
        except SameFileError:
            print(f"{option[1]} already exists in this directory")
            return


# Loop to get the file manager running
counter = 0

print("Input the command")

while True:
    input_command = input().split()

    if not input_command:
        continue  # Skip empty input

    command = input_command[0]

    match command:
        case "break":
            break

        case "pwd":
            print(os.getcwd())

        case "ls":
            list_f_and_dir(input_command)

        case "cd":
            manipulate_directory(input_command)

        case "rm":
            remove_file(input_command)

        case "mv":
            move_file(input_command)

        case "mkdir":
            make_directory(input_command)

        case "cp":
            copy_file(input_command)

        case _:
            print("Invalid command")  # Handle unknown commands
