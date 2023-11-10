#!/usr/bin/env python3

import argparse
import shlex
import subprocess
import json
import webbrowser
import os

# File to store the shortcuts
SHORTCUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shortcuts.json')

# Function to add a shortcut
def add_shortcut(shortcut, url):
    try:
        with open(SHORTCUT_FILE, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

    data[shortcut] = url

    with open(SHORTCUT_FILE, 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Shortcut '{shortcut}' added for URL: {url}")


# Function to open a shortcut
def open_shortcut(shortcut):
    try:
        with open(SHORTCUT_FILE, 'r') as f:
            data = json.load(f)
            if shortcut in data:
                url = data[shortcut]
                #subprocess.run(shlex.split(f'wsl {url}'))
                webbrowser.open(url)
            else:
                print(f"No URL found for shortcut '{shortcut}'")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("No shortcuts found. Please add some shortcuts first.")


# Command line argument parser
parser = argparse.ArgumentParser(description='URL shortcut manager')
subparsers = parser.add_subparsers(dest='command', help='Available commands')

# Subparser for adding a shortcut
add_parser = subparsers.add_parser('add', help='Add a new shortcut')
add_parser.add_argument('shortcut', type=str, help='The shortcut name')
add_parser.add_argument('url', type=str, help='The URL to associate with the shortcut')

# Subparser for opening a shortcut
open_parser = subparsers.add_parser('open', help='Open a URL using a shortcut')
open_parser.add_argument('shortcut', type=str, help='The shortcut name')

# Parse the command line arguments
args = parser.parse_args()

# Perform the appropriate action based on the provided command
if args.command == 'add':
    add_shortcut(args.shortcut, args.url)
elif args.command == 'open':
    open_shortcut(args.shortcut)
else:
    parser.print_help()
