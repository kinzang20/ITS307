# find i-th bit from right
def ibit(n, i):
	print ((n & (1 << (i - 1))) >> (i - 1))

n = 15
i = 3

# function call
ibit(n, i)