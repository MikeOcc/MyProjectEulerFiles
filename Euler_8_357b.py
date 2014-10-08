#
#
#  Euler Problem 357
#
#[]
from Functions import divisors,IsPrime,RofPrimes
from time import time

def f(n):
  #if not IsPrime(1 + n):return False
  if not IsPrime(2 + n/2):return False
  
  D = divisors(n)
  D = D[2:len(D)/2]
  #l = len(D)

  for d in D:
    if not IsPrime(d + n/d):return False
  return True

st = time()
print "calculating primes"
P = RofPrimes(2,10000001)
print "looking for candidates...", time()-st
summ = 1   #  Start out with sums of 1 and 6 since these 'n's (1,6) fall thru the filter
for p in P: 
   if (p-3)%4==0 and f(p-1):
     summ +=p-1
     #print i,i

print "Sum of integers <=100,000,000 such that for every divisor d of n, d+n/d is prime is",summ
print "process time is",time()-st












