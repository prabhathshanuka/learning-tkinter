from cProfile import label
from tkinter import *
import time


root = Tk()
root.title("Time")
#root.iconbitmap(<path>)
root.geometry("400x200")

def cloak():
    hour = time.strftime("%I")
    minute =time.strftime("%M")
    second = time.strftime("%S")
    am_pm = time.strftime("%p")
    time_zone = time.strftime("%Z")

    my_label.config(text=hour + ":" + minute + ":" + second+" "+ am_pm)
    my_label.after(1000, cloak)
    my_label2.config(text=time_zone)
def update():
    my_label.config(text= "New Text")


my_label = Label(root, text="", font=("Helvetica", 48), fg = "green", bg= "black")
my_label.pack(pady=20)
my_label2 = Label(root, text="", font=("iskolapotha", 20))
my_label2.pack(pady=10)

cloak()

#my_label.after(5000, update)

root.mainloop()