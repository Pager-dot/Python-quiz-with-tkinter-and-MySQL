from tkinter import *
import time
root = Tk()

def timer(t):
    while t>0:
        lable_correct =Label(root,text= 9-5,font=('arial', 30))
        lable_correct.grid(column=2,row=2)
        lable_correct.after(1)
        #print(t)
        t= t-1
        time.sleep(1)
    a =Label(root,text="times up bitch!!" ,font=('arial', 30))
    a.grid(column=1,row=1)
timer(5)

#def tim():
#    a = Label(root,text="1")
#    a.grid(column=1,row=1)
#    a.destroy()
#    b = Label(root,text="2")
#    b.grid(column=1,row=1)


root.mainloop()






#def destroy2():
#    for widgets in lable.winfo_children():
#      widgets.destroy()
#lable = LabelFrame(root, text="this is my ",padx=200,pady=200)
#lable.pack()
#
#def correct():
#    Label(lable,text="True").grid(row=2,column=2)
#def quiz():
#    
#    button1=Button(lable, text="4", command=correct)
#    button1.grid(row=1,column=1)
#Label(lable, text="What is 2+2 ? ").grid(row=1,column=0)
#quiz()
#
#a = Button(root, text="destroy",command= destroy2)
#a.pack(padx=0,pady=0)