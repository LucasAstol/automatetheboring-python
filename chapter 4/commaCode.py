
theList = []

itemsNum = int(input('How many items do you want to enter?'))

for y in range(itemsNum):
    theItem = str(input('Enter item no. ' + str(y+1)+' '))
    if theItem != '':
        theList.append(theItem)
    else:
        theItem = str(input('Please enter something for item no. ' + str(y+1) + '. Otherwise item will be filled with blabla'))
        if theItem != '':
            theList.append(theItem)
        else:
            theList.append('blabla')

if len(theList) > 0:
    for x in range(len(theList)):
        if x+1 != len(theList):
            print(str(theList[x]), end=', ')
        else:
            print('and ' + str(theList[x]))
else:
    print('List is empty')