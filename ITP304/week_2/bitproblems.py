def evenAND(n):
	if (n & 1) == 0:
		print("even")
	else:
		print("odd")

def evenXOR(n):
	if (n ^ 1) == n +1:
		print("even")
	else:
		print("odd")

def countBit(n):
	count = 0
	while n > 0:
		count += 1
		n = n >> 1

	return count

	
if __name__ == '__main__':
	for i in range(5):
		n = int(input())
		# evenAND(n)
		evenXOR(n)
	