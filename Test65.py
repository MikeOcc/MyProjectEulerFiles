#
# Euler 2 - 57
#
#  1 + 1/(2 + 1/(2 + 1/(2 + 1/2)))
#

d1 = (2+ .5)

print d1

for i in xrange(1001):

   d1 = 2 + 1/d1
   print d1,

print d1
   