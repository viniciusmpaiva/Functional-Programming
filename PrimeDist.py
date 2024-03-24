
def isPrime(x,y):
    if(y <=1):
        return True
    if x%y == 0:
        return False
    else:
        return isPrime(x,y-1)

    

def findNextPrime(x,y):
    if(x>=y):
        return 0
    if(isPrime(x+1,x)):
        return x+1
    else:
        return findNextPrime(x+1,y)


def primeMaxDist(x,y):
    nextPrime = findNextPrime(x,y)
    if(not isPrime(x,x-1)):
        return primeMaxDist(nextPrime,y)
    if(nextPrime == 0):
        return 0
    
    dist = nextPrime - x 
    distNextPrime = primeMaxDist(nextPrime,y)
    if(dist>distNextPrime):
        maxDist = dist
    else:
        maxDist = distNextPrime
    return maxDist 

x = int(input())
y=int(input())
print(primeMaxDist(x,y))
    
