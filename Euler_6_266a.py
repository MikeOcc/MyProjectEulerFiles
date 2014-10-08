#
# Problem 266
#[]
#
global basex

basex=1777

from Functions import IsPrime,RofPrimes
from math import floor,sqrt
from itertools import combinations

def ml(L):

 v = 1
 for lv in L:
   v*=lv
 return v

primes = RofPrimes(5,190)
p=1
for P in primes:
  p*=P

b = int(p**.5)
print b
print
l = len(primes)
print l
print
rmin,rmax=0,0
z,zp=1,1
for i in xrange(l):
  zp = z
  z *= primes[i]
  if z>b:
    rmin = i-1
    print "min =",zp,
    print "rmin",rmin
    break


z,zp=1,1
print "$$$$$$$$"
for i in xrange(l-1,0,-1):
  zp = z
  z *= primes[i]

  if z>b:
    rmax = l-i
    print "max =",zp
    print "rmax",rmax,i+1
    break

nv=0;ctr=1

load = combinations(primes,21)
for sperms in load:
     numsperms=ml(sperms)
     if numsperms>nv and numsperms < b:
        nv = numsperms
        print ctr,":",nv;ctr+=1
 

