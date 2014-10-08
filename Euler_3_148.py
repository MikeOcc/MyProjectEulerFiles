#
#
#  Problem 148
#
#

from Functions import nCr

ctr=0
for i in xrange(7,200):
  print i,";",
  ctr2=0

  if i%2==1:
    dbl = True
    rng = int(i/2.)
  else:
    dble = False
    rng = int(i/2.) 
  
  for j in xrange(1,rng+1):
    #print nCr(i,j), 
    x=nCr(i,j)
    if x%7==0: 
      #ctr +=1
      ctr2 +=1
     # print x
  if dbl:
    ctr2 *=2 
  else:
    ctr2 =ctr*2 
  ctr += ctr2
  print "***** ",i,ctr2
  print
print
print ctr





