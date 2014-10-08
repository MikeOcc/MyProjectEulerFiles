#
#  Problem 317 - Fire Cracker
#
#
from math import pi, sin, cos

def fragheight(v,theta):

  h =200 + (v**2 * (sin(theta))**2)/(2*9.81)

  return h


def fragdist(v,theta):

  d = (v**2 * (sin(2*theta))**2)/9.81

  return h


  
d={} 
t=0
ctr=0
theta = 0
zsupermax = 0
while pi/2.0 - theta > 4.9e-15:
  t=0
  ctr=0  
  z = 0
  tzmax = 20*sin(theta)/9.81
  zmax = 100. + 20. * sin(theta) * tzmax - 4.905 * tzmax**2
  xcos = 20. * cos(theta)
  xsin = 20. * sin(theta)
  zippy = 4.*4.905
  blah = 400.*(sin(theta)**2)
  while True:
    if z>zmax:break
    #z = 100 + 20 * sin(theta) * t- 4.905 * t**2
    # -4.905t^2 + 20sin(theta)t + (100-z)
    # t = (-20sin(theta) + (400sin(theta)**2 + 4(4.905)(100-z))**.5)/(9.81)
    #print theta,z,
    #x = 20 * cos(theta) * ( 20 * sin(theta) + (400*sin(theta)**2 + 4*4.905*(100-z))**.5)/(9.81)
    x = xcos * ( xsin + (blah + zippy*(100.0-z))**.5)/(9.81)
    if z < 0:break
    if z not in d:
      d[z]=x
    else:
      if x>d[z]:
        d[z]=x
        #print "*",
    #print t,":",z,x
    z+=.0001

  theta += .01

V=0
l = len(d)

#print d

f = sorted(d)

for i in f:
  #V += ((f[i] + f[i-1])/2.0)**2 * pi * .001 
  V += (d[i])**2 * pi * .0001
  #print "V:",V
print '%f' % V

