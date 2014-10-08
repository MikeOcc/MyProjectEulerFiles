


from Functions import IsPrime, RofPrimes
from itertools import combinations




Spot = 10**3

#P=[]

P = RofPrimes(2,100)

print P
print len(P)

X = combinations(P,4)

for x in X:
  print x





  