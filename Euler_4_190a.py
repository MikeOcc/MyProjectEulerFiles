#
#
#  Euler Problem 190
#
#
from time import time

def P(m):
  tot = 1
  k = 2.0 * float(m)/float(m*m + m)

  for i in xrange(1,m+1):tot *= (i * k)**i

  return int(tot)

st = time()

print "Sum of P(m) is",sum([P(j) for j in range(2,16)])
print "process time is", time()-st





