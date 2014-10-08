#
#  Euler #53
#
#
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
#
# How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater # than one-million?
#


from math import factorial
from time import time

def nCr(sel,frm):
#
#  combinatorics nCr = n!/(r!(n-r)!)
#
  return factorial(frm)/factorial(sel)/factorial(frm - sel)

if __name__ == '__main__':

  st = time()
  ctr = 0

  for i in range(22,101):
    for j in range(1,100):
       if (i>=j) and nCr(j,i)> 1000000:
         ctr +=1

  print "Number of values of nCr > 10**6 is", ctr
  print "Process times is ", time() - st


