    #Simple Python Quiz with Tkinter and Mysql
#module used in the program(tkinter and mysql connector for GUI
#and using database for recording and totaling quiz marks)
from tkinter import *
from PIL import Image
from PIL import ImageTk
import mysql.connector

#creating timer 
counter = 6 
def timer(timer_Count):
  def count():
    global counter
    counter -= 1
    if counter == -1:
        counter = 5
    else:
        timer_Count.config(text=str(counter))
        timer_Count.after(1000, count)
    return
  count()

#connecting to Mysql 
mydb = mysql.connector.connect(host="localhost",
                                user="root",
                                passwd="paritosh")
my_cursor = mydb.cursor()
my_cursor.execute("Drop DATABASE IF EXISTS quizmarks")
my_cursor.execute("CREATE DATABASE IF NOT EXISTS quizmarks")
my_cursor.execute("use quizmarks")
my_cursor.execute("CREATE TABLE marks (Question int,marks int)")

#Creating GUI for quiz
root = Tk()
root.title('Python Quiz with Tkinter and Mysql')
root.configure(background = "#f04d75")
root.minsize(height= 700,width=900)
quiz_img = Image.open('Logo.png')
render = ImageTk.PhotoImage(quiz_img)
img =Label(root,image=render,background= "#f04d75")
img.place(x=310,y=80)

#Greetings tab
def Start_tab():

    global title
    title = Label(root,text="To Play Press Start", font=('arial',40),bg= '#f04d75',fg="white")
    title.pack(side=TOP)
    global start_button
    start_button= Button(root,text="Start",command=tab1,\
         font=('arial', 35),height= 1, width=8)
    start_button.place(x=350,y=420)

#fist question
def tab1():
    img.destroy()
    title.destroy()
    start_button.destroy()
    #defining a function to print true if option is correct
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial', 30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        #disabling the buttons to comfim the user choice
        button1['state']=DISABLED
        button2['state']=DISABLED
        button3['state']=DISABLED

        #inserting value as 1 for question 1 to the table 
        #if the option is correct
        my_cursor.execute("insert into marks values(1,1)")
        mydb.commit()

    #defining a function to print false if option is not correct
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial', 30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        #disabling the buttons to comfim the user choice
        button1['state']=DISABLED
        button2['state']=DISABLED
        button3['state']=DISABLED

        #inserting value as 0 for question 1 to the table 
        #if option is not correct
        my_cursor.execute("insert into marks values(1,0)")
        mydb.commit()

    # To display the question
    global label1
    label1 = Label(root,text = '''Which of the following is the correct way
    to assign a number to a variable? ''', font=('arial',25),bg= '#f04d75',fg="white")
    label1.pack()
    
    #buttons(option)
    global button1
    button1=Button(root, text="var = 8", command= correct ,\
     font=('arial',20),height= 2, width=6)
    button1.place(relx=0.1,rely=0.4)
    global button2
    button2=Button(root, text="var = '8'", command=Not_correct,\
        font=('arial', 20),height= 2, width=6)
    button2.place(relx=0.4,rely=0.4)
    global button3
    button3=Button(root, text="var == 8", command= Not_correct,\
        font=('arial', 20),height= 2, width=6)
    button3.place(relx=0.7,rely=0.4)

    #skip button(to move to next question)
    global button4
    button4 = Button(root,text = 'Skip', command= tab2 ,font=('arial', 20))
    button4.pack(side= BOTTOM)
    button4.after(5000,tab2)
    
    #calling the timer
    global timer_Count
    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#redefining the Lable from correct and Not_correct funtion 
#as to move to next question 
#lable should be defined in order to remove the output from the lable
lable_correct =Label(root)
lable_incorrect =Label(root)

