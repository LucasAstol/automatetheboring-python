#! python3
# removeCsvHeaders.py - removes the first line of a csv

import csv, os, sys

folderPath = sys.argv[1]

for aFile in os.listdir(folderPath):
    if aFile.endswith('.csv'):
        csvFile = open(os.path.join(folderPath, aFile))
        csvReader = csv.reader(csvFile)
        newCsvfile = open('withoutHeader' + aFile, 'w', newline = '')
        csvWriter = csv.writer(newCsvfile)
        for aLine in csvReader:
            if csvReader.line_num != 1:
                csvWriter.writerow(aLine)
        csvFile.close()
        newCsvfile.close()
