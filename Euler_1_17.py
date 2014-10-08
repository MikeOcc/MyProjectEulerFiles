#
#
# [::-1]
#

from string import replace

 #ones=[('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')]


ones=("",'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
teens=('eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty')
tens=('twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','one hundred')
hundreds=('hundred')
thousands=('thousand')

TotNum = 0
x=0

for i in range(1,11):
   x = ones[i]
   TotNum += len(str(x))
   print x

for i in range(0,9):
   x = teens[i]
   TotNum += len(str(x))
   print x

for i in range(0,8):
  for j in range(0,10):
    x = tens[i] + " " +ones[j]
    TotNum += len(replace(str(x)," ",""))

    print x

print TotNum

print "_________________________"

for i in range(0,9):
  for j in range(0,10):
    for k in range(0,11):

      #print "ijk",i,j,k

      if j == 0:
        if k == 0:
          x= ones[i+1] + " hundred"
          TotNum += len(replace(str(x)," ",""))
          print x
        else:
          x = ones[i+1] + " hundred" +  " and " + ones[k]
          TotNum += len(replace(str(x)," ",""))
          print x  
      elif j == 1:
        if k>8:continue
        x = ones[i+1] + " hundred" + " and " + teens[k]
        TotNum += len(replace(str(x)," ",""))
        print x
      else:
        if k>9:continue
        x = ones[i+1] + " hundred" + " and " + tens[j-2] + " " +ones[k]
        TotNum += len(replace(str(x)," ",""))
        print x

x = "one thousand"
TotNum += len(replace(str(x)," ",""))
print x

print "_________________________"

print "The total number of characters in the words One to One Thousand is", TotNum 



exit()     




