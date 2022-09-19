# import math

# def primeSieve(n):

# 	primes = [1 for i in range(n+1)]
# 	p = 2

# 	while(p <= math.sqrt(n)):
# 		if primes[p]:
# 			for i in range(p*p, n+1, p):
# 				primes[i] = 0
# 		p+=1

# 	return primes

# if __name__ == '__main__':
# 	n = 20
# 	print(primeSieve(n))
			


import math

def primesieve(n):
	primes=[1 for i in range(n+1)]
	p=2
	