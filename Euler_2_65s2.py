#
# Euler 65 study 2
#
# aghoneim  

a = [2]
i = 0
k = 1
while i < 99:
    a.append(1)
    a.append(2 * k)
    a.append(1)
    k += 1
    i += 3

print a
print

# 2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536
# [2, 1, 2, 1, 1, 4, 1, 1, 6, 1]
for i in xrange(2, 101):
    n = 1
    d = a[i-1]
    j = i
    while j > 2:
        n = a[j-2] * d + n
        n,d = d,n
        j -= 1
        print "j,n,d",j,n,d
    n = a[0] * d + n
    print i, ' - ', n, d

print sum([int(x) for x in str(n)])


