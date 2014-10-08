

def num_days_year(nyear):
     if is_leap_year(nyear):
       return 366
     else:
       return 365

     return 365

def is_leap_year(nyear):

     leapyear = False

     if nyear%4 ==0:
        leapyear = True

     if nyear%100 == 0:
        leapyear = False

     if nyear%400 == 0:
        leapyear = True

     return leapyear


def first_day_of_year(nyear):
 
     num_days = 0
     first_day = 1
     for i in range(1900,nyear):
        num_days += num_days_year(i)
        
     first_day = num_days%7 + 1

     return first_day

if __name__ == '__main__':
   
     mlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     m2list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

     dowlist = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
     moylist = ["January","February","March","April","May","June","July","August","September","October","November","December"]
     numsuns = 0
     n2 = 0,

     firstyear = 1901
     lastyear = 2001

     for j in range(1901,2001):
         print "Year", j
         n2=0
         fday = first_day_of_year(j)

         if fday == 7 or fday ==0: numsuns = numsuns + 1
         print fday
         print "The first day of Year", j, "is", dowlist[fday]   #fday
         d2d = 0
         if is_leap_year(j)==True:
           ulist = m2list
         else:
           ulist = mlist
         for k in range(0,11):
           d2d = d2d + ulist[k]
           nextdayofmonth = (fday + d2d)%7   #mlist[]
           if nextdayofmonth==0: 
              numsuns+=1
              n2=n2+1
           print k+2,d2d, nextdayofmonth
         print "number of sundays in Year ", j, "is" ,n2
           
     print "The number of Sundays that fall on the first day of the month from ",firstyear, "to", lastyear, " is" , numsuns

