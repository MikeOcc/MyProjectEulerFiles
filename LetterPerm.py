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

if __name__ == '__main__':

  L ="ABCDEFGHIJK"
  l = len(L) 
  nextfound = False

  
  if pandig(L) == True: 
      print "Eureka!"

  ctr = 0
  while nextfound==False:

    bp = 0

    if nextfound:break
    
    for i in range(10,0,-1):
       x = L[i];y = L[i-1] 
       print i, ")",x, y, x>y 
       if x<y:
         bp = i-1
         #break

    if bp == 0:
      bp = 9
    else:
      bp = bp

    print
    print bp,L,L[bp]
    print

    a=L[:bp]
    b=L[:bp+1:-1]
    #c=L[bp-1:bp+(10-bp)]

    print "abc:", a, b

    L = a + b 
    #L= L[:bp-1]+L[bp:bp+1]+L[bp-1:bp + (10-bp)]

    print ctr,":",L

    ctr = ctr + 1

    if ctr>3:
      nextfound=True
      break


