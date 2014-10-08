#
#  Problem 317 - Fire Cracker
#
#
from math import pi, sin, cos
from time import time

st = time()

# z = 100 + v(z) * t + .5 * 9.81 * t**2
# z = 100 + 20 * sin(theta) * t + 4.905 * t**2 
# zmax : t=0 => 120.3873598369011
# z = 0, theta = 0: t =  ((4* 4.905 * 100)**.5)/9.81
# xmax: t(z=0, theta=0) => 99.07330908846423

# mold parabola for zmax and xmax
# z = zmax - a* x**2
# a = zmax / xmax**2 = .0147625
def x(z):
  #if 120.3873598369011 - z < 0:  print z
  x = (round(120.3873598369011 - z,13) / .0122625) **.5
  
  return x
  
zmax = 120.3873598369011
num_slices = 4000000
inc = zmax / num_slices
#print inc
V = 0
for i in xrange(0,num_slices):
  #print i,x(i*inc)
  # z1 = i * inc
  # z2 = i *inc + inc
  # xavg = (x(z2) + x(z1))/2.
  # deltaV = inc * pi * xavg**2
  # V += deltaV
  V += inc * pi* ((x(i*inc) + x((i+1.)*inc))/2.0)**2
  
print '%f' % V

print "time elapsed: ", time() - st
