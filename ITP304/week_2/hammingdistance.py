# Function to calculate hamming distance
def hammingDistance(n1, n2) :
 
    x = n1 ^ n2
    setBits = 0
 
    while (x > 0) :
        setBits += x & 1
        x >>= 1
     
    return setBits
 
if __name__=='__main__':
    n1 = 1
    n2 = 4
    print(hammingDistance(1, 4))