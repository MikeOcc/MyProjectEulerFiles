#
#  Euler 204
#

from sets import Set
from math import log10, ceil

from Functions import RetFact,IsPrime,primes


p = primes(100)

end = 10**9

def doIt(setin,mul):
    s = set()
    for y in setin:
        z = y
        while z <end:
            s.add(z)
            z*=mul
    return s
s= set()
s.add(1)
for x in p:
    s = doIt(s,x)
print len(s)