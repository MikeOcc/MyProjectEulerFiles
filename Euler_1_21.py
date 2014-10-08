#
#  Euler Problem 21
#  find the sum of all amicable pairs under 1000
#

def retdiv(n):
  #from math import sort
  #print "start factoring"
  fact = [1]

  #r=n

  #if n%2==0: 
  #  r = n/2
  #else:
  #  r = n/3
  
  for j in range(2, int(n**.5)+1): #range(2,n/2+1):
 
    if n%j ==0:
       fact.append(j)
       fact.append(n/j)
       #print j, fact

  #print "end factoring"
  #print "n,fact", n, fact
  #fact = sorted(fact)
  return fact


if __name__ == "__main__":

  from time import time
  starttime = time()

  zum1,ami1, ami2, sumdiv1, sumdiv2,ctr = 0,0,0,0,0,0
  maxnum = 20000

  for i in range(1,maxnum):

     ami1 = i                  # possible first # of amicable pair
     divami1 = retdiv(ami1)    # divisor list of poss. amicable #
     sumdiv1 = 0                  # sum divs to create 2d poss. ami #
     for x in divami1:sumdiv1 +=x

     ami2 = sumdiv1
     divami2 = retdiv(ami2)    # create divs of 2d poss. ami #
     sumdiv2 = 0                  # sum divs to compare to first #
     for x in divami2:sumdiv2 += x
       
     #print ami1, sumdiv1, ami2, sumdiv2
     #print "amicable pair:", ami1  , ami2

     if (ami1==sumdiv2 and ami2==sumdiv1 and ami1!=ami2):
        ctr +=1
        print "Amicable Pair (",ctr,") is " , ami1,ami2
        zum1 += ami1 

print "We found",ctr,"amicable pairs!"
print "The sum of amicable pairs below ", maxnum,"is" ,zum1
print "Process took ", time()-starttime, "seconds"

 


