#
#
#  Euler Problem 320
#
#
from Functions import RetFact
from math import factorial


ifacts = []

P = 1234567890
#
#  start with factors of factorial 10 ([2,8],[3,4],[5,2],[7,1]), 
# count # of occurances
# and multiple by P 
#
iseed = [[2,8],[3,4],[5,2],[7,1]]
ifact = iseed

for j in xrange(4):
  nf = iseed[j][1]
  nf *= P
  ifact[j][1] = nf

print iseed
print ifact

'''
for i in xrange(2,n+1):
  fs = RetFact(i)
  for f in fs:
'''    

