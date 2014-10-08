#
#  Euler 142
#
from Functions import RetFact

def IsSq(sq):
  z = int(sq**.5)
  return pow(z,2)==sq


def f(x,y,z):

  if IsSq(x+y) and IsSq(x-y) and IsSq(x+z) and IsSq(x-z) and IsSq(y+z) and IsSq(y-z): return True

x1,y1,z1 = 0,0,0
minxyz = 0
# for x in xrange(300000,400000):
  # for y in xrange(3,x):
    # for z in xrange(2,y):

      # if x>y>z and f(x,y,z):
        # t = x+y+z
        # if minxyz==0:
          # minxyz = t
          # x1,y1,z1 = x,y,z
          # print x1,y1,z1,t
        # elif t < minxyz:
          # minxyz = t
          # x1,y1,z1 = x,y,z


for z in xrange(10000,20000):
  for y in xrange(z+1,z+6000):
    if IsSq(y-z) and IsSq(y+z):
	  #print x,y,z
      for x in xrange(y+1,y+4000):
      #if x-y < 1 : continue  
        if IsSq(x+y) and IsSq(x-y) and IsSq(x+z) and IsSq(x-z) and IsSq(y+z):print x,y,z

#print minxyz
print x1,y1,z1

             











