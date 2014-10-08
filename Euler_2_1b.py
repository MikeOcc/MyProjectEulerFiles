###
# Problem 51 of Project Euler
###

from math import *

sum = 0
fibnum = 0
firstnum = 0
secondnum = 1
ctr = 1

#startnumber=13
#startnumber*=1.0



def IsPrime(startnumber):

  startnumber*=1.0
 
  if startnumber/2==int(startnumber/2):
     return False


  for divisor in range(3,int(startnumber**0.5)+1,2):
      if startnumber/divisor==int(startnumber/divisor):
          return False
          
  return True

#IsPrime(13)

if __name__ == "__main__":

  maxlevel = 8
  numprimes = 0
  smallestprime = 0

  for i in range(1, 200):
    for j in range(1,11,2):

       numprimes = 0
       #baseprime = int(str(i) + str(0) + str(0) + str(j))
       baseprime = i * 1000 + j

       for k in range(0,11):
          #strnum = str(i) + str(k) + str(k) + str(j)
          strnum = i*1000 + k * 100 + k * 10 + j
          basenum = int(strnum)
          
          if IsPrime(basenum)==True:
            numprimes = numprimes + 1  
            if numprimes == maxlevel:
               smallestprime = baseprime
       print "numprimes for ", baseprime, " is ", numprimes


  for i in range(1, 200):
    for v in range(0,10):
      for j in range(1,10,2):
  
        baseprime = i*10000 + v*100 + j
        numprimes = 0
        for k in range(0,10):
      
          #print l,m
          #print "2 level",baseprime
          strnum2 = (i)*10000 + k*1000 + v * 100 + k * 10 + j
     
          if IsPrime(strnum2)==True:
             numprimes = numprimes + 1
             if numprimes == maxlevel:
                smallestprime = basenum
        
             #print "basenum 2", strnum2  
        print "numprimes2 for ", baseprime, " is ", numprimes
  
  for i in range(1, 10):
    for l in range(0,10):
      for j in range(1,10,2):
  
        baseprime = i*1000 + l*10 + j
        numprimes = 0
        for k in range(0,10):
      
          #print l,m
          #print "2 level",baseprime
          strnum3 = (i)*10000 + k*1000 + k * 100 + l * 10 + j
     
          if IsPrime(strnum3)==True:
             numprimes = numprimes + 1
             if numprimes == maxlevel:
                smallestprime = baseprime

             #print "basenum3", strnum3  
        print "numprimes3 for ", baseprime, " is ", numprimes


  for i in range(0, 10):
    for l in range(0,10):
      for j in range(1,10,2):
  
        baseprime = i*100 + l*10 + j
        numprimes = 0
        for k in range(0,10):
      
          #print l,m
          #print "2 level",baseprime
          strnum4 = (k)*10000 + k*1000 + i * 100 + l * 10 + j
     
          if IsPrime(strnum4)==True:
             numprimes = numprimes + 1
             if numprimes == maxlevel:
                smallestprime = baseprime

             print "basenum4", strnum4  
        print "numprimes4 for ", baseprime, " is ", numprimes


  if smallestprime > 0:
     print "The Smallest Prime for Family of ",maxlevel," is: ", smallestprime
  else:
     print "Level 8 not found"










