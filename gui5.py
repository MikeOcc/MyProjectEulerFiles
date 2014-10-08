#! % gui1.py &

from Tkinter import *
class HelloButton(Button):
    def __init__(self, parent = None, **config):
        Button.__init__(self, parent, config)
        self.pack()
        self.config(command=self.callback)
        self.msg = "6 thick"

    def callback(self):
        print "Later!"
        print self.msg
        self.quit()

if __name__ == '__main__':
    HelloButton(text = 'Bite me! subclass').mainloop()


#root = Tk()
#widget = Label(root)
#widfet.config(text = 'Look At the Bright Side of Life!')
#widget.pack(side=TOP, expand=YES, fill=BOTH)
#Button(root, text="Press Me!", command=root.quit).pack(side=TOP,expand=YES, fill=X)
#Button(root, text="No, Press Me!", command=root.quit).pack(side=TOP,expand=YES, fill=Y)
#root.title('Eat Me!')
#root.mainloop()
