#
#
#  Euler Problem 4 173
#
#
# number of tiles n for side l
#  n = 2*L + 2*(L-2) = 4*l - 4
#
# formula for laminae (OL,IL):
#  for even OL:
#  OL**2 - IL**2
#
#
from time import time
from math import *
from itertools import count
st = time()
lim = 1000000
laminae=[]
OL = int((lim + 4.)/4.)
ctr=0




for i in xrange(OL,2,-1):
  #  for j in xrange(i-2,0,-2):
  if i**2-lim <=0:z=0
  else:z=int(sqrt(i**2-lim))-1
  ctr+=sum(int(i**2 -j**2 <=lim) for j in xrange(i-2,z,-2))
     
  #   ctr+=1
  #   print ctr,"), i,j",i,j
  #   laminae.append((i**2-j**2,i,j))
print ctr
print "Process time is", time()-st
