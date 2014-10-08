from time import time
sttm=time()
# import psyco
# psyco.full()
from collections import defaultdict

def polmul1(l1,l2) :
   lr1=[0]*(len(l1)+len(l2)-1)
   for i1,n1 in enumerate(l1) :
      for i2,n2 in enumerate(l2) : lr1[i1+i2]+=n1*n2
   return lr1


def p386(lm1=10**6) :
   cn1,cn2,lm2,lp1=0,0,lm1,[0]*(lm1+1)
   while lm2 : cn2,lm2=cn2+1,lm2>>1
   while cn2 : cn1,cn2=cn1+1,cn2>>1
   lp1[1]=1
   for n1 in xrange(2,lm1+1,2) : lp1[n1]=1
   n1=4
   while n1<=lm1 :
      for n2 in xrange(n1,lm1+1,n1) : lp1[n2]+=1
      n1*=2
   for n1 in xrange(3,lm1+1,2) :
      if lp1[n1] : continue
      for n2 in xrange(n1,lm1+1,n1) : lp1[n2]=(lp1[n2]<<cn1)+1
      n3=n1*n1
      while n3<=lm1 :
         for n2 in xrange(n3,lm1+1,n3) : lp1[n2]+=1
         n3*=n1
   dp1=defaultdict(int)
   for n1 in xrange(2,lm1+1) : dp1[lp1[n1]]+=1
   lp1=[]
   sm1,cn11=1,(1<<cn1)-1
   for (n1,n10) in dp1.items() :
      if n1<(1<<cn1) : sm1+=n10
      elif n1<(1<<(2*cn1)) : sm1+=n10*(min(n1&cn11,n1>>cn1)+1)
      else :
         pl1,n2=[1],0
         while n1 :
            n3=n1&cn11
            pl1=polmul1(pl1,[1]*(n3+1))
            n2+=n3
            n1>>=cn1
         sm1+=n10*pl1[n2/2]
   return sm1

sm1=p386(10**8)

print '\nThe sum  is ',sm1
print "\nTime taken ",time()-sttm," s"