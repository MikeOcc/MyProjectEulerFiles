#
#  Euler 142
#

def IsSq(sq):
  return sq**.5 == int(sq**.5)


def f(x,y,z):

  if IsSq(x+y) and IsSq(x-y) and IsSq(x+z) and IsSq(x-z) and IsSq(y+z) and IsSq(y-z): return True

x1,y1,z1 = 0,0,0
minxyz = 0
for x in xrange(300000,400000):
  for y in xrange(3,x):
    for z in xrange(2,y):

      if x>y>z and f(x,y,z):
        t = x+y+z
        if minxyz==0:
          minxyz = t
          x1,y1,z1 = x,y,z
          print x1,y1,z1,t
        elif t < minxyz:
          minxyz = t
          x1,y1,z1 = x,y,z


print minxyz
print x1,y1,z1

             











