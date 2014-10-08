#
#
#  Euler 228
#
#
from math import sin, cos, pi
def S(k):

  V= []

  for n in xrange(1,k+1):
    x = cos((2*k-1)/n*pi/2)
    y = sin((2*k-1)/n*pi/2)
    V.append((x,y))

  return V

s=1864
for i in xrange(1865, 1910):
  s+= i - 1



print s


print S(3)
print S(4)

