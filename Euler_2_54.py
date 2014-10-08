#
#  Who wins the most poker hands in poker.txt
#
#
from string import *
from time import time

st = time()

f = open("poker.txt","r")

x=f.readlines()

'''
for hands in x:
  print hands
  print "*",len(hands),type(hands)

exit()
'''

total = 0

uc = {"T":10,"J":11,"Q":12,"K":13,"A":14}
suit = {"S":4,"H":3,"D":2,"C":1}

ctr = 0


for hands in x:
  hand1 = list(replace(hands[:14]," ",""))
  hand2 = list(replace(hands[14:29]," ",""))
  ctr+=1
  print
  print ctr,hand1, hand2

  isHC = False
  isOnePair = False
  isTwoPairs = False
  isStraight = False
  isFlush = False
  isFullHouse = False
  is3Kind = False
  is4Kind = False
  isStFlush = False
  isRoyalFlush = False

  isHC2 = False
  isOnePair2 = False
  isTwoPairs2 = False
  isStraight2 = False
  isFlush2 = False
  isFullHouse2 = False
  is3Kind2 = False
  is4Kind2 = False
  isStFlush2 = False
  isRoyalFlush2 = False

  OnePairVal = 0
  OnePairVal2 = 0
  OnePairNextHigh = 0
  OnePairNextHigh2 = 0

  HCVal = 0
  HCVal2 = 0
  HCNextHigh = 0
  HCNextHight2 = 0

  HR = []

  rank1 = []
  suit1 = []
  rank2 = []
  suit2 = []

  print "*********"
 
  for i in xrange(10):
    if i%2==0:
      if hand1[i] in "TJQKA":
        rank1.append(uc[hand1[i]])
      else:
        rank1.append(int(hand1[i]))
    else:
      suit1.append(suit[hand1[i]])
  
  rank1 = sorted(rank1)

  print rank1,suit1
    
  for i in xrange(10):
    if i%2==0:
      if hand2[i] in "TJQKA":
        rank2.append(uc[hand2[i]])
      else:
        rank2.append(int(hand2[i]))
    else:
      suit2.append(suit[hand2[i]])
  rank2 = sorted(rank2)
  print rank2,suit2


  set1 = sorted(list(set(rank1)))
  len1 = len(set1)
  if len1 == 2:
    print "full house or 4 of a kind"
    for card in set1:
      if rank1.count(card) == 4: print "!!!!!"; is4Kind = True
      elif rank1.count(card) ==3: print "%%%%"; isFullHouse = True
  elif len1 == 3:
    print "Two Pair or 3 of a kind"
    for card in set1:
      if rank1.count(card) == 3: print "###";  is3Kind = True
      elif rank1.count(card) ==2: print "22222" ;  isTwoPairs = True  
  elif len1 == 4:
    print "One Pair"
    isOnePair = True
    for card in set1:
      if rank1.count(card) == 2: print "$$$"; OnePairVal = card 
  elif len1 == 5:
    print "High Card Rules"
    isHC = True
    HCVal = rank1[4]
    HCNextHigh = rank1[3]

  set2 = sorted(list(set(rank2)))
  len2 = len(set2)
  if len2 == 2:
    print "full house or 4 of a kind"
    for card in set2:
      if rank2.count(card) == 4: print "!!!!!"; is4Kind2 = True
      elif rank2.count(card) ==3: print "%%%%"; isFullHouse2 = True
  elif len2 == 3:
    print "Two Pair or 3 of a kind"
    for card in set2:
      if rank2.count(card) == 3: print "###"; is3Kind2 = True
      elif rank2.count(card) ==2: print "22222"; isTwoPairs2 = True 
  elif len2 == 4:
    print "One Pair"
    isOnePair2 = True
    for card in set2:
      if rank2.count(card) == 2: print "$$$"; OnePairVal2 = card 
  elif len2 == 5:
    print "High Card Rules"
    isHC2 = True
    HCVal2 = rank2[4]
    HCNextHigh2 = rank2[3]


  isFlush = (len(set(suit1))==1)
  isStraight = (len(set(rank1))==5 and sum(rank1)==(rank1[0]+rank1[4])*5/2 and rank1[0]+4==rank1[4])
  print isFlush,isStraight
  print len(set(rank1))

  isFlush2 = (len(set(suit2))==1)
  isStraight2 = (len(set(rank2))==5 and sum(rank2)==(rank2[0]+rank2[4])*5/2 and rank2[0]+4==rank2[4])
  print isFlush2,isStraight2
  print len(set(rank2))

  # check for four of a kind
  # No four of a kinds in the list, so not coded

  # check for full house
  if isFullHouse and not isFullHouse2: total +=1;print "Full House wins";continue
  if isFullHouse2 and not isFullHouse: continue

  # check for flush
  if isFlush and not isFlush2: total +=1;print "Flush wins";continue
  if isFlush2 and not isFlush: continue

  # check for straight
  if isStraight and not isStraight2: total +=1;print "Straight wins";continue
  if isStraight2 and not isStraight: continue

  # check for 3 of a kind
  if is3Kind: total +=1;print "Three of a kind wins";continue
  if is3Kind2: print "Three of a kind 2d hand wins";continue
 
  # check for 2 pairs
  if isTwoPairs and not isTwoPairs2: total +=1;print "Two Pair wins";continue
  if isTwoPairs2 and not isTwoPairs: print "Two Pair 2d hand wins";continue

  # check for 1 pair
  if isOnePair and not isOnePair2: total +=1;print "One Pair wins";continue
  if isOnePair2 and not isOnePair: print "One Pair 2d hand wins";continue
  # check when each hand has 1 pair
  if isOnePair and isOnePair2:
    if OnePairVal > OnePairVal2:
       total +=1; print "Higher Pair wins";continue
    elif OnePairVal == OnePairVal2: print "YO YO";continue    # no one pair match, no need to check further

  #HCVal = 0
  #HCVal2 = 0
  #HCNextHigh = 0
  #HCNextHight2 = 0
    
  if isHC:
    if HCVal > HCVal2:total+=1;print "High Card Wins";continue
    elif HCVal == HCVal2 and HCNextHigh > HCNextHight2:total+=1;print "High Card Plus Second Wins";continue


  '''
  if len(set(rank1)) < len(set(rank2)): total +=1;print "Higher number of same card wins";continue

  if len(set(rank1)) == len(set(rank2)) and len1 == 2: total+=(rank1[3]==rank2[3] and rank1[2]>rank2[2]) ;print "!!!"
  if len(set(rank1)) == len(set(rank2)) and len1 == 2: total+=rank1[3]>rank2[3] ;print "!!!"


  if len(set(rank1)) == len(set(rank2)) and len1 == 1: total+=(rank1[4]==rank2[4] and rank1[3]>rank2[3]) ;print "!!!"
  if len(set(rank1)) == len(set(rank2)) and len1 == 1: total+=rank1[4]>rank2[4] ;print "!!!"


  if len(set(rank1)) == len(set(rank2)): total+= max(rank1)>max(rank2);print "!!!"
  '''
  print "*********"  
  print

  #exit()
  
  
print "total # of hands won by player one is", total
print "process time is", time()-st