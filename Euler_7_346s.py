from math import sqrt
import itertools
from time import time
st=time()
repunitsDict = {}
 
LIMIT = 10 ** 12
BASE_LIMIT = int(sqrt(LIMIT))
 
for base in xrange (2, BASE_LIMIT + 1):
    for n in itertools.count(3):
        value = (base ** n - 1) / (base - 1)
        
        if value >= LIMIT: break
        #print "base,n,value:",base,n,value
        repunitsDict[value] = 1
 
result = 1 + sum(repunitsDict.keys())  # 1 is special case.
 
print "Result:", result
print "process time", time()-st