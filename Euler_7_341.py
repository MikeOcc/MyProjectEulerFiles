#
#  Euler Problem 341
#
#
#
#
from mpmath import *
from bisect import bisect
import timeit

#Finds the Nth golumb number from the
#sequence x(n) using a binary search

def findNthGolumb(n, x, upto) :
    print n, 1, upto
    return bisect(x, n, 1, upto) - 1

#Creates the sequence x(n) where x(n) is k
#if the first appearance of n in the golumb
#sequence is at position k (1-based)




from mpmath import *
 

def gol2(k):
	phi = (1+sqrt(5))/2
	g = []
	#for n in xrange(k):
	n= 0
	while n<k+1:
		g.append(phi**(2-phi)*n**(phi-1))
		g[n] = round(g[n])
		n+=1
	return g


def golumb(n) :
    x = [0]*100000000
    x[1], x[2] = 1, 2
    cur, start = 2, 3

    while x[start - 1] < n :
        times = findNthGolumb(cur, x, start)
        while times :
            x[start] = x[start - 1] + cur
            start += 1
            times -= 1
        cur += 1

    return findNthGolumb(n, x, start)

summ = gol2(1000000**3)    #0
#for i in xrange(1,1000000):
#  summ+=golumb(i*i*i)
#
print "answer is ", summ

 

#print timeit.Timer("print golumb(2000000000)", 'from __main__ import golumb').timeit(number=1)
