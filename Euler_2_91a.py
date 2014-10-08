#
#
#  Euler Problem 91
#
from time import time

def d(p1,p2):
  # determine distance between two points
  dx = p1[0]-p2[0]
  dy = p1[1]-p2[1]
  return (dx**2 + dy**2)  

st = time()

ctr = 0
x1=0;y1=0
p1 = (0,0)
for x2 in xrange(0,51):
  for y2 in xrange(0,51):
     for x3 in xrange(0,51):
       for y3 in xrange(0,51):

          # this should optimize the count since any triangle that has points P2 and P3 
          # on the x/y axes is automatically a right triangle but it actually slowed it by a couple secs 
          #if (x2==0 and y3==0) or (x3==0 and y2==0): ctr+=1;continue

          p2 = (x2,y2)
          p3 = (x3,y3)
          if (p1==p2 or p1==p3 or p2==p3):continue

          a=d(p1,p2);b=d(p1,p3);c=d(p2,p3)

          if (a+b==c) or (a+c==b) or (b+c==a) : ctr+=1

print
print "Total # of Right Triangles for range L=50 is",ctr/2
print "process time is", time()-st
           

