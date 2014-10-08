#
#
#  Problem 347
#
#


from math import log10
from Functions import RofPrimes
from time import time

st = time()

N=10**7

p = RofPrimes(2,N/2+1)          # get range of primes


#print "primes",p
#logN = log10(N)
tot=0

# search through range of prime pairs p[i],p[j]
for i in xrange(0,len(p)+1):
  isFound = False    # detect when loop is churning out nothing but zeros

  for j in xrange(i+1,len(p)):
    p1,p2 = p[i],p[j]       # pull to save time for searching list multiple times

    m1 = int(log10(N/p2)/log10(p1))  #  find the highest possible exponent  
    m2 = int(log10(N/p1)/log10(p2))
    mn = 0                    #  set max # found to zero

    #  loop through all the possible exponent pairs.  I realize now that
    #  should of used log(N/p2) for exp1, yada yada to optimize
    for k in range(1,m1+1):
      for l in range(1,m2+1):
        val = p1**k * p2**l
        if val<=N and val>mn:
          mn = val
          isFound = True   #  We are still finding #s for the range, so we keep going
    #print i,j,":",p[i],p[j],mn
    tot+=mn      # sum the max #s, duh
    if isFound==False:break   # break out of the loops once we've reached the end
  if isFound==False:break

print "total for S(10 000 000) is", tot
print "process time is", time()-st
