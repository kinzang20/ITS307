import math

N = 20
def totient():
	prime = [1 for i in range(N)]
	# construct prime sieve
	for j in range(2, int(math.sqrt(N))):
		for k in range(j*j, N, j):
			prime[k] = 0

	# no. of coprime till i
	phi = [i for i in range(N)]
	for i in range(2, N):
		if prime[i]:
			for j in range(i, N, i):
				phi[j] //= i # n/p
				phi[j] *= (i-1) # n/p * (p-1)
	
	return phi

if __name__ == '__main__':
	print(totient())