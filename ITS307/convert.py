def convertBits(n):
	ans =0
	p=1
	while(n)
	lastBits = n & 1
	ans = lastBits * p
	p = p*10
	n = n>>1

if __name__ == '__main__':
	prints(convertBits(10))