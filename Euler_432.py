

from Functions import RetFact

m = 510510
Phi1 = 92160

i = 2
sum = Phi1

while i < 1000000:
  if ((i%2==0) or (i%3==0) or(i%5==0) or(i%7==0) or(i%11==0) or(i%13==0) or(i%17==0)) :
    y = Phi1 * i
    #print i, y
    sum += y
	
  i +=1
	


print sum



#  209175442378852950     
	 
