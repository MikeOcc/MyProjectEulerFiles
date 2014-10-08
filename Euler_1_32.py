# Find the sum of all products whose 
# multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.\\def 



def PanDig(n):
  nset = set(str(n))
  for m in range(1,10):   
    if str(m) not in nset: return False
  return True


if __name__ == '__main__':

  pandigprod = []
  for i in range(1,101):
    for j in range(60,2001):
      z = str(i)+str(j)+str(i * j)
      if not (len(z) == 9 and PanDig(z)):continue     
      #print i,j,i*j,":",z
      pandigprod.append(i*j)
  pandigprod = list(set(pandigprod))
  pandigprod.sort()
  sum1 = 0
  for k in pandigprod:
     print int(k)
     sum1 += int(k)

  print "Sum of pan dig products is ", sum1






