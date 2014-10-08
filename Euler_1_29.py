
def multlist():
  plist =[]
  
  for a in range(2,101):
    for b in range(2,101):
       plist.append(a**b)
      # plist.append(b**a)
  
  print len(plist)
  
  #print len(set)
  
  plist=list(set(plist))
  plist.sort()
  print plist


  return len(plist)

if __name__ == '__main__':
  print multlist()
