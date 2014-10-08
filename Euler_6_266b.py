#
# Problem 266
#[]
#
global basex

basex=1777

from Functions import IsPrime,RofPrimes
from math import floor,sqrt
from itertools import combinations

def bs(v,L):
  lo = 0
  hi = len(L)
  while (hi-lo) >= 200:

    
    mid = (lo+hi)/2
    midval = L[mid]
    #print "!",lo,hi,v,midval
    if midval < v:
      lo = mid+1
    elif midval > v: 
      hi = mid
    else:
      return mid
  return lo
    
          

def ml(L):

 v = 1
 for lv in L:
   v*=lv
 return v

primes = RofPrimes(2,190)
p=1
for P in primes:
  p*=P

b = int(p**.5)

print "b:",b

s1,s2,=[],[]
for i in xrange(0,42):
  if i%2==0:
    s1.append(primes[i])
  else:
    s2.append(primes[i])


print s1
print s2
P1=[];P2=[]

ctr=0
for i in xrange(1,22):
  zzz = combinations(s1,i)
  for zzzz in zzz:
   val = ml(zzzz)
   P1.append(val)
   ctr+=1
P1 = sorted(P1)

for i in xrange(1,22):
  zzz = combinations(s2,i)
  for zzzz in zzz:
   val = ml(zzzz)
   P2.append(val)

P2 = sorted(P2)

print "counter",ctr

nv=2200000000000000000000000000000000000;ctr=1

ln = len(P2)

for p1 in P1:

  fv = b/p1

  i = bs(fv,P2)
  #print p1,i
  for j in xrange(i-100,i+100):
     if j>=ln or j<0:continue
     val = p1*P2[j]
     if val>nv and val < b:
        nv = val
        print ctr,":",nv,":",nv%10**16;ctr+=1
 
print nv%10**16

exit()


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
 

