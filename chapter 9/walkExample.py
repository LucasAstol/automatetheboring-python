import os

for folderName, subFolders, files in os.walk('C:\\Lucas'):
    print(folderName)

    for subFolder in subFolders:
        print(f'Subfolder in {folderName} is: {subFolder}')

    for theFile in files:
        print(f'File in {folderName} is: {theFile}')

