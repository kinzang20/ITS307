
# Naive iterative solution to calculate pow(x, n)
def power(x, n):
 
    # initialize result by 1
    pow = 1
 
    # Multiply x for n times
    for i in range(n):
        pow = pow * x
 
    return pow
 
 
# Driver code
if __name__ == '__main__':
 
    x = 2
    n = 3
 
    print(power(x, n))