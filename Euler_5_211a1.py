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

#st = time()

maxp = 64000

res = 15015*17*19

hasRes = [False]* res

for i in xrange(res):
  hasRes[i*i % res] = True  

st = time()
  
p=primes(maxp)

total = 1
for i in xrange(maxp+1):  #00000):
  if i in p:continue
  
  if hasRes[i%res]:
    if i**.5 == int(i**.5):continue
  
  o = O2(i)
  
  if hasRes[o%res]:
    if o**.5 == int(o**.5):
      print i,i**.5,hasRes[i % res]     #o,divisors(i),RetFact(i)
      print
      total += i

print "Sum of O2 for i<64,000,000 is",total
print "process time",time()-st

