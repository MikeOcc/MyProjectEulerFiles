#
#
#  Euler Problem 211
#
#
from Functions import divisors,RetFact,primes

from time import time


def O2(n):
  tot = 0
  D = divisors(n)
  #print n,D
  for d in D:
    tot += d*d

  return tot

st = time()

maxp = 44

# res = 15015

# hasRes = [False]* res

# for i in xrange(res):
  # hasRed[i*i % res] = True  

p=primes(maxp)

total = 1
for i in xrange(maxp+1):  #00000):
  if i in p:continue
  o = O2(i)
  if o**.5 == int(o**.5):
    print i,o,divisors(i),RetFact(i)
    print
    total += i

print "Sum of O2 for i<64,000,000 is",total
print "process time",time()-st

