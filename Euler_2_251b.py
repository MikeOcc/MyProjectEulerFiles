#
#  Euler Problem 251
#
#
#
from math import *
from time import time

st = time()
ctr = 0
lim = 1000
maxi,maxj,maxk=0,0,0

for i in xrange(1,149):
  ii = i * 3 -1
  for j in xrange(1,1000):
    for k in xrange(1,1000):

      ii,jj,kk = float(ii),float(j),float(k)
      #print "IJK:", ii,j,k
      if ii + j + k > lim: continue
      
      r1 = (ii + jj*sqrt(kk))**(1./3.)
      r2 = ii - jj*sqrt(kk)
      if r2 < 0:
        r2 = -abs(r2)**(1./3.)
      z = round(r1 + r2,7)
      
      #z = (ii + jj*sqrt(kk))**(1./3.) + (ii - jj*sqrt(kk))**(1./3.)
      
      if z==1.0:
        ctr+=1
        print int(ii),j,k,":",z, " # of hits:",ctr
        if ii>maxi:maxi=ii
        if j>maxj:maxj=j
        if k>maxk:maxk=k

print "Number of Cardano Triplets <=",lim, "is", ctr, maxi,maxj,maxk
print "Process time is", time()-st
