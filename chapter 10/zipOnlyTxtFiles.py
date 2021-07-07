#! python3
# zipOnlyTxtFiles.py - Creates a zip file with only .txt files within a given folder and subfolders.
# Zip file will contain same name as folder but incremental and will be placed in the destination folder.

import os, zipfile as zfile, re, pyinputplus as pyip


def onlyTxt(folder,destination):
    number = 1

    if(os.path.exists(f'{folder}')):
        folderName = os.path.basename(f'{folder}') # get folder name
        parentName = os.path.dirname(f'{folder}') # get folder's parent path
        print(f'{folderName} \n{parentName}')

        # generate zipName in destination folder
        while True:
            zipName = folderName + '_' + str(number) +'.zip'
            destinationPath = f'{destination}\{zipName}'
            # If it exists user has option to override it otherwise new incremental name is generated
            if(os.path.exists(f'{destinationPath}')): 
                if 'yes' == pyip.inputYesNo(f'{destinationPath} already exists. Do you want to replace it? '):
                    break
                else:
                    number += 1
                    continue
            else:
                break
        
        print('Creating ' + destinationPath + ' ...')
        theZipFile = zfile.ZipFile(f'{destinationPath}', 'w')

        for aFolder, subFolders, fileNames in os.walk(f'{folder}'):
            print(f'Adding folder: {aFolder} ...')
            theZipFile.write(aFolder)
            
            for filename in fileNames:
                if filename.endswith('.txt'):
                    print(f'Adding file: {filename} ...')
                    theZipFile.write(os.path.join(aFolder,filename))
    
    theZipFile.close()


onlyTxt('C:\Lucas\MailsFolder', 'C:\Lucas\paraZips')
