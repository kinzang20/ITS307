import math
 
 
# Function to check if x is power of 4
def isPowerOfFour(n):
    if (n == pow(4, (math.log(n)/math.log(4)))):
        return True
    return False
 
 
test_no = 16
if(isPowerOfFour(test_no)):
    print(test_no, ' is a power of 4')
else:
    print(test_no, ' is not a power of 4')