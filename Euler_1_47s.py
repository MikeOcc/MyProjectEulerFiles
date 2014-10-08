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
    
    if factors[i]==0:

        # i is prime
        count =0
        val =i

        while val < Limit:
            factors[val] += 1
            val+=i
            print factors[val-i], val-i,i 

    elif factors[i] == 4:

        count +=1
        print "!",factors[i], count 

        if count == 4:
            print i-3 # First number
            break
    else:

        count = 0

print "Process time is", time() - st

