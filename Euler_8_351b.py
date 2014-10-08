#
#
#  Euler Problem 351
#
#

from time import time
from itertools import imap

class Totient:
    def __init__(self, n):
        self.totients = [1]*n 
        for i in xrange(2, n):
            if self.totients[i] == 1:
                for j in xrange(i, n, i):
                    self.totients[j] *= i - 1
                    k = j / i
                    while k % i == 0:
                        self.totients[j] *= i
                        k /= i
    def __call__(self, i):
        return self.totients[i]


#########################################
#
#  I SO wanted to solve this problem by just doing *ray casting* by drawing rays from the last row
#  of trees to the center tree and counting the intersection of grid spots.  This would allow the
#  splitting of the Hexagon into 12 pieces, I still think this would be fastest way, I'm going to post
#  it when I get it to work.
#
st = time()        #  start time

N = 10000000 #0      #  number of rows

# The easiest part of the problem, I knew this formula as a kid even before I heard about Rene Descartes
NumSector = int((N+1)*(N/2))   # calculate number of trees in 1/6th of the orchard (minus center).
print
print "Initiate Totient Class for N =",N
totient = Totient(N+1)  # Set up 

for phi_nh in imap(totient,range(1,N+1)):
  NumSector -= phi_nh

print "Number of hidden trees in Hexagon Orchard of", N, "rows is", NumSector * 6

print "process time:",time()-st
print


