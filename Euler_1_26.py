import math
import string

#
# [:]
#

def mydivide(div):

  num = 1
  #div = n
  div = int(div)
  sumstr = "0."

  ldiv = len(str(div)) 
  multfactor = numchunk = int(10**ldiv)

  sumstr = "0." + "0" * (ldiv-1)

  for i in range(1,1000):
  
    x1 = int(numchunk/div)
    x2 = int(numchunk%div)

    if x1 == 0:
      sumstr = sumstr+"0"
    else: 
      sumstr = sumstr+str(x1)
  
    numchunk = x2 * 10

  return sumstr


def findgreatestseq(n,qnum):

  snumlen = len(qnum)
  fchunk = qnum[7:12]
  fpos = qnum.find(fchunk,0)
  spos = qnum.find(fchunk,fpos+1)

  print
  print n," seq ", (spos-fpos) , ":", seqnum
  print

  return (spos - fpos)

if __name__ == "__main__":
 
  cutoff = 1000
  nummaxlen = 0
  maxlengrtseq = 0

  for i in range(1, cutoff):
    seqnum = mydivide(i)

    lengrtseq = findgreatestseq(i,seqnum)
    if lengrtseq > maxlengrtseq:
       maxlengrtseq = lengrtseq
       nummaxlen = i
    
    #print
    #print i, ":", seqnum
 
  print
  print "The divisor with the greatest repeating sequence is ",nummaxlen," with a length of ", maxlengrtseq, " digits!"




