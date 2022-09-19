def facto(n):
	if n == 1:
		return 1
	return n * facto(n-1)

def febo(n):
	if n == 0:
		return 0
	
	if n == 1:
		return 1

	f1 = febo(n-1)
	f2 = febo(n-2)

	return f1 + f2

def power(a, n):
	if n == 0:
		return 1
	return a * power(a, n - 1)

# faster
def fastPower(a, n):
	if n == 0:
		return 1
	subProb = fastPower(a, n//2)
	subProbSquare = subProb * subProb

	if n & 1:
		return a * subProbSquare
	return subProb

def tiling(n):
	if n <= 3:
		return n
	
	return tiling(n-1) + tiling(n-2)	


if __name__ == '__main__':
	print(febo(7)) # 13
	print(facto(5)) # 120
	print(fastPower(2, 5))
	print(tiling(4))