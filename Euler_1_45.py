#
#
#  Euler Problem 35
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	Pn=n(3n-1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n-1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.
#

from math import sqrt

print

for i in range(285, 285 + 100000000):


  T = round((i**2. +i)/2.0,2)

  j = int(round((1 + sqrt(1.+4.*3.*(i*i + i)))/6.,2))

  P = j * (3. * j -1.)/2.0
 
  k = int(round((4. + sqrt(4. + 16.*(3.*j*j - j))/8.),2))

  H = k * (2. * k -1)

  #print i, T , j, P, k, H

  if abs(T-P) ==0 :
    print "Found!",i, T, j, P, k, H 
    print
