from tkinter import *
root=Tk()
def var_states():
    print("hobby 1:%d,\nHobby 2:%d, \nHobby 3:%d"%(var1.get(),var2.get(), var3.get()))

var1=IntVar()
c1=Checkbutton(root, text="hobby 1", variable=var1)

var2=IntVar()
c2=Checkbutton(root, text="hobby 2", variable=var2)
b=Button(root, text="show", command=var_states)

var3=IntVar()
c3=Checkbutton(root, text="hobby 3", variable=var3)

c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)
b.pack(side=LEFT)
