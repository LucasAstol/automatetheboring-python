#! python3

import re, sys
from pathlib import Path

if len(sys.argv) == 3:
    folder = Path(f'{sys.argv[1]}')
    userRegex = re.compile(f'{sys.argv[2]}')

    if (folder.exists() and folder.is_dir()):
        for filePath in list(folder.glob('*.txt')):
            print(f'Results for {filePath.name}:')
            for line in open(filePath, 'r').readlines():
                if userRegex.search(line) != None:
                    print(line)
    else:
        print("I'm sorry the specified folder does not exist nor it is not a directory")
