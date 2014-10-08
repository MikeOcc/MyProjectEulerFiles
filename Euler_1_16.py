#
#  Project Euler #26  Sum digits in 2**1000
#
#


#z= reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, str(2**1000).split()))])

print reduce(lambda x, y: x + y, [int(i) for i in str(reduce(lambda x, y: x * y, str(2**1000).split()))])

print "or"

print reduce(lambda x, y: x + y, [int(i) for i in str(2**1000)])

