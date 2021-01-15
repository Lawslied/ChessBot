import chess.pgn



pgn = open("pgnTest.pgn")

first_game = chess.pgn.read_game(pgn)
second_game = chess.pgn.read_game(pgn)


board = first_game.board()
i=0
for move in first_game.mainline_moves():
	print("-------" + str(i) + "---------------")
	print(board.unicode())
	board.push(move)
	i=i+1
	
print(board.unicode())


