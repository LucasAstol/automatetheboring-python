#! python3
# findBiggestFolder.py - finds the folder with most number of files in the given path.

import os

def findBiggestFolderIn(mainFolder):
    
    if os.path.isdir(f'{mainFolder}'):

        theBigOne = {'path':'', 'files':0}

        for folder, subfolder, filename in os.walk(mainFolder):
            # Avoid using the mainfolder since we want to search for the folders inside the main folder    
            if folder != 'C:\Lucas':
                if len(filename) > theBigOne.get('files'):
                    theBigOne['path'] = folder
                    theBigOne['files'] = len(filename)

        print(f"{theBigOne.get('path')} is the biggest folder with {theBigOne.get('files')} files")                    

findBiggestFolderIn('C:\Lucas')