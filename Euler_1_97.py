#
#  calculate last ten digs of 28433 * 2**7830457 +1
#
# this is a huge number, but only need last tend digs
# therefore use mod 10**12 to pare down digs

x = 7830457
y = 28433 * ((2**x) % 1000000000000)
y = y + 1
z = str(y)[-10:]

print "Results is ", z

#Results is  8739992577