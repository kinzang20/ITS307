def extendGCD(a, b):
	if b == 0:
		return [1, 0, a]

	result = extendGCD(b, a%b)

	x_dash = result[0]
	y_dash = result[1]

	x = result[1]
	y = x_dash - (a//b)*y_dash
	gcd = result[2]

	return [x, y, gcd]


if __name__ == '__main__':
	a = 5
	b = 2

	print(extendGCD(a, b))