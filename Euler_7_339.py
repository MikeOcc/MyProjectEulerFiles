#
#  Euler 339
#
#
from random import randint,seed
N=5

seed('X')

B,W=N,N
Bt,Wt=0,0
NumAttempts=5
ctr,ctr1=0,0
print "######################"

for j in xrange(NumAttempts):
  
  ctr1=0
  B,W=N,N
  rndrng = 1
  while W!=0:
    totSheep=B+W
    remsheep = False
    x = randint(0,totSheep*1)
    x = randint(0,totSheep*1)
    ctr+=1;ctr1+=1
    #print "X", x
    if x <= B*rndrng:
     
      B+=1
      W-=1
    else:
      remsheep = True
      B-=1
      W+=1
    
    if remsheep==True:
      nsheeptrem = 4   # abs((B-W)/2)+1
      if nsheeptrem>W:nsheeptrem=W 
      W-= nsheeptrem; totSheep-= nsheeptrem
    else:
      nsheeptrem = 0  # abs(B-W)+1
      if nsheeptrem>W:nsheeptrem=W 
      W-= nsheeptrem; totSheep-= nsheeptrem
        
    if B==0 or W==0:break
    Bt+=B #; AvgB = Bt/float(ctr1)
    #print "Black Sheep, White Sheep,Avg", B,W,AvgB
    
  #print "Black Sheep, White Sheep", B,W

AvgB = Bt/float(ctr)
print "!!!The Avg # of Black Sheep is",AvgB

