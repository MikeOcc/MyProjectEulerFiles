# euler 358
from Functions import IsPrime

def check_order(x, p, n = None):
    """ Returns True if the order of x mod p is p-1 """
    if n is None:
        n = p - 1
    if pow(x, n, p) != 1:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            if pow(x, d, p) == 1 or pow(x, n//d, p) == 1:
                return False
        d += 1

    return True

p, q = 0, 0
while p != 99999:
    p = (p + 56789) % 100000
    q += 1

print "p,q",p,q

p = 10**11 // 138
pMin = p - p % 100000 + q
pMax = 10**11 // 137

print "pmin,pmax", pMin, pMax

for p in range(pMin, pMax, 100000):
    if IsPrime(p) and check_order(10, p):
        s = 9*(p-1)//2
        print p
        print ("Answer:", s)   # Answer: 3284144505