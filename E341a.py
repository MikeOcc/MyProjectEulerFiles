#
#
#  Euler Problem 341 test.
#
#

x = 1
incr = 1
incr2 =1
bump = 0.0
flipflop = True
#hasdouble = false

for i in xrange(1,300):
  
    for j in range(1, incr+1):
      print j,x
    x+=1
     
    if incr2==incr:
       incr +=1
       incr2 = 1
    else:
       incr2 +=1