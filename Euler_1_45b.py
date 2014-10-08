#
#
#  Euler Problem 35
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.
#

from math import *


print

tset = []
pset = []
hset = []
iset = []

xtra = 100000000

for i in range(286, 286 + xtra):

  tnum = int((i*i +i)/2.0)

  tset.append(tnum)

for i in range(166, 166 + xtra):
  pnum = (3.*i*i -i)/2.0
  pset.append(pnum)

for i in range(285, 285 + xtra):
  hnum = (2.*i*i -i)
  hset.append(hnum)

Tset = set(tset)
Pset = set(pset)
Hset = set(hset)

Iset = Tset.intersection(Pset)
TPHset = Iset.intersection(Hset)

print Iset
print TPHset


