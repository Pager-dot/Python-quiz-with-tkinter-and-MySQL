from logging import root
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import pickle

root =Tk()
root.title("Employee management system")
root.geometry('1300x1000')

def Exit1():
    res=tkinter.messagebox.askquestion(message="Do you want to EXIT")
    if res=="yes":
        root.destroy()
def ClearFrame():
    for widget in F2.winfo_children():
        widget.destroy()
q
root.mainloop()
