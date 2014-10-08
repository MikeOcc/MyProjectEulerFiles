#
#  Euler Problem 251
#
#
#
from math import *

ctr = 0
lim = 1000
maxi,maxj,maxk=0,0,0

for i in xrange(1,445):
  for j in xrange(1,1000):
    for k in xrange(1,1000):

      ii,jj,kk = float(i),float(j),float(k)
      #print "IJK:", i,j,k
      if i + j + k > lim: continue
      
      r1 = (ii + jj*sqrt(kk))**(1./3.)
      r2 = ii - jj*sqrt(kk)
      if r2 < 0:
        r2 = -abs(r2)**(1./3.)
      z = round(r1 + r2,7)
      
      #z = (ii + jj*sqrt(kk))**(1./3.) + (ii - jj*sqrt(kk))**(1./3.)
      
      if z==1.0:
        ctr+=1
        print i,j,k,":",z, " # of hits:",ctr
        if i>maxi:maxi=i
        if j>maxj:maxi=j
        if k>maxk:maxi=k

print "Number of Cardano Triplets <=",lim, "is", ctr, maxi,maxi,maxk