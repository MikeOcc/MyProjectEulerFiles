from math import sqrt,floor, ceil
from project_euler import import_problem

#sum_one_to, divides = import_problem(1, 'sum_one_to', 'divides')
#is_even = import_problem(2, 'is_even')
#factorize = import_problem(3, 'factorize')

#divides = import_problem(1, 'divides')

def divides(a, b):
    """
    divides(int, int) -> bool
    
    Return whether or not a evenly divides b.
    """
    return (b % a) == 0


def is_prime_factor(i, num):
    """
    is_prime_factor(int, int) -> bool
    
    Return whether or not a number i is a prime factor of num. This method
    uses a sieve to figure out if a number is a prime factor. Note: this does
    not use the sieve of eratosthenes.
    """
    
    # a non-factor cannot possibly be a prime factor
    if not divides(i, num):
        return False

    done_checking = False
    
    # if a number might be a prime then investigate it, looking
    # at our starting set of primes. the set of the primes < 1000
    # will hopefully allow us to quickly dismiss this factor as
    # a prime
    for j in start_primes:
        if divides(j, i):
            done_checking = True
            break
    
    # we didn't find a small prime factor of our possible prime
    # factor, do a naive look for bigger prime factors. We know
    # that a composite number will have a prime number <= its
    # square root, so look in the range of checked prime numbers
    # up to the numbers square root for a factor of the number.
    # if no factor is found, then the number is prime, whence it
    # is the largest prime factor of num
    if not done_checking:
        j = max(start_primes)+2
        end = int(floor(sqrt(i)))
        
        while j <= end:
            
            # j isn't a factor of our starting number the we simply
            # don't care about it
            if not divides(j, num):
                j = j+2
                continue
            
            # i has a factor, i.e. i isn't a prime, and so cannot be
            # a prime factor of num
            if divides(j, i):
                done_checking = True
                break
            
            j = j+2
        
        # i is a prime factor of num
        if not done_checking:
            return True
    
    return False
            

def factorize(num):
    """
    factorize(int) -> list
    
    Return the sequence of prime factors for a given number. This method
    uses a sieve to figure out if a number is a prime factor. Note: this does
    not use the sieve of eratosthenes.
    """
    reduced_num = num
    
    # set of matched primes
    matched_primes = []
    
    # try to reduce the problem to a slightly smaller problem
    # by attempting to divide out a small set of known primes
    # i.e. use the prime decomposition theorem to try to make
    # our problem smaller
    for p in start_primes:
        t, exp = divide_factor(reduced_num, p)
        
        if t < reduced_num:
            matched_primes.append((p, exp))
            reduced_num = t
    
    # go over the range in which our highest prime will be in
    # and look for it, starting from the bottom. The numbers we
    # are going over might be too big for a range, and so we
    # will have to emulate the C-style for loop
    i = max(start_primes)+2
    while i <= reduced_num:
        
        # if we've found a prime factor then record it and reduce
        # the range of numbers to check
        if is_prime_factor(i, num):
            reduced_num, exp = divide_factor(reduced_num, i)
            matched_primes.append((i, exp))
            
        i = i+2
    
    # return the prime decomposition of our number
    return matched_primes


def sum_one_to(n):
    """
    choose2(int) -> int
    
    Return the number of subsets of length 2 that can be formed from a set
    of size n, or alternatively: sum the numbers from 1 to n, inclusive.
    """
    n = int(n)+1
    return int((n * (n-1)) / 2)

def is_even(n):
    """
    is_even(int) -> Bool
    
    Return whether or not a given number is even.
    """
    return (n & 1) == 0

def num_factors(n):
    """
    num_factors(int) -> int
    
    Return the number of factors (prime or not) for a given number.
    """
    factors = factorize(n)
    num = 1
    for x, exp in factors:
        num *= (exp+1)
    return num

def triangle_with_min_num_factors_slowest(min_num_factors):
    """
    triangle_with_min_num_factors_slower(int) -> (int, int, int)
    
    Find the first triangle number that has at least min_num_factors factors.
    This method uses the prime factorizer from a previous question to find
    all of the prime factors for each triangle number and by extension the
    number of factors for the number.
    """
    i = 1
    factor_count = 1
    num = 1
    
    while factor_count < min_num_factors:
        i = i+1
        num = sum_one_to(i)
        factor_count = num_factors(num)
    else:
        return i, num, factor_count

def triangle_with_min_num_factors_slower(min_num_factors):
    """
    triangle_with_min_num_factors_slower(int) -> (int, int, int)
    
    Find the first triangle number that has at least min_num_factors factors.
    This method works by noticing that half of the factors for a given number
    will be contributed by a number's square root.
    """
    i = 0
    num = 0
    num_factors = 0
    
    while num_factors < 500:
        i = i+1
        num += i
        num_factors = 0
        root = int(sqrt(num))

        for n in xrange(1, root+1):
            if divides(n, num):
                num_factors += 2

        if pow(root, 2) is num:
            num_factors -= 1
    else:
        return i, num, num_factors

def max_prime_factor(x):
    """
    max_prime_factor(int) -> int
    
    Return the maximum prime factor of a given number."""
    return max(factorize(x))

def triangle_with_min_num_factors_slow(min_num_factors):
    
    """
    triangle_with_min_num_factors_slower(int) -> (int, int, int)
    
    Find the first triangle number that has at least min_num_factors factors.
    This method is similar to the one that used prime factorization; however,
    this method uses memoization in order to avoid doing redundant factorization
    by noticing that the sum from 1 to n is n*(n+1) / 2.
    """
    i = 1
    factor_count = 0
    factor_table = {1:1}
    
    while factor_count < min_num_factors:
        i += 1
        j = i+1
        
        if i%2==0:   #is_even(i):
            factor_count = factor_table[i / 2]
        else:
            j /= 2
            factor_count = factor_table[i]
        
        factor_table[j] = num_factors(j)
        factor_count *= factor_table[j]
    else:
        return i, sum_one_to(i), factor_count

def divide_factor(num, factor):
    """
    factor_number(int, int) -> (int, int)
    
    Divide out factor from num.
    """
    i = 0
    
    while divides(factor, num):
        num = num / factor
        i = i+1
    
    return num, i
        
if __name__ == "__main__":
    
    start_primes = (
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,  
    59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 
    191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 
    257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 
    331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
    467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 
    563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 
    631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 
    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 
    797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 
    877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 
    967, 971, 977, 983, 991, 997
)

    num, triangle, num_factors = triangle_with_min_num_factors_slow(500)
    
    print """First triangle number with >= 500 factors is triangle(%d)=%d
    %d has %d factors.""" % (num, triangle, triangle, num_factors)












