#
# Euler 65 study 1
#

factors = [2]
for a in xrange(1,34):
    factors.append(1)
    factors.append(a*2)
    factors.append(1)

print factors

res = (1,0)
for a in xrange(100):
    last = factors.pop()
    res = (res[1]+(last*res[0]),res[0])
    print last, res, float(res[0])/float(res[1])
print sum([int(ch) for ch in str(res[0])])