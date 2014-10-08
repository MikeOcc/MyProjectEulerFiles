#
#
#  Euler Problem 273
#
#

from Functions import IsPrime,RetFact
from itertools import combinations
from time import time

def Prod(f):
  retval = 1
  for vv in f:
    retval *= vv
  return retval

st = time()
  
p=[]

# Generate primes of type p : p=4k + 1
for k in range(1,39):
  v = 4*k + 1
  if IsPrime(v): p+=[v]
  
print p

l = len(p)
D={}     #  Use dict for storing squares 

# Initialize squares for single primes of 4k+1 up to 150
for i in range(1,2):
  n = combinations(p,i)
  for t in n:
    N = Prod(t)

    for c in xrange(1,int(N**.5)):
      u = c**2
      v = (N - u) **.5
      if v == int(v):
        D[N] = [[c,int(v)]]
        break

summ = 0

# Generate N using all combinations of p
for i in range(2,len(p)+1):
  n = combinations(p,i)
  for t in n:
    print t
    N = Prod(t)
    mx = t[-1]
    z = N/mx
    l2 = len(D[z])
    c = D[mx][0][0]
    d = D[mx][0][1]

    # sift through pairs of squares
    for q in range(0,l2):
      a = D[z][q][0]
      b = D[z][q][1]
      acbd1 = abs((a*c + b*d))
      adbc1 = abs((a*d - b*c))
      acbd2 = abs((a*c - b*d))
      adbc2 = abs((a*d + b*c))
      if N not in D:
        D[N]=[[acbd1, adbc1]]
      else:
        D[N]+=[[acbd1, adbc1]]
      D[N]+=[[acbd2, adbc2]]

print

cnt = 0
#print D
print "Time elapsed is", (time()-st)/60.

# sum lesser element of each square pair
for x in D:
  y = D[x]
  cnt += len(y)
  for z in y:

    u = z[0]
    v = z[1]

    zz = min(u,v)
    summ += zz

print "number of elements in D is",cnt	
print "Sum of S(N) is ", summ
print "Time elapsed is", (time()-st)/60.
