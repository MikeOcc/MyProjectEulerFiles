#
#
#  Euler 73
#
"""
from Functions import gcd
 
L = 12000+1
c = 0
for n in range(5, L):
  for k in range(n/3 + 1, (n-1)/2 + 1):
    if gcd(n,k) == 1: c+=1
 
print "Answer to PE73 =", c
"""
from math import floor, ceil

u = 1.0 / 2.0
l = 1.0 / 3.0
lim = 12000
 
def interval(l, u, d):
  return range(int(floor(l*d)+1), int(ceil(u*d)-1)+1)
 
# all fractions in the interval as sieve[denominator] = set([nominators])
sieve = [set([])]
s = 0
for i in range(1, lim+1):
  sieve.append(set(interval(l, u, i)))
 
i = 0
for denom in sieve:
  for nom in denom:
    # delete all fractions that you get from extending the current one
    for n in range(2, lim/i+1):
      sieve[n * i].discard(n * nom)
  i += 1
  s += len(denom)
print s
