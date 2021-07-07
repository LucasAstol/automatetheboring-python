import zipfile as zfile

newZip = zfile.ZipFile('C:\\Lucas\\blabla.zip', 'w')

newZip.write('C:\\Lucas\\forPython.txt', compress_type=zfile.ZIP_DEFLATED)
newZip.close()

newZip = zfile.ZipFile('C:\\Lucas\\blabla.zip', 'a')
newZip.write('C:\\Lucas\\forPython2.txt', compress_type=zfile.ZIP_DEFLATED)
newZip.close()