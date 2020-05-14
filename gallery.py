from tkinter import *

def printSomething():
    print("Hey whatsup bro, i am doing something very interresting.")

root = Tk()

button = Button(root, text="Print Me", command=printSomething)
button.pack()

root.mainloop()
