#
#
#  Euler 354
#
#
from time import time
from decimal import Decimal
from Functions import RetFact
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
Max = 1000
cellcnt = {}
slopes=[]
h2,h=0,0

for i in xrange(1,240):
  y0 = i%2 
  for j in xrange(y0,3*i,2):
    if j >= 3*i: continue
    x = a * i; y = b * j; h2 = round(x**2 + y**2,8);h=h2**.5

    if 1:
    #if h2%59241 !=0:  #17464629.0:
     #print i,j, ":", x, Decimal(y),":",h2,h
     #print i,j, ":", x, y,":",h2,h,":",y/x
     #print i,j, ":", x, y,":",h,h2
     slopes.append(y/x)
     ctr +=1
     #print "!",h2,h
     if cellcnt.has_key(h2):
       cellcnt[h2]+=1
     else:
       cellcnt[h2]=1
     #break

print
print "sum = ", ctr*6

#print  cellcnt
#print
nlist=[]
#cellcnt=sorted(cellcnt)
kys = cellcnt.keys()
for a in kys:
  if cellcnt[a]>0:
    print a, cellcnt[a]
    nlist.append((a,cellcnt[a]))
print
print
'''
slopeset=sorted(list(set(slopes)))
for a,b in enumerate(slopeset):
  print a,b,slopes.count(b)
'''
for a in sorted(nlist):
  print a,":",a[0]**.5,":",int(a[1])*6

print "process time is", time()-st
