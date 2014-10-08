
summ = 0 

from itertools import combinations,permutations

sq = [i*i for i in xrange(0,10)]

lst = []

x = combinations(sq,3)

for y in x:
  print y
  if sum(y)==144:
    print y

exit()




'''
for a in xrange(18):
  for b in xrange(10):
   for c in xrange(10):
    for d in xrange(10):
      for e in xrange(10):
        for f in xrange(10):
          for g in xrange(10):
            for h in xrange(10):
               for i in xrange(10):

                 x=81*a+64*b+49*c+36*d+25*e+16*f+9*g+4*h+i 
                 if a+b+c+d+e+f+g+h+i < 21 and int(x**.5)**2 == x:
                   print a+b+c+d+e+f+g+h+i,a,b,c,d,e,f,g,h,i,":", x
                   summ += x

'''
print
print summ
