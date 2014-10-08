#
#
#


def Phi(Achnum,factlist):

  n1,m1,o1,p1,q1,r1,s1,t1,u1=0,0,0,0,0,0,0,0,0
  
  #powlist = list(set(factlist))

  #if Achnum == 5000:print factlist

  powlist = "["+factlist.rstrip(",")+"]"
  powlist = list(set(map(int,powlist.strip('[]').split(','))))

  """
  if Achnum == 5000:
    print factlist,powlist,type(powlist)
    for kk in range(0,len(powlist)):
      print powlist[kk]
  """    

  # Phi = Totient(n) 
  
  #if Achnum == 5488:print "Check 5488"

  Phi = Achnum       #  start out with achilles # and then whittle down

  for i in powlist:
    Phi = Phi * (int(i)-1)
    Phi = Phi / int(i)

#  if Achnum == 5000:print "Phi5000:",Phi

  return Phi

"""

Phi(6) = 2*3*(1/2)*2(/3) = 4
Phi(8) = 2*2*2*(1/2) = 4
Phi(7) = 6
Phi(8) = 4
Phi(9) = 3*3*(2/3)=6
Phi(10) = 2*5*(1/2)*(4/5)= 4

 
"""
N = 10
for i in range(6,11);

