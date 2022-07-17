from tkinter import *
root = Tk()
def correct():
    Label(root,text="True").grid(row=2,column=2)
def quiz():
    
    button1=Button(root, text="4", command=correct)
    button1.grid(row=1,column=1)
Label(root, text="What is 2+2 ? ").grid(row=1,column=0)



quiz()
root.mainloop()