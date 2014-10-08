#
#
#  Euler problem 338
#
#
from Functions import IsPrime
from math import sqrt

def F0(w,h):
  if IsPrime(w) and IsPrime(h):return 0
  if w + h ==2: return 0
  if w==1 or h==1:return 1
  sum2 = 0
  if w%(h-1) == 0: sum2+=1
  if h>1 and h%2==0: sum2+=1
  if w>1 and w%2==0 and w!=h: sum2+=1
  if sqrt(w)==h*2:sum2+=1
  return sum2

def F(w,h):
  if IsPrime(w) and IsPrime(h):return 0
  if w + h ==2: return 0
  if w==1 or h==1:return 1
  sum2 = 0
  if w%(h-1) == 0: sum2+=1
  if h>1 and h%2==0: sum2+=1
  if w>1 and w%2==0 and w!=h: sum2+=1
  if sqrt(w)==h*2:sum2+=1
  return sum2

ctr = 0
sum1 = 0
max = 10**5
for i in range(1,max+1):
  for j in range(1,max+1):

     if i>=j:
       print "Initial squares",i,"x",j
       ctr+=1
       temp = F(i,j)
       print i,'x',j,'=',temp
       sum1+=temp
   
     
print ctr,sum1

