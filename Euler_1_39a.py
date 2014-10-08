from math import factorial

indx0 = "0123456789"

topperm = 999999

isdone=False

curperm = topperm

while !isdone:

  
  lowfact = 1
  highfact = 10
  
  for i in range(lowfact,highfact+1):
       if factorial(i) > curperm:
          nextnum = i-1
          break

       n1 = int(curperm/factorial(nextnum))
       curperm = curperm - n1* factorial(nextnum)



