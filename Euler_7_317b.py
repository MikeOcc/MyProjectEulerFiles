#
#  Problem 317 - Fire Cracker
#
#
from math import pi, sin, cos
from time import time

st = time()
d={} 
t=0
ctr=0
theta = 0.0
fourA = 4.*4.905
xmax = 0
thetamax = 0
while pi/2.0 - theta >= 0.0:
 

  xsin = 20. * sin(theta)
  xcos = 20. * cos(theta)
  xcosg = xcos/9.81
  tzmax = xsin/9.81
  zmax = 100. + xsin * tzmax - 4.905 * tzmax**2

  BeSquare = 400.*(sin(theta)**2)
  
  #  Solve x for z(theta) and store.  If x(z) increaes update the 
  #  dictionary.  Climb from z = to to apex value of z.  Don't
  #  worry about the lesser value of x when z> 100.
  z = 0.0
  while True:
    if z>zmax:break
    # use quadratic formula to solve for t(z) ;  z = 100 + vt + 1/2 gt**2
    # t = (-20sin(theta) + (400sin(theta)**2 + 4(4.905)(100-z))**.5)/(9.81)
    # Sub t for formula in x;  x=vx*t = v*cos(theta)*t 
    x = xcosg * ( xsin + (BeSquare + fourA*(100.0-z))**.5)
    if x> xmax:
      xmax = x
      thetamax = theta
    if z not in d:
      d[z]=x
    else:
      if x>d[z]:
        d[z]=x
      # else:
        # #break
        # print "*",theta,z
    #print t,":",z,x
    z+= .1  #.0025

  theta += .0001    #.00005

V=0
f = sorted(d)

bef = 0
for i in f:
  if i == 0: continue

  V+= ((d[i]+d[bef])/2.0)**2*(i-bef)*pi
  bef = i


print '%f' % V
print '%f' % thetamax
print "xmax, thetamax", xmax, thetamax
print "time elapsed: ", time() - st
