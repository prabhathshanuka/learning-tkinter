
from tkinter import *

root = Tk()

e = Entry(root, width= 100, bg="#ff3430", fg="#f0f0f0", borderwidth=5)
e.insert(0,"Enter Your Name: ")
e.pack()


def myClick():
    hello = "Welcome " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    

#creating a button
myButton = Button(root, text = "Enter your Name", padx=50, pady=25, command=myClick, bg= "#7fff0a")
#displaying button
myButton.pack()

root.mainloop()
