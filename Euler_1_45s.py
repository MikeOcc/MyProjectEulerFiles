from sets import *
from time import *
 
def T(n):
    return (n*(n+1))/2
 
def P(n):
    return (n*(3*n-1))/2
 
def H(n):
    return n*(2*n-1)
 
start = clock()
Ts = Set([T(x) for x in range(286,100000)])
Ps = Set([P(x) for x in range(166,100000)])
Hs = Set([H(x) for x in range(144,100000)])
 
print Ts.intersection(Ps.intersection(Hs))
print "Time taken = %.2f" % (clock()-start)