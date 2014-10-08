#MATH PROBLEM
#A father died leaving money in his estate. #All the money was 
# to be divided among his #children in the following manner
#
#$X to the 1st born plus 1/16 of what remains
#$2X to the 2nd born plus 1/16 of what remains
#$3X to the 3rd born plus 1/16 of what remains, AND SO ON...

#After the distribution, each child received the SAME AMOUNT of 
#money & no money leftover. HOW MANY CHILDREN did the father have?


#  nX =r/16 - (n-1)x
# []

P=[]
T = 15000.0
x = T/(225.0)
n = 0
while 1:
  n+=1
  p = n*x
  r = (T-p)/16.0
  p+= r
  T = T - p

  P.append(p)

  print n, p, T
  if T<=.1:
    break



print "number of children is",n

print

#print P
#print




  