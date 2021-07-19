#! python3
# customWordIvitations.py - generates a word document with an invitation per page for each guest.


import os, docx, sys
from pathlib import Path

filePath = Path(sys.argv[1])
wordPath = Path(sys.argv[2])

if os.path.exists(str(filePath)) and os.path.exists(str(wordPath)):
    print('Opening guests file...')
    guestsFile = open(filePath)
    print('Opening word document...')
    wordDoc = docx.Document(str(wordPath))
    for line in guestsFile.readlines():
        print('Generating word document...')
        wordDoc.add_paragraph('It would be a pleasure to have you:').style = 'Style1 Main'
        wordDoc.add_paragraph(line).style = 'Style1 Guest'
        wordDoc.add_paragraph('at Wilhelm-hertz 8b on: ').style = 'Style1 Main'
        wordDoc.add_paragraph('January 16th').style = 'Style1 Date'
        wordDoc.add_paragraph('at 12 PM').style = 'Style1 Main' 
        print(wordDoc.paragraphs)

        lastPar = len(wordDoc.paragraphs) - 1    
        wordDoc.paragraphs[lastPar].runs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
            
    wordDoc.save(os.path.join(str(wordPath.parent), 'invitations.docx'))
    guestsFile.close()

print('Done!')