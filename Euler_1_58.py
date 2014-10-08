#
#
#
#
#If one complete new layer is wrapped around the spiral above,
# a square spiral with side length 9 will be formed. If this 
#process is continued, what is the side length of the square 
#spiral for which the ratio of primes along both diagonals
# first falls below 10%?
#
#
from Functions import IsPrime
ctr = 0.0
ctr1=0.0
for i in range(3,30000,2):
  ctr1+=1
  seDiag = i**2
  swDiag = seDiag-(i-1)
  nwDiag = swDiag-(i-1)
  neDiag = nwDiag-(i-1)
  numDiags =(ctr1)*4.0 +1.

  #print i, numDiags 

  print i,"num diags", numDiags,":",seDiag,swDiag,nwDiag,neDiag
  
  if IsPrime(swDiag):ctr+=1
  if IsPrime(nwDiag):ctr+=1
  if IsPrime(neDiag):ctr+=1

  rat = ctr/numDiags

  print i,") Ratio of Primes to Diags is",ctr, numDiags, rat
  print
  if rat < .1:
    print "Found", i, rat
    break


