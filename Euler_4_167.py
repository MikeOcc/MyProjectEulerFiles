#
#
#
#
from itertools import *
from time import time
st = time()
i = 1
while 1:
  i+=1
  if i > 10**11:
    breal

print "process time", time()-st
exit()



u = [2,5]
#u[0] = 0
#u[1] = 1
#u[2] = 2
x = u[-1]
for i in xrange(1,800):
  x +=1
  numsols = 0
 
  for y in combinations(u,2):
    if sum(y) == x:
      #print i,x,y
      numsols +=1
      if numsols > 1:
        break
  if numsols == 1:
     u.append(x)


print u
print sum(u)
print
sy=0 
for i in xrange(7,7+32):
  sy += u[i]
print sy
sy=0 
for i in xrange(40,40+32):
  sy += u[i]
print sy
