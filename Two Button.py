from tkinter import *
root=Tk()
root.title("harsh")
def callback():
    print("clicl!")
button1=Button(root, text="one", command=callback, bg="red", fg="green")
button2=Button(root, text="two", command=callback, bg="red", fg="green")

w=root.winfo_screenwidth()
h=root.winfo_screenheight()
print("screen width:",w)
print("screen height:",h)
root.geometry(str(w)+ "x" + str(h))

button1.place(x=200,y=200)
button2.place(x=500,y=500)
