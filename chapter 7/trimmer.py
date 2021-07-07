import re

def modifyTheText(theText, anyCharacters=None):
    if(anyCharacters == None):
        trimmingRegex = re.compile(r'( *)(.+)( *)')
        return trimmingRegex.sub(r'\2', theText)
    else:
        customRegex = re.compile(r'([^'+anyCharacters+']*)(['+ anyCharacters + ']*)([^'+anyCharacters+']*)')
        return customRegex.sub(r'\1\3',theText)

print(modifyTheText(' blaba ','l'))