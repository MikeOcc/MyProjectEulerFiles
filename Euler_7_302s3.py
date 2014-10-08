import math
import fractions
from Functions import primes as pr
from time import time

global primes

global plen

st = time()
primes = pr(int((10**14/4)**(1/3.)))     # [x for x in range(pmax) if p[x]]
plen = len(primes)

print "length of prime set is", plen

def factor(x):
    factors = {}
    for p in primes:
        if p * p > x:
            break
        i = 0
        while x % p == 0:
            x //= p
            i += 1
        if i:
            factors[p] = i
    if x > 1:
        factors[x] = 1
    return factors

	
def totient(f):
    ff = f.copy()
    for x, c in f.items():
        for k, cc in factors[x-1].items():
            if k in ff:
                ff[k] += cc
            else:
                ff[k] = cc
        if ff[x] == 1:
            del ff[x]
        else:
            ff[x] -= 1
    return ff	

	
def a(x):
    g = 0
    for f, c in totient(x).items():
        if c == 1:
            return False
        g = fractions.gcd(g, c)
    return g == 1
	

def z(n=1, g=0, imax=plen):
    for i in reversed(range(imax)):
        k = 3 if n == 1 else 2
        nn = n * primes[i] ** k
        while nn < nmax:
            f[primes[i]] = k
            gg = fractions.gcd(g, k)
            if gg == 1:
                yield f
            for x in z(nn, gg, i):
                yield x
            k += 1
            nn *= primes[i]
            del f[primes[i]]
	
	
	
nmax = 10 ** 14

pmax = int((nmax // 4) ** (1 / 3))

p = pmax*[True]

p[0:2] = [False,False]

for x in range(2, int(math.sqrt(pmax) + 1)):
    if p[x]:
        for y in range(2 * x, pmax, x):
            p[y] = False


factors = {p-1: factor(p-1) for p in primes}
factors[1] = {}
    
f = {}

print(sum(1 for x in z() if a(x)))
print "time elapsed is", time()-st