#
#  Euler Problem 170
#  
#
from itertools import permutations
from time import time

def PanDig(n):

  nset = set(str(n))
  #lnset = len(nset)
  if len(nset)>10:return False
  for m in xrange(1,10):
    if str(m) not in nset: return False

  return True

def MultDig(n):
  # If a digit is duplicated, return True
  nlist = list(str(n))
  nset = list(set(list(str(n))))
  # print nlist
  # print nset
  if len(nlist)==len(nset):return False
  return True

def notJ(j,ii):
  z =list('1234567890')
  jlist = list(str(j))
  for zz in jlist:
    z.remove(str(zz))
  for iii in list(ii):
    if iii in z:z.remove(iii)
  return ''.join(z)
	
  
if __name__ == '__main__':

  st = time()
  maxval = 0
  for i in range(3,30,3):
    if MultDig(i):continue
    ii = str(i)
    for j in range(1234,98765):
        ff = False
        strj = str(j)
        for iii in list(ii):
          if iii in strj:
            ff = True
        if ff == False and not MultDig(j):
          x = i * j
          
          if not MultDig(x):
            y = notJ(j,ii) 
            yy = permutations(y)
            for zz in yy:
              w1 = ''.join(zz)
              w = int(w1)
              v = i * w
              if not MultDig(v):
                val = int(str(x) + str(v))
                if not MultDig(val) and PanDig(val):
                  #print "combined pandigital found ", i,j,x,w,v,val
                  if val>maxval:
                    maxval = val
                    #print "combined pandigital found ", i,j,x,w,v,val
  print
  print "Maximum combined Pandigital ",maxval
  print "Elapsed time is ", time()-st
  
  #9876541032
  # 9760521384


