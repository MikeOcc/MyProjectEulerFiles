


def f():

  n = 4
  
  t=(-2	,-1,1,1)
  x =1
  z = x**n + t[0]*x**(n-1) + t[1]*x**(n-2) + t[2]*x**(n-3) + t[3]
  
  print z
  
  x =2
  z = x**n + t[0]*x**(n-1) + t[1]*x**(n-2) + t[2]*x**(n-3) + t[3]
  
  print z  
  

# for a in [-1,1]:
  # for b in [-2,2]:
    # for c in [-3,3]:
      # for d in [-4,4]:
        # a1 = a + b + c + d
        # a2 = a*b + a*c + b*c +a*d +d*b +d*c
        # a3 = d*a*b + d*a*c + d*b*c + a*b*c
        # a4 = a*b*c*d
        # print (a,b,c,d),":",a1, a2, a3, a4
		
# for a in [3**.5]:
  # for b in [2**.5]:
    # for c in [2*3**.5]:
      # for d in [2*2**.5]:
        # a1 = a + b + c + d
        # a2 = a*b + a*c + b*c +a*d +d*b +d*c
        # a3 = d*a*b + d*a*c + d*b*c + a*b*c
        # a4 = a*b*c*d
        # print (a,b,c,d),":",a1, a2, a3, a4
Z=5
for a in range(-0,Z):
  for b in range(0,Z):
    for c in range(0,Z):
      for d in range(0,Z):
        a1 = -1*(a + b + c + d)
        a2 = 1*(a*b + a*c + b*c +a*d +d*b +d*c)
        a3 = -1*(d*a*b + d*a*c + d*b*c + a*b*c)
        a4 = a*b*c*d
        x1 = a**4 + a1*a**3 + a2*a**2 + a3*a + a4
        x2 = b**4 + a1*b**3 + a2*b**2 + a3*b + a4
        x3 = c**4 + a1*c**3 + a2*c**2 + a3*c + a4
        x4 = d**4 + a1*d**3 + a2*d**2 + a3*d + a4
        if x1==0:print (a,b,c,d),x1,x2,x3,x4,":",a1, a2, a3, a4