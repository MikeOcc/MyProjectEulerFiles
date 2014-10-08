#
#
#  Euler 353
#
#
from time import time
from math import sin, cos, acos,pi
# ]

def d(p1,p2,r):

  theta = acos(p1[0]*p2[0]/float(r*r) + p1[1]*p2[1]/float(r*r) + p1[2]*p2[2]/float(r*r))
  return r*theta
  

def M(r):
  
  # x**2 + y**2 + (z-2**.5) = r*2 + 2

  l = []
  summ = 0
  for z in xrange(-r,r+1):
    for y in xrange(0,r+1):
      m = r**2 - z**2 - y**2 
      if m >=0:
        x = m**.5
        if int(x)==x:
          print z,y,x
          #print z,y,-x
          #break
          if (z,y,x)==(0,0,7.0):
            l.append((0,0,7))
          else:
            l.append((z,y,x))
          break
  print 
  print
  prevz = 0
  for i in xrange(0,len(l)):
    z = l[i][0]
    #if z==prevz:continue
    print l[i],
    prevz = z
    if i > 0:
      L = d(l[i],l[i-1],r)
      print l[i],l[i-1],r,L
      b = (L/(pi*r))**2
      print "b",b
      summ += b

    print "Sum",summ

#
#   (0,0,r),(0,0,-r),(0,r,0),(0,-r,0),(r,0,0),(-r,0,0)
#
#
#
#

R = 2**3-1

M(R)
print
print d((0,0,-7),(3,2,-6),7)
print d((0,0,-7),(-3,2,-6),7)
print d(( 3, 2,-6),(6,2,-3),7)
print d(( 3, 2,-6),(-6,2,-3),7)
print d(( 3, 2,-6),(2,6,-3),7)
print d(( 3, 2,-6),(-2,6,-3),7)

a= d((0,0,-7),(3,2,-6),7)
b= d((3,2,-6),(6,2,-3),7)
c= d((6,2,-3),(6,3,-2),7)

d1= d((6,3,-2),(6,3,2),7)

f= d((6,3,2), (3,2,6),7)

g= d((3,2,6),(2,3,6),7)

h= d((2,3,6),(0,0,7),7)
xx = (a,b,c,d1,f,g,h)

print xx

summm = 0
for v in xx:
  summm += (v/(pi*7))**2

print "Sum2", summm
