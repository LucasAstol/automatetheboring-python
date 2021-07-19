#! python3
# pdfParanoiaDecrypt.py - decrypts all files in a given folder.

import PyPDF2, os, sys, pyinputplus as pypi
from pathlib import Path

encryptedFolder = Path('/scratch/home/lastolfi/Education/automatetheboring-python/chapter 15')
#Path(r'%s',sys.argv[1])

if (os.path.exists(encryptedFolder) and os.path.isdir(encryptedFolder)):
    decryptFolder = encryptedFolder / 'new_decrypted'
    decryptFolder.mkdir(exist_ok=True)
    for folder, subfolders, filenames in os.walk(encryptedFolder):
        for filename in filenames:
            if filename.endswith('.pdf'):
                print('unpdf')
                basePdf = open(os.path.join(folder,filename),'rb')
                pdfReader = PyPDF2.PdfFileReader(basePdf)
                if pdfReader.isEncrypted:
                    print('is encrypted')
                    thePass = pypi.inputPassword(f'Please enter the pass to decrypt the file {filename}: ')
                    if pdfReader.decrypt(thePass) == 0:
                        continue

                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))
                    
                    newPdf = open(os.path.join(str(decryptFolder), 'decrypt_' + filename), 'wb')

                    pdfWriter.write(newPdf)
else:
    print('Path does not exist')
                     


                
