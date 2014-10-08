#
#  Euler Problem 170
#  
#


def PanDig(n):

  nset = set(str(n))
  #lnset = len(nset)

  for m in xrange(1,10):
    if str(m) not in nset: return False

  return True

def MultDig(n,exchunk="0"):
  #print "n",n
  nset = str(n)
  lnset = len(nset)

  if lnset==2:
    nset="0"+nset
    lnset==3

  chklst = [0]*10
  
  for z in xrange(lnset):

    if nset[z] in exchunk:
       #print nset[z],exchunk
       return False
    if chklst[int(nset[z])]==0:
       chklst[int(nset[z])]=1
    else:
       return False
  return True

if __name__ == '__main__':

  print MultDig(12345)
  exit()

  for i in range(2,10):

    for j in range(1234,9876):
        if MultDig(j):
          x = i * j
          z = str(j)+str(x)
      
        if MultDig(i,z):   #  and PanDig(z):
          print z
        if i ==3:exit()



