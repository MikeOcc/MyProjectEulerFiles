import string
from math import *


a1 = 1
a2 = 4
a3 = 2
a4 = 3
temp = 0
sum = 0

numsum = 0

while numsum < 55:
   sum = a1 + a2 + a3 + a4
   a1 = a2
   a2 = a3
   a3 = a4
   a4 = sum
   numsum = numsum + 1

print "The final Sum is ", sum

#stirlings appx

x = (sqrt(pi*2.0*10) * pow(10/e,10))

print "X = ", x
