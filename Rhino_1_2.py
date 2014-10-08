from math import *

def perfect(n):
  for i in xrange(2,14):
     if round(pow(n,1./float(i)),6)**i==n:return True
  return False
i,ctr=1,0
while ctr<1000:
  i+=1
  if not perfect(i):ctr+=1
print ctr,"nth # is",i
     