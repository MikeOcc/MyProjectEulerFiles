
from Tkinter import *

#root = Tk()

class GUI(Frame):
    def __init__(self, parent=None, **config):
        self.root = Tk()
        self.root.title('Frame Styles')
        for bdw in range(5):
            setattr(self, 'of%d' % bdw, Frame(self.root, borderwidth=0))
            Label(getattr(self, 'of%d' % bdw),text='borderwidth = %d  ' % bdw).pack(side=LEFT)

            ifx = 0

            for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
                setattr(self, 'f%d' % ifx, Frame(getattr(self, 'of%d' % bdw),  borderwidth=bdw, relief=relief))

                Button(getattr(self, 'f%d' % ifx), text=relief, width=10).pack(side=LEFT)

                getattr(self, 'f%d' % ifx).pack(side=LEFT, padx=7-bdw, pady=5+bdw)        

                ifx = ifx+1
                #Button(getattr(self),  text = "Grab my Big One", command = exit).pack(side=BOTTOM)          
                getattr(self, 'of%d' % bdw).pack()  
                
#widget1.pack()      

myGUI = GUI()
myGUI.root.mainloop()