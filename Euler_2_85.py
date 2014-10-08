#
#  Euler Problem 85
#
#

from time import time
st=time()
desired_area=2000000
closest=10000
x,y = 0,0

for n in xrange(25, 101):
  for k in xrange(25, 101):

    if k>n:break

    total = abs(n*(n+1)*k*(k+1)/4 - desired_area)
        
    if total<closest:
       x = n
       y = k
       closest = total

print "Area of rectangle is",x,"*",y,"=", x*y
print "Number of Rectangles is", x*(x+1)*y*(y+1)/4
print "process time is", time()-st
print closest
