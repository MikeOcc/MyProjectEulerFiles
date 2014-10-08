#
#
#  Euler Problem 96
#
#
from string import strip

global p,g
p = []
g = []

def print_g():
  for row in xrange(9):
    for col in xrange(9):
      print g[row][col],
    print
  print

def print_p():
  for row in xrange(9):
    for col in xrange(9):
      print row,col,p[row][col]

def gen_nots_template():
  
  for row in xrange(9):
    for col in xrange(9):
       if g[row][col]>0:
          #print row,col
          p[row][col]=-1
       else:
          p[row][col]=range(1,10)

def count_not_0s():
  cnt = 0
  for row in xrange(9):
    for col in xrange(9):
      if g[row][col]!=0: cnt+=1
  return cnt

def search_rows_and_cols():

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
         l = p[row][col]
         for v in l:
           aortaken=True
           for k in xrange(9):
             if k==row:continue
             if g[k][col]==0:
               found_in_row=False
               for m in xrange(9):
                  if g[k][m]==v:found_in_row=True
               if found_in_row==False:
                  aortaken=False
                  break
           if aortaken == True:
              g[row][col]=v
              p[row][col]=-1 
              
              for i in xrange(9):
                if p[i][col]!=-1 and v in p[i][col]: 
                  t = p[i][col]
                  t.remove(v)   
                  p[i][col]=t

   search_4_certains()

   return


def gen_nots_by_row():

   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
         for i in xrange(9):
           if g[row][i] in p[row][col]: 
             t = p[row][col]
             t.remove(g[row][i])   
             p[row][col]=t
         for i in xrange(9):
           if g[i][col] in p[row][col]: 
             t = p[row][col]
             t.remove(g[i][col])   
             if t==[]:print "emptied!",row,col 
             p[row][col]=t

   search_4_certains()

   return

def gen_nots_by_quadrant():
   r,c=0,0
   for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
         
         if col<3:c=0
         elif col<6:c=3
         else: c=6

         if row<3:r=0
         elif row<6:r=3
         else: r=6

         for i in xrange(r,r+3):
           for j in xrange(c,c+3):
             if (i,j) == (row,col):
               #print "*",i,j,row,col,p[row][col]
               continue
             if g[i][j] in p[row][col]: 
               t = p[row][col]
               if len(t)==1:print row,col, p[row][col],t
               t.remove(g[i][j])

               if t==[]:print "emptied",i,j,row,col   
               p[row][col]=t

   search_4_certains()

   return

def search_4_certains():

  for row in xrange(9):
   for col in xrange(9):
     if p[row][col]!=-1 and len(p[row][col])==1:
        g[row][col]=p[row][col][0]
        p[row][col]=-1


def solve(g):

  cnt=[0]*10
  print # "cnt",cnt
  for row in xrange(9):
    for col in xrange(9):
       v=g[row][col]
       #print v
       cnt[v]+=1
  
  #print cnt 
  #print

  print_g()

  gen_nots_template()


  #print_p()

  
  # start solving by cycling thru different methods
  for z in xrange(8):
  
  
    while 1:
      num = count_not_0s()
      #print "a:",num
      gen_nots_by_row()
      #print
      #print_g()
      num2 = count_not_0s()
      if num2==num:
        break
      else:
        num=num2
        #print "b:",num

    #print_p()
    #print "****"

    ctr=1
    while 1:
      #print "ctr:",ctr
      num = count_not_0s()
      #print "a:",num
      gen_nots_by_quadrant()
      #print
      #print_g()
      num2 = count_not_0s()
      if num2==num:
        break
      else:
        num=num2
        #print "b:",num
      ctr+=1

    ctr=1
    while 1:
      #print "ctr:",ctr
      num = count_not_0s()
      #print "a:",num
      search_rows_and_cols()
      #print
      #print_g()
      num2 = count_not_0s()
      if num2==num:
        break
      else:
        num=num2
        #print "b:",num
      ctr+=1
    
    if count_not_0s() == 81:
      print "solved:"
      print
      print_g()
      print
      return g[0][0]*100+g[0][1]*10+g[0][2]

  print "unsolved:"
  print
  print_g()
  print  
  return 0
########

S = [ [ [idx for idx in range(50) ] for row in range(9)] for col in range(9)]

f = open('sudoku.txt','r')

Solved=[]
summ = 0

ctr=-1
ctr1=0
for x0 in f.readlines():
  #
  x = x0.strip()
  #print len(x0)
  #print x0
  if x[0]=="G":
   #print x
   ctr+=1
   ctr1=0
   continue
  else:
    for y in xrange(0,9):
      z = x[y]
      #print ctr,ctr1,y,z
      S[ctr1][y][ctr] = int(z)
    ctr1+=1

print
Sctr = 0
for i in xrange(50):

  g = [ [0 for z in range(9) ] for x in range(9)]
  p = [ [0 for z in range(9) ] for x in range(9)] 

  # extract puzzle from main array
  for row in xrange(9):
    for col in xrange(9):
       g[row][col] = S[row][col][i]

  print
  print "****************"
  print "Sudoku puzzle #",i+1
  print_g
  val = solve(g)
  if val>0:Sctr+=1;Solved.append(i+1)
  summ += val
  print
  print

print "number of puzzles solved is", Sctr
print "puzzle solved list is:",Solved
print "total sum of Sudoku subrows is", summ