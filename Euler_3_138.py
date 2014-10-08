from time import time
st = time()
tot=0
ctr=0
for i in xrange(2,1000000000):

    b= 2*i
    h1 = b + 1
    h2 = b - 1
    
    L1 = pow(h1**2 + i**2,.5)
    if int(L1)==L1:

      tot +=L1	
      ctr+=1
      print "L1 ",ctr, h1, b, int(L1), int(tot)
      if ctr>=25 :break
	  
    L2 = pow(h2**2 + i**2,.5)
    if int(L2)==L2:
	
      ctr+=1
      tot +=L2	
      print "L2 ",ctr, h2, b, int(L2), int(tot)
      if ctr>=25 :break


print int(tot)
print time() - st