def findUnique(arr):
	xor = 0
	for i in range(len(arr)):
		xor = xor ^ arr[i]
	return xor

if __name__ == '__main__':
	arr = [3, 4, 1, 1, 2, 3, 2]
	print(findUnique(arr))

