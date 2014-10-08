
#
#  Problem 157
#
from time import time

def diophantine(a,b,P,n):

 return 10**n*( b + a)==a*b*P

#for i in xrange(1,10):

st = time()
n= 1
a,b =0,0

ctr = 0
for p in range(1,21):
  for a in range(1,120):
    for b in range(1,120): 
      if a<=b and diophantine(a,b,p,n)==True:
        print "a,b,p,n",a,b,p,10**n
        ctr+=1

print "Total is", ctr
print "Process time is", time() - st
