# from ctypes import sizeof
from tkinter import *
from tkinter.ttk import Sizegrip
from typing import Sized
from PIL import Image,ImageTk
from tkinter import font
import data

root = Tk()

formap = Frame(root)
forlogin = Frame(root)
startFrame = Frame(root)
root.geometry("1200x600")
root.title("Best Journy for You")
font1 = font.Font(family='Georgia', size='22', weight='bold')
# def sta_Fra():
#     bt3 = Button(startFrame,text="Login",command=to_login).place(x=550,y=550)
#     startFrame.pack(fill="both",expand=1)
def get_val():
    print(f"{namevalue1.get(),namevalue2.get()}")
    print(data.datacheck(namevalue1.get(),namevalue2.get()))
def to_map():
    # image1 = Image.open("C:\map1.jpg")
    # photo = ImageTk.PhotoImage(image1)
    label1 = Label(formap,image=photo)
    label1.pack()
    name1 = Label(formap, text="From").place(x=750,y=425)
    name2 = Label(formap, text="TO").place(x=750,y=450)

    nameentry1 = Entry(formap, textvariable=namevalue1).place(x=800,y=425)
    nameentry2 = Entry(formap, textvariable=namevalue2).place(x=800,y=450)
    # nameentry.pack()
    btn1 = Button(formap,text="Start Your Journy",fg="red",relief=SUNKEN,bg="gray",command=get_val).place(x=800, y=525)
    formap.pack(fill='both', expand=1)
    forlogin.pack_forget()
    
    
def to_login():
   btn2 = Button(forlogin, text="Next", command=to_map,fg="red",relief=SUNKEN).place(x=550,y=525)
   forlogin.pack(fill='both', expand=1)
   formap.pack_forget()
  

image1 = Image.open("C:\map1.jpg")
photo = ImageTk.PhotoImage(image1)
image2 = Image.open("C:\image1.jpg")
photo1 = ImageTk.PhotoImage(image2)
namevalue1 = StringVar()
namevalue2 = StringVar()
# label1 = Label(formap, text="Hey ", foreground="green3",image=photo)
# label1 = Label(formap,image=photo)
# label1.pack()
label2 = Label(forlogin,foreground="blue",image=photo1)
label2.pack()
# sta_Fra()
to_login()
# to_map()

root.mainloop()
