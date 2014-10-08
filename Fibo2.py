i, j, term = 0, 1, 2 

while True: 
  fib = i+j 
  if len(str(fib)) >= 1000: 
    print term, ":", fib 
    break 
  i, j, term = j, fib, term+1 