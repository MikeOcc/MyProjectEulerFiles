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

for k in range(1,39):
  v = 4*k + 1
  if IsPrime(v): p+=[v]
  
print p

l = len(p)
D={}
summ = 0
for i in range(1,2):
  n = combinations(p,i)
  for t in n:
    N = Prod(t)
    Found = False
    for c in xrange(1,int(N**.5)):
      u = c**2
      v = (N - u) **.5
      if v == int(v):
        print "Found", N, c,int(v)
        D[N] = [[c,int(v)]]
        Found = True
        summ += c
        break
    # if Found==False: print "unfactored N:",N

for i in range(2,17):  #len(p)+1):
  n = combinations(p,i)
  for t in n:
    N = Prod(t)
    mx = t[-1]
    z = N/mx
    l2 = len(D[z])
    c = D[mx][0][0]
    d = D[mx][0][1]

    for q in range(0,l2):
      #print "Z: ",D[z],l2,q,mx
      #print "MX:",D[mx],l2,q,mx
      a = D[z][q][0]
      b = D[z][q][1]
      #print "DMX:", D[mx],q

      acbd1 = abs((a*c + b*d))
      adbc1 = abs((a*d - b*c))
      acbd2 = abs((a*c - b*d))
      adbc2 = abs((a*d + b*c))
      if N not in D:
        D[N]=[[acbd1, adbc1]]
      else:
        D[N]+=[[acbd1, adbc1]]
      D[N]+=[[acbd2, adbc2]]
      #print "Obtained", N,acbd1, adbc1
      #print "Obtained", N,acbd2, adbc2	

	
#print D
print
#summ = 0
#D = sorted(D)
cnt = 0
#print D
print "Time elapsed is", (time()-st)/60.

for x in D:
  #print x,":",D[x]
  #print x
  y = D[x]
  cnt += len(y)
  for z in y:
    #print x
    u = z[0]
    v = z[1]
    #print z, u, v
    zz = min(u,v)
    summ += zz

#print "number of elements in D is",len(D)
print "number of elements in D is",cnt	
print "Sum of S(N) is ", summ
print "Time elapsed is", (time()-st)/60.