#! python3
# pdfPassBreaker.py - tries to guess the password of an encrypted pdf file 
#                       provided that it is within the 44K words contained in a txt file whether lowercase or uppercase


import sys, PyPDF2
from pathlib import Path

pdfPath = sys.argv[1]
pdfFile = open(pdfPath, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)

dictionary = open(Path(r'%s', sys.argv[2]))

for line in dictionary.readlines():
    line = line.strip()
    if pdfReader.decrypt(line.lower()) != 0:
        print('Password found: ' + line.lower())
        break
    elif pdfReader.decrypt(line.upper()) != 0:
        print('Password found: ' + line.upper())
        break

pdfFile.close()
dictionary.close()