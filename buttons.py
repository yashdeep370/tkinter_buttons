from tkinter import *

root = Tk()
root.geometry("655x333")

def hello():
    print("hello tkinter")
    
def name():
    print("yash deep")


fram = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
fram.pack(side=LEFT, anchor="nw")

b1 = Button(fram, fg="red", text="print now",command=hello)
b1.pack(side=LEFT)

b2 = Button(fram, fg="red", text="your name",command=name)
b2.pack(side=LEFT,padx=13)

b3 = Button(fram, fg="red", text="print now")
b3.pack(side=LEFT)

b4 = Button(fram, fg="red", text="print now")
b4.pack(side=LEFT)

root.mainloop()