#
# alternate soln
#

from time import time

st = time()

Limit=1000000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.

#print factors

count=0

for i in xrange(2,Limit):
    print "I!!!",i
    if factors[i]==0:

        # i is prime
        count =0
        val =i

        while val < Limit:
            factors[val] += 1
            val+=i
            #print factors[val-i], val-i,i 
       
        if i==2:
          print factors
          exit()
    elif factors[i] == 4:
        #exit()
        count +=1
        #print "!",factors[i], count 

        if count == 4:
            print i-3 # First number
            print factors
            break
    else:

        count = 0

print "Process time is", time() - st

