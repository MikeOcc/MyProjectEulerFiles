#
# Euler problem 1_38
#
#
from math import factorial

def IsPanDig(n):
  haszero = False
  nstr = str(n)
  lstr = len(str(n))
  sumdig = 1
  panstring =""

  for i in range(0,lstr):
    if nstr[i]=="0":
      haszero = True
    else:
      sumdig = sumdig * int(nstr[i])
    if nstr[i] in panstring: return False
    panstring += nstr[i]

  if haszero: lstr = lstr -1
  #print "sumdig,lstr", sumdig, nstr, lstr ,sumdig == factorial(lstr),panstring 

  if sumdig == factorial(lstr):return True
  return False



if __name__ == "__main__":

  maxnum = 0
  for i in range(10000,1,-1):
       summ = ""
       for k in range(1,10):
         summ+=str(i * (k))
       summ=summ[:9]
       if "0" in summ: continue
       if len(summ)==9 and IsPanDig(summ) and int(summ) > maxnum:
         print "i",i,summ
         maxnum=summ

  print
  print "The maximum concatenated Pandigital number is", maxnum

