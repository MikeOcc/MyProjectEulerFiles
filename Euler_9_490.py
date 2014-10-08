from itertools import combinations
from Functions import gcd, nCr

def T(n):

  ntmax = n/2
  tot = 0
  for i in xrange(ntmax):
    opentiles = n - i*2
    c = nCr(n,opentiles)
    tot +=c
    print n,i,opentiles, c, 10**opentiles
  return tot
	
for i in xrange( 2, 10):
  print T(i)