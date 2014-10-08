
# # 84246500
ctr = 0
for j in range(21061625*3,21061625*3+1):
  ctr = -4
  for i in range(0,j+1):
    #print i,j
    x = (j**2 - i**2)**.5
    if int(x)**2 == x**2:
      print i+j, x
      print -i+j, x
      print i+j, -x
      print -i+j, -x 
      ctr +=4
  
  #if ctr > 100: print j,ctr
  print j,ctr
  
  
# r  = 21061625
# r2 = 248431625
# tot = 0
# inc = 0
# lim = 10**11
# N=r2
# while True:
   # N += r2
   # inc +=1
   # if N > lim:
     # break 
   # tot += N
 
# print tot
   