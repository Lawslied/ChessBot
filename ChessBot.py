import chess


              
def MoveGenerator(board:chess.Board,int:square):

	mvList = []
	piece = board.piece_at(square)


	if piece.color == board.turn:
		pieceType = piece.piece_type
		pieceColor = piece.color
                
		pieceSquare = chess.square_name(square)
		#0-A 7-H
		pieceFile = chess.square_file(square)
		pieceRank = chess.square(square)
                
		#PAWN
		if pieceType == 1:

			#Taking to right
			#Cant take to right if its on the right side of the board
			#Or its on the 7th rank of the board(2th rank for black)
			if (square + 1) % 2 != 0:
				if board.piece_at(square + 9) is not None and square < 55:
					mvList.append(str(ord(pieceFile)+1) + str(pieceRank+1))
                        	
			#Taking to left
			#Cant take to left if its on the left side of the board
			#or itss on the 7th rank of the board
			if square % 2 != 0:
				if board.piece_at(square + 7) is not None and square < 55 and square != 48:
					mvList.append(str(ord(pieceFile)-1) + str(pieceRank+1))
                        	
			if square < 56 and board.piece_at(square + 8) is None:
	                    	mvList.append(str(ord(pieceFile)) + str(pieceRank+1))

			if pieceRank == 2 and board.piece_at(square + 16) is None:
				mvList.append(str(ord(pieceFile)) + str(pieceRank+2))

		
		elif pieceType == 2:
			"""KNIGHT"""

		elif pieceType == 3:
			"""BISHOP"""

		elif pieceType == 4:
			"""ROOK"""

		elif pieceType == 5:
			"""QUEENN"""

		else:
			"""KING"""
                
		return mvList



board = chess.Board()


print("\n-----START-----\n")
print(board.unicode())


printCrntSquares(board)


print("\n-------1-------\n")
moveToPlay = ""
maxMoveRate =  0

print(board_unicode())
print(board.legal_moves)



print(MoveGenerator(board,8))
print(MoveGenerator(board,9))
print(MoveGenerator(board,10))
print(MoveGenerator(board,11))  



