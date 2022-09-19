m = 7
N = 1000000
fact = [0 for i in range(N)]

def addm(x,y):
	return (x+y) % m

def subm(x,y):
	return ((x - y) % m + m) % m

def mulm(x,y):
	return (x * y) % m

# fast exponentation
def powm(a, b):
	result = 1:
	while b:
		if b & 1 :
			result *= a
		a = a * a
		b = b>>1

	return result

# fermats theorem
def divm(x, y):
	return (mulm((x % m), powm(y, m-2) % m )) % m


def calFact():  # O(N)
	fact[0] = 1
	for i in range(1, N):
		fact[i] = mulm(fact[i-1], i) #taking % since factorial can be huge#


def ncr(n, r):
	return mulm(mulm(fact[n], (powm(fact[r], p-2))), powm(fact[n-r], p-2))


if __name__ == '__main__':
	print(addm(3,5)) #  O(1)
	print(subm(3,5))  # O(1)
	print(mulm(324,234)) # O(1)
	print(divm(56, 2)) # 3, (50,2) = 0 , p =5
	
	#factorial%p
	n = 5
	calFact()
	print((fact[n-1] % p * n)%p) # 1, p=7, O(logy), pow takes logy T
	
	print(ncr(5, 2)) # 3, O(logy), 
	print(ncr(5777, 123)) # 0

# cal npr yourself
