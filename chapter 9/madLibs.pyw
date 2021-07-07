#! python3

import re, sys

toReplace = re.compile(r'(NOUN|ADJECTIVE|ADVERB|VERB){1}')


if (sys.argv) == 2:
    p = Path(r'%s' % (sys.argv[1]))
    textFile = open(p, 'w')
    textWords = textFile.read().split(' ')

    for i in range(len(textWords)):
        if textWords[i] == 'NOUN':
            textWords[i] = input('Please enter a noun')
        elif textWords[i] == 'ADJECTIVE':
            textWords[i] = input('Please enter an adjective')
        elif textWords[i] == 'ADVERB':
            textWords[i] = input('Please enter a adverb')
        elif textWords[i] == 'VERB': 
            textWords[i] = input('Please enter a verb')
    
    finalText = ' '.join(textWords)
    textFile.write(finalText)
    textFile.close()


    


