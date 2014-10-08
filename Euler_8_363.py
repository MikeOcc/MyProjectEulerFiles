#
#
#  Euler 363
#
#
from math import pi


#
# x(t) = (2-3*v)*t**3 + (3*v-3)t**2 + 1
# y(t) = (3*v-2)*t**3 + (3-6*v)*t**2 + 3*v*t

def x(t,v):

  # (2-3*v)*t**3 + (3*v-3)*t**2 + 1

  #return (2-3*v)*t**3 + (3*v-3)*t**2 + 1
  return 3*t*(-3*t*v+2*t+2*v-2)
  
def y(t,v):

  #  (3*v-2)*t**3 + (3-6*v)*t**2 + 3*v*t
  #return (3*v-2)*t**3 + (3-6*v)*t**2 + 3*v*t
  return 3*(t-1)*(t*(3*v-2)-v)

def xprime(t,v):

  # 3*(2-3*v)*t**2 + 2*(3*v-3)*t
  return (6 - 9*v)*t**2 + (6*v - 6)*t

def yprime(t,v):

  # 3*(3*v-2)*t**2 + 2*(3-6*v)*t + 3*v
  return (9*v-6)*t**2 + (6-12*v)*t + 3*v


v = 2. -((66.-15.*pi)**.5/3.)

prev = 0
prec = int(1./0.00000095367431640625)
deltat = 0.00000095367431640625
L=0
for i in xrange(1,prec):
  
  t = i * deltat

  dx = xprime(t,v) - xprime(prev,v)
  dy = yprime(t,v) - yprime(prev,v)
  #print prev,t,dx,dy
  prev = t

  L += (dx**2 + dy**2)**.5

print L






