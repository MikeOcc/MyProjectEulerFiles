#
#
#  Euler 214
#
#
from collections import defaultdict
# from functools import reduce
# from itertools import combinations
# from operator import mul
from time import time
from euler import miller_rabin
from Functions import primes,RetFact

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
       if f[p]==[]:f[p]=[p]
  return f, t

  
def phi(n):
  v = n
  f = list(set(RetFact(n)))
  for z in f:
    v *= (z-1)
    v /= z
  return v
  
  
st = time()

p=primes(40000000)
  
F,Phi=Factor(10000001)
print time()-st


#print len(Phi)

def chain(n,Phi,p):

  dispch=False
  
  if n==9548417 or n==9576857 or n==9577397:
    dispch=True

  ctr=1
  if dispch:print n
  while n > 1:
    if n in Phi:
      n = Phi[n]
    # elif n in p:
      # n = n - 1
    # else:
      # n = phi(n)
    if dispch==True:
      print n
    ctr +=1
  return ctr

  
#9548417 25 []
#9576857 25 []
#9577397 25 []
  #9548417+9576857+9577397=28702671
summ=0
for j in xrange(600000,700000):  #len(p)):
  i=p[j]
  #print i,j
  l = chain(i,Phi,p)
  if l == 25:
    print i,l,F[i]
    summ+=i
print "sum is", summ
print time()-st












