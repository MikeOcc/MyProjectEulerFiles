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

  prime = True

  for divisor in range(2,startnumber/2,2):
      if float(startnumber)/float(divisor)==int(float(startnumber)/float(divisor)):
          prime=False

  return prime

#IsPrime(13)

if __name__ == "__main__":

  sdfdsf=0

  numprimes = 0
  smallestprime = 0

  for i in range(56, 110):
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
            if numprimes == 8:
               smallestprime = basenum
       print "numprimes for ", baseprime, " is ", numprimes


  for i in range(5, 20):
    for l in range(0,11):
      for j in range(1,11,2):
  
        baseprime = i*10000 + l*100 + j
        numprimes = 0
        for k in range(0,11):
      
          #print l,m
          #print "2 level",baseprime
          strnum2 = (i)*10000 + k*1000 + l * 100 + k * 10 + j
     
          if IsPrime(strnum2)==True:
             numprimes = numprimes + 1
             if numprimes == 8:
                smallestprime = basenum

             #print "basenum 2", strnum2  
          print "numprimes2 for ", baseprime, " is ", numprimes
  
  for i in range(5, 20):
    for l in range(0,11):
      for j in range(1,11,2):
  
        baseprime = i*10000 + l*10 + j
        numprimes = 0
        for k in range(0,11):
      
          #print l,m
          #print "2 level",baseprime
          strnum3 = (i)*10000 + k*1000 + k * 100 + l * 10 + j
     
          if IsPrime(strnum3)==True:
             numprimes = numprimes + 1
             if numprimes == 8:
                smallestprime = basenum

             #print "basenum 3", strnum2  
        print "numprimes3 for ", baseprime, " is ", numprimes


  if smallestprime > 0:
     print "The Smallest Prime for Family of 8 is: ", smallestprime
  else:
     print "Level 8 not found"










