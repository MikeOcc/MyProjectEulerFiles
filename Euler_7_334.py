#
#
#
#
#

from math import floor

t={} 
b={} 

t[0]=123456 


for i in range(1,1000):

  if i%2 == 0:
     t[i] = t[i-1]/2  
  else:
     t[i] = int(floor(t[i-1]/2))^926252

  b[i] = t[i]%(2048) + 1

  print i, b[i],  t[i]

print

print b





