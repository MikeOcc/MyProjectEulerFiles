from math import factorial

indx0 = "0123456789"

topperm = 999999

isdone=False

curperm = topperm

nthpermstr =""

while len(nthpermstr)<10:
  
  lowfact = 1
  highfact = 10
  nextnum = 0
  
  for i in range(lowfact,highfact+1):
       
       x=factorial(i)
       if x > curperm:
          #print "hit"
          nextnum = i-1
          break
       
  #print "i",i,"nextnum",nextnum
       
  n1 = int(curperm/factorial(nextnum))
  curperm = curperm - n1* factorial(nextnum)

  print "i",i,"nextnum",nextnum,"quotient",n1,"remainder",curperm  
     
  nthpermstr +=indx0[n1]
  indx0=indx0[:n1]+indx0[n1+1:]

print "1000000th Lexicographic Perm is ",nthpermstr


       


       
       


