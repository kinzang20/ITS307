def multMat(m1, m2):
	rows, cols = (len(m1), len(m2[0]))
	# print(rows, cols)
	res = [[0] * cols for row in range(rows)]
	# iterate m1 row
	for i in range(rows):
		# iterate col m2
		for j in range(cols):
			# iterate by rows of m2
			for k in range(len(m2)):
				res[i][j] += m1[i][k] * m2[k][j]
	return res


def matExp(T, n):
	if (n <= 2):
		return 1
	# same as result = 1, F1
	F = [[1],[0]] 
	
	# O(logn)
	while(n):
		if(n & 1): # set bit
			F = multMat(T, F)
		
		T = multMat(T, T)
		n = n//2 # right shift
	
	return F[0][0]

if __name__ == '__main__' :
	n = 10
	T = [[1,1], [1,0]]
	print(matExp(T, n-1))

