#
# Euler 56
#
#
#
from time import *
st=time()
maxn ,maxi,maxj= 0,0,0

for i in xrange(50,100):
  for j in xrange(50,100):
    
     y = sum([int(k) for k in str(i**j) ] )
     if y > maxn:
        maxn=y
        maxj=j
        maxi=i



print "Max Sum", maxi,maxj,maxn
print "process time is",time()-st

print max( [ sum( [ int( i ) for i in str( a ** b ) ] ) for a in xrange( 90, 100 ) for b in xrange( 90, 100 ) ] )

print sum([sum( [ int( i ) for i in str( a ** b ) ] ) for a in xrange( 90, 100 ) for b in xrange( 90, 100 )  ] )

print max(map(lambda x: sum(int(c) for c in str(x)), set(a**b for a in range(90, 100) for b in range(90, 100))))


print map(lambda x: sum(int(c) for c in str(x)), set(a**b for a in range(90, 100) for b in range(90, 100)))