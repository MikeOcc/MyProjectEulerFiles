def pandigital_fib():
    bottom_i = bottom_j = 1
    top_i = top_j = 1
 
    count = 2
    while 1:
        s = str(bottom_j)[-9:]
        # Looks ugly, but fastest way I found to do the test
        if ("1" in s and "2" in s and "3" in s and
            "4" in s and "5" in s and "6" in s and
            "7" in s and "8" in s and "9" in s):
            t = str(top_j)[:9]
            if ("1" in t and "2" in t and "3" in t and
                "4" in t and "5" in t and "6" in t and
                "7" in t and "8" in t and "9" in t):
                return count
 
        bottom_i, bottom_j = bottom_j, bottom_i+bottom_j
        bottom_j = bottom_j % 1000000000
 
        top_i, top_j = top_j, top_i+top_j
        while top_j > 1000000000000000000:
            top_i //= 10
            top_j //= 10
 
        #print count, top_j
        count += 1
from time import time
st = time()
print "Found:", pandigital_fib()
print "Process time is",time()-st
