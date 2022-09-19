def extendGCD(a, b):
	if b == 0:
		return [1, 0, a]

	result = extendGCD(b, a%b)

	x_dash = result[0]
	y_dash = result[1]

	x = result[1]
	y = x_dash - (a//b)*y_dash
	gcd = result[2]

	return [x,y, gcd]

def MMI(a, m):
	result = extendGCD(a, m)
	x = result[0]
	gcd = result[2]

	if gcd != 1:
		print("MMI doesn't exist")
		return -1

	mmi = (x%m + m)%m # mmi can be negative values
	return mmi

def crt(m, a):
	result = 0
	l = len(m)
	M = 1
	Mi = [0]*l
	# find M
	for i in range(l):
 		M *= m[i]
 	
	# find M1, M2
	for j in range(l):
		Mi[j] = M//m[j]

	mmi = [0]*l
	for i in range(l):
		mmi[i] = MMI(Mi[i], m[i])
		result += (a[i]*Mi[i]*mmi[i])
	
	return result%M

if __name__ == '__main__':
	a = [1, 2, 3]
	m = [2, 3, 5]
	print(crt(m, a))