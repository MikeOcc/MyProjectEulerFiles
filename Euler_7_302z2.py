#
#
# Euler Problem 302
#
#

from Functions import gcd,RetFact,primes
from operator import mul
from collections import defaultdict

#global F

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
  
def Phi(Achnum,factlist):

 # powlist = "["+factlist.rstrip(",")+"]"
 # powlist = list(set(map(int,powlist.strip('[]').split(','))))

  
  Phi = Achnum      
  powlist=list(set(factlist))
  for i in powlist:
    Phi = Phi * (int(i)-1)
    Phi = Phi / int(i)


  return Phi
  
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
  
l=[5,3]
N=864
Lim=10**8
#p,q=2,3
p =1217 #,q=2,8191
ctr=0

qp=primes(600000)
#F=FactorSieve(2000000)


#for q in qp: len(qp)-1000
sctr=0
for qq in xrange(1,len(qp)):
  q = qp[qq]
  ii,jj,vv=0,0,0
  imax,jmax=0,0
  ctr=0
  for i in xrange(2,56):   #57
    for j in xrange(3,36):
      if gcd(i,j)>1:continue
      n = [p]*i + [q]*j
      v = reduce(mul,n)
      if v> 10**18: break
      A= isAchilles(n)
      if not A:continue
      phiA = Phi(v,n)
      fphi=RetFact(phiA) #F[phiA]
      #fphi=F[phiA]
      B = isAchilles(fphi)
      if not B:continue
      ctr+=1
      if v>vv:ii,jj,vv=i,j,v
      if i>imax:imax=i
      if j>jmax:jmax=j
      print i,j,":" , v, fphi
  if ctr>0:
    print
    print p,q,ctr, ":", RetFact(q-1)
    print ii,jj,vv
    print imax,jmax
    print "###############"
    sctr+=ctr
	
print "total count", sctr