# num = int(input("Enter the integer number:"))
# i = 0
# res = 0
# while res < num:
# 	res = 1<<i
# 	if res == num:
# 		print("Yes the enter numer is power of 2",i)
# 		break
# 	i = i + 1
# else:
# 	print("enter numer is not a power of 2")

n=int(input("Enter the interger number:"))
i=0
res=0
while res<n:
	res=1<<i
	if res==n:
		print(i,"Enter number is power of 2")
		break
	i=i+1
else:
	print("Enter number is not a powerof 2")