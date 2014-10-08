f = x = 0 
i = 1 
while (f <= 500): 
  x = x + i 
  i = i + 1 
  f = 2 
  if (x == 1): #just being anal :) 
    f = 1 
    a = 1 
    j = 0 
    y = x 
while (y > 1): 
  k = 1 
  while (x%(int(L[j])**k) == 0): 
    k = k + 1 
    if (x%(int(L[j])) == 0): 
      a = a * k 
      y = y/(int(L[j])**(k-1)) 
      j = j + 1 
      if (a > f): 
         f = a 
         print x,f 