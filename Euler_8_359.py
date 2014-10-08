#
#  Euler Problem 359
#
#

from Functions import RetFact, divisors

facts = RetFact(71328803586048)

rooms = divisors(71328803586048)

print len(rooms)


# 1    1,1
# 2    2,1
# 3    1,2     = 4
# 4    3,1 
# 5    4,1
# 6    3,2     = 9
# 7    2,2     = 9
# 8    1,3     = 9
# 9    5,1
# 10   6,1
# 11   5,2     = 16
# 12   4,2     = 16
# 13   3,3     = 16
# 14   2,3     = 16
# 15   1,4     = 16
# 16   7,1
# 17   8,1
# 18   7,2     = 25
# 19   6,2     = 25
# 20   5,3     = 25
# 21   4,3     = 25
# 22   3,4     = 25
# 23   2,4     = 25
# 24   1,5     = 25
# 25   9,1
# 26   10,1    
# 27   9,2     = 36
# 28   8,2     = 36
# 29   7,3     = 36


#
#   n =   1   4   9    16    25   36
#   f =   1   3   5     7     9   11
#   f(i,1) = ((i+1)/2)**2 for odd floors, first room => square # (n)
#
#   n =   2   5   10    17   26   37
#   f =   2   4   6     8    10   12
#   f(i,1) = (i/2)**2 + 1 for even floors first room => square #+1 (n)

#  f(1,n) = n**2
#  

for i in xrange(1,40):
  if i%2==1:
    print (i, ((i+1)/2)**2)
  else:
    print (i,(i/2)**2 + 1)

 
    



