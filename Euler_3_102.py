#
#
#  Euler Problem 102
#
# []
from itertools import izip
from time import time
from string import *

def dot(a,b):
  return sum(x*y for (x,y) in izip(a,b))

def PIT(A,B,C):

  v0 = (C[0]-A[0],C[1]-A[1])
  v1 = (B[0]-A[0],B[1]-A[1])
  v2 = (0-A[0],0-A[1])

  d00 = dot(v0,v0)
  d01 = dot(v0,v1)
  d02 = dot(v0,v2)
  d11 = dot(v1,v1)
  d12 = dot(v1,v2)

  inv = 1.0 / (d00 * d11 - d01 * d01)
  u = (d11 * d02 - d01 * d12) * inv
  v = (d00 * d12 - d01 * d02) * inv

  # Check if point is in triangle
  return (u > 0) and (v > 0) and (u + v < 1)

st = time()
f = open('triangles.txt','r')
x = f.readlines()

ctr = 0

for a in x:
 
  b = a.strip().split(",")
  v1 = (int(b[0]),int(b[1]))
  v2 = (int(b[2]),int(b[3]))
  v3 = (int(b[4]),int(b[5]))

  ctr += PIT(v1,v2,v3)


print "The number of triangles out of 1000 that contain the origin is", ctr
print "Process time is", time()-st











