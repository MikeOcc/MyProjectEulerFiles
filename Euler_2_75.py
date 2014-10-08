#
#
# Euler Problem 75
#
#
from Functions import gcd
from time import time
from math import sqrt
st=time()
lim = 1500000
lim2 = int(sqrt(lim))
ar=[0]*(lim+1)


for m in xrange(1,lim2,2):
  for n in xrange(2,lim2-m,2):
    if gcd(m,n) == 1:
      #print "m,n",m,n
      a=abs(m**2-n**2)
      b=2*m*n
      c=m**2+n**2
      l=a+b+c
      #k=1
      for s in range(l, lim, l):
        ar[s]+=1

      ''' 
      while l<=lim:
        
        #l *= k
        #if l>lim:break
        ar[l]+=1
        l+=l
        #print a*k,b*k,c*k,":",l
      '''

print
print

#for m in xrange(1,300):
#  print m,ar[m]
'''
summ=0
for l in ar:
  if l==1:summ+=1
'''

print
print "answer is" ,ar.count(1)
print "process time is",time()-st





