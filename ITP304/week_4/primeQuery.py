def primeSieve(n):

	primes = [1 for i in range(n+1)] # +1 index starts from 0
	p = 2

	while(p*p <= n):
		if primes[p]:
			for i in range(p*p, n+1, p):
				primes[i] = 0
		p+=1

	return primes


def sumPrime(sieve):
	csum = [0  for i in range(len(sieve))]
	for i in range(2, len(sieve)):
		# prime
		if sieve[i]:
			csum[i]= csum[i-1]+1
		# not prime
		else:
			csum[i] = csum[i-1]

	return csum

if __name__ == '__main__':
	n = 20
	sieve = primeSieve(n)
	csum = sumPrime(sieve)

	a = 1
	b =10

	print(csum[b] - csum[a-1])
