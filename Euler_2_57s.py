from itertools import starmap
from math import log10
 
def expansions( n):    
    num, den = 2, 1                  # r = 2
    for _ in xrange(n):
        yield num + den, num         # 1 + 1/r
        num, den = 2*num + den, num  # r = 2 + 1/r
def ndig( n):
    #print n,int(log10(n)+1)
    return int(log10(n)+1)
# main:
print sum( starmap( lambda num, den: ndig(num) > ndig(den),expansions( 1000)))


#for x in starmap( lambda num, den: ndig(num) > ndig(den),expansions( 1000)):
#  print x

#for x in expansions(1000):
#  print x