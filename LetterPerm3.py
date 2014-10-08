#
#
#  Letter Perms
#
#

#ABCD E F
#ABC DF E
#ABC E DF
#ABCE F D
#ABC F E D
#ABDCFE
#ABDECF
#ABDEFC
#ABDFCE
#ABDFEC

def pandig(lstr):

  Q= {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K"}

  P = {"A":0,"B":0,"C":0,"D":0,"E":0,"F":0,"G":0,"H":0,"I":0,"J":0,"K":0}
  
  for i in xrange(len(lstr)):
    if P[lstr[i]] == 0:
       P[lstr[i]] =1
    else:
      return False
  return True

def NextPerm(P):

  TP = P

  ctr = 0
  isBigger = False
  noneSmaller = False
  finis = False

  while not finis:

    if not isBigger:

      bp = 0
    
      for i in range(len(P)-1,0,-1):
        x = TP[i];y = TP[i-1] 
        print i, ")",x, y, x>y 
        if x<y:
          bp = i-1
          break
      
      if bp == 0:
          noneSmaller = True
          isBigger = True
          bp = 9
      elif bp==8 or bp==9:
          bp = bp - 1
      else:
          bp = bp - 1

      print "bp",bp
      TP = TP[:bp]+TP[10:bp-1:-1]
      if TP>P:
        print "big"
        isBigger = True
      print TP

    elif isBigger:
      print "!!!"
      temp = TP
      bp = bp +1
      TP = TP[:bp]+TP[10:bp-1:-1]
      print bp,TP,temp, TP<temp, TP>P
      if TP<=temp and TP>P:
        if bp>8:
          print "break"
          break
          noneSmaller=True
      elif temp>TP:
        TP=temp
        noneSmaller=True
    print "big,small",isBigger, noneSmaller
    if isBigger and noneSmaller:return TP
  return "!",TP

if __name__ == '__main__':

  #L ="ABCDEFGHIKJ"
  L ="ABCDEFGHJIK"
 # l = len(L) 
 # if pandig(L) == True: 
 #     print "Eureka!"
  print L
  print NextPerm(L)
