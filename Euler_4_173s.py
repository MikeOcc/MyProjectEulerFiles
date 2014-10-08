#
#
#  Euler Problem 4 173
#
#
# number of tiles n for side l
#  n = 2*L + 2*(L-2) = 4*l - 4
#
# formula for laminae (OL,IL):
#  for even OL:
#  OL**2 - IL**2
#
#
from time import time
st = time()
import math

 
def problem173(number_of_tiles):
    l = [(number_of_tiles+n**2)/(2*n) for n in range(2,int(math.sqrt(number_of_tiles)),2)]
    return sum(map(lambda x, y: len(range(x,y+1)), range(3,l[-1]+1,2), l))
 
print 'Total', counter

print "Process time is", time()-st