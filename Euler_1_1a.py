
from math import *

TOTAL = 0

for NUM in range( 1 , 1000): 
  if NUM%3 == 0 or NUM % 5 == 0 :
     TOTAL += NUM 

print TOTAL


#______________________________________

#print sum(n*(n%3) for n in range(1,1000))


#  sum3(n)
sum1 = 0
for i in range(1, int(500/3)  ):
     sum1+=3*i

sum2 = 0
for i in range(1, int(500/5)  ):
     sum2+=5*i

sum3 = 0
for i in range(1, int(500/15)  ):
     sum3+=3*i

print sum1 + sum2 - sum3