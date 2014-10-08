#
#
#  Euler 363
#
#
from math import pi
from decimal import Decimal

'''
def avgcp(p1,p2):   # average of 2 control points
  xavg = (p1[0] + p2[0])/2.0
  yavg = (p1[1] + p2[1])/2.0  

  return xavg, yavg



Pi4 = pi/4.0
v0 = .35
v1 = .65

P0=[1,0]
P1=[1,v]
P2=[v,1]
P3=[0,1]

Area,L = 0,0
prev = -1

while 1:

  v = (v0 + v1)/2.0
'''

def x(t,v):
  return (1-t)*(1-t)*(1-t)+3*(1-t)*(1-t)*t+3*(1-t)*t*t*v  

def y(t,v):
  return t*t*t+3*t*t*(1-t)+3*t*(1-t)*(1-t)*v

def Dist(x1,y1,x2,y2):
  return ((x2-x1)**2 + (y2-y1)**2)**.5

d = 300000
low = .5
high = .6
while (high - low > 1e-9):

  v = (high+low)/2
  S = 0
  for i in xrange(d):
    cur = i/d
    nex = (i+1)/d
    S += x(cur, v)*y(nex, v)-x(nex, v)*y(cur, v)
    if (S > pi/2):
       high = v
    else:
       low = v

print "v",v

L = 0
d = 3000
for i in xrange(d): 
  cur = i/d
  nex = (i+1)/d
  L += Dist(x(cur, low), y(cur, low), x(nex, low), y(nex, low))
  print L
print (100*(L-pi/2.)/pi*2.)





