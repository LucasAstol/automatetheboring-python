#! python3
# renameDateds.py - Renames files with American date format MM-DD-YYYY to European format DD-MM-YYYY

import os, re
from pathlib import Path

americanRe = re.compile(r'^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$')

mailsFolder = Path(f'C:\Lucas\MailsFolder')

for mail in mailsFolder.glob('*.txt'):
    mo = americanRe.search(mail.name)
    if mo != None:
        print('File to be changed: ' + mail.name)
        beforeDate = mo.group(1)
        theMonth = mo.group(2)
        theDay = mo.group(4)
        theYear = mo.group(6)
        afterDate = mo.group(8)

        newName = f'{beforeDate}{theDay}-{theMonth}-{theYear}{afterDate}'
        print('New name will be: ' + newName + '\n')
        os.rename(mailsFolder / mail.name, mailsFolder / newName)

print(os.listdir(mailsFolder))
    


