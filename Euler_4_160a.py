#
#
# Euler 160
#
#

from math import factorial

d={}
f=factorial(9)
for x in xrange(10,300001):
  f*=x
  while True:
    fp = f
    res = f%10
    if res!=0:
      f=fp
      break
    else:
      f/=10
      #print f
  f%=1000000000000000000000000000000
  if f in d:
    d[f]+=1
  else:
    d[f]=1
  #print x,f%100000
  #if f==25696:
   # print x, f
  #if (x-1)%150000==0:
  #if x>1000000000-4:
    #print x, f
  #if (x)%300==0:
  #if (x>=300 and x<400)  or (x>=600 and x<700):
    #print x, f
  if (x-0)%1000==0:
  #if f%100000==16576:
    print x, f%100000
	# for i in d:
    # if d[i] > 4:
      # print i,d[i]
	
  
  