#Question2
def tab2():
    
    #destroying the lable and previous buttons 
    #to see and choose the question and option
    lable_correct.destroy()
    lable_incorrect.destroy()
    label1.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()
    button4.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),fg="white",bg= '#f04d75')
        lable_correct.place(relx=0.44,rely=0.79)
        button5['state']=DISABLED
        button6['state']=DISABLED
        button7['state']=DISABLED
        my_cursor.execute("insert into marks values(2,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False", font=('arial',30),fg="white",bg= '#f04d75')
        lable_incorrect.place(relx=0.44,rely=0.79)
        button5['state']=DISABLED
        button6['state']=DISABLED
        button7['state']=DISABLED
        my_cursor.execute("insert into marks values(2,0)")
        mydb.commit()
    global label2
    label2 = Label(root,text = '''Which of the following is the correct output
    on running the below code in python ?

    print("The output is : ")

    print('"Hello world") ''', font=('arial',25),bg= '#f04d75',fg="white")
    label2.pack()
    global button5
    button5=Button(root, text='''The output is :
    Hello!''', command= Not_correct ,font=('arial', 20),height= 3, width=12)
    button5.place(relx=0.1,rely=0.5)
    global button6
    button6=Button(root, text="Syntax error", command=Not_correct,\
        font=('arial', 20),height= 3, width=12)
    button6.place(relx=0.4,rely=0.5)
    global button7
    button7=Button(root, text='''None of the 
    above''', command= correct,font=('arial', 20),height= 3, width=12)
    button7.place(relx=0.7,rely=0.5)
    global button8
    button8 = Button(root,text = 'Skip' , command= tab3\
        ,font=('arial', 20))
    button8.pack(side= BOTTOM)
    button8.after(5000,tab3)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)
    
