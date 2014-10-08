#
#
#  Euler 354
#
#
from time import time
from decimal import Decimal
st = time()
a = 1.5
b = (3**.5)/2

# 
#     x         y
#_________________________
#      0         0
#    1.5 (a)     3b        
#    3.0 (2a)    6b
#    4.5 (3a)    9b
#

#_________________________
print
ctr = 0
Max = 6
cellcnt = {}
slopes=[]
h2,h=0,0

for i in xrange(1,Max+1):  #10**8,int(1.5*10**8)):
  if i%2 == 1:
     y0 = 1
  else:
     y0 = 0
  for j in xrange(y0,3*i+1,2):
    if j >= 3*i: continue
    x = a * i; y = b * j; h2 = (x**2 + y**2);h=h2**.5

    if 1:
    #if h == 147:
     #print i,j, ":", x, Decimal(y),":",h2,h
     print i,j, ":", x, y,":",h2,h,":",y/x
     slopes.append(y/x)
     ctr +=1
     #print "!",h2,h
     if cellcnt.has_key(h):
       cellcnt[h]+=1
     else:
       cellcnt[h]=1

print
print
print "sum = ", ctr*6
print "process time is", time()-st
#print  cellcnt
print
kys = cellcnt.keys()
for a in kys:
  if cellcnt[a]>1:
    print Decimal(a), cellcnt[a]
print
print
slopeset=sorted(list(set(slopes)))
for a,b in enumerate(slopeset):
  print a,b,slopes.count(b)
