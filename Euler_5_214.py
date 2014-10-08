#
#  Euler 204
#

from sets import Set
from math import log10, ceil

from Functions import primes
from time import time
import gmpy2

def factorialMod(n, modulus):
    ans=1
 

    for i in range(1,modulus-n):
        ans = (ans * i) % modulus
    ans = gmpy2.invert(ans, modulus)

    #Since m is an odd-prime, (-1)^(m-n) = -1 if n is even, +1 if n is odd
    if n % 2 == 0:
        ans = -1*ans + modulus
    return ans % modulus
	

t = time()
	
print "calculating primes up to the 8th power"
p = primes(10**8)
print "primes generated"
summ = 0



for x in p:

  if x< 5:continue
  
  z = factorialMod(x-1,x) +factorialMod(x-2,x)+ factorialMod(x-3,x)+ factorialMod(x-4,x)+ factorialMod(x-5,x)
  #print x,z,z%x
  summ += z % x

print "Sum is ", summ
print "Time elapsed is ",time() - t

