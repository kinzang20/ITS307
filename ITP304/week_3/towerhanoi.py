def towerHanoi(n, fr, helper, to):
	if n == 0:
		return
	towerHanoi(n-1, fr, to, helper)
	print(fr+"->"+to) # move n disk to 'to'
	towerHanoi(n-1, helper, fr, to)

if __name__ == '__main__':
	n = 3
	towerHanoi(n, 'A', 'B', 'C')