# program to find subset in the given string 
s="hello"
d={}
for i in s:
	d[i]=0
for i in s:
	d[i]= d[i]+1 #sum=sum+1 or incrementing i+1 logically
print(d)

for i in s:
	if (d[i]==1):
		print(i)
