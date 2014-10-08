#
#
#  Euler Problem 357
#
#[]
from Functions import divisors,IsPrime
from time import time

def f(n):
  if not IsPrime(1 + n):return False
  if not IsPrime(2 + n/2):return False
  
  D = divisors(n)
  D = D[2:len(D)/2]
  #l = len(D)

  for d in D:
    if not IsPrime(d + n/d):return False
  return True

st = time()

summ = 7   #  Start out with sums of 1 and 6 since these 'n's (1,6) fall thru the filter
for i in xrange(1,500000,2):   #50000001,2):
  if i%10 in [1,5,9]:
   if f(2*i):
     summ +=2*i
     #print i,2*i, f(2*i)

print "Sum of integers <=100,000,000 such that for every divisor d of n, d+n/d is prime is",summ
print "process time is",time()-st












