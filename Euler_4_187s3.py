import math
from time import time
st = time()
 
nmax = 10 ** 8
 
primes = nmax // 2*[True]
 
primes[0:2] = [False,False]
 
for x in range(2, int(math.sqrt(nmax // 2) + 1)):
    if primes[x]:
        for y in range(2 * x, len(primes), x):
            primes[y] = False
 
p = [x for x in range(len(primes)) if primes[x]]
 
c = 0
 
for x in range(len(p)):
    for y in range(x, len(p)):
        if p[x] * p[y] >= nmax:
            break
        c += 1
 
print(c)
print "process time",time()-st