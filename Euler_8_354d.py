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

MX = 21**.5  #222222222
ER = int(MX*2/3)   #74074074*2

for x in xrange(ER,0,-1):
   y = (MX**2 - (x*1.5)**2)**.5
   #if round(y/3**.5,8) == int(y/3**.5):
   if round(y/b,8) == int(y/b):
     print x*1.5, 2*y/3**.5


exit()

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

for i in xrange(1,10000):  #10**8,int(1.5*10**8)):
  y0 = i%2 
  for j in xrange(y0,3*i,2):
    if j >= 3*i: continue
    x = a * i; y = b * j; h2 = round((x**2 + y**2),6); h=h2**.5

    if 1:
    #if h2%59241 !=0:  #17464629.0:
     #print i,j, ":", x, Decimal(y),":",h2,h
     #print i,j, ":", x, y,":",h2,h,":",y/x
     slopes.append(y/x)
     ctr +=1
     #print "!",h2,h
     if cellcnt.has_key(h2):
       cellcnt[h2]+=1
     else:
       cellcnt[h2]=1
     #break

print
print
print "sum = ", ctr*6

#print  cellcnt
print
nlist=[]
#cellcnt=sorted(cellcnt)
kys = cellcnt.keys()
for a in kys:
  if cellcnt[a]>=0:
    #print a, cellcnt[a]
    nlist.append((a,cellcnt[a]))
print
print
'''
slopeset=sorted(list(set(slopes)))
for a,b in enumerate(slopeset):
  print a,b,slopes.count(b)
'''

for a,b in enumerate( sorted(nlist)):
  print a,b[0],":",b[1]*6
#print "Sum is", len(nlist)
print "process time is", time()-st