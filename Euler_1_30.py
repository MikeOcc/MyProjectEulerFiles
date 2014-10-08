



tothits = 0
totsum = 0
#p1,p2,p3,p4 = 0,0,0,0

for i in range(2,9999999):

  
  I = str(i)
  #d1 , d2, d3, d4 = I[0],I[1],I[2],I[3]
  len1 = len(I)
  I = "0"*(7-len1)+I
  p1 ,p2,p3, p4,p5,p6,p7 = int(I[0]),int(I[1]),int(I[2]),int(I[3]),int(I[4]),int(I[5]),int(I[6])

  #if i == 93084:
  #  print "gotchya",p1,p2,p3,p4,p5,p6

  if len1 == 4:
    n = p4**5 + p5**5 + p6**5 + p7**5 
  elif len1 ==5:
    n = p3**5 + p4**5 + p5**5 + p6**5 + p7**5 
  elif len1 ==6:
    n = p2**5 + p3**5 + p4**5 + p5**5 + p6**5 + p7**5
  else:
    n = p1**5 + p2**5 + p3**5 + p4**5 + p5**5 + p6**6 + p7**6

  if i == n:
     print "Hit!", i, n, p1, p2, p3, p4, p5, p6
     totsum += i
     tothits += 1

print tothits, totsum
