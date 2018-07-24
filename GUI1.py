#1.
import tkinter as Tk
root = Tk.Tk()
root.title("dispalying a message")
l = Tk.Label(root,text="Hello!World")
b = Tk.Button(root,text="EXIT",command = root.destroy)
l.pack()
b.pack()
root.mainloop()

#2.
import tkinter as Tk
root = Tk.Tk()
def message():
    print("on click message")
bu = Tk.Button(root, text="CLICK", command=message)
bu.pack()
root.mainloop()
#4.
def type():
    global e
    string = e.get()
    print(string)

from tkinter import *
root = Tk()

root.title('Get text and print')

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='ENTER',command=type)
b.pack(side='bottom')
root.mainloop()