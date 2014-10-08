#
#
# Euler 231
#
#

from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul
from time import time
from Functions import primes
from euler import miller_rabin


def RetFact(n,p,F):
  #from time import time
  #st = time()
  ndiv = n
  factlist=[ ]
 
  ctr = 0
  while ndiv >1:
    #temp = ndiv
    if (ndiv)%(p[ctr])==0:
      factlist.append(p[ctr])
      ndiv /= (p[ctr])
      if ndiv in p:
        factlist.append(ndiv)
        return factlist
      elif ndiv in F:
        factlist += F[ndiv]
        #print "4)",n,ndiv,factlist
        return factlist
    else:
      ctr +=1
  #print "process time",time()-st
  return factlist

def FactorSieve(n):

  n += 1
  f = defaultdict(list)

  for p in xrange(2, n):
     if p not in f:

       for i in xrange(p + p, n, p):
         j = i
         while j % p == 0:
           j //= p
           f[i].append(p)
           #f[i]=[p]
           #break
		   
     if p not in f: f[p]=[p]
  return f

def facPrimeSum(n, leastPrimeFac):
  z = 0
  for i in xrange(1, n+1): 
    j = i
    while (j > 1):
      p = leastPrimeFac[j]
      z += p
      j /= p
  
  return z;

        
  
st=time()

#F = FactorSieve(5000000)
#p = primes(20000000)
#print F
print time()-st
#exit()
N = 20000000
K = 15000000
summ = 0
        
leastPrimeFac = [0]*(N + 1)

for i in xrange(2, N+1):
  if (leastPrimeFac[i] == 0):
    leastPrimeFac[i] = i
    if (i * i <=N):
      for j in xrange(i*i,N+1,i):
        if (leastPrimeFac[j] == 0):
           leastPrimeFac[j] = i

v= facPrimeSum(N, leastPrimeFac)
summ = v
print "total sum of prime factors is", v
v=facPrimeSum(K, leastPrimeFac)
summ -= v
print "sum of prime factors of 150Mil", v
v = facPrimeSum(N - K, leastPrimeFac)
summ -= v
print "sum of prime factors of 50M", v

print "sum of prime factors is", summ
print time()-st
