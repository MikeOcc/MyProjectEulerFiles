from math import *
from string import strip

def perfect(n):
  for i in xrange(2,29):
     x=round(pow(n,1./float(i)),6)
     if x**i==n:
        print "perfect, niic: for #",n,"to the",strip(str(i))+"th root returns:",x
        return True
     if x<2:return False
  return False

i,ctr=1,0
while ctr<2000:
  i+=1
  if perfect(i):
    ctr+=1
     #;print ctr,i
     #pass