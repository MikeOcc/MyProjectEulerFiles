#
#
#  Euler Problem 286
#
#

from decimal import Decimal

def probThat20WereMade( q ):

  p = [[0 for col in range(52)] for row in range(52) ] 

  p[51][51] = 1  # [x][y] = given x shots (1,2,..,x), probability that y were made
  #p[0][0] = 1
  for x in xrange(51,0,-1 ):
    for numMade in xrange(x,0,-1 ):

      if numMade > 0:
         p[x][numMade] = p[x-1][numMade-1]*(1.-x/q)
      else:
         p[x][numMade] = p[x-1][numMade-1]*(1.-x/q) + p[x-1][numMade]*(x/q)

  #print p
  return p[50][20]



lo = 50.
hi = 53.
while ( hi - lo > 1e-13 ):

  mid = (lo+hi)/2.
  prob = probThat20WereMade( mid )
  print prob,mid
  if ( prob > .02 ):
    lo = mid
  else:
    hi = mid


print Decimal(lo) 








