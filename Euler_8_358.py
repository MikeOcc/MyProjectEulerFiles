#
#
#  Euler 358
#
#
from Functions import RofPrimes

def HasAll(n):

  nstr=str(n)
  for j in xrange(1,10):
    if str(j) not in nstr:return False
  return True

b = 10
p = 7

#print (b**(p-1) -1)/p
M=7
P = RofPrimes(M,M+100)

for p in P:
  print
  #print p, (pow(b,p-1)-1)/p  #   (b**(p-1) -1)/p
  c = (b**(p-1) -1)/p
  l = len(str(c))
  #if c%100000==56789:
  #if HasAll(c):
  print p, c , l, len(str(c*l)), len(str(c*(l+1)))
  #  break
