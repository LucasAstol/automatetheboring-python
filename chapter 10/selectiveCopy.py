#! python3 
# selectiveCopy.py - Copies files with certain extension to a selected folder

import os, shutil

def copyFileToFolder(sourceFolder, extensions, destinationFolder):

    # is source a directory
    if os.path.isdir(f'{sourceFolder}'):
        # walkthrough folder and compare file extension with endswith
        for folder, subfolders, filenames in os.walk(f'{sourceFolder}'):
            for filename in filenames:
                for extension in extensions:
                    if filename.endswith(extension):
                        # copyfile
                        shutil.copy(os.path.join(folder,filename),os.path.join(destinationFolder,filename))

copyFileToFolder('C:\Lucas', ['.jpg', 'pdf'], 'C:\Myfolder')