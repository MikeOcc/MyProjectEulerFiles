#
#
#  Euler Problem 86
#
#  []


def sp(a,b,c):

  r = []
  r.append((a**2 + (b+c)**2)**.5)
  r.append((b**2 + (a+c)**2)**.5)
  r.append((c**2 + (a+b)**2)**.5)

  mindy = min(r)
  if int(mindy)==mindy:
    return 1

  return -1

###########
from time import time
st = time()
M=2000

print sp(3,5,6)
ctr = 0
for i in xrange(1,M+1): 
  print i,")",ctr
  for j in xrange(1,M+1):  
   for k in xrange(1,M+1):
     if i>=j>=k:
       if sp(i,j,k)>0:
         #print i,j,k
         ctr +=1
         if ctr>1000000:
           print ctr, i, j, k
           if i==j==k:
             break
           
print "total is", ctr, ":", i,j,k
print "Process time is", time()-st
