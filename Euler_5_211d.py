#
#
#  Euler Problem 211
#
#
from Functions import divisors,RetFact,primes

from time import time


def O2(l):
  tot = 0
  D = divisors(n)
  #print n,D
  for d in D:
    tot += d*d

  return tot

st = time()

maxp = int(64000000**.5)

p=primes(maxp)

print "Prime Max", p[-1]

total = 0

for i in p:
  for j in p:
    z = (i,j)
    sigma2=O2(z)
    if int(x**.5)**2 == x:
      print "n,x:", i*j,i,j,x


print "Sum of O2 for i<64,000,000 is",total
print "process time",time()-st

