#
#
#  Euler 355
#
#

from Functions import RofPrimes,RetFact,IsPrime
from math import log
from time import time

def prevprime(V2,Pused):
  while 1:
   V2-=1
   if IsPrime(V2) and V2 not in Pused:
     return V2
  return 0

def MaxNum(p,Max,L):
  n=0
  maxdiff = 0
  bsv,xsv,maxval=0,0,0
  while 1:
    n+=1
    b = p**n
    if b>Max: break
    for x in L:
      
      val = b * x
      if val<=MX:
        diff = val - p - x
        
        if diff>maxdiff:
          #print p,b,n,x,val,diff
          maxval,bsv,xsv,maxdiff = val,b,x,diff
      else:
        break
  return maxval,bsv,xsv,maxdiff
###################

st = time()

MX = 1000000

SubSet = RofPrimes(2,MX)

# Add 1
SubSet.append(1)

print "init sum", sum(SubSet)

SqMax = int(MX**.5)+1

Srch = RofPrimes(SqMax-1,MX)

SqSet = sorted(RofPrimes(2,SqMax),reverse = False)
pused=[]
dupes = []
ctr = 0
prev = 0
for i in SqSet:
   ctr +=1
   nval,nb,np,diff = MaxNum(i,MX,Srch)
   pused.append(np)
   pused.append(nb)
   #print i, nval,nb,np,diff
   dupes.append([i,nb,np])
   SubSet.remove(i)

# Search for duples in primes and search for next lowest free prime
prev = 0;prevnb=0
for i in xrange(len(dupes)-1):
  v = dupes[i]
  v1=v[1];v2 = v[2] 

  if v2==prev:   #duple found

    prevp = prevprime(v2,pused)
    dupes[i-1]=[i-1,prevnb,prevp]
  
  prevnb = v1;prev = v2


# special case.  in other cases each dupe you took the next lowest unused prime.
# In the last prime under sqrt(MX) you simply take the square to achieve the greatest 
# value. Any higher prime goes over and any lesser prime has been used by now.

lastval = dupes[-1]
v1=lastval[1]
dupes[-1]=[i,v1,v1]

# uncomment if you want to display entire set of altered primes
'''
for i,v in enumerate(dupes):
  v1=v[1];v2 = v[2]
  print i,v1,v2,v1*v2
'''

#  remove old primes, add new coprimes
for v in dupes:
  if v[2] in SubSet:SubSet.remove(v[2])
  SubSet.append(v[1]*v[2])

print "Sum of Maximal Subset C(",MX,") is", sum(SubSet)
print "Process time is", time()-st

'''  
# uncomment if you want to display entire maximal subset.
for i,v in enumerate(SubSet):
  print i,v

'''

