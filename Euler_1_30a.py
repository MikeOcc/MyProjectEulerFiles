i,answer = 1,0 
while i<999999: 
  if sum(int(j)**5 for j in str(i)) == i: 
    print i
    answer += i    
  i += 1 


print answer