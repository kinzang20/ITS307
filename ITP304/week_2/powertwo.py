# def powerTwo(n):
# 	if n & (n-1) == 0:
# 		print("Is power of two.")
# 		return True
# 	else:
# 		print("Not power of two.")
# 		return False

# if __name__ == '__main__':
# 	n = 16
# 	powerTwo(n)

def powerTwo(n):
	if n & (n-1)==0:
		print("Is a power of 2.")
		return True
	else:
		print("Is not a power of 2.")
		return False

if __name__=='__main__':
	n=16
	powerTwo(n)
