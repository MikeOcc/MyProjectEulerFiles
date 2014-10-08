from Functions import gcd

#-------------------------------
# Real (rational) divisors
#-------------------------------
def sum_divisors_rational(n):
    '''Returns the sum of rational divisors of all numbers between 1 and n, inclusive. A fast
    implementation that decomposes the requested sum, sum_{a=1}^n a*floor(n/a) into local
    and smooth parts, because floor(n/.) becomes increasingly smoother for larger values of
    the argument. Runtime complexity: O(sqrt(n)).'''
    # Optimal split to balance local and smoth work
    q = int(n ** 0.5)
    # Local part
    s_local = sum(a * (n / a) for a in xrange(1L, n / q + 1))
    # Smooth part
    s_smooth = 0L
    for k in xrange(1L, q):
        r1, r2 = n / (k + 1), n / k
        # print '\t', r1, r2
        s_smooth += k * (r1 + r2 + 1) * (r2 - r1)
    s_smooth /= 2
    # print n, K, s_local, s_smooth
    
    return s_local + s_smooth

#-------------------------------
# Complex divisors
#-------------------------------
def g_sum(n, p):
    '''Return the inner-most sum of complex Gaussian divisors with positive real part of all k, k=1..n.
    Using a summation formula. Runtime complexity: O(n^(1/2)).'''
    # Optimal split to balance local and smoth work
    q, s = int((n / p) ** 0.5), 0L
    # Local part
    for g in xrange(1L, n / (p * q) + 1):
        K = n / (p * g)
        s += (K * g + K * (K + 1) / 2)
    # Smooth part
    for k in xrange(1L, q):
        r1, r2 = n / (p * (k + 1)), n / (p * k)
        G = (r1 + r2 + 1) * (r2 - r1) / 2
        s += (k * G + k * (k + 1) * (r2 - r1) / 2)
    return s

'''Return the sum of complex Gaussian divisors with positive real part of all k, k=1..n.
Using a summation formula. Runtime complexity: O(n).'''
sum_divisors_complex = lambda n: \
sum(a * sum(g_sum(n, a * a + b * b) for b in xrange(1, int((n - a * a) ** 0.5) + 1) if gcd(a, b) == 1)
    for a in xrange(1, int((n - 1) ** 0.5) + 1))

sum_divisors_gaussian = lambda n: sum_divisors_rational(n) + sum_divisors_complex(n)
 
if __name__ == "__main__":
    print sum_divisors_gaussian(10L ** 8)