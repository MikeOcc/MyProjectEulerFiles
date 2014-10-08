from array import array
global array 

def p311(N = 10**10):
    N /= 2
    count = 0
    S = 10**8
    for i in xrange(N/S + 1):
        L = i*S
        U = (i+1)*S
        counters = array('B', [0])*(S/2)
        for x in xrange(int(N ** 0.5) + 1):
            if x*x < L:
                y_first = max((int((L - x*x)**0.5)&~1) + (x&1) - 4, x + 2)
            else:
                y_first = x+2
            for y in xrange(y_first, int((N - x*x) ** 0.5) + 1, 2):
                z = x*x + y*y
                if (z >= U):
                    break
                if (L <= z):
                    counters[(z - L)/2] += 1
        for c in counters:
            count += c*(c-1)*(c-2)/6
    return count


print p311(10000)