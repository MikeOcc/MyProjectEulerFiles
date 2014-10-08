#
# divide 1 by any integer > 2
#

def MyDivide(num,div,decplaces):

  from string import replace,lstrip
  from math import log10

  num0,div0=num,div

  #num = 1

  #div = 983

  ldiv = len(str(int(div))) 
  lnum = len(str(int(num)))
  
  if int(div) ==0: ldiv = 0
  if int(num) ==0: lnum = 0

  sumstr = ""

  numchunk = int(replace(str(num),".",""))
  div = int(replace(str(div),".",""))

  numdigits = 1000

  for i in range(1,numdigits):
  
    x1 = int(numchunk/div)
    x2 = int((numchunk)%div)

    if x1 == 0:
      sumstr = sumstr+"0"
    else: 
      sumstr = sumstr+str(x1)
  
    numchunk = x2 * 10  

  digplace = lnum-ldiv

  print digplace

  if digplace ==0:
     #print "$$$",digplace,num0>div0
     if num0>div0:
        digplace = 1
        #if sumstr[:1]=="0":sumstr = sumstr[1:]
        sumstr = sumstr[:digplace] + "."+ sumstr[digplace:]
     elif num0==div0:
        digplace = 1
        #if sumstr[:1]=="0":sumstr = sumstr[1:]
        sumstr = sumstr[:digplace] + "."+ sumstr[digplace:]       
     else:
       #if sumstr[:1]=="0":sumstr = sumstr[1:]
       sumstr=lstrip(sumstr,"0")
       sumstr = "."+ sumstr
  elif digplace < 0:
    #print "$$$",digplace
    if digplace<0 :
       pref = "0"*(abs(digplace))
       #print pref   #,lstrip(sumstr,"0")
       sumstr = pref + lstrip(sumstr,"0")
    #if sumstr[:1]=="0":sumstr = sumstr[1:]
    sumstr = "."+ sumstr
  else:
    print "$$$:",digplace  #,sumstr
    sumstr=lstrip(sumstr,"0")
    #xx=str(float(num0)/float(div0))
    xx=str(10**(log10(num0)-log10(2)))
    #digplace=xx.find(".")
    digplace +=1
    print "$$:",digplace ,xx, num0, div0 #,sumstr
    sumstr = sumstr[:digplace] + "."+ sumstr[digplace:]

  return sumstr[:decplaces]


if __name__ == "__main__":
  #print MyDivide(8*10**18-1,2,24)
  #print MyDivide(3999999999999999999,2,24)
  a = 8*10**18-1
  b = 2
#  while 1:
  for ii in xrange(5):
    x = MyDivide(a,b,24)
    print x
    d = x.find(".")
    remn = int(x[d+1:])
    if remn>0:
      a-=1
      b+=1
    else:
      a=int(x[:d])-1
      b=2
      print "@@",remn
    



