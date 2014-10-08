#
#
#  Euler Project 1_9 (#9) There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#  Find the product abc.
#
#

import string
from math import *


a = b = c = 0

# a + b + c = 1000
# a*a + b*b = c*c 

#
#  a*a = (1000 - b -c) * (1000 - b -c)
#  a*a = 1000000 + b*b + c*c -2000*b  -2000*c +2*b*c = c*c - b*b
#   1000000 + 2b*b -2000*b -2000*c + 2 b*c = 0


for a in range(500,1,-1):
   for b in range(1,500):

     c = 1000 - a - b
     if (a*a + b*b == c*c):
        print a, b, c
        break