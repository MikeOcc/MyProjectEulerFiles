#
# Euler 31
#
#
from itertools import *
from string import rstrip

coins=[200, 100, 50, 20, 10, 5,2,1]
 
def findposs( money,  maxcoin):
    sum = 0;
    
    if (maxcoin == 7): return 1
    
    for i in xrange(0,maxcoin):
        if (money-coins[i] == 0): sum+=1
        if (money-coins[i] > 0): sum+=findposs(money-coins[i], i)
    
    return sum

 
if __name__=='__main__':
    for jj in xrange(8):
      print findposs(200,jj)



#print "total number of combinations is " , summ


