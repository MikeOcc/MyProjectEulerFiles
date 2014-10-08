from Functions import gcd
from math import sqrt

L = 1500000
sqrt_L = int(sqrt(L))
tx = [0]*L
for i in range(1, sqrt_L, 2):
  for j in range(2, sqrt_L- i , 2):
    if gcd(i, j) == 1: 
      sum = abs(j*j - i*i) + 2*i*j + i*i + j*j
      for s in range(sum, L, sum):
        tx[s]+=1
 
print "Answer to PE75 = ", tx.count(1)