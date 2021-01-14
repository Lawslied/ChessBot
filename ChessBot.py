import chess

#Copied from some stackoverflow page
#The guy coded thiis for only starting position for some reason
def printCrntSquares(board:chess.Board):
    print(" square | row | col | type | piece | color | field")
    print("--------+-----+-----+------+-------+-------+------")
    for row in range(0,8):
         for col in range(0,8):
            squareIndex=row*8+col
            square=chess.SQUARES[squareIndex]
            piece = board.piece_at(square)
            fieldColor=(col+row)%2==1
            if piece is None:
                assert row in {2,3,4,5}
            else:
                print("%7d | %3d | %3d | %4d | %5s | %4s | %4s" % (square,row,col,piece.piece_type,piece.symbol(),"white" if piece.color else "black","black" if col%2!=row%2 else "white"))
            if row in {0,1}:
              assert piece.color==chess.WHITE
              # white symbols are upper case
              assert ord(piece.symbol())>ord('A') and ord(piece.symbol())<ord('Z')
            if row in {6,7}:
              assert piece.color==chess.BLACK
              # black symbols are lower case
              assert ord(piece.symbol())>ord('a') and ord(piece.symbol())<ord('z')

'''

blckPawn1 = chess.Piece(1,0)
blckPawn2 = chess.Piece(1,0)
blckPawn3 = chess.Piece(1,0)
blckPawn4 = chess.Piece(1,0)
blckPawn5 = chess.Piece(1,0)
blckPawn6 = chess.Piece(1,0)
blckPawn7 = chess.Piece(1,0)
blckPawn8 = chess.Piece(1,0)

blckKnght1 = chess.Piece(2,0)
blckKnght2 = chess.Piece(2,0)

blckBshp1 = chess.Piece(3,0)
blckBshp2 = chess.Piece(3,0)

blckRook1 = chess.Piece(4,0)
blckRook2 = chess.Piece(4,0)

blckQnn = chess.Piece(5,0)
blckKng = chess.Piece(6,0)



whtPawn1 = chess.Piece(1,1)
whtPawn2 = chess.Piece(1,1)
whtPawn3 = chess.Piece(1,1)
whtPawn4 = chess.Piece(1,1)
whtPawn5 = chess.Piece(1,1)
whtPawn6 = chess.Piece(1,1)
whtPawn7 = chess.Piece(1,1)
whtPawn8 = chess.Piece(1,1)

whtKnght1 = chess.Piece(2,1)
whtKnght2 = chess.Piece(2,1)

whtBshp1 = chess.Piece(3,1)
whtBshp2 = chess.Piece(3,1)

whtRook1 = chess.Piece(4,1)
whtRook2 = chess.Piece(4,1)

whtQnn = chess.Piece(5,1)
whtKng = chess.Piece(6,1)
'''

board = chess.Board()


print("\n-----START-----\n")
print(board.unicode())


printCrntSquares(board)


print("\n-------1-------\n")
moveToPlay = ""
maxMoveRate =  0

print(board.legal_moves)

def printCrntSquares(board:chess.Board):
    for row in range(0,8):
         for col in range(0,8):
            squareIndex=row*8+col
            square=chess.SQUARES[squareIndex]
            piece = board.piece_at(square)
            fieldColor=(col+row)%2==1

            if piece.color == board.turn:
                pieceType = piece.piece_type
                pieceColor = piece.color

                if pieceType == 1:
                else if pieceType == 2:
                else if pieceType == 3:
                else if pieceType == 4:
                else if pieceType == 5:
                else:

'''
            if piece is None:
                assert row in {2,3,4,5}
            else:
                print("%7d | %3d | %3d | %4d | %5s | %4s | %4s" % (square,row,col,piece.piece_type,piece.symbol(),"white" if piece.color else "black","black" if col%2!=row%2 else "white"))
            if row in {0,1}:
              assert piece.color==chess.WHITE
              # white symbols are upper case
              assert ord(piece.symbol())>ord('A') and ord(piece.symbol())<ord('Z')
            if row in {6,7}:
              assert piece.color==chess.BLACK
              # black symbols are lower case
              assert ord(piece.symbol())>ord('a') and ord(piece.symbol())<ord('z')

'''

print(board_unicode())    

