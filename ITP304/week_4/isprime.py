import math

# brute force approach
def isPrime(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

# Faster
def isPrimeSR(n):
	if n == 1:
		return False
	i = 2
	# (or) i * i <= n
	while (i <= math.sqrt(n)):
		if n%i == 0:
			return False
		i += 1
	return True

if __name__ == '__main__':
	print(isPrime(10))
	print(isPrimeSR(10))