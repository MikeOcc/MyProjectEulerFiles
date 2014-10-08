import math
from decimal import Decimal

def avg(A,B):
   return (A[0]+B[0])*0.5,(A[1]+B[1])/2
def euler363(P0,P1,P2,P3,n=20):
   """Return area,length"""
   if n==0:
      y=(P0[1]+P3[1])/2
      dx=P0[0]-P3[0]
      dy=P0[1]-P3[1]
      return dx*y,math.sqrt(dx*dx+dy*dy)
   Q0=avg(P0,P1)
   Q1=avg(P1,P2)
   Q2=avg(P2,P3)
   R0=avg(Q0,Q1)
   R1=avg(Q1,Q2)
   B=avg(R0,R1)
   print "*",n
   A0=euler363(P0,Q0,R0,B,n-1)
   print "!",n
   A1=euler363(B,R1,Q2,P3,n-1)
   print "%",n
   return A0[0]+A1[0],A0[1]+A1[1]

def e363():
   vlow=0.55177847
   vhigh=0.55177848
   for n in range(50):
      v=(vlow+vhigh)*0.5
      a,l=euler363((1,0),(1,v),(v,1),(0,1))
      if a>math.pi/4:
         vhigh=v
      else:
         vlow=v
      pi2=math.pi/2
      print Decimal(round(100*(l-pi2)/pi2,10))


e363()