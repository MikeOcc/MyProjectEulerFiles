#
#
#  Euler Problem 111
#
#

from Functions import IsPrime
from itertools import permutations


x = "3"
total = 0
primes = []

d = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

for i in range(1,10):
  for j in [1,3,7,9]:
    x = i*10**9 + j
    if IsPrime(x):
      total += x
      d[0]=d[0] + x
      print x
# print

# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 111111110 + j
    # if IsPrime(x):
      # total += x
      # print x

# print
	  
# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 222222220 + j
    # if IsPrime(x):
      # total += x
      # print "Z",x

# print
	  
# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 333333330 + j
    # if IsPrime(x):
      # total += x
      # print x

# print
	  
# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 444444440 + j
    # if IsPrime(x):
      # total += x
      # print x
# print

# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 555555550 + j
    # if IsPrime(x):
      # total += x
      # print x
# print

# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 666666660 + j
    # if IsPrime(x):
      # total += x
      # print x

# print

# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 777777770 + j
    # if IsPrime(x):
      # total += x
      # print x	  

# print

# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 888888880 + j
    # if IsPrime(x):
      # total += x
      # print x	  
	  
# print

# for i in range(1,10):
  # for j in [1,3,7,9]:
    # x = i*10**9 + 999999990 + j
    # if IsPrime(x):
      # total += x
      # print x	  

print "---------------------------"
	  
for i in range(1,10):
  for j in [1,3,9]:
    x = i*10**9 + 111111111 * j
    if IsPrime(x):
      total += x
      print "V:",x	  

# print
	 
# for i in range(1,10):
  # print
  # for j in [1,3,7,9]:
    # x = i* 1111111110 + j
    # if IsPrime(x):
      # total += x
      # print x		 


# print "---------------------------"
	  
# for i in [2,8]:
  # for j in range(1,100):
    # x = i* 1111111100 + j
    # if IsPrime(x):
      # total += x
      # print "W:",x	  
# print
print "---------------------------"
print
	  
for i in [2,8]:
  x0=i * 1111111111
  for j in range(0,10):
    for k in range(0,10):
      if k<=j: continue
      if j==10 and k==0: continue
      for l in range(10):
        for m in range(10):
          x = x0
          x += -i*10**j - i*10**k + l *10**j + m*10**k
          if x<10**9:continue
          if IsPrime(x):
            total += x
            print "Q:",x,j,k,l,m,-i*10**j ,- i*10**k ,+ l *10**j ,+ m*10**k	 
	  
	  
# for i in range(10,100):
    # x = i* 10**8 +  22222222 
    # print "U:",x	
    # if IsPrime(x):
      # total += x
      # print "U:",x	  
	  
print "---------------------------"
	  

for i in range(1,10):
  for j in range(0,10):
    for k in range(0,10):
      x = i* 1111111111 - i*10**j + k * 10**j
      if IsPrime(x):
        total += x
        print x,i       #,j,k,i* 1111111111 , 10**j , k * 10**j
	  
print "total is: ", total
print d
