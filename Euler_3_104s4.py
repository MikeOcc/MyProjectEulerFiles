from time import time
st=time()
a, b, c, d, i, S = 1, 1, 1, 1, 2, set('123456789')
while set(str(b)) != S or set(str(d)[:9]) != S:
    a, b, c, d, i = b, (a + b) % 10**10, d, c + d, i + 1
    if d > 10**15: c, d = c / 10, d / 10
print i
print "process time is",time()-st
