


sum=0

x = 500*499/2
maxum = 0
maxsum = 0
bestrow = 0

rstart = 12375
estart = 12377
showall = False

for r in range(rstart,estart):

  

  trinum = r*(r+1)/2
  #trinum = r  
  sum=0

  if trinum%2==0:
     endrange = (trinum/2) + 1
  elif trinum%3==0:
     endrange = (trinum/3) + 1
  elif trinum%5==0:
     endrange = (trinum/5) + 1
#  elif trinum%7==0:
#     endrange = (trinum/7) + 1
#  elif trinum%9==0:
#     endrange = (trinum/9) + 1
  else:
     continue

  print r

  for i in range(1,endrange):
      #z=float(trinum)/float(i)
      #print i, "z = ",z
  
      if trinum%i==0:
        sum = sum + 1
        #print i,float(trinum)/float(i)

  sum = sum + 1
  
  #print "maxsum ", maxsum

  if showall == True or sum > maxsum:
        print "\nRow:", r, ",triangle number :",trinum, ", number of factors:",sum  


  if sum > maxsum:
        maxsum = sum
        maxum = trinum
        bestrow = r
  
 
      
  if maxsum > 500:break;       



print "\nFor r =", bestrow, ", the number of factors =",maxsum, "for triangle number =", maxum



#6720 - 384, 6546