#The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
#in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
#which is correct, is obtained by cancelling the 9s.
#
#We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
#There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator 
#and denominator.
#
#If the product of these four fractions is given in its lowest 
#common terms, find the value of the denominator.
#

dset = []

for i in range(10,101):
  for j in range(10,i-1):

    if i%10==0 or j%10==0: continue

    #dset.append()

    jstr=str(j)
    istr=str(i)

    cmp = float(j)/float(i)    

    n1 = float(jstr[0])
    n2 = float(jstr[1])

    d1 = float(jstr[0])
    d2 = float(jstr[1])

    if n1/d2 == cmp: print j,i,n1,d2,cmp
    if n2/d1 == cmp: print j,i,n2,d1,cmp

 
 #   print j,i,j/i,float(j)/float(i)






