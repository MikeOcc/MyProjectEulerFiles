#
#
#  Euler 120
#
#


def f(a,n):

  return ((a-1)**n + (a+1)**n)%a**2


rmax = 0
nth = 0
summ = 0

for j in xrange(3,1001):
  nth=0
  rmax=0
  for i in xrange(1,1500):
    r = f(j,i)
    if r>rmax:
      rmax=r
      nth=i
  print nth,rmax
  summ+=rmax

print
print "sum of rmax is",summ

