#! python 3
# Finds phone numbers and email addresses on the clipboard

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4})
    (\s*(ext|ext.|x)\s*(\d{2,5}))?
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    (\w+(\.|\-)?)+          # username
    \@                      # @
    (\w+(\-|\.)?\w+){1,2}   # domain name that can contain some extra characters
    (\.[a-z]{2,4}\.?)       # extension
    ([a-z]{2,3})?           # could have second extension
    )''', re.VERBOSE | re.IGNORECASE)

textToSearch = pyperclip.paste()

matches = []

print(str(phoneRegex.findall(textToSearch)))

for phone in phoneRegex.findall(textToSearch):
    matches.append(phone[0])


for email in emailRegex.findall(textToSearch):
    matches.append(email[0])

pyperclip.copy('\n'.join(matches))