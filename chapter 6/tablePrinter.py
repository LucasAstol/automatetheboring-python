tableData=[['apples', 'oranges', 'cherries', 'banana'],
           ['Alice', 'Bob', 'Carol', 'David'],
           ['dogs', 'cats', 'moose', 'goose']]


def getLongestLength(innerList):
    longestLength=0
    for theString in innerList:
        if len(theString) > longestLength:
            longestLength = len(theString)
    return longestLength

def printTable(theList):
    colWidths = [0] * len(theList)
    for i in range(len(colWidths)):
        colWidths[i] = getLongestLength(theList[i])
    
    for x in range(len(theList[0])):
       # whtToPrint = [0]*len(theList)
        whtToPrint=''
        for y in range(len(theList)):
            whtToPrint = whtToPrint + theList[y][x].rjust(colWidths[y])+' '
            #whtToPrint[y] = theList[y][x].rjust(colWidths[y])
        print(whtToPrint)
        #print(' '.join(whtToPrint))

printTable(tableData)