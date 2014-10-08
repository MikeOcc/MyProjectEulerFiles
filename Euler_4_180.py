#
#  Euler 180
#
from itertools import combinations

def f1n(n,x,y,z):
#
#  x**(n+1) + y**(n+1) - z**(n+1)
#
#  n=-2   :=>   x^-1 + y^-1 -z^-1
#  n=-1   :=>   1 +1 - 1 = 1
#  n=1    :=>   x^2 + y^2 -z^2
#  n=2    :=>   x^3 + y^3 -z^3
#
  return x**(n+1) + y**(n+1) - z**(n+1)   


def f2n(n,x,y,z):
#
# (x*y + y*z + z*x)*(x**(n-1) + y**(n-1) - z**(n-1))
#
#  n=-2   :=>   (x*y + y*z + z*x)*(x^-3 + y^-3 - z^-3)= (yx^-2 + xy^-2 - xyz^-3) + (yzx^-3 + zy^-2 - yz^-2) + (zx^-2 + zxy^-3 - xz^-2)
#
#  n=-1   :=>   (x*y + y*z + z*x)*(x^-2 + y^-2 -z^-2)= (yx^-1 + xy^-1 - xyz^-2) + (yzx^-2 + zy^-1 - 
#  n=1    :=>   (x*y + y*z + z*x)*(1+1-1) = (x*y + y*z + z*x)
#  n=2    :=>   (x*y + y*z + z*x)*
#

  return (x*y + y*z + z*x)*(x**(n-1) + y**(n-1) - z**(n-1))  #  yx


def f3n(n,x,y,z):
#
#
#
#
#
#
  return (x*y*z)*(x**(n-2) + y**(n-2) - z**(n-2))   #  x^n-1*yz - x*y^n-1z 


def fn(n,x,y,z):

  return f1n(n,x,y,z) + f2n(n,x,y,z) + f3n(n,x,y,z)



##################
n=-3

xyz1 = []

for b in range(2,11):
  for a in xrange(1,b):
    xyz1.append((a,b))

print "Len xyz1", len(xyz1)

print xyz1
#exit()

summ=[]
while 1:
  n+=1

  if n==0:continue

  XYZ = combinations(xyz1,3)

  for xyz in XYZ:
    x = float(xyz[0][0])/xyz[0][1]
    y = float(xyz[1][0])/xyz[1][1]
    z = float(xyz[2][0])/xyz[2][1]
    print "xyz",x,y,z
    a=fn(n,x,y,z)

    if a==0:
      print "hit!", n,x,y,z,(x+y+z)
      if not (x+y+z) in summ:summ.append(x+y+z)
    else: 
      print "$",n,x,y,z,a

  if n > 1:break


print len(summ)
print sum(summ)



