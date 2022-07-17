from tkinter import *
import tkinter
messageWindow= Tk()

messageWindow.title("İstanbul")
messageWindow.geometry("400x600")
messageWindow.resizable(width=False,height=False)
frame1 = Frame(messageWindow, width =400, height=100, relief = tkinter.FLAT)
frame1.pack(side=TOP, expand= True, fill=BOTH)
frame2 = Frame(messageWindow, width =400, height=500, relief = tkinter.FLAT)
frame2.pack(side=TOP, expand= True, fill=BOTH)
def goSearchBarButton():
    searchbarFrame = Frame(messageWindow,width =400, height=600, relief = tkinter.FLAT)
    searchbarFrame.place(x=0,y=0)
    nframe1 = Frame(searchbarFrame, width =400, height=100, relief = tkinter.FLAT)
    nframe1.pack(side=TOP, expand= True, fill=BOTH)
    nframe2 = Frame(searchbarFrame, width =400, height=500, relief = tkinter.FLAT, background="black")
    nframe2.pack(side=TOP, expand= True, fill=BOTH)
    def goBack():
        nframe1.destroy()
        nframe2.destroy()  ## here is the part im having trouble with
    backIcon1 = PhotoImage(file="backIcon.png")
    backIconButton1 = Button(nframe1,image=backIcon1, command= goBack)
    backIconButton1.image= backIcon1
    backIconButton1.place(x=0, y=14)

messageWindow.mainloop()