


n = 600851475143L    #/1837L
n = n/(59569)

#n= 71,839,1471
b = float(n)/2.0

n=6857L

print n

for i in range(2, 10000, 1):
  
  fact1 = n / i * i
  
  if fact1 == n:
      print "Factor is ", i, n, fact1
      break