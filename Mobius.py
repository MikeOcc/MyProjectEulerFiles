#
#  Totient and Mobius functions
#
#

def totient(n):
    if n == 1: return 1
    return sum(d * mobius(n / d) for d in range(1, n+1) if n % d == 0)


def mobius(n):
    result, i = 1, 2
    while n >= i:
        if n % i == 0:
            n = n / i
            if n % i == 0:
                print 0
                return 0
            result = -result
        i = i + 1
    print result
    return result

####################

for i in xrange(2,20000):
  print mobius(i)

