#! python3
# mapIt.py - opens a google maps page and search for the given address

import webbrowser, sys, pyperclip as pyp

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard
    address = pyp.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)