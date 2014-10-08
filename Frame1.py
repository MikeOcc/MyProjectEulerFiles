from Tkinter import *

root = Tk()
frame = Frame(root, height = 100)
frame.pack()

def test1():
  print "This is a Test"

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", bg="red", command = test1)
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black", command = exit)
blackbutton.pack( side = BOTTOM)

root.mainloop()