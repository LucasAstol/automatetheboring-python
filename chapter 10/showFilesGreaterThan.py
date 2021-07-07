#! python3
# showFilesGreaterThan.py - shows files whose size is greater than a desired value

import os

def showFilesWithSizeGreaterThan(folder,size):

    for aFolder, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if os.path.getsize(os.path.join(aFolder,filename))/1000000 > size:
                print(filename)

showFilesWithSizeGreaterThan('C:\Lucas', 20)