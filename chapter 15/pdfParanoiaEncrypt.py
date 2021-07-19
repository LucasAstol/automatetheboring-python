#! python3
# pdfParanoiaEncrypt.py - searchs for PDF files in the given folder and subfolders, encrypts them and saves them to a new folder.

import PyPDF2, os, sys
import pyinputplus as pypi
from pathlib import Path

pathToPdfs = Path(r'%s',sys.argv[1])

os.mkdir('/scratch/home/lastolfi/Education/automatetheboring-python/new_encrypted')

for folder, subfolders, pdfFiles in os.walk(pathToPdfs):
    for aPdf in pdfFiles:
        if aPdf.endswith('.pdf'):
            pdfPath = os.path.join(folder, aPdf)
            
            thePdf = open(pdfPath, 'rb')
            pdfReader = PyPDF2.PdfFileReader(thePdf)
            if pdfReader.isEncrypted:
                passDecrypt = pypi.inputPassword(f'{os.path.basename(aPdf)} is already encrypted. Please enter pass to decrypt it: ')
                pdfReader.decrypt(passDecrypt)
            
            newPdfName = (Path(folder) / aPdf).stem + '_encrypted.pdf'
            newPdf = open(os.path.join('/scratch/home/lastolfi/Education/automatetheboring-python/new_encrypted', 
            newPdfName), 'wb')

            pdfWriter = PyPDF2.PdfFileWriter()
            for pageNum in range(pdfReader.numPages):
                pdfWriter.addPage(pdfReader.getPage(pageNum))

            passPdf = pypi.inputPassword(f'Please enter a pass to encrypt new pdf {newPdfName}: ')
            pdfWriter.encrypt(passPdf)
            pdfWriter.write(newPdf)

            newPdf.close()
            thePdf.close()

            



            


