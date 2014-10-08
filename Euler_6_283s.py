#
#
#  Euler Problem 283
#
#
from math import sqrt,floor
from Functions import RetFact,gcd,divisors
from time import time

def euler283(low=1,top=1000):
   M=[]
   st = time()
   t=0
   for m in xrange(low,top+1):
      print "m:",m,
      psum = 0
      for u in xrange(1,2*m+1):
         if (2*m)%u: continue
         for v in xrange(1,int(floor(sqrt(3)*u)+1)):
            if gcd(v,u)!=1: continue
            F=4*m**2*(u**2+v**2)
            #fs=set(RetFact(m))
            #fs=fs.union(set(RetFact(u**2+v**2)))
            #fs.add(2)
            for d1 in divisors(F):
               if (d1+2*m*u)%v: continue
               d2=F/d1
               if d1>d2: continue
               if (d2+2*m*u)%v: continue               
               a=(d1+2*m*u)/v + 2*m*v/u
               b=(d2+2*m*u)/v + 2*m*v/u
               c=(d1+d2+4*m*u)/v
               if b>c: continue
               #print m,":",a,b,c,a+b+c,d1,d2
               t+=a+b+c
               psum+=a+b+c
      print psum,
      print  
      M.append(psum)
      
   print t
   print time()-st
   print
   print
   print M

euler283()