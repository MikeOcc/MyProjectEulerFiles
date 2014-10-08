#
#
# Euler 154


def nf(n,d):
  ctr = 1
  tot = 0
  while True:
    summ = n/(d**ctr)
    if summ==0:break
    ctr +=1
    tot+=summ
  return tot

l2=[]
for i in xrange(1,200001):
  l2.append(nf(i,2))
  #print i, nf(i,2)
  
l5=[]
for i in xrange(1,200001):
  l5.append(nf(i,5))
  #print i, nf(i,2)
  
print l2[-1],len(l2)
print l5[-1],len(l5)
ctr=0

x = 0
while True:
    # case 1: x = y < z
    y = x
    z = 200000 - x - y
    try:
      if 199982 >= (l2[x]+l2[y]+l2[z]) and 49986 >= (l5[x]+l5[y]+l5[z]):
        result += 3
    except:
      print x,y,z,x+y+z
		
    # case 2: x < y = z
    if x % 2 == 0:
        y = (200000 - x)/2
        z = y
        if 199982 >= (l2[x]+l2[y]+l2[z]) and 49986 >= (l5[x]+l5[y]+l5[z]):
            result += 3
			
    # case 3: x < y < z
    a = 1
    while 2*a < (200000 - 3*x):
        y = x + a
        z = 200000 - x - y
        if 199982 >= (l2[x]+l2[y]+l2[z]) and 49986 >= (l5[x]+l5[y]+l5[z]):
            result += 6
        a += 1
    x += 1
    if x>666666:break
	
print x