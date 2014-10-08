from operator import add 

def getPermutations(a): 
  if len(a)==1: 
    yield a 
  else: 

    for i in range(len(a)): 
      this = a 
      rest = a[:i] + a[i+1:] 

      for p in getPermutations(rest): 
        yield [this] + p 

index = 0 
for k in getPermutations(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]): 
  index += 1 
  if index == 100: 
    print k 
    break 