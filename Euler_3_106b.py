#
#
# Euler 106
#
#

from itertools import combinations

def f(n):
  t = 0
  S= set(range(1,n+1))

  c1 = combinations(range(1,n+1),n//2)

  for s in c1:
    B = set(s); C = S-B
    if list(B)[0]  <  list(C)[0] : 
      print B,C,sum(B),sum(C),sum(B)==sum(C)
      t += sum(B)==sum(C)
  return t  


total = 0
for i in xrange(4,13,2):
  sum1 = f(i)     #len(generator(12,i))
  print i,sum1
  total += sum1

print "total", total