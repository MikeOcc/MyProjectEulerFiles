from Tkinter import *
from math import *

root = Tk()
frame = Frame(root, height = 200)

#class TestFrame(frame):
#    print "This is a test class"

class HelloButton(Button):
    def __init__(self, parent = None, **config):
        Button.__init__(self, parent, config)
        self.pack()
        self.config(command=self.callback)
        self.msg = "6 thick"

    def callback(self):
        print "Later!"
        print self.msg
        #self.printextra()
        self.quit()

    def printextra(self):
        print "This is more test text"

class Hello(Frame):
    def __init__(self, parent=None ):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_me_some_widgets()

    def make_me_some_widgets(self):
        widget1 = Button(self, text = "Calculate", command = self.message)
        widget1.pack(side = LEFT)
        widget2 = HelloButton(self, text = "Runaway", command = HelloButton.printextra)
        widget2.pack()
    def message(self):

        #self.data = self.data + 1
        #print "My big one is %s mm in circumference!" % self.data
        #if self.data > 130:
        #   print "Wow, that is a thick one!"

        n = 3.0
        targetnum = 1290 # 1314036 #7373170279853
        f1 = 0
        f2 = 0
        f3 = 0
        f4 = 0
        tnum =  int(round(pow(targetnum,(1.0/n)),5))
        tnumlast = int(round(pow(targetnum /4.0,(1.0/n)),5)) 
 
        numint = 0
        numsol = 0
        print "\n"
        print "We are slicing the following number into 4 or less cubes:", targetnum
        print "Initial number is ", tnum

        for f1 in range(tnum,tnumlast-1,-1):
            
            f2 = int(round(pow(int(targetnum - pow(f1,n)),(1.0/n)),5))
            #print "F1 * F1 * F1 is ", pow(f1,n), " F2 is ", f2
            tnum2 = int(ceil(f2))
              
            for f2 in range(tnum2,-1,-1):
                #print f1, f2, 1.0/n
                f3 = int(round(pow((targetnum - pow(f1,n) - pow(f2,n)),(1.0/n)),5))
                #print "F3 is ", f3
                tnum3 = int(f3)       
                
                
                for f3 in range(tnum3,-1,-1):            

                    tnum4 = int(round(pow(abs((targetnum - pow(f1,n) - pow(f2,n) - pow(f3,n))),(1.0/n)),5))
 
                    #print "tnum4", tnum4

                    for f4 in range(tnum4,-1,-1):
                        numint = numint + 1
                        tot = pow(f1,n) + pow(f2,n) + pow(f3,n) + pow(f4,n)
                        #print "Prelim totals",f1," ",f2," ",f3," ",f4, ": ",tot 

                        if tot == targetnum:
                            numsol = numsol + 1
                            print "The sum of the following cubes: ",f1,",",f2,",",f3,",",f4, '= ', tot
                            print "Finding these cubes took ", numint, " iterations!"
                            #break
                           
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            
            break
        
        #else:
        #    #continue
        #break    #    print "no sum of square exists", f1, f2, f2, f4

        if numsol == 0:
           print "No Solutions found with 4 factors or less"
        else:
           print "The Number of solutions is ", numsol



if __name__ == "__main__" :  Hello().mainloop()

