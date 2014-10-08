
from Functions import gcd, RetFact, divisors
from math import factorial
from Functions import primes
from collections import defaultdict
from time import time
from itertools import combinations

st = time()
p = primes(10**8)

print "time to calculate seive up to 10**8 is ", time()-st

print len(p)

mx = (10**8)/2
d=defaultdict(int)
tot = 1

for i in xrange(2,10**8+1):
  if i in p:
    d[i]=1
  else:	
    f = RetFact(i)
    for ff in f:
     d[ff]+=1
	 
# for dd in d:
  # print dd,d[dd]

# l = sorted(d)

# for ll in l:
  # print ll,d[ll]
  
# for prime in p:
  # if prime > mx: tot += (prime**2)%(10000000000)
  
# tot = tot%1000000009

print tot

print "time elapsed is ", time() - st


