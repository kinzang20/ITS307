def getiBit(n, i):
	mask = 1 << i

	if (n & mask) > 0:
	 	return 1 

	return 0

def cleariBit(n, i):
	mask = ~(1 << i)
	n = n & mask
	return n

def setiBit(n, i):
	mask = 1 << i
	n = n | mask

	return n

def updateiBit(n, i, v):
	n = cleariBit(n, i)
	mask = v << i
	n = mask | n
	return n

def countsetbits(n):
	count  = 0
	while(n>0):
		last_bit = n & 1
		count += last_bit
		n  = n >> 1

	return count

#faster
def countsetbits2(n):
	count = 0
	while(n > 0):
		n = n & (n-1)
		count += 1

	return count

def converttoBin(n):
	ans = 0
	p = 1

	while(n>0):
		last_bit = n & 1
		ans += last_bit * p 
		p= p * 10
		n = n >> 1

	return ans


if __name__ == '__main__':
	n = 10
	print(getiBit(10, 3)) # 1
	print(cleariBit(10, 3)) # 2
	print(setiBit(10, 2)) # 14
	print(updateiBit(10, 3, 0)) # 2
	print(countsetbits(10)) # 2
	print(countsetbits2(10)) # 2
	print(converttoBin(10)) # 1010
