#  Euler Problem 1_49

def FiboNum(n):

  if n == 0: return 1

  FS1 = 0
  FS2 = 1
  Fibo = 1
  FiboBefore = 0

  #print 1,0
  print "F1",1

  for i in range( 1, n ):
    Fibo = FS1 + FS2
    FS1 = FS2
    FS2 = Fibo
    print "F"+str(i+1), Fibo
    if len(str(Fibo))==1000:
      print "Found it!"
      break

  return Fibo

if __name__ == "__main__":

  n=10000
  fn = FiboNum(n)
  print "\nSeq of ",n,"Fibonacci Numbers ends in", fn
  print