#
#  Euler Problem 251
#
#
#
from math import *
from time import time

st = time()
ctr = 0
lim = 110000000
maxi,maxj,maxk=0,0,0

for i in xrange(1,6000):
  a = i * 3 -1
  f = (i**2) * (8*i -3)

  if f< lim:
    b=1;c=f
    if a + b + c > lim:continue
    ctr+=1
    #print a, b,c,":",a+b+c,ctr
    

 
  for j in range(2,int(sqrt(f))+1):
    if f/float(j*j) == int( f/j/j):
      b= j; c = f/(j*j)
      if a + b + c > lim:continue
      ctr+=1 
      #print a, b,c,":",a+b+c,ctr
      

print "Number of Cardano Triplets <=",lim, "is", ctr
print "Process time is", time()-st
