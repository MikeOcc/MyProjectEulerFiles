#
#
#
#
#
from math import ceil
from Functions import nCr,RetFact
from time import time

st = time()

sf = {}

for r in xrange(0, 51):
  for c in xrange(1,int(ceil(r/2))+1): 
    v = nCr(r,c)
    if v in sf: continue
    facts = RetFact(v)
    setfacts = set(facts)
    if len(facts)>len(setfacts): continue
    sf[v]=v

print
#print sf
#print

print 1 + sum(sf)
print time()-st











