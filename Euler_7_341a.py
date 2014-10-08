#
#  Euler Problem 341
#
#
#
#

from bisect import bisect
import timeit

#Finds the Nth golumb number from the
#sequence x(n) using a binary search

def findNthGolumb(n, x, upto) :
    #print "@:",n,x
    return bisect(x, n, 1, upto) - 1

#Creates the sequence x(n) where x(n) is k
#if the first appearance of n in the golumb
#sequence is at position k (1-based)

def golumb(n) :
    x = [0]*700000
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

print
#summ = 0
seq = []
ctr=0
temp=1
for i in xrange(1,1400):
  x = golumb(i)
  if temp==x:
     ctr+=1
  else:
     seq.append((temp,ctr))
     ctr=1;temp=x
  print i,x

#print "answer is ", summ
print
for z in seq:
  print z
 

#print timeit.Timer("print golumb(2000000000)", 'from __main__ import golumb').timeit(number=1)
