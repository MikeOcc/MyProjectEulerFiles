#
#
# Euler Problem 302
#
#

from Functions import gcd,RetFact
from operator import mul
from time import time
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
  
st = time()
N=864
Lim=10**18
i,j=5,3
ctr=0
lst = []
for i in xrange(0,57):   #57
 if i ==1:continue
 for j in xrange(0,36):
  if j ==1:continue
  for k in xrange(0,23):
    if k ==1:continue
    if i+j+k==0:
      n0=[]
      v=0
    else:
      n0 = [2]*i + [3]*j + [5]*k 
      v = reduce(mul,n0)
      #if v==1944:print "!",i,j,k,n0,v
    if v> Lim: break

    for l in xrange(0,22): 
     if l ==1:continue
     n1 = n0+ [7]*l
     if n1==[]:v=0
     else:v = reduce(mul,n1)
     if v> Lim: break

     for m in xrange(0,18):
      if m ==1:continue
      n2 = n1 + [11]*m 
      if n2==[]:v=0
      else:v = reduce(mul,n2)
      if v> Lim: break     

      for o in xrange(0,17): 
        if o ==1:continue
        n3 = n2 + [13]*o
        if n3==[]:v=0
        else:v = reduce(mul,n3)
        if v> Lim: break 

        for p in xrange(0,15):
         if p ==1:continue
         n4 = n3 + [23]*p
         if n4==[]:v=0
         else:v = reduce(mul,n4)
         if v> Lim: break 

         for q in xrange(0,15):
           if q==1:continue
           n5 = n4 + [97]*q		
           if n5==[]:v=0
           else:v = reduce(mul,n5)
           if v> Lim: break 		   

           for r in xrange(0,6):
             if r>0 and r<3:continue
             n = n5 + [1013]*r		
             if n==[]:v=0
             else:v = reduce(mul,n)
             if v> Lim: break

             A= isAchilles(n)
             if not A:continue
             phiA = Phi(v,n)
             fphi=RetFact(phiA)
             B = isAchilles(fphi)
             if not B:continue
             ctr+=1
             lst.append(v)
             if r>0:print i,j,k,l,m,o,p,q,r,":" , v
lst=sorted(lst)
# for j,x in enumerate(lst):
  # print j, x, RetFact(x)
print
print ctr
print "time elapsed", time()-st