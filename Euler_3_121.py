#
#
#  Euler Problem 121
#
#
from math import factorial
from time import time

def genfunc(n):
  # generate coefficients of generating function
  p = [0]*(n+1)
  p[0] = 1

  for i in xrange(n+1):
    for j in xrange(n,0,-1):
      prev = p[j]
      p[j] += i * p[j-1]
      #print i,j,prev,p[j-1],p[j]

  #print p   # uncomment to find full generating func.
  return p

st = time()

for n in xrange(15,16):
  P = genfunc(n)
  # determine # of numerators (i.e., how many blue chip
  # combos that generate a win.
  if n%2==0:
    m = n/2 
  else:
    m = (n-1)/2 + 1
  
  # sum req. # of numerations and divide by (n+1)!
  # invert and take int to obtain max prize allowed.
  Pn = sum(P[:m])/float(factorial(n+1))
  print n,P[:m],Pn, ":",int(1./Pn)

print "process time is", time() - st


