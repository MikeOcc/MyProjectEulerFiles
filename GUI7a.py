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
        widget1 = Button(self, text = "Grab my Big One", command = self.message)
        widget1.pack(side = LEFT)
        widget2 = HelloButton(self, text = "Runaway", command = HelloButton.printextra)
        widget2.pack()
    def message(self):
        #self.data = self.data + 1
        #print "My big one is %s mm in circumference!" % self.data
        #if self.data > 130:
        #   print "Wow, that is a thick one!"

        targetnum = 8000
        f1 = 0
        f2 = 0
        f3 = 0
        f4 = 0
        tnum =  int(sqrt(targetnum))
        f1 = tnum 
        print "initial number is ", tnum
        for f1 in range(tnum,1,-1):
            
            f2 = sqrt(int(targetnum - (f1*f1)))
            #print "F1 * F1 is ", f1*f1, " F2 is ", f2
            tnum2 = int(f2)
            print "F1 * F1 is ", f1*f1, " F2 is ", f2, " tnum2 is ", tnum2
              
            for f2 in range(0,tnum2+1,1):
                f3 = sqrt(targetnum - f1*f1 -f2*f2)
                print "F3 is ", f3
                tnum3 = int(f3)       
                
                for f3 in range(0,tnum3+1,1):            
                    
                    for f4 in range(0,10,1):
                        tot = pow(f1,2) + pow(f2,2) + pow(f3,2) + pow(f4,2)
                        print "Prelim totals",f1,f2,f3,f4,tot 

                        if tot == targetnum:
                            print f1,f2,f3,f4, 'squares =  ', tot,  targetnum
                            break
                           
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





if __name__ == "__main__" :  Hello().mainloop()

