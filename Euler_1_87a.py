#
#
#  Euler Problem 87
#
summ = 0
from Functions import RofPrimes
from time import time
st = time()

r1 = RofPrimes(2,7100)
r2 = RofPrimes(2,380)
r3 = RofPrimes(2,92)

numlist = []

for i in r1:
  a = i**2
  for j in r2:
    b= j **3
    for k in r3:
      bignum = a + b + k**4
      if bignum < 50000000:
         #print i,j,k,bignum
         numlist.append(bignum)


numset=set(numlist)
summ = len(numset)


print "Answer is", summ
print "Process time is", time()-st