#
# divide 1 by any integer > 2
#

def MyDivide(num,div,decplaces):

  import string

  #num = 1

  #div = 983

  ldiv = len(str(div)) 
  lnum = len(str(num))
  numchunk = int(10**ldiv)
  #maxlen = len(str(numchunk))

  sumstr = ""    #"0." + "0" * (ldiv-lnum)

  #digplace = lnum-ldiv

  numchunk = numchunk * num

  #print maxlen

  #print multfactor

  numdigits = 1000

  for i in range(1,numdigits):
  
    x1 = int(numchunk/div)
    x2 = int((numchunk)%div)
 
    #print numchunk, x1, x2

    if x1 == 0:
      sumstr = sumstr+"0"
    else: 
      sumstr = sumstr+str(x1)
  
    numchunk = x2 * 10  

  digplace = lnum-ldiv
  overunder = 0

  if (num > div):
 
    if slice(str(num)[:1])>slice(str(div)[:1]) or len(str((num/div)))>1 or (num>div): overunder = 1

  elif num == div:
    overunder = 1

  else:
    if slice(str(div)[:1])<slice(str(num)[:1]) : overunder = 1

  #print digplace, overunder, len(str((num/div)))

  if digplace < 0:
    sumstr = "0."+  "0" * (ldiv-lnum - overunder ) + sumstr
  #elif digplace ==0:
  #  sumstr = sumstr[:digplace+overunder]+"."+ sumstr[digplace+overunder:]
  #elif digplace ==1:
  #  sumstr = sumstr[:digplace+overunder]+"."+ sumstr[digplace+overunder:]
  else:
    sumstr = sumstr[:digplace+overunder]+"."+ sumstr[digplace+overunder:]

  #print num, " divided by ", div , " = ", sumstr

  return sumstr[:decplaces]


if __name__ == "__main__":
  print MyDivide(41,29,20)

