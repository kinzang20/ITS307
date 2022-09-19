def solve(enc, first):
   arr = [first]
   for i in range(0, len(enc)):
      arr.append(arr[i] ^ enc[i])
   return arr

enc = [8,3,2,7]
first = 4
print(solve(enc, first))