from Functions import primes,RetFact
from time import time
global p
global N
N = 10**2
p=primes(N)



from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul

def Factor(n):

  n += 1
  f = defaultdict(list)
  t = range(n)

  for p in xrange(2, n):
     if p not in f:
       t[p] = p - 1
       for i in xrange(p + p, n, p):
         j, k = i, 1
         while j % p == 0:
           j //= p
           k *= p
         f[i].append(k)
         t[i] = t[i] * (p - 1) // p
  return f, t


def M(n):
  amax=0
  amost=0
  for a in xrange(n/2,n):
    #v = a**2%n
    v = (a*(a-1))%n
    if v==0 and a>amax:
      amax = a
      amost = a
    #if amax==0:amost,amax=1,1
      print n,a
  return amost,amax

def Prod(l):
  tot =1
  for i in l:
    tot*=i
  return tot
  
def find_idempotents(n):
  f, t = Factor(n + 1)
  #print "time elapsed is",time()-st
  yield 0 # i = 1
  for i in xrange(2, n + 1):

    if len(f[i]) <2:
    # prime or prime power
       yield 1
       continue
    def uw():
      for j in xrange(1, len(f[i])):
        for c in combinations(f[i], j):
          #u = reduce(mul, c)
          u = Prod(c)
          v = i // u
          w = pow(u, t[v] - 1, v)
          yield u * w
    yield max(uw())
	
st = time()
tot = 0

#f,t = Factor(100)	

# for i in f:
  # print i,f[i]
 
# print

# for i in t:
  # print i, t



print "time elapsed is",time()-st

for idem in find_idempotents(10000000):
  tot += idem
  #print idem

print "sum of idempotents is ", tot  
print "time elapsed is",time()-st
