#
#
# Euler Problem 302
#
#

from Functions import gcd,RetFact
from operator import mul

def Phi(Achnum,factlist):

 # powlist = "["+factlist.rstrip(",")+"]"
 # powlist = list(set(map(int,powlist.strip('[]').split(','))))

  
  Phi = Achnum      
  powlist=list(set(RetFact(Phi)))
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
p,q=2,9127
ctr=0
ii,jj,vv=0,0,0
imax,jmax=0,0
for i in xrange(3,56):   #57
  for j in xrange(3,36):
  
    n = [p]*i + [q]*j
    v = reduce(mul,n)
    if v > 10**18: continue
    A= isAchilles(n)
    if not A:continue
    phiA = Phi(v,n)
    fphi=RetFact(phiA)
    B = isAchilles(fphi)
    if not B:continue
    ctr+=1
    if v>vv:ii,jj,vv=i,j,v
    if i>imax:imax=i
    if j>jmax:jmax=j
    print i,j,":" , v
	
print
print ctr
print ii,jj,vv
print imax,jmax