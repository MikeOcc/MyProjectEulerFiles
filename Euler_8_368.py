#
#
#  Euler 368
#
#


n = 0


for i in xrange(1,1000000000):
  if '9' not in str(i):
    #print i
    n += 1./i

print n




