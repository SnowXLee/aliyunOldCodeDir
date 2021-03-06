#! python
# multiclipboard.pyw - Saves and loads pieces of text to the clipboard.
"""
 Usage: py.exe multiclipboard.pyw save <keyword> - Saves clipboard to
keyword.
 py.exe multiclipboard.pyw <keyword> - Loads keyword to clipboard.
 py.exe multiclipboard.pyw list - Loads all keywords to clipboard.
"""

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
  mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
  
# List keywords and load content.

mcbShelf.close()
