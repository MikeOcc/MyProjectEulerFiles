#
#
#  Euler problem 388
#
#

ctr = 0
sum1 = 0
max = 1
d = {}
for i in range(-max,max+1):
  for j in range(-max,max+1):
    if i==0 or j==0:continue
    slope = j/(i*1.)
    if slope not in d:
      d[slope]=1
      ctr += 1
      print i,j,":",j/(i*1.)

	
center = 8
edge = 9
lines = 26

# for i in range(2,max+1):

  

    # ctr += 1
    #print i,j
	
# print "root level", ctr-1
# ctr-=1
# ctr =(ctr+1) * (2*max + 1) -1 
#ctr -= 1
    
print "number of lattice lines", ctr + 3

