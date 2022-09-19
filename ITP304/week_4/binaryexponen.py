m = 1e9 + 7
# iterative
def pow(a, b):
	res = 1

	while(b):
		if (b&1): # checking set bit, odd
			res *= a # a^1
		a *= a
		b = b//2 
		
	return res


# modular binary exponentiation
def pow2(a, b):
	res = 1

	while(b):
		if (b&1):
			res = (res * a) % m

		a = a * a 
		b = b//2 

	return res

if __name__ == '__main__':
	print(pow(2,10)) # 1024
	print(pow(2,200)) 
	print(pow2(2,200))
