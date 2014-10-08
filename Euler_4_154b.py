#
#
# Euler 154
from time import time
st=time()

def nf(n,d):
  ctr = 1
  tot = 0
  while True:
    summ = n/(d**ctr)
    if summ==0:break
    ctr +=1
    tot+=summ
  return tot

l2={}
for i in xrange(0,200001):
  l2[i]=nf(i,2)
  #print i, nf(i,2)
  
l5={}
for i in xrange(0,200001):
  l5[i]=nf(i,5)
  #print i, nf(i,2)
  
print l2[200000],len(l2)
print l5[-1],len(l5)
ctr=0

x = 0
result=0
while x<=66666:
    # case 1: x = y < z
  y = x	
  #z = 200000 - x - y
  z = 200000 - (x<<1)
  
  #if (l2[x]+l2[y]+l2[z]) <=199982  and (l5[x]+l5[y]+l5[z]) <= 49986 :
  try:
    if (l2[x]<<1+l2[z]) <=199982  and (l5[x]<<1+l5[z]) <= 49986 :
      result += 3
  except:
    print x,y,z,x+y+z
    print time()-st
    exit()
		
    # case 2: x < y = z
  if x % 2 == 0:
      y = (200000 - x)/2
      #z = y
      #if (l2[x]+l2[y]+l2[z]) <=199982  and (l5[x]+l5[y]+l5[z]) <= 49986:
      if (l2[x]+(l2[y]<<1)) <=199982  and (l5[x]+(l5[y]<<1)) <= 49986:
        result += 3
			
    # case 3: x < y < z
  a = 1
  while (2*a) < (200000 - 3*x):
    y = x + a
    z = 200000 - x - y
    if (l2[x]+l2[y]+l2[z]) <= 199982 and (l5[x]+l5[y]+l5[z]) <= 49986:
      result += 6
    a += 1
  x += 1
  # if x>66666:
    # print "!",x  
    # break
	
print result
print time()-st