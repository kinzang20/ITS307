def printboard(n, board):
	for i in range(n):
		for j in range(n):
			print(board[i][j], end =" ")
		print()

def canPlace(n, board, r, c):
	# check col
	for row in range(r):
		if (board[row][c] == 1):
			return False

	# left diagonal
	x = r
	y = c
	while(x >= 0 and y >= 0):
		if (board[x][y] == 1):
			return False
		x -= 1
		y -= 1

	# right diagonal
	while(r>=0 and c<n):
		if (board[r][c] == 1):
			return False
		r -= 1
		c += 1

	return True

def nqueen(n, board, i):
	# base case 
	if (i == n):
		printboard(n, board)
		return True

	# recursive case
	
	# traverse each col
	for j in range(n):
		# check is pos i, j is valid
		if (canPlace(n, board, i, j)):
			board[i][j] = 1
			validPos = nqueen(n, board, i+1)

			if validPos:
				# move to next row
				return True
			# remove queen, backtrack
			board[i][j] = 0
	# return to previous row, checked all columns
	return False


if __name__ == '__main__':
	# n = int(input())
	n = 4
	rows, cols = (n,n)
	board = [[0]*cols for i in range(rows)]

	nqueen(n, board, 0)
