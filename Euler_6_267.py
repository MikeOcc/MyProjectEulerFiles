#
#
# Euler 267
#

from random import random

# 0.453325564805

f = 0.453325564805
fp = 0
while 1:
  stcap = 1

  bet = 0
  for i in xrange(1,1001):
    if bet == 0:
      bet = 1
    else:
      bet = 0

    flip = ""
    if bet>.5:
      win = 2* f * stcap
      flip = "H"
      stcap = stcap + win
    else:
      loss = f * stcap
      flip = "T"
      stcap = stcap - loss
  print f,stcap
  if stcap == 10**9:
    break
  elif stcap < 10**9:
    f = .9999999999999 * f
  else:
    f = 1.0000000000001 * f

#print "Final money is", stcap
print "f is ", f





