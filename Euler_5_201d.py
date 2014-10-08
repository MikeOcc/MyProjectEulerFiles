#
#
#  Euler Problem 201
#
from Functions import nCr
from itertools import combinations

#print nCr(100,50)


def find(i,S):

  n=i
  nc = 0
  for i in range(1,101):
    val = sum(S[i:49+1])
    if val ==i:
       nc+=1
    else if val>i:
       x = combinations(S[1:49+i],50):
       for j in x:
        if sum(j)==n:
          nc+=1
        
   





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

for i in xrange(summin,summax+1):
 
  x = numsols(i,S)


