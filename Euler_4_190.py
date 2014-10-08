#
#
#  Euler Problem 190
#
#
from time import time

def P(m):

  x=[0]*(m+1)


  #summ = 0
  tot = 1
  k = 2.0 * float(m)/float(m*m + m)

  for i in xrange(1,m+1):
    #i * k
    x[i] = i * k
    #summ += x[i]
    tot *= x[i]**i

  #print x
  #print summ
  #print int(tot)

  return int(tot)

##############

st = time()

total = 0
for j in xrange(2,16):
  total += P(j)

print
print "Sum of P(m) is", total
print "process time is", time()-st





