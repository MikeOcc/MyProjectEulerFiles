#
#  Euler Problem 85
#
#
from time import time
st=time()

MaxK = 12000
Lim = 14000 

# Initialize a list to store N values for each k, and an array to store offsets
k = [0 for  row in range(MaxK + 1)]
n = [[] for row in range(Lim + 1)]

# Dynamically generate N using 3 loops and k will follow 
for i in range( 2, Lim / 2 +1) :
        # since N(k) does not necessary increase, start with negative offset
        n[i] += [(-i + 1)];
        #print n[i]
        # iterate over offsets		
        for num in n[i] :
            curN = 2*i   # init current N to 2 * i
            N = num - 1   #  set new N to offset - 1
            #print num, curN, N
            # skim from 2 to i
            for xyzygy in range( 2, i + 1): 
                n[curN]+=[N]   # add new offset to slot curN (2 * i)
                #print num, curN, N,curN + N
                nextK = curN + N  # Propose next K by adding 2*i to offset
                # Check to see if new value of k:N is less than current val or if slot hasn't been filled
                if (nextK <= MaxK and (curN < k[nextK] or k[nextK] == 0)): 
				    k[nextK] = curN
                N-= 1        # decrement N for next offset addition
                curN += i    # add i for next loop
                if (curN > Lim): break   # Cut down on iterations, break if N > than preset limit
        #print k

summ = sum(set(k))
        
print "Sum of k is:",summ
print "Time elapsed is: ",time()-st 
