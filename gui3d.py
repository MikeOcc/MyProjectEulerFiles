#! % gui1.py &

from Tkinter import *


class HelloCallable:
    def __init__(self):
        self.msg2 = 'I have a thick one'
        self.girth = "6 inches"

    def __call__(self):
        print self.msg2
        print self.girth
        import sys; sys.exit()

widget = Button(None, text = 'Hello World', command = HelloCallable())
widget.pack()
widget.mainloop()


#root = Tk()
#widget = Label(root)
#widget.config(text = 'Look At the Bright Side of Life!')
#widget.pack(side=TOP, expand=YES, fill=BOTH)
#Button(root, text="Press Me!", command=root.quit).pack(side=TOP,expand=YES, fill=X)
#Button(root, text="No, Press Me!", command=root.quit).pack(side=TOP,expand=YES, fill=Y)
#root.title('Eat Me!')
#root.mainloop()
