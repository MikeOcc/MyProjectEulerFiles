def find_all(n, x, a, add, tot):
    res = 0
    for k in xrange(1, n + 1):
        if a[-1] != 0: res += tot
        cursum = sum(a[i] * a[k-i] for i in xrange(1, k)) + add
        for ak in xrange(x):
            val = 2 * a[0] * ak + cursum
            if val % x == ak:
                print ak
                a.append(ak)
                add = val // x
                tot += ak
    return res

def find(n, x):
    res = 0
    for a0 in xrange(x):
        val = a0 * a0
        if val % x == a0:
           z = find_all(n, x, [a0], val // x, a0)
           #print a0,z
           res += z
    print res

find(10000, 14)