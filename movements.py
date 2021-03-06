def GetValidMovements(board_state, row, column, check = False):
		'''Gets all the valid movements for the piece with the specified coordinates'''
		#Because the pawn's attacks and moves are different, I put a flag to facilitate the generation of valid moves


		piece = board_state.pieces[board_state.board[row][column]]
		moves = list()

		if (piece.type is "knight"):
			moves.append((row+2, column+1))
			moves.append((row+2, column-1))
			moves.append((row-2, column+1))
			moves.append((row-2, column-1))
			moves.append((row+1, column+2))
			moves.append((row+1, column-2))
			moves.append((row-1, column+2))
			moves.append((row-1, column-2))

		if (piece.type is "king"):
			moves.append((row+1, column+1))
			moves.append((row+1, column-1))
			moves.append((row-1, column+1))
			moves.append((row-1, column-1))
			moves.append((row+1, column))
			moves.append((row-1, column))
			moves.append((row, column-1))
			moves.append((row, column+1))

		if (piece.type is "bishop" or piece.type is "queen"):
			for i in range (1,8):
				if (row+i > 7 or column+i>7):
					break
				moves.append((row+i, column+i))
				if (board_state.board[row+i][column+i] is not 0):
					break
			for i in range (1,8):
				if (row-i<0 or column+i>7):
					break
				moves.append((row-i, column+i))
				if (board_state.board[row-i][column+i] is not 0):
					break
			for i in range (1,8):
				if (row-i < 0 or column-i < 0):
					break
				moves.append((row-i, column-i))
				if (board_state.board[row-i][column-i] is not 0):
					break
			for i in range (1,8):
				if (row+i > 7 or column-i < 0):
					break
				moves.append((row+i, column-i))
				if (board_state.board[row+i][column-i] is not 0):
					break

		if (piece.type is "rook" or piece.type is "queen"):
			for i in range (1,8):
				if (row+i > 7):
					break
				moves.append((row+i, column))
				if (board_state.board[row+i][column] is not 0):
					break
			for i in range (1,8):
				if (row-i<0):
					break
				moves.append((row-i, column))
				if (board_state.board[row-i][column] is not 0):
					break
			for i in range (1,8):
				if (column-i < 0):
					break
				moves.append((row, column-i))
				if (board_state.board[row][column-i] is not 0):
					break
			for i in range (1,8):
				if (column+i > 7):
					break
				moves.append((row, column+i))
				if (board_state.board[row][column+i] is not 0):
					break

		elif(piece.type is "pawn"):
			if (piece.color is "black"):
				if (not check):
					if(board_state.board[row+1][column] is 0):
						moves.append((row+1, column))
					if (piece.moved is 0 and board_state.board[row+2][column] is 0 ):
						moves.append((row+2, column))
					if (column > 0):
						if (board_state.board[row+1][column-1] is not 0
							and board_state.pieces[board_state.board[row+1][column-1]].color is "white"):
							moves.append((row+1, column-1))
					if (column < 7):
						if (board_state.board[row+1][column+1] is not 0
							and board_state.pieces[board_state.board[row+1][column+1]].color is "white"):
							moves.append((row+1, column+1))
				else:
					moves.append((row+1, column-1))
					moves.append((row+1, column+1))

			if (piece.color is "white"):
				if (not check):
					if(board_state.board[row-1][column] is 0):
						moves.append((row-1, column))
					if (piece.moved is 0 and board_state.board[row-2][column] is 0):
						moves.append((row-2, column))
					if (column > 0):
						if (board_state.board[row-1][column-1] is not 0
							and board_state.pieces[board_state.board[row-1][column-1]].color is "black"):
							moves.append((row-1, column-1))
					if (column < 7):
						if (board_state.board[row-1][column+1] is not 0
							and board_state.pieces[board_state.board[row-1][column+1]].color is "black"):
							moves.append((row-1, column+1))
				else:
					moves.append((row-1, column-1))
					moves.append((row-1, column+1))

		final = list()
		for item in moves:
			row = item[0]
			column = item[1]
			if (row > 7 or row < 0 or column > 7 or column < 0):
				pass
			elif(board_state.board[row][column] is 0):
				final.append(item)
			elif (board_state.pieces[board_state.board[row][column]].color is piece.color):
				pass
			else:
				final.append(item)

		#print final

		return final