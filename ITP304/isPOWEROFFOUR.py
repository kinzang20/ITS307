def isPowerOfFour(num):
	if num <= 0:
		return False
	if num & num-1 !=0:
		return False
	b = bin(num)[::-1]
	p = b.index("1")
	return p % 2 == 0

if __name__ == '__main__':
	num =5
	if (isPowerOfFour(num)):
		print(num,'poweroffour')
	else:
		print(num, 'not a power of four')