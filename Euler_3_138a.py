#
#  Euler 138
#
from time import time
st = time()

def a(n):

  if n == 0:
    return 1
  elif n == 1:
    return 17
  else:
    return 18*a(n-1)-a(n-2) 
##############################
tot = 0

for i in xrange(1,13):
  L = a(i)
  tot += L
  print L


print "Total is ", tot
print "Time Elapsed is",time() - st