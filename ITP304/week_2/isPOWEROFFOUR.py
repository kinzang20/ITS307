def isPowerOfFour(num):
	if num<0:
		print("false")
	while num%4 == 0:
		num=num/4
	if num==1:
		print("true")
	else:
		print("false")
isPowerOfFour(5)


