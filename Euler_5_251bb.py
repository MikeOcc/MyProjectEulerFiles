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
  ctr1 = 3
  while ndiv >1:

   if (ndiv)%(2)==0:
      factlist.append(2)
      ndiv /= (2)
   else:
      while ndiv >1:
        if (ndiv)%(ctr1)==0:
          factlist.append(ctr1)
          ndiv /= (ctr1)
        else: ctr1+=2

  #print "process time",time()-st
  return factlist
#-----------------------------
st = time()
ctr = 0
lim = 110000000 # 1000000   #110000000

#
# 10000, 1632, 1475 turns 1.476s
# 20000, 3312, 2950 turns 4.978s
# 100000, 16916, 15000 turns 121.767s
# 1000000, 171128 15000 turns 11784.549s
# 110000000, 1165775, 300000, 44606.1135292

numturns = 300000  # 150000
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
  #R=sorted(R)
 
  yy = lim-a
  for b in R:
    #print "J",j,R,f,M,S
    xx = (b*b)
    #if f/float(j*j) == int( f/j/j):
    if f%xx==0:
       c = f/xx
       if b + c > yy:continue
       ctr+=1 
       #print ctr,")",i,":",a, b,c,":",a+b+c,f
 

print "Number of Cardano Triplets <=",lim, "is", ctr
print "Process time is", time()-st
