from itertools import izip_longest, combinations, product
from functools import reduce
 
def filt_func(c1, c2):
    print "c1,c2",c1,c2,c1[0] > c2[0]
    if c1[0] > c2[0]:
        return False
    print "c1,c2,izip",sorted(c1),sorted(c2),izip_longest(sorted(c1), sorted(c2))
    for a in izip_longest(sorted(c1), sorted(c2)): print a
    R = reduce(lambda x, y: x and (y[0] < y[1]), izip_longest(sorted(c1), sorted(c2)))  #, True)
    print "R", R
    return not R
 
def generator(n, k):
    print "*******",n,k
    s1 = combinations(range(n), k // 2)
    comb_total = []
    for comb1 in s1:
        print comb1
        left_nums = set(range(n)) - set(comb1)
        s2 = (c for c in combinations(left_nums, k // 2) if filt_func(comb1, c))
        #print "prod s2",product([comb1], s2)
        comb_total.extend(product([comb1], s2))
        print "L",len(comb_total)
    return comb_total
 
if __name__ == '__main__':
#    result = sum(len(generator(12, i)) for i in range(4, 13, 1))
    result = 0
    for i in xrange(4,13,2):
      res1 = len(generator(12,i))
      print i,res1
      result += res1
    print("The result is:", result)