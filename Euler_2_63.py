#
# Euler 63
#

ctr = 0
for i in xrange(0,210):
  for j in xrange(0,100):

    z = i**j

    zlen = len(str(z))

    if zlen == j:
     print ctr,")",i,j,z,zlen
     ctr+=1


print ctr

print
print sum(len(str(i**j))==j for i in xrange(1,100) for j in xrange(1,100))