#
#  Euler Problem 251
#
#
#
from math import *
from time import time
from itertools import combinations
from operator import mul

def RetFact(n):
  #from time import time
  #st = time()
  ndiv = n
  factlist=[ ]
  ctr = 2
  while ndiv >1:
    #temp = ndiv
    if (ndiv)%(ctr)==0:
      factlist.append(ctr)
      ndiv /= (ctr)
    else:
      ctr +=1
  #print "process time",time()-st
  return factlist

st = time()
ctr = 0
lim = 10000# 110000000
maxi,maxj,maxk=0,0,0

numturns =2000 # 60000
print "Cardano Numbers for limit with turns:", lim, numturns
for i in xrange(1,numturns):
  a = i * 3 -1
  f = (i**2) * (8*i -3)

  if f< lim:
    b=1;c=f
    if a + b + c > lim:continue
    ctr+=1
    #print ctr,")",i,":",a, b,c,":",a+b+c,f
    
  L = RetFact(f)
  #M= L   #remove

  S = sorted(set(L))
  P=[]

  for k in S:
    x=L.count(k)
    if (x/2)>=1:
      P.append(x/2)
    else:
      L.remove(k)
  S = sorted(set(L))
  L=list(S)

   #print L

  for m in xrange(len( P)):
    if P[m]>1:
      #print "P",P[m]
      for j in xrange(1,P[m]):
        #print i,j,S[m]
        L.append(S[m])
  
  R=[]

  for jj in range(1, len(L)+1):
    for subset in combinations(L, jj):
      #print(subset)
      R.append(reduce(mul,subset))
  
  R=list(set(R))
  R=sorted(R)
 
  for j in R:
    #print "J",j,R,f,M,S
    if f/float(j*j) == int( f/j/j):
      b = j; c = f/(j*j)
      if a + b + c > lim:continue
      ctr+=1 
      #print ctr,")",i,":",a, b,c,":",a+b+c,f
 

print "Number of Cardano Triplets <=",lim, "is", ctr
print "Process time is", time()-st
