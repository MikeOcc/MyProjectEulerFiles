#
#
# Euler 114
#
#
from math import factorial
count = 1
N=50 # length of grid
s=3  # smallest block size
s2=3
s3=3

for b1 in xrange(s,N+1):
  z = (N-b1 + 1)
  count += z
  #print b1, z, count

print "!"

for N1 in xrange(N,6,-1):
  #print "n2",N1
  for b1 in xrange(s,N1-4+1):
    for b2 in xrange(s2, N1-b1):
      if b1+b2+1>N1: continue
      y = N1 - b1 - b2  
      count += y
      #print b1,b2,y
      
print "$"

for N1 in xrange(N,10,-1):
  print "n3",N1
  for b1 in xrange(s,N1-4*2+1):
    for b2 in xrange(s2, N1-b1):
      for b3 in xrange(s3, N1-b1-b2):
        if b1+b2+b3+2>N1: continue
        y = N1 - b1 - b2 - b3
        count += y
        #print b1,b2,b3,":",y, N1
	  
print count
	
	
    # y = N - i - j
    # if y ==1: count+=1;continue
    # if y ==2: count+=3;continue
    # if y ==3: count+=6;continue
    # x=0
    # if y%2==0:x=(y+1)*(y/2)
    # if y%2==1:x=(y)*((y+1)/2)	
    # count += x
    # print i, j, i+j, y,x
	
	

	