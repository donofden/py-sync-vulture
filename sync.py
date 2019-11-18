#!/usr/bin/python
import os
import sys
import subprocess
import platform
import os.path
import time
import argparse


# sync files between source and destination
def sync(src, file, dest):
    if not os.path.isfile(dest + '/' + file):
        # Not Exist, Copy file to destination
        copy_file(src, file, dest)
    else:
        # Exist in destination check for any changes
        destination_file = dest + '/' + file
        source_file = src + '/' + file

        if last_modified_date(source_file) != last_modified_date(destination_file):
            # copy file to destination
            copy_file(src, file, dest)


# copy file to destination
def copy_file(src, file, dest):
    rsync = 'rsync --times '
    # Only show progress when we're running in a terminal (and not cron):
    if sys.stdout.isatty():
        rsync = rsync + '--progress '
    cmd = rsync + ' "' + src + '/' + file + '" "' + dest + '/' + file + '"'
    process = subprocess.Popen(cmd, shell=True)
    try:
        process.wait()
    except KeyboardInterrupt:
        process.kill()
        sys.exit(1)


# Function will return last modified date of a file
def last_modified_date(path_to_file):
    """
        Try to get the date that a file was created, falling back to when it was
        last modified if that isn't possible.
        See http://stackoverflow.com/a/39501288/1709587 for explanation.
        """
    if platform.system() == 'Windows':
        return time.ctime(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        return time.ctime(stat.st_mtime)


# Function will return creation date of a file
def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return time.ctime(os.path.getctime(path_to_file))
    else:
        stat = os.stat(path_to_file)
        try:
            return time.ctime(stat.st_birthtime)
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


# Check is the directory exist else create directory
def is_directory_exist(dest):
    # if we're in a directory that doesn't exist in the destination folder
    # then create a new folder
    if not os.path.isdir(dest):
        os.mkdir(dest)
        print('Directory created at: ' + dest)
    return 1

# Here is where all madness happens!!!
def main():
    # use argparse to get source and destination
    parser = argparse.ArgumentParser(
        description="""Py-Sync""",
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument(
        '-src', help='Specify the full path of source folder in this machine', required=True)
    parser.add_argument(
        '-dest', help='Specify the full path of destination folder in this machine', required=True)
    args = parser.parse_args()

    if args.src == '':
        print("Please enter full path of source folder.")
    else:
        src = args.src

    if args.dest == '':
        print("Please enter full path of source folder.")
    else:
        dest = args.dest

    print("----------------------------------------------------------")
    print("Source Folder        : " + src)
    print("Destination Folder   : " + dest)
    # python3 sync.py -src='/Users/aravindkumar/Year_End_Report' -dest='/Users/aravindkumar/test-sysn'
    print("----------------------------------------------------------")

    for root, dirs, files in os.walk(src):
        # figure out where we're going
        dest = dest + root.replace(src, '')

        # Check is the directory exist else create directory
        is_directory_exist(dest)

        # loop through all files in the directory
        for f in files:
            if f.startswith(".") or f.endswith(".DS_Store"):
                continue
            sync(root, f, dest)


if __name__ == "__main__":
    # calling main function
    main()
