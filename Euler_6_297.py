#
#
#  Euler 297
#
#

def F():
    a,b = 0,1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

def SubFib(startNumber, endNumber):
    for cur in F():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

f=[1]
for i in SubFib(2, 10**6):
  f.append(i)
  if i> 10**17: break  
  #print i

print f
print len(f)

skip =2
summ=0
summ2=0
for i in xrange(0,30,skip):
  summ+=1
  summ2+=summ	
  if summ>10**6:
    summ-= 1
    break


print summ
print summ2