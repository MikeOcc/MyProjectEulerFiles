
#  Find larger Palindrome from product of 2 3-digit #s


def IsPal(dig):
  import string
  
  strdig = str(dig)
  revstr = strdig[::-1]

  if strdig == revstr:
    return True
  else:
    return False

if __name__ == '__main__':

  maxpal = 0; maxi = 0; maxj = 0

  for i in range(1,1000, 1):
    for j in range(1,1000, 1):
      palinpos = i * j
      #print "pos ",i, palings
      if IsPal(palinpos):
        pal = palinpos
        print "Palindrome is ", i,j, pal
        if pal > maxpal:
           maxpal = pal; maxi = 1; maxj = j
      
print "Our Max Palindrome is ", maxi, maxi, maxpal