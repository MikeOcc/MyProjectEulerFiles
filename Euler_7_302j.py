#
#
# Euler 302
#
#

from Functions import RetFact,gcd
from collections import defaultdict

def isAchilles(l):

  s = set(l)
  prev = 0
  psetlist=[]
  #hasOdds=False
  for v in s:
    z = l.count(v)
    if z < 2: return False
    #if z%2==1: hasOdds=True
    psetlist.append(z)
  if len(set(psetlist))==1:
    return False
  #if hasOdds==False:
  #  return False
  hasOdds = False
  for zz in xrange(1,len(psetlist)):
    if gcd(psetlist[zz],psetlist[zz-1])==1:
      hasOdds=True
      break
  if hasOdds==False:return False
  return True

def Phi(Achnum,factlist):

 # powlist = "["+factlist.rstrip(",")+"]"
 # powlist = list(set(map(int,powlist.strip('[]').split(','))))
  
  Phi = Achnum      
  #powlist=list(set(RetFact(Phi)))
  powlist=list(set(factlist))
  
  for i in powlist:
    Phi = Phi * (int(i)-1)
    #Phi = Phi / int(i)

  for i in powlist:
    #Phi = Phi * (int(i)-1)
    Phi = Phi / int(i)
	
  return Phi
 
def FactorSieve(n):

  n += 1
  f = defaultdict(list)

  for p in xrange(2, n):
     if p not in f:

       for i in xrange(p + p, n, p):
         j, k = i, 1
         while j % p == 0:
           j //= p
           k *= p
           f[i].append(p)
       if f[p]==[]:f[p]=[p]
  return f
 
from time import time
st = time()
N=1*10**7
print "factoring integers up to ", N
F=FactorSieve(N) 
print "factor sieve complete and hogging memory..."
ctr = 0
for i in xrange(72,N+1):
  f = F[i]
  if F[i]==1:continue
  A = isAchilles(f)
  if not A:continue
  phiA = Phi(i,f)
  #fphi=RetFact(phiA)
  fphi=F[phiA]
  B = isAchilles(fphi)
  if not B:continue
  #if A and B and (set(f)==set([2,3]) or set(f)==set([3,2])): print i, f,":",phiA, fphi
  #if A and B and (set(f)==set([2,3])): print i, f,",",f.count(2),f.count(3),":",phiA, fphi
  if A and B: print i, len(set(f)),":", f ,":",fphi #,",",f.count(2),f.count(3),":",phiA, fphi
  ctr+=1
    

print
print ctr
print "time elapsed ",time()-st