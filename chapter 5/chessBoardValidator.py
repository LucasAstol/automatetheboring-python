theBoard = {'1f':'bpawn'}

def validate_the_board():
    numPieces = True
    if 32 != len(list(theBoard.values())):
        numPieces = False
        print('Invalid amount of total pieces: ' + str(len(list(theBoard.values()))))

    keysNames = True
    for k in theBoard.keys():
        if int(k[0]) not in range(1,9) or k[1] not in ['a','b','c','d','e','f','g','h']:
            print()
            print('The following space is not valid: ' + k)
            keysNames = False 

    piecesColors = True
    for v in theBoard.values():
        if v[0] not in ['b','w'] or v[1:len(v)] not in ['pawn','knight','bishop','rook','queen','king']:
            print('The following piece is not valid: ' + v )
            piecesColors = False
        
    if numPieces and keysNames and piecesColors:
        print('Valid board')
    else:
        print('Invalid board')

validate_the_board()