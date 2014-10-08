#
#
#  Euler Problem 273
#
#

from Functions import IsPrime,RetFact
from itertools import combinations

def Prod(f):
  retval = 1
  for vv in f:
    retval *= vv
  return retval

p=[]
S=set([])
for k in range(1,39):
  v = 4*k + 1
  if IsPrime(v): p+=[v]
  
print p

l = len(p)
summ = 0
cnt = 0
for i in range(1,3):
  n = combinations(p,i)
  for t in n:
    N = Prod(t)

    for c in xrange(1,int(N**.5)+1):
      u = c**2
      v = (N - u) **.5
      if v == int(v) and c<v:
        summ += c
        #print "Found", N, c,v,t,RetFact(c),RetFact(v),(c*1.0)/N
        if N not in S:S.add(N)
        cnt += 1

	
print "Sum of S(N) is ", summ
print "number of items is ", cnt

print
print sorted(S)