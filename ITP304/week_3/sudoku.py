def canPlace(mat, i, j, num):
	# check in same row and same col
	for k in range(9):
		if (mat[k][j] == num or mat[i][k] == num):
			return False

	# check subgrid
	sx = (i//3)*3
	sy = (j//3)*3
	for x in range(sx, sx+3):
		for y in range(sy, sy+3):
			# print(x,y)
			if (mat[x][y] == num):
				return False

	return True


def sudoku(mat, i, j, n):
	# base case
	if (i == n):
		# print solution
		for r in range(n):
			for c in range(n):
				print(mat[r][c], end = " ")
			print()

		return True

	# recursive case
	if (j == n): 
		# move to next row
		return sudoku(mat, i+1, 0, n)

	# skip filled cell
	if (mat[i][j] != 0):
		return sudoku(mat, i, j+1, n)

	# fill cell
	for num in range(1, n+1):
		if canPlace(mat, i, j, num):
			mat[i][j] = num
			subprob = sudoku(mat, i, j+1, n)

			if subprob:
				return True

	# cant place in this pos, backtrack
	mat[i][j] = 0

	return False


if __name__ == '__main__':
	n = 9

	mat = [[5,3,0,0,7,0,0,0,0],
			[6,0,0,1,9,5,0,0,0],
			[0,9,8,0,0,0,0,6,0],
			[8,0,0,0,6,0,0,0,3],
			[4,0,0,8,0,3,0,0,1],
			[7,0,0,0,2,0,0,0,6],
			[0,6,0,0,0,0,2,8,0],
			[0,0,0,4,1,9,0,0,5],
			[0,0,0,0,8,0,0,7,9]]

	if (sudoku(mat,0,0,n) == 0):
		print("No solution exists")

