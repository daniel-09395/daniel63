from tkinter import *
root=Tk()
v=IntVar()
v.set(0)
lang_list=[("python",0),("java",1),("c",2),("DOT nET",3),("PHP",4)]
def showchoice():
    print("you selected choice number:",v.get())
l=Label(root,text="select your favourite programming language:")
l.pack()
for txt,val in lang_list:
    r=Radiobutton(root, text=txt, variable=v, command=showchoice, value=val)
    r.pack()
