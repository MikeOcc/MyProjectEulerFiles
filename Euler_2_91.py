#
#
#  Euler Problem 91
#

def d(p1,p2):
  dx = p1[0]-p2[0]
  dy = p1[1]-p2[1]
  return (dx**2 + dy**2)**.5

summ=0
ctr = 0
x1=0;y1=0
for x2 in range(0,3):
  for y2 in range(0,3):
     for x3 in range(0,3):
       for y3 in range(0,3):
            p1 = (0,0)
            p2 = (x2,y2)
            p3 = (x3,y3)
            if (p1<>p2 and p1<>p3 and p2<>p3) and \
               (not(x1==x2==x3)) and (not(y1==y2==y3)):
              a=d(p1,p2);b=d(p1,p3);c=d(p2,p3)
              
              #print ctr,":",p1,p2,p3,":",a,b,c

              L = [a,b,c]
              L = sorted(L)
              A = L[0];B=L[1];C=L[2]
              #print "A,B,C",A,B,C, A**2 + B**2 - C**2,round(abs(A**2 + B**2 - C**2),6)
              if round(abs(A**2 + B**2 - C**2),6)==0:
                ctr+=1
                print ctr,":",p1,p2,p3,":","A,B,C",A,B,C

print
print "Total # of Triangles for range (0,0),(2,2) is",ctr
           

