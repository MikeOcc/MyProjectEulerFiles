#
#
# Euler Problem 315
#
# []
#

global d
d = [6,2,5,5,4,5,6,4,7,6]



def numer(n):

  s = list(str(n))
  t=0
  for a in s:
    t+=int(a)
  return t



print numer(60)









