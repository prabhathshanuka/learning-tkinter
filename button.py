
from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look! I clicked a button")
    myLabel.pack()
    

#creating a button
myButton = Button(root, text = "click me!", padx=50, pady=25, command=myClick, bg= "#7fff0a")
#displaying button
myButton.pack()

root.mainloop()
