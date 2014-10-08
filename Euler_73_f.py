a=1./3.
b=1./2.
bestNum = 0bestDenom = 1
N=12001for currDenom in xrange( 2 , N):
  currNum = (a*currDenom - 1) / b  if bestNum*currDenom < currNum*bestDenom:     bestNum = currNum     bestDenom = currDenomprint bestNum, bestDenom