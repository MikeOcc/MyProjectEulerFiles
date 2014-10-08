#
#  Project Euler Problem 1_39
#
#If p is the perimeter of a right angle triangle with integral length #sides, {a,b,c}, there are exactly three solutions for p = 120.
#
#{20,48,52}, {24,45,51}, {30,40,50}
#
#For which value of p <= 1000, is the number of solutions maximised?
#
#from math import sort
maxctr = 0
maxp = 0
for p in range(10,1002,2):

  ctr = 0
  print "Perimeter P:",p,"___________________"
  s1 = int(p/2)
  #s2 = int(round(sqrt(p**2-s1**2),2))

  for i in range(1,s1):
    for j in range(1,s1+1):

       k = p - (i + j)

       if (k< 1) or (j<i): continue
       if i**2 + j**2 == k**2:
         ctr+=1
         print str(ctr),") IJK", i,j,k,"I+J+K,P", i+j+k, p, float(j)/float(i)
  print "Number of solutions for p =",p, " is ", ctr
  if ctr>maxctr: maxctr=ctr;maxp=p

print "The number of solutions is maximized for P =",maxp," # is  Sols: ",maxctr

     