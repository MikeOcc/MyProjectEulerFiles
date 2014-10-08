import operator
from Functions import RofPrimes
primes = RofPrimes(2,100001)
 
#@memoize
def prime_factors(n):
    if n <=1: return []
 
    for p in primes:
        if n%p==0: break
 
    while (n%p)==0:  n/=p
    return [p] + prime_factors(n)
 
def rad(n):
    return reduce(operator.mul, prime_factors(n),1)
 
print sorted(range(1,100001), key=rad)[10000-1]