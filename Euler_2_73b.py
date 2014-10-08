#
#
#  Euler 73
#

from Functions import gcd
from math import ceil
from time import time
st=time()
ctr = -2
d={}
# mini = 1./3.
# maxi = .5
for i in xrange(1,12001):
  x=int(ceil(i/3.))
  #print x	,i
  for j in xrange(x,int(i/2)+1 ):
    #val = (1.0*j)/i
    #print x
    if gcd(i,j) == 1:
      # if not( val>mini and val < maxi):
        # print i,j
        # continue
      if i*12000+j not in d:
        ctr +=1
        d[i*12000+j]=1
      


print "total is ", ctr
print "time elapsed is ", time()-st
