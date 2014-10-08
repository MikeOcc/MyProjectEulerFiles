#! % gui1.py &

from Tkinter import *

def quit():
   print 'Hello, I must be going'
   import sys; sys.exit()


root = Tk()
widget = Label(root)
#widget.config(text = 'Look At the Bright Side of Life!')
widget.pack(side=TOP, expand=YES, fill=BOTH)
Button(root, text="Press Me!", command=root.quit).pack(side=TOP,expand=YES, fill=X)
#Button(root, text="No, Press Me!", command=root.quit).pack(side=TOP,expand=YES, fill=Y)
root.title('Eat Me!')
root.mainloop()
