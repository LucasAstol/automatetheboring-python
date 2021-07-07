#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: python.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        python.exe mcb.pyw <keyword> - Loads keyword to cilpboard
#        python.exe mcb.pyw list - Loads all keywords to clipboard
#        python.exe mcb.pyw delete <keyword> - Deletes keyword
#        python.exe mcb.pyw delete -a - Deletes all keywords

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] == '-a':
            mcbShelf.clear()
        elif sys.argv[2].lower() in mcbShelf:
            del mcbShelf[sys.argv[2].lower()]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()