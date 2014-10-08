from Tkinter import *

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
        self.data = self.data + 1
        print "My big one is %s mm in circumference!" % self.data
        if self.data > 130:
           print "Wow, that is a thick one!"

if __name__ == "__main__" :  Hello().mainloop()

