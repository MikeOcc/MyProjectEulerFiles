#An irrational decimal fraction is created by concatenating the positive #integers:
#
#  0.123456789101112131415161718192021
#
#It can be seen that 1 is the 12th digit of the fractional part is 1.
#
#If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 x d10x  d100 x  d1000 x d10000 x d100000 x  d1000000

from time import time

starttime = time()


dnum = ""
ctr=0

while len(dnum)<1000001:
   ctr+=1
   dnum += str(ctr) 

#print drum
#print 
#print "ctr = ",ctr

d1 = int(dnum[0])
d10 = int(dnum[10-1])
d100 = int(dnum[100-1])
d1000 = int(dnum[1000-1])
d10000 = int(dnum[10000-1])
d100000 = int(dnum[100000-1])
d1000000 = int(dnum[1000000-1])

totmult = d1*d10*d100*d1000*d10000*d100000*d1000000

#print d1,d10,d100,d1000,d10000,d100000,d1000000
print "multiplicative total of d(n) for n in range(1,1000000,10**n-1) is",totmult

print "Process time is ", time()-starttime

#print dnum

