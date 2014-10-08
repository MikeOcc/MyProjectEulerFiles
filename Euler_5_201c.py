#
#
#  Euler Problem 201
#
from Functions import nCr
from itertools import combinations

#print nCr(100,50)

S = sorted(set(i*i for i in xrange(1,101)))
#S = sorted(set(i*i for i in xrange(100,1,-1)), reverse=True)

print S
print
summin = sum(S[:50])
summax = sum(S[50:])

print summin, summax, summax - summin
print

dict1 = {}

#sets = combinations(S,2)

cnt = 0

for i in range(0,51):
 
  cnt+=1
  summ = sum(S[i:i+50])

  print i,S[i],S[i+49], summ
  dict1[summ]=(

