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
      print "Z:",row,col,p[row][col]

def check_row(n,cur_row):
  for col in xrange(9):
    #print "GCRC:",n,cur_row,col
    #print "tt", type(cur_row),type(col)	
    if g[cur_row][col] == n: return True
  return False

def check_col(n,cur_col):
  for row in xrange(9):
     if g[row][cur_col] == n: return True
  return False
  

def examine_square(r,c):

  if r != 8 or c!=0: return

  print
  
  r1,c1=[],[]
  if (c+1)%3 == 1:
    c1=[c+1,c+2]
  elif (c+1)%3 ==2:
    c1=[c-1,c+1]
  else:
    c1=[c-2,c-1]

  if (r+1)%3 == 1:
    r1=[r+1,r+2]
  elif (r+1)%3 ==2:
    r1=[r-1,r+1]
  else:
    r1=[r-2,r-1]	
  
  for v in p[r][c]:
    #print "RCV", r, c, v
    a1 = check_row(v,r1[0])
    a2 = check_row(v,r1[1])  

    a3 = check_col(v,c1[0])     # 
    a4 = check_col(v,c1[1])
    if r==8 and c==0 and v==6 :
      print "r:", r, r1[0], r1[1]
      print "c:", c, c1[0], c1[1]
      print "a1,a2,a3,a4:",a1,a2,a3,a4
      
    #if r==8:
    # row 8, col 0
    #if a1 and p[r1[1]][c1[0]]== -1: a3=True
    if a2 and p[r1[0]][c1[1]]== -1: a4=True
    if a3 and p[r1[0]][c1[1]]== -1: a1=True
    #if a4 and p[r1[0]][c1[1]]== -1: a2=True
    if r==8 and c==0 and v==6 :
      print "#######",r,c
      print 0,0,r1[0],c1[0],p[r1[0]][c1[0]]
      print 0,1,r1[0],c1[1],p[r1[0]][c1[1]]
      print 1,0,r1[1],c1[0],p[r1[1]][c1[0]]
      print 1,1,r1[1],c1[1],p[r1[1]][c1[1]]
      print "!!!!!!!!!!!",r,c,a1,a2,a3,a4
    if a1 and a2 and a3 and a4:
      print "hit!!!!!!!!!!!!!r",r,"C",c,v
      g[r][c]=v
      p[r][c]=-1
      for x in range(9):
        z=p[r][x]
        if type(z)==int:continue
        if v in z:
          z.remove(v)
          p[r][x]=z
          if z==[]: p[r][x]=-1		  
      for y in range(9):
        z=p[y][c]
        if type(z)==int:continue
        if v in z:
          z.remove(v)
          p[y][c]=z
          if z==[]: p[y][c]=-1		    
      break
     
  return
	  
def examine_board():
  for row in xrange(9):
    for col in xrange(9):
      if p[row][col]!=-1:
        examine_square(row,col)
  return
  
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
              print "Found:",row,col,v
              g[row][col]=v
              p[row][col]=-1 
              
              for ii in xrange(9):
                if p[ii][col]!=-1 and v in p[ii][col]: 
                  t = p[ii][col]
                  t.remove(v)   
                  p[ii][col]=t

              for ii in xrange(9):
                if p[row][ii]!=-1 and v in p[row][ii]: 
                  t = p[row][ii]
                  t.remove(v)   
                  p[row][ii]=t
				  
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
        #print "bazinga!", row , col


def solve(g,zz):

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

    if z==0:print_p()
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
    if z==0:print_p()

    if zz==14:
      print
      print_g()
    ctr=1

    while 1 and z>4:
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

    examine_board()
	  
    if zz==14:
      print
      print_g()
    
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

S = [ [ [idx for idx in range(51) ] for row in range(9)] for col in range(9)]

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
for i in xrange(1,2) :       #51):

  g = [ [0 for z in range(9) ] for x in range(9)]
  p = [ [0 for z in range(9) ] for x in range(9)] 

  # extract puzzle from main array
  for row in xrange(9):
    for col in xrange(9):
       g[row][col] = S[row][col][i]

  #if i<50:continue
  print
  print "****************"
  print "Sudoku puzzle #",i+1
  #print_g()
  val = solve(g,i)
  if val>0:Sctr+=1;Solved.append((i+1,val))
  summ += val
  print
  print

print "number of puzzles solved is", Sctr
print "puzzle solved list is:",Solved
print "total sum of Sudoku subrows is", summ