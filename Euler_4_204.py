#
#  Euler 204
#

# -1]  

from Functions import IsPrime

factors = [] 

for i in range(2,100):
  if IsPrime(i):
    factors.append(i)

from itertools import combinations

print factors
x = combinations(factors,len(factors)/2)
ctr=0
for z in x:
  print z
  mut =1 
  for y in z:
     mut*=y
     if y <=10**9:
       ctr+=1

print ctr