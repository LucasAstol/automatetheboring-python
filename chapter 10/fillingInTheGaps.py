#! python3
# fillingInTheGaps.py - 


import os, re
from pathlib import Path

def fillIntheGaps(folder,prefix):

    theRegex = re.compile(f'{prefix}')

    folder = os.path.abspath(f'{folder}')
    p = Path(f'{folder}')

    numbering = 1
    files = list(p.glob('*'))

    if p.is_dir():
        for filename in files:
            mo = theRegex.search(filename.name)
            if mo != None:
                if int(mo.group(3)) > numbering:
                    print(filename)
                    print(mo.group(3))
                    newName = p / (mo.group(1) + mo.group(2) + str(numbering) + mo.group(4)) 
                    filename.rename(newName)   
                numbering = numbering + 1     

fillIntheGaps('C:\Lucas\ToNumber', '^(spam)(0+)(\d+)(.txt)$')