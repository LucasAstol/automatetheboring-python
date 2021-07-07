import os, zipfile
from pathlib import Path

p = Path(r'C:\Lucas')

theZip = zipfile.ZipFile(p / 'pdfs.zip')
for afile in theZip.namelist():
    print(f'{afile} compressed size: {theZip.getinfo(afile).compress_size}')
