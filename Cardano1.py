
#int CardanoTriplets1(int Max)

Max = 1000

count1 = 0;

for a in range(1,Max):     #Max(a = 1; a < Max; a++)
 
  for b in range(1, Max-a):   #(b = 1; b < Max - a; b++)

     for c in range(1, Max -a -b + 1):   #(c = 1; c <= Max - a - b; c++)

         if (8*a*a*a + 15*a*a + 6*a - 1) == 27*b*b*c:

            count1+=1


print "Cardano count is", count1