n=int(input("Enter Number:"))
L1=len(str(n))   #Convert number into str function
L2=len(set(str(n))) # we are applying set function so that we can removed duplicate values/number

if L1==L2:
	print(n,"is a unique number")
else:
	print(n,"is not a unique number")