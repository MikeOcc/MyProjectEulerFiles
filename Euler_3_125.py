#
#
#  Euler Problem 125
#

#[]

from time import time
st=time()

sqs = []

for i in xrange(10001):
  sqs.append(i*i)

tot=[]
for i in xrange(1,4001):
  for j in xrange(1,4001):
    if j>i:
      sum1 = 0
      for k in xrange(i,j+1):
        sum1+=sqs[k]
      if sum1>=10**8:break
      if str(sum1)[::-1]==str(sum1):
        #print i,j,sum1   
        tot.append(sum1)

tot = sum(list(set(tot)))

print
print "Total sum of cons. squares is",tot
print "Process time is",time()-st
