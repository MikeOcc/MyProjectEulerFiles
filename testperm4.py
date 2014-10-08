


def permutations(li):


  if len(li) <= 1:
    yield li
  else:
    for el in li:
      for p in permutations([e for e in li if not e == el]):
        yield [el] + p


if __name__ == '__main__':

   x=list( "ABCDEFGHIJK")
   ctr = 1
   for p in permutations(x):
     ctr+=1
     print p
     if ctr > 100:break