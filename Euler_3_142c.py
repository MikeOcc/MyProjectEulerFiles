#
#  Euler 142
#
from time import time

def IsSq(sq):
  return sq == (int(sq**.5))**2


def f(x,y,z):

  if IsSq(x+y) and IsSq(x-y) and IsSq(x+z) and IsSq(x-z) and IsSq(y+z) and IsSq(y-z): return True

st = time()

for n in xrange(100,1000):
  for m in xrange(n + 2 ,n+1000,2):

    x =  int((m**2 + n**2))/2
    y =  int((m**2 - n**2))/2
    #if int(x)!=x:continue
    #print x,y,x+y,(x+y)**.5
    #print x,y,x-y,(x-y)**.5

    #print
    for p in xrange(500, 1000):
        if (2*y-p**2)<1:break
        o = (2*y-p**2)**.5
        z= int((o**2-p**2)/2.)

        if f(x,y,z): 
           print "yeah!!!!!!!"
           print int(o),p,m,n,":",x,y,z,x+y+z
           print "elapsed time is ",time()-st
           exit()






