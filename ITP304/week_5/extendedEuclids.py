def extendGCD(a, b):
	if b == 0:
		return [1, 0]

	result = extendGCD(b, a%b)

	x_dash = result[0]
	y_dash = result[1]

	x = y_dash
	y = x_dash - a//b*y_dash

	return [x,y]


if __name__ == '__main__':
	a = 12
	b = 30

	print(extendGCD(12, 30))