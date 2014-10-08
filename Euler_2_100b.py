#
#
#  Euler Problem 100
#
# By finding the first arrangement to contain over 10^12 = 
# 1,000,000,000,000 discs in total, determine the number of blue
# discs that the box would contain.1513744654945

from math import sqrt
from time import time
def Problem_100():
 
   #Dim A As Double, B As Double
   #Dim TEMP    As Double
   #Dim Answer As Double, T As Single
   Answer = 0
   #T = Timer
 
   A = 1
   B = 1
 
   while Answer < sqrt(0.5) * 10 ** 12:
      TEMP = A
      A = A + 2 * B
      B = TEMP + B
      Answer = (B + 1) / 2   #'the number of Blue discs
 
 
   print Answer,TEMP,B  #; "  Time:"; Timer - T
st = time()
Problem_100()
print "Process Time is",time()-st
#756872327473
