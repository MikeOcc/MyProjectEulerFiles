#
#  Problem 317 - Fire Cracker
#
#
from math import pi, sin, cos
from time import time

def fragheight(v,theta):

  h =200 + (v**2 * (sin(theta))**2)/(2*9.81)

  return h


def fragdist(v,theta):

  d = (v**2 * (sin(2*theta))**2)/9.81

  return h


st = time()
d={} 
t=0
ctr=0
theta = 0.0
zsupermax = 0
fourA = 4.*4.905
d[0]=(20. * ( fourA*(100.0))**.5)/9.81
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
  z = zmax # 0.0
  while True:
    #if z>zmax:break
    if z<0:break
    # use quadratic formula to solve for t(z) ;  z = 100 + vt + 1/2 gt**2
    # t = (-20sin(theta) + (400sin(theta)**2 + 4(4.905)(100-z))**.5)/(9.81)
    # Sub t for formula in x;  x=vx*t = v*cos(theta)*t 
    #if BeSquare + fourA*(100.0-z) <0: print theta,z,BeSquare + fourA*(100.0-z)
    x = xcosg * ( xsin + round(BeSquare + fourA*(100.0-z),10)**.5)

    if z not in d:
      d[z]=x
    else:
      if x>d[z]:
        d[z]=x
      #else:
        #break
        #print "*",
    #print t,":",z,x
    #z+=.01
    z-=.01

  theta += .005    #.00005

V=0
l = len(d)

#print d

f = sorted(d)

bef = 0
for i in f:
  if i == 0: continue
  #print i,
  V+= ((d[i]+d[bef])/2.0)**2*(i-bef)*pi
  bef = i
  #V += ((f[i] + f[i-1])/2.0)**2 * pi * .001 
  #V += (d[i])**2 * pi * .0001
  #print "V:",V

print '%f' % V

print "time elapsed: ", time() - st
