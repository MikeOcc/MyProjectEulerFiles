#
#
#  test of zeta function
#
#


s = 0

n = 900000
z = 0
for i in xrange(1,n+1):
  z += 1./i**s
  print i, 1./i**s, z

print
print "z = ", z