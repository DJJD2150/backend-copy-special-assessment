#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# give credits
__author__ = "DJJD2150, got help from Kano Marvel, Nikal Morgan's walkthrough zoom meeting"

import re
import os
import sys
import shutil
import subprocess
import argparse


def get_special_paths(dirname):
    """Given a dirname, returns a list of all its special files."""
    # creates an empty list "path_list" to eventually list all of the absolute paths 
    path_list = []
    # lists the directory path names
    paths = os.listdir(dirname)
    # loops through the files in each of the listed directories
    for filename in paths:
        # regex statement checks to see whether or not the characters "__", followed by a word
        # of one or more letters, then another "__", exist in the file name
        special_file = re.findall(r'__(\w+)__', filename)
        # If the regex statement's conditions are met, then the absolute path is appended to the
        # "path_list" list
        if special_file: 
            # os.path.abspath gets the absolute path for the file name
            path_list.append(os.path.abspath(filename))
    # print(path_list)
    return path_list


def copy_to(path_list, dest_dir):
    """Returns a directory copy containing all the special files listed in the 'get_special_paths' function."""
    # if the "dest_dir" directory doesn't currently exist, make the directory
    # if it does exist, don't do anything though.  This conditional just makes 
    # sure the directory is created or already exists before the next step.
    if not os.path.isdir(dest_dir):
        # os.path.isdir checks to see if it's a directory, os.makedirs makes a directory
        os.makedirs(dest_dir)
    # loops through the paths in path_list,
    for path in path_list:
        # copy "path" to the location "dest_dir"
        # shutil.copy's first argument is what you're copying
        # the second argument is where you're adding the copy to 
        shutil.copy(path, dest_dir)
    return


def zip_to(path_list, dest_zip):
    """Returns a zip file containing the directory copy created in the 'copy to' function."""
    for path in path_list:
        print(f'zip -j {dest_zip} {path}')
        subprocess.run(['zip', '-j', dest_zip, path])
    return


def main(args):
    """Main driver code for copyspecial."""
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    # TODO: add one more argument definition to parse the 'from_dir' argument
    parser.add_argument('from_dir', help='find dir for special files')
    ns = parser.parse_args(args)

    # TODO: you must write your own code to get the command line args.
    # Read the docs and examples for the argparse module about how to do this.

    # Parsing command line arguments is a must-have skill.
    # This is input data validation. If something is wrong (or missing) with
    # any required args, the general rule is to print a usage message and
    # exit(1).

    # Your code here: Invoke (call) your functions
    if len(sys.argv) < 1:
        parser.print_usage()
    path_list = get_special_paths(ns.from_dir) # ns.from_dir gets the files from the given directory
    # calls the "copy_to" function if the "--todir" command is typed, or calls the "zip_to" function
    # if the "--tozip" command is typed, otherwise it just prints the various paths listed in "path_list"
    if ns.todir:
        copy_to(path_list, ns.todir)
    elif ns.tozip:
        zip_to(path_list, ns.tozip)
    else:
        for path in path_list:
            print(path)
    # print(get_special_paths("."))

if __name__ == "__main__":
    main(sys.argv[1:])
