#! python3

import re, sys
from pathlib import Path

if len(sys.argv) == 2:
    p = Path(f'{sys.argv[1]}')
    textFile = open(p, 'r')
    textWords = textFile.read().split(' ')

    for i in range(len(textWords)):
        if textWords[i] == 'NOUN':
            textWords[i] = input('Please enter a noun: ')
        elif textWords[i] == 'ADJECTIVE':
            textWords[i] = input('Please enter an adjective: ')
        elif textWords[i] == 'ADVERB':
            textWords[i] = input('Please enter a adverb: ')
        elif textWords[i] == 'VERB': 
            textWords[i] = input('Please enter a verb: ')
    
       
    textFile.close()
    finalText = ' '.join(textWords)
    finalFile = open('finalText.txt', 'w')
    finalFile.write(finalText)
    finalFile.close()
