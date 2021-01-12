board = [[" " for x in range(8)] for y in range(8)]



def is_bounded(board, y_end, x_end, length, d_y, d_x):
	board = [row+["b"] for row in board] + [["b"]*9]
	return ["CLOSED", "SEMIOPEN", "OPEN"][(board[y_end+d_y][x_end+d_x] == " ")+(board[y_end-length*d_y-d_y][x_end-length*d_x-d_x] == " ")]