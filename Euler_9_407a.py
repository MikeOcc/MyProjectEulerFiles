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
    # """Factorize the numbers up to n, returning a pair (factorization,
    # totient).

    # factorization is a dictionary mapping each composite i below n to
    # a list of numbers p ** e where p is a prime and e is the exponent
    # of p in the factorization of i.

    # totient is a list whose i'th element is Euler's totient function
    # applied to i (the count of numbers less than i which are coprime
    # to i).

        # >>> from pprint import pprint
        # >>> f, t = factorize(10)
        # >>> pprint((dict(f), t))
        # ({4: [4], 6: [2, 3], 8: [8], 9: [9], 10: [2, 5]},
         # [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4])

    # """
  n = n + 1
  f = defaultdict(list)
  t = list(range(n))

  for p in range(2, n):
     if p not in f:
       t[p] = p - 1
       for i in range(p + p, n, p):
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

st = time()
tot = 0

f,t = Factor(10)	

for i in f:
  print i,f[i]
 
print

for i in t:
  print i, t



print "time elapsed is",time()-st
exit()

for j in xrange(2,N+1):
  if j in p:
    m,max = 1,1
  else:
    m,max = M(j)
  tot += m
  #print "a:",j,max,m
  #print

a2=[]

#for j in xrange(1,10**7):
#  a2.append(j*j)
  
print
print "total is ", tot
