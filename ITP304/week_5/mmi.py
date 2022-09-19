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
	
	mmi = x%m 
	if mmi < 0:
		return (mmi+m)% m # mmi can be negative values
	
	return mmi

if __name__ == '__main__':
	a = 6
	m = 7
	print(MMI(a, m))