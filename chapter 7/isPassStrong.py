import re

lengthRegex = re.compile(r'^([A-Z]|[a-z]|\d){8,}$')

upperregex = re.compile(r'[A-Z]+')

lowerRegex = re.compile(r'[a-z]+')

digitsRegex = re.compile(r'\d+')

def strongPass(thePass):
    mo1 = lengthRegex.search(thePass)
    mo2 = upperregex.search(thePass)
    mo3 = lowerRegex.search(thePass)
    mo4 = digitsRegex.search(thePass)

    if(mo1 != None and mo2 != None and mo3 != None and mo4 != None):
        return 'Pass is strong'
    else:
        return 'Pass is not strong'

print(strongPass('3tyhERe33'))