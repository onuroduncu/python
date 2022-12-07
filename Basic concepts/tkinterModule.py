#import tkinter
#or
from tkinter import * #this is preventing tkinter. writing

def Hello():
    print('Hello World')

window = Tk() #create window

window.title("New Application") #name of application
b1 = Button(window, text= "Click on",state=DISABLED,borderwidth=20) #it cannot visible
b2 = Button(window, text= "Click on",command=Hello,bg='#FFD733',fg='green',borderwidth=8) #it cannot visible #hexadecimal color palette
#b1. pack() #this show the button
#b2.pack()

#direction
#b1.pack(padx=20,pady=30)
#b2.pack(padx=15,pady=10)

#create label
l = Label(window,text="Hello World",bg='yellow',fg='red')
l.pack()
b1.pack(side=LEFT,padx=5)
#b2.pack(side=RIGHT)

#or
b2.place(x=150,y=100,width=100,height= 50) #pixel 

#window.iconbitmap('Pictures/py.png') #favicon
window.mainloop() #prevent close the window
