from math import sqrt

# brute force method, O(n)
def primefac1(n):
	for i in range(2, n):
		# print(i, n)
		if (n%i == 0):
			count = 0
			while(n%i == 0):
				count+=1
				n = n//i
			print(str(i)+"^"+str(count), end= " ")

# O(sqrt(n))
def primefac2(n):
	for i in range(2, int(sqrt(n))):
		if (n%i == 0):
			count = 0
			while(n%i == 0):
				count+=1
				n = n//i
			print(str(i)+"^"+str(count), end =" ")

	if n != 1:
		print(str(n)+"^"+"1")

def primeFactorization(n):
	sieve = [i for i in range(n+1)] 
	# construct sieve, O(log(logn))
	for i in range(2, n):
		# is prime
		if sieve[i] == i:
			for j in range(i*i, n+1, i):
				sieve[j] = i

	# factorization, O(logn)
	while(n!=1):
		factor = sieve[n]
		print(factor, end=" ")
		n = n//factor


if __name__ == '__main__':
	# primefac1(84)
	# primefac2(84)
	# primefac2(99)
	primeFactorization(20)
