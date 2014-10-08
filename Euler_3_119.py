#
#
#  Euler Problem 119
#
#
from time import time

def sumofdigits(n):
    total = 0
    while n>0:
        total += n%10
        n //= 10
    return total

st = time()
L = []

for j in xrange(2,10):
  for i in xrange(2,j*11):

    n = i**j

    #if i == sum([int(m) for m in list(str(n))]):
    if i == sumofdigits(n):
      #print j,i,n
      if n not in L:
        L.append(n)
print
#print
L = sorted(L)
#print L
#print 
#print len(L)
#print
print "Answer is",L[29]
print "Process time is", time()-st
