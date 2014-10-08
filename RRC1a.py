#MATH PROBLEM
#A father died leaving money in his estate. #All the money was 
# to be divided among his #children in the following manner
#
#$X to the 1st born plus 1/16 of what remains
#$2X to the 2nd born plus 1/16 of what remains
#$3X to the 3rd born plus 1/16 of what remains, AND SO ON...

#After the distribution, each child received the SAME AMOUNT of 
#money & no money leftover. HOW MANY CHILDREN did the father have?
#
# p = amount awarded to each child
# n = number of children
# nx = p
# T = total amount of money
# np = n(nx) = T
# p = x + (T-p)/16
# p = x + T/16 - p/16
# p(1 + 1/16) = x + T/16
# p(16 + 1) = 16x +T
# 17p = 16x + T


#  nx = p
#  nnx = T +> x = T/(n*n)



#  nX =r/16 - (n-1)x
# []

P=[]
T = 16000.0

n = 1

while 1:
  n +=1
  x = T/(n**2)
  t = T
  isFound = False
  #p = 0
  P=[]
  for i in xrange(1,n+1):
    p= i*x 
    r = (t-p)/16.0
    p += r
    P.append(p)
    t -= p
    if t <.01:
      isFound = True
      break
  if isFound == True:
    break
  

print n, p, T
print P
print
print "number of children is",n

print

#print P
#print




  