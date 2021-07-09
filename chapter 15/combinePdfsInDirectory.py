#! python3

import os, PyPDF2

pdfFiles = os.listdir('C:\Lucas\Educacion\Automate the boring stuff\chapter 15')
pdfWriter = PyPDF2.PdfFileWriter()

for i in range(len(pdfFiles)):
    if pdfFiles[i].endswith('.pdf'):
        pdfFile = open(os.path.join('C:\Lucas\Educacion\Automate the boring stuff\chapter 15', pdfFiles[i]), 'rb')
        pdfFileReader = PyPDF2.PdfFileReader(pdfFile)
        for pageNum in range(1, pdfFileReader.numPages):
            pdfWriter.addPage(pdfFileReader.getPage(pageNum))
        pdfFile.close()

outputFile = open('C:\\Lucas\\Educacion\\Automate the boring stuff\\chapter 15\\theCombinedOutput.pdf', 'wb')
pdfWriter.write(outputFile)
outputFile.close()