#Question3
def tab3():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label2.destroy()
    button5.destroy()
    button6.destroy()
    button7.destroy()
    button8.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.45,rely= 0.65)
        button9['state']=DISABLED
        button10['state']=DISABLED
        button11['state']=DISABLED
        my_cursor.execute("insert into marks values(3,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False", font=('arial',30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button9['state']=DISABLED
        button10['state']=DISABLED
        button11['state']=DISABLED
        my_cursor.execute("insert into marks values(3,0)")
        mydb.commit()
    global label3
    label3 = Label(root,text = "What do 'R' and 'E' mean in 'REPL'",\
        font=('arial',25),bg= '#f04d75',fg="white")
    label3.pack()
    global button9
    button9=Button(root, text="Run and Enter", command= Not_correct,\
        font=('arial', 20),height= 2, width=14)
    button9.place(relx=0.02,rely=0.4)
    global button10
    button10=Button(root, text="Read and Execute", command= correct,\
        font=('arial', 20),height= 2, width=14)
    button10.place(relx=0.35,rely=0.4)
    global button11
    button11=Button(root, text="Read and Enter", command= Not_correct,\
        font=('arial', 20),height= 2, width=14)
    button11.place(relx=0.68,rely=0.4)
    global button12
    button12 = Button(root,text = 'Skip' , command= tab4,font=('arial', 20))
    button12.pack(side= BOTTOM)
    button12.after(5000,tab4)
    
    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question4
def tab4():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label3.destroy()
    button9.destroy()
    button10.destroy()
    button11.destroy()
    button12.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button13['state']=DISABLED
        button14['state']=DISABLED
        button15['state']=DISABLED
        my_cursor.execute("insert into marks values(4,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial',30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button13['state']=DISABLED
        button14['state']=DISABLED
        button15['state']=DISABLED
        my_cursor.execute("insert into marks values(4,0)")
        mydb.commit()
    global label4
    label4 = Label(root,text = '''Which of the following is the correct way to print the 
    result of addition of 10 and 7 to get 17 ?''',font=('arial',25),bg= '#f04d75',fg="white")
    label4.pack()
    global button13
    button13=Button(root, text="print('10+7')", command= Not_correct,\
        font=('arial', 20),height= 2, width=10)
    button13.place(relx=0.1,rely=0.4)
    global button14
    button14=Button(root, text="print(10+7)", command= correct,\
        font=('arial', 20),height= 2, width=10)
    button14.place(relx=0.4,rely=0.4)
    global button15
    button15=Button(root, text="print('10'+'7')", command= Not_correct,\
        font=('arial', 20),height= 2, width=10)
    button15.place(relx=0.7,rely=0.4)
    global button16
    button16 = Button(root,text = 'Skip', command= tab5,\
        font=('arial', 20))
    button16.pack(side= BOTTOM)
    button16.after(5000,tab5)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question5
def tab5():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label4.destroy()
    button13.destroy()
    button14.destroy()
    button15.destroy()
    button16.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button17['state']=DISABLED
        button18['state']=DISABLED
        button19['state']=DISABLED
        my_cursor.execute("insert into marks values(5,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial',30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.44,rely= 0.65)
        button17['state']=DISABLED
        button18['state']=DISABLED
        button19['state']=DISABLED
        my_cursor.execute("insert into marks values(5,0)")
        mydb.commit()
    global label5
    label5 = Label(root,text = '''Which of the following prints the
    file name in he command line argument ?''',font=('arial',25),bg= '#f04d75',fg="white")
    label5.pack()
    global button17
    button17=Button(root, text="print(sys.argv[0])", command= correct,\
        font=('arial',20),height=2,width=14)
    button17.place(relx=0.02,rely=0.4)
    global button18
    button18=Button(root, text='''print("sys.argv[0]")''',\
        command= Not_correct,font=('arial',20),height=2,width=14)
    button18.place(relx=0.35,rely=0.4)
    global button19
    button19=Button(root, text="print(sys.argv[1])", command= Not_correct,\
        font=('arial',20),height=2,width=14)
    button19.place(relx=0.68,rely=0.4)
    global button20
    button20 = Button(root,text = 'Skip', command= tab6,font=('arial', 20))
    button20.pack(side= BOTTOM)
    button20.after(5000,tab6)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question6
def tab6():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label5.destroy()
    button17.destroy()
    button18.destroy()
    button19.destroy()
    button20.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button21['state']=DISABLED
        button22['state']=DISABLED
        button23['state']=DISABLED
        my_cursor.execute("insert into marks values(6,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial',30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button21['state']=DISABLED
        button22['state']=DISABLED
        button23['state']=DISABLED
        my_cursor.execute("insert into marks values(6,0)")
        mydb.commit()
    global label6
    label6 = Label(root,text = '''Which of the following variables stores 
    the arguments in the command line ?''',font=('arial',25),bg= '#f04d75',fg="white")
    label6.pack()
    global button21
    button21=Button(root, text="Arg", command= Not_correct,\
        font=('arial',20),height=2,width=3)
    button21.place(relx=0.1,rely=0.4)
    global button22
    button22=Button(root, text="agrc", command= Not_correct,\
        font=('arial',20),height=2,width=3)
    button22.place(relx=0.44,rely=0.4)
    global button23
    button23=Button(root, text="agrv", command= correct,\
        font=('arial',20),height=2,width=3)
    button23.place(relx=0.8,rely=0.4)
    global button24
    button24 = Button(root,text = 'Skip' , command= tab7,\
        font=('arial', 20))
    button24.pack(side= BOTTOM)
    button24.after(5000,tab7)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question7
def tab7():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label6.destroy()
    button21.destroy()
    button22.destroy()
    button23.destroy()
    button24.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button25['state']=DISABLED
        button26['state']=DISABLED
        button27['state']=DISABLED
        my_cursor.execute("insert into marks values(7,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial',30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.44,rely= 0.65)
        button25['state']=DISABLED
        button26['state']=DISABLED
        button27['state']=DISABLED
        my_cursor.execute("insert into marks values(7,0)")
        mydb.commit()
    global label7
    label7 = Label(root,text = '''Which of the following is the correct command 
    to exit from an interpreter in python ? ''',font=('arial',25),bg= '#f04d75',fg="white")
    label7.pack()
    global button25
    button25=Button(root, text="exit()", command= correct,\
        font=('arial',20),height=2,width=4)
    button25.place(relx=0.1,rely=0.4)
    global button26
    button26=Button(root, text="end()", command= Not_correct,\
        font=('arial',20),height=2,width=4)
    button26.place(relx=0.44,rely=0.4)
    global button27
    button27=Button(root, text="stop()", command= Not_correct,\
        font=('arial',20),height=2,width=4)
    button27.place(relx=0.75,rely=0.4)
    global button28
    button28 = Button(root,text = 'Skip' ,command= tab8,\
        font=('arial',20))
    button28.pack(side= BOTTOM)
    button28.after(5000,tab8)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question8
def tab8():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label7.destroy()
    button25.destroy()
    button26.destroy()
    button27.destroy()
    button28.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button29['state']=DISABLED
        button30['state']=DISABLED
        button31['state']=DISABLED
        my_cursor.execute("insert into marks values(8,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial',30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.44,rely= 0.65)
        button29['state']=DISABLED
        button30['state']=DISABLED
        button31['state']=DISABLED
        my_cursor.execute("insert into marks values(8,0)")
        mydb.commit()
    global label8
    label8 = Label(root,text = '''Which of these is not a core data type ?''',\
        font=('arial',25),bg= '#f04d75',fg="white")
    label8.pack()
    global button29
    button29=Button(root, text="Tuples", command= Not_correct,\
        font=('arial',20),height=2,width=9)
    button29.place(relx=0.1,rely=0.4)
    global button30
    button30=Button(root, text="Dictionary", command= Not_correct,\
        font=('arial',20),height=2,width=9)
    button30.place(relx=0.4,rely=0.4)
    global button31
    button31=Button(root, text="Class", command= correct,\
        font=('arial',20),height=2,width=9)
    button31.place(relx=0.7,rely=0.4)
    global button32
    button32 = Button(root,text = 'Skip' , command= tab9,\
        font=('arial',20))
    button32.pack(side= BOTTOM)
    button32.after(5000,tab9)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question9
def tab9():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label8.destroy()
    button29.destroy()
    button30.destroy()
    button31.destroy()
    button32.destroy()
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial',30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely=0.84)
        button33['state']=DISABLED
        button34['state']=DISABLED
        button35['state']=DISABLED
        my_cursor.execute("insert into marks values(9,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial',30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.44,rely=0.84)
        button33['state']=DISABLED
        button34['state']=DISABLED
        button35['state']=DISABLED
        my_cursor.execute("insert into marks values(9,0)")
        mydb.commit()
    global label9
    label9 = Label(root,text = '''Find the output of the following program:
    
    nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 

    pos = nameList.index("GeeksforGeeks") 

    print (pos * 3)''' ,fg="white", font=('arial',25),bg= '#f04d75')
    label9.pack()
    global button33
    button33=Button(root, text=''' ValueError: 
    'GeeksforGeeks'
    is not in list''', command= correct,height=6,width=15,font=('arial',20))
    button33.place(relx=0.02,rely=0.5)
    global button34
    button34=Button(root, text=''' Harsh
    Harsh
    Harsh''', command= Not_correct,height=6,width=15,font=('arial',20))
    button34.place(relx=0.36,rely=0.5)
    global button35
    button35=Button(root, text='''Harsh''', command= Not_correct,\
        height=6,width=15,font=('arial',20))
    button35.place(relx=0.7,rely=0.5)

    global button36
    button36 = Button(root,text = 'Skip' ,command= tab10,\
        font=('arial',20))
    button36.pack(side= BOTTOM)
    button36.after(5000,tab10)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question10
def tab10():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label9.destroy()
    button33.destroy()
    button34.destroy()
    button35.destroy()
    button36.destroy()
    
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",\
        font=('arial', 30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button37['state']=DISABLED
        button38['state']=DISABLED
        button39['state']=DISABLED
        
        my_cursor.execute("insert into marks values(10,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial', 30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button37['state']=DISABLED
        button38['state']=DISABLED
        button39['state']=DISABLED
        my_cursor.execute("insert into marks values(10,0)")
        mydb.commit()
    global label10
    label10 = Label(root,text = '''What is the output of the following program : 
    print (0.1 + 0.2 == 0.3) ''',font=('arial', 25),bg= '#f04d75',fg="white")
    label10.pack()
    global button37
    button37=Button(root, text="True", command= Not_correct,\
        font=('arial', 20),height= 2, width=6)
    button37.place(relx=0.1,rely=0.4)
    global button38
    button38=Button(root, text="False", command= correct,\
        font=('arial', 20),height= 2, width=6)
    button38.place(relx=0.41,rely=0.4)
    global button39
    button39=Button(root, text="Error", command= Not_correct,\
        font=('arial', 20),height= 2, width=6)
    button39.place(relx=0.73,rely=0.4)
    global button40
    button40 = Button(root,text = 'Skip' ,\
         command= tab11,font=('arial', 20))
    button40.pack(side= BOTTOM)
    button40.after(5000,tab11)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)

#Question11
def tab11():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label10.destroy()
    button37.destroy()
    button38.destroy()
    button39.destroy()
    button40.destroy()
    
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",\
        font=('arial', 30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button41['state']=DISABLED
        button42['state']=DISABLED
        button43['state']=DISABLED
        
        my_cursor.execute("insert into marks values(11,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial', 30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button41['state']=DISABLED
        button42['state']=DISABLED
        button43['state']=DISABLED
        my_cursor.execute("insert into marks values(11,0)")
        mydb.commit()
    global label11
    label11 = Label(root,text = '''    What is output of following code : 

    L = [1,2,6,5,7,8]
    L.insert(9)''',fg="white",font=('arial', 25),bg= '#f04d75')
    label11.pack()
    global button41
    button41=Button(root, text="Type Error", command= correct,\
        font=('arial', 20),height= 2, width=14)
    button41.place(relx=0.05,rely=0.4)
    global button42
    button42=Button(root, text="L=[1,2,6,5,7,8,9]", command= Not_correct,\
        font=('arial', 20),height= 2, width=14)
    button42.place(relx=0.36,rely=0.4)
    global button43
    button43=Button(root, text="L=[9,1,2,6,5,7,8]", command= Not_correct,\
        font=('arial', 20),height= 2, width=14)
    button43.place(relx=0.67,rely=0.4)
    global button44
    button44 = Button(root,text = 'Skip' ,\
        command=tab12, font=('arial', 20))
    button44.pack(side= BOTTOM)
    button44.after(5000,tab12)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)


#Question12
def tab12():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label11.destroy()
    button41.destroy()
    button42.destroy()
    button43.destroy()
    button44.destroy()
    
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",\
        font=('arial', 30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button45['state']=DISABLED
        button46['state']=DISABLED
        button47['state']=DISABLED
        
        my_cursor.execute("insert into marks values(12,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial', 30)\
        ,bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button45['state']=DISABLED
        button46['state']=DISABLED
        button47['state']=DISABLED
        my_cursor.execute("insert into marks values(12,0)")
        mydb.commit()
    global label12
    label12 = Label(root,text = '''What is the correct way to
    create a function in Python?''',font=('arial', 25),\
    fg="white",bg= '#f04d75')
    label12.pack()
    global button45
    button45=Button(root, text="function():", command= Not_correct,\
        font=('arial', 20),height= 2, width=14)
    button45.place(relx=0.05,rely=0.4)
    global button46
    button46=Button(root, text="def Function():", command= correct,\
        font=('arial', 20),height= 2, width=14)
    button46.place(relx=0.36,rely=0.4)
    global button47
    button47=Button(root, text="create Function():", command= Not_correct,\
        font=('arial', 20),height= 2, width=14)
    button47.place(relx=0.67,rely=0.4)
    global button48
    button48 = Button(root,text = 'Skip' ,\
        command=tab13, font=('arial', 20))
    button48.pack(side= BOTTOM)
    button48.after(5000,tab13)
    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)


#Question13
def tab13():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label12.destroy()
    button45.destroy()
    button46.destroy()
    button47.destroy()
    button48.destroy()
    
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",\
        font=('arial', 30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button49['state']=DISABLED
        button50['state']=DISABLED
        button51['state']=DISABLED
        
        my_cursor.execute("insert into marks values(13,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",\
        font=('arial', 30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button49['state']=DISABLED
        button50['state']=DISABLED
        button51['state']=DISABLED
        my_cursor.execute("insert into marks values(13,0)")
        mydb.commit()
    global label13
    label13 = Label(root,text = '''Which of these collections defines a SET?''',\
        font=('arial', 25),bg= '#f04d75',fg="white")
    label13.pack()
    global button49
    button49=Button(root, text='''{"name":"apple"}''', command= Not_correct,\
        font=('arial', 20),height= 2, width=15)
    button49.place(relx=0.02,rely=0.4)
    global button50
    button50=Button(root, text='''{"apple","banana"}''', command= correct,\
        font=('arial', 20),height= 2, width=15)
    button50.place(relx=0.35,rely=0.4)
    global button51
    button51=Button(root, text='''("apple","banana")''', command= Not_correct,\
        font=('arial', 20),height= 2, width=15)
    button51.place(relx=0.68,rely=0.4)
    global button52
    button52 = Button(root,text = 'Skip' ,\
        command=tab14, font=('arial', 20))
    button52.pack(side= BOTTOM)
    button52.after(5000,tab14)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)


#Question14
def tab14():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label13.destroy()
    button49.destroy()
    button50.destroy()
    button51.destroy()
    button52.destroy()
    
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",\
        font=('arial', 30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button53['state']=DISABLED
        button54['state']=DISABLED
        button55['state']=DISABLED
        
        my_cursor.execute("insert into marks values(14,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial', 30)\
        ,bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button53['state']=DISABLED
        button54['state']=DISABLED
        button55['state']=DISABLED
        my_cursor.execute("insert into marks values(14,0)")
        mydb.commit()
    global label14
    label14 = Label(root,text = '''How do you start writing a while
    loop in Python?''',font=('arial', 25),bg= '#f04d75',fg="white")
    label14.pack()
    global button53
    button53=Button(root, text='''if x > y:''', command= correct,\
        font=('arial', 20),height= 2, width=10)
    button53.place(relx=0.08,rely=0.4)
    global button54
    button54=Button(root, text='''if x > y then:''', command= Not_correct,\
        font=('arial', 20),height= 2, width=10)
    button54.place(relx=0.39,rely=0.4)
    global button55
    button55=Button(root, text='''if (x > y)''', command= Not_correct,\
        font=('arial', 20),height= 2, width=10)
    button55.place(relx=0.7,rely=0.4)
    global button56
    button56 = Button(root,text = 'Skip' ,\
        command=tab15, font=('arial', 20))
    button56.pack(side= BOTTOM)
    button56.after(5000,tab15)

    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)


#Question15
def tab15():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label14.destroy()
    button53.destroy()
    button54.destroy()
    button55.destroy()
    button56.destroy()
    
    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",\
        font=('arial', 30),bg= '#f04d75',fg="white")
        lable_correct.place(relx=0.44,rely= 0.65)
        button57['state']=DISABLED
        button58['state']=DISABLED
        button59['state']=DISABLED
        
        my_cursor.execute("insert into marks values(15,1)")
        mydb.commit()
    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False",font=('arial', 30),bg= '#f04d75',fg="white")
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button57['state']=DISABLED
        button58['state']=DISABLED
        button59['state']=DISABLED
        my_cursor.execute("insert into marks values(15,0)")
        mydb.commit()
    global label15
    label15 = Label(root,text = '''How do you insert COMMENTS in Python code?''',\
    font=('arial', 25),bg= '#f04d75',fg="white")
    label15.pack()
    global button57
    button57=Button(root, text='''//Hello world''', command= Not_correct,\
        font=('arial', 20),height= 2, width=11)
    button57.place(relx=0.1,rely=0.4)
    global button58
    button58=Button(root, text='''/*Hello world*/''', command= Not_correct,\
        font=('arial', 20),height= 2, width=11)
    button58.place(relx=0.4,rely=0.4)
    global button59
    button59=Button(root, text='''#Hello world''', command= correct,\
        font=('arial', 20),height= 2, width=11)
    button59.place(relx=0.7,rely=0.4)
    global button60
    button60 = Button(root,text = 'Show result' ,\
        command=result_tab, font=('arial', 20))
    button60.pack(side= BOTTOM)
    button60.after(5000,result_tab)
    
    timer_Count = Label(root, font=('arial',70), fg="#4df0bc",bg="#f04d75")
    timer_Count.place(x=80,y=90)
    timer(timer_Count)


#To show the final resutl(marks scored in quiz)
def result_tab():

    lable_correct.destroy()
    lable_incorrect.destroy()
    label15.destroy()
    button57.destroy()
    button58.destroy()
    button59.destroy()
    button60.destroy()
    a = Label(root, text="The total marks scored is : ",\
        font=('arial',25),bg= '#f04d75',fg="white")
    a.place(relx=0.25,rely=0.3)
    def show_result():
        #To create the sum of all the marks scored 
        my_cursor.execute('''SELECT SUM(marks) AS "Total marks" FROM marks;''')
        #fetch all the marks from my_cursor as a variable result
        result = my_cursor.fetchall()
        for x in result:
            marks = Label(root, text= x , font=("Arial", 50),bg= '#f04d75',fg="white")
            marks.place(relx=0.45,rely=0.45)
     
    show_result()
Start_tab()

root.mainloop()