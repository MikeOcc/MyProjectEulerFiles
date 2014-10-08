#
#
#  Euler 135
#

N = 1000000
L = [0]*N 
summ = 0
    
for i in xrange(1,N+1):
  for j in xrange(int(i/3),N/2 + 1):

     #'NN = (I + J + J) ^ 2 - (I + J) ^ 2 - I * I
     # 'Reorder
     n = (3 * j**2) + (2 * j*i) - (i**2)
     if n > 0:
        if n < N:
           L[n] = L[n] + 1
        else:
           break


for i in xrange(1,999999):
   if L[i] == 10: summ +=1
 
print "Answer is",summ





