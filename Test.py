print sum(4*n**2-6*n+6 for n in range(3, 1002, 2))+1


z=500
sum1 = 0
for i in xrange(500):
  x= sum(32*n+52 for n in xrange(i))+24
  sum1 += x

print sum1 + 1


#print sum(sum(32*n+52 for n in xrange(i))+24) for i in xrange(500))

sum(sum((32*n + 52) for n in xrange(i))+24 for i in xrange(500)) +1
