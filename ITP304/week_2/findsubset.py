def subsequence(s):
	l = len(s)
	for i in range(1 << l):
		j = 0 # index to iterate str
		while i > 0:
			last_bit = i & 1  # iterate from R->L
			if last_bit:
				print(s[j], end="")
			j += 1
			i = i >> 1
		print()

if __name__ == '__main__':
	s = "abc"
	subsequence(s)