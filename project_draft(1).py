from tkinter import *
import tkinter
import mysql.connector
import turtle


mydb = mysql.connector.connect(host="localhost",user="root",passwd="paritosh")
my_cursor = mydb.cursor()
my_cursor.execute("Drop DATABASE IF EXISTS quizmarks")
my_cursor.execute("CREATE DATABASE IF NOT EXISTS quizmarks")
my_cursor.execute("use quizmarks")
my_cursor.execute("CREATE TABLE marks (Question int,marks int)")

root = Tk()
canvas = tkinter.Canvas(master = root,width=150,height=150,highlightbackground="green")
canvas.place(x=10,y=10)
root.configure(background = "green")
root.minsize(height= 500,width=600)
draw = turtle.RawTurtle(canvas)
draw.getscreen().bgcolor("green")
def result_tab():

        lable_correct.destroy()
        lable_incorrect.destroy()
        label10.destroy()
        button37.destroy()
        button38.destroy()
        button39.destroy()
        button40.destroy()


        a = Label(root, text="The total marks scored is : ",font=('arial',25))
        a.place(relx=0.25,rely=0.3)
        def show_result():
            my_cursor.execute('''SELECT SUM(marks) AS "Total marks" FROM marks;''')
            result = my_cursor.fetchall()
            for x in result:
                marks = Label(root, text= x , font=("Arial", 50))
                marks.place(relx=0.45,rely=0.45)
        show_result()

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
            lable_correct =Label(root,text="True",font=('arial', 30))
            lable_correct.place(relx=0.44,rely= 0.65)
            button37['state']=DISABLED
            button38['state']=DISABLED
            button39['state']=DISABLED
            my_cursor.execute("insert into marks values(10,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False",font=('arial', 30))
            lable_incorrect.place(relx=0.43,rely= 0.65)
            button37['state']=DISABLED
            button38['state']=DISABLED
            button39['state']=DISABLED

            my_cursor.execute("insert into marks values(10,0)")
            mydb.commit()

        global label10
        label10 = Label(root,text = '''What is the output of the following program : 

print (0.1 + 0.2 == 0.3) ''',font=('arial', 25))
        label10.pack()
        global button37
        button37=Button(root, text="True", command= Not_correct,font=('arial', 20),height= 2, width=6)
        button37.place(relx=0.1,rely=0.4)
        global button38
        button38=Button(root, text="False", command= correct,font=('arial', 20),height= 2, width=6)
        button38.place(relx=0.41,rely=0.4)
        global button39
        button39=Button(root, text="Error", command= Not_correct,font=('arial', 20),height= 2, width=6)
        button39.place(relx=0.73,rely=0.4)

        global button40
        button40 = Button(root,text = 'Show result' , command= result_tab,font=('arial', 20))
        button40.pack(side= BOTTOM)

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
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.44,rely=0.79)
            button33['state']=DISABLED
            button34['state']=DISABLED
            button35['state']=DISABLED
            my_cursor.execute("insert into marks values(9,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False",font=('arial',30))
            lable_incorrect.place(relx=0.44,rely=0.79)
            button33['state']=DISABLED
            button34['state']=DISABLED
            button35['state']=DISABLED

            my_cursor.execute("insert into marks values(9,0)")
            mydb.commit()

        global label9
        label9 = Label(root,text = '''Find the output of the following program:
        
    nameList = ['Harsh', 'Pratik', 'Bob', 'Dhruv'] 
 
    pos = nameList.index("GeeksforGeeks") 
 
    print (pos * 3)''' , font=('arial',25))
        label9.pack()
        global button33
        button33=Button(root, text='''ValueError: 
'GeeksforGeeks'
is not in list''', command= correct,height=4,width=11,font=('arial',20))
        button33.place(relx=0.02,rely=0.5)
        global button34
        button34=Button(root, text='''Harsh
Harsh
Harsh''', command= Not_correct,height=4,width=11,font=('arial',20))
        button34.place(relx=0.36,rely=0.5)
        global button35
        button35=Button(root, text='''Harsh''', command= Not_correct,height=4,width=11,font=('arial',20))
        button35.place(relx=0.7,rely=0.5)

        global button36
        button36 = Button(root,text = 'Next' ,command= tab10,font=('arial',20))
        button36.pack(side= BOTTOM)

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
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.44,rely= 0.65)
            button29['state']=DISABLED
            button30['state']=DISABLED
            button31['state']=DISABLED
            my_cursor.execute("insert into marks values(8,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False",font=('arial',30))
            lable_incorrect.place(relx=0.44,rely= 0.65)
            button29['state']=DISABLED
            button30['state']=DISABLED
            button31['state']=DISABLED

            my_cursor.execute("insert into marks values(8,0)")
            mydb.commit()

        global label8
        label8 = Label(root,text = '''Which of these is not a core data type ?''',font=('arial',25))
        label8.pack()
        global button29
        button29=Button(root, text="Tuples", command= Not_correct,font=('arial',20),height=2,width=9)
        button29.place(relx=0.1,rely=0.4)
        global button30
        button30=Button(root, text="Dictionary", command= Not_correct,font=('arial',20),height=2,width=9)
        button30.place(relx=0.4,rely=0.4)
        global button31
        button31=Button(root, text="Class", command= correct,font=('arial',20),height=2,width=9)
        button31.place(relx=0.7,rely=0.4)

        global button32
        button32 = Button(root,text = 'Next' , command= tab9,font=('arial',20))
        button32.pack(side= BOTTOM)

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
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.44,rely= 0.65)
            button25['state']=DISABLED
            button26['state']=DISABLED
            button27['state']=DISABLED
            my_cursor.execute("insert into marks values(7,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False",font=('arial',30))
            lable_incorrect.place(relx=0.44,rely= 0.65)
            button25['state']=DISABLED
            button26['state']=DISABLED
            button27['state']=DISABLED

            my_cursor.execute("insert into marks values(7,0)")
            mydb.commit()

        global label7
        label7 = Label(root,text = '''Which of the following is the correct command 
     to exit from an interpreter in pyhton ? ''',font=('arial',25))
        label7.pack()
        global button25
        button25=Button(root, text="exit()", command= correct,font=('arial',20),height=2,width=4)
        button25.place(relx=0.1,rely=0.4)
        global button26
        button26=Button(root, text="end()", command= Not_correct,font=('arial',20),height=2,width=4)
        button26.place(relx=0.44,rely=0.4)
        global button27
        button27=Button(root, text="stop()", command= Not_correct,font=('arial',20),height=2,width=4)
        button27.place(relx=0.75,rely=0.4)

        global button28
        button28 = Button(root,text = 'Next' ,command= tab8,font=('arial',20))
        button28.pack(side= BOTTOM)

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
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.44,rely= 0.65)
            button21['state']=DISABLED
            button22['state']=DISABLED
            button23['state']=DISABLED
            my_cursor.execute("insert into marks values(6,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False",font=('arial',30))
            lable_incorrect.place(relx=0.43,rely= 0.65)
            button21['state']=DISABLED
            button22['state']=DISABLED
            button23['state']=DISABLED

            my_cursor.execute("insert into marks values(6,0)")
            mydb.commit()

        global label6
        label6 = Label(root,text = '''Which of the following variables stores 
the arguments in the command line ?''',font=('arial',25))
        label6.pack()
        global button21
        button21=Button(root, text="Arg", command= Not_correct,font=('arial',20),height=2,width=3)
        button21.place(relx=0.1,rely=0.4)
        global button22
        button22=Button(root, text="agrc", command= Not_correct,font=('arial',20),height=2,width=3)
        button22.place(relx=0.44,rely=0.4)
        global button23
        button23=Button(root, text="agrv", command= correct,font=('arial',20),height=2,width=3)
        button23.place(relx=0.8,rely=0.4)

        global button24
        button24 = Button(root,text = 'Next' , command= tab7,font=('arial', 20))
        button24.pack(side= BOTTOM)

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
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.44,rely= 0.65)
            button17['state']=DISABLED
            button18['state']=DISABLED
            button19['state']=DISABLED
            my_cursor.execute("insert into marks values(5,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False",font=('arial',30))
            lable_incorrect.place(relx=0.44,rely= 0.65)
            button17['state']=DISABLED
            button18['state']=DISABLED
            button19['state']=DISABLED

            my_cursor.execute("insert into marks values(5,0)")
            mydb.commit()

        global label5
        label5 = Label(root,text = '''Which of the following prints the
     file name in he command line argument ?''',font=('arial',25))
        label5.pack()
        global button17
        button17=Button(root, text="print(sys.argv[0])", command= correct,font=('arial',20),height=2,width=12)
        button17.place(relx=0.02,rely=0.4)
        global button18
        button18=Button(root, text='''print("sys.argv[0]")''', command= Not_correct,font=('arial',20),height=2,width=12)
        button18.place(relx=0.35,rely=0.4)
        global button19
        button19=Button(root, text="print(sys.argv[1])", command= Not_correct,font=('arial',20),height=2,width=12)
        button19.place(relx=0.68,rely=0.4)

        global button20
        button20 = Button(root,text = 'Next', command= tab6,font=('arial',20))
        button20.pack(side= BOTTOM)

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
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.44,rely= 0.65)
            button13['state']=DISABLED
            button14['state']=DISABLED
            button15['state']=DISABLED
            my_cursor.execute("insert into marks values(4,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False",font=('arial',30))
            lable_incorrect.place(relx=0.43,rely= 0.65)
            button13['state']=DISABLED
            button14['state']=DISABLED
            button15['state']=DISABLED

            my_cursor.execute("insert into marks values(4,0)")
            mydb.commit()

        global label4
        label4 = Label(root,text = '''Which of the following is the correct way to print the 
     result of addition of 10 and 7 to get 17 ?''',font=('arial',25))
        label4.pack()

        global button13
        button13=Button(root, text="print('10+7')", command= Not_correct,font=('arial', 20),height= 2, width=8)
        button13.place(relx=0.1,rely=0.4)
        global button14
        button14=Button(root, text="print(10+7)", command= correct,font=('arial', 20),height= 2, width=8)
        button14.place(relx=0.4,rely=0.4)
        global button15
        button15=Button(root, text="print('10'+'7')", command= Not_correct,font=('arial', 20),height= 2, width=8)
        button15.place(relx=0.7,rely=0.4)

        global button16
        button16 = Button(root,text = 'Next', command= tab5,font=('arial', 20))
        button16.pack(side= BOTTOM)

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
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.45,rely= 0.65)
            button9['state']=DISABLED
            button10['state']=DISABLED
            button11['state']=DISABLED
            my_cursor.execute("insert into marks values(3,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False", font=('arial',30))
            lable_incorrect.place(relx=0.43,rely= 0.65)
            button9['state']=DISABLED
            button10['state']=DISABLED
            button11['state']=DISABLED

            my_cursor.execute("insert into marks values(3,0)")
            mydb.commit()
        global label3
        label3 = Label(root,text = "What do 'R' and 'E' mean in 'REPL'",font=('arial',25))
        label3.pack()

        global button9
        button9=Button(root, text="Run and Enter", command= Not_correct,font=('arial', 20),height= 2, width=12)
        button9.place(relx=0.02,rely=0.4)
        global button10
        button10=Button(root, text="Read and Execute", command= correct,font=('arial', 20),height= 2, width=12)
        button10.place(relx=0.35,rely=0.4)
        global button11
        button11=Button(root, text="Read and Enter", command= Not_correct,font=('arial', 20),height= 2, width=12)
        button11.place(relx=0.68,rely=0.4)
        global button12
        button12 = Button(root,text = 'Next' , command= tab4,font=('arial', 20))
        button12.pack(side= BOTTOM)
      
def tab2():
        timer()
        lable_correct.destroy()
        lable_incorrect.destroy()
        label1.destroy()
        button1.destroy()
        button2.destroy()
        button3.destroy()
        button4.destroy()

        def correct():
            global lable_correct
            lable_correct =Label(root,text="True",font=('arial',30))
            lable_correct.place(relx=0.44,rely=0.79)
            button5['state']=DISABLED
            button6['state']=DISABLED
            button7['state']=DISABLED
            my_cursor.execute("insert into marks values(2,1)")
            mydb.commit()

        def Not_correct():
            global lable_incorrect
            lable_incorrect =Label(root,text="False", font=('arial',30))
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

print('"Hello world") ''', font=('arial',25))
        label2.pack()

        global button5
        button5=Button(root, text='''The output is :
Hello!''', command= Not_correct ,font=('arial', 20),height= 3, width=9)
        button5.place(relx=0.1,rely=0.5)
        global button6
        button6=Button(root, text="Syntax error", command=Not_correct,font=('arial', 20),height= 3, width=9)
        button6.place(relx=0.4,rely=0.5)
        global button7
        button7=Button(root, text='''None of the 
 above''', command= correct,font=('arial', 20),height= 3, width=9)
        button7.place(relx=0.7,rely=0.5)

        global button8
        button8 = Button(root,text = 'Next' , command= tab3,font=('arial', 20))
        button8.pack(side= BOTTOM)
       
def tab1():

    def correct():
        global lable_correct
        lable_correct =Label(root,text="True",font=('arial', 30))
        lable_correct.place(relx=0.44,rely= 0.65)
        button1['state']=DISABLED
        button2['state']=DISABLED
        button3['state']=DISABLED
        my_cursor.execute("insert into marks values(1,1)")
        mydb.commit()

    def Not_correct():
        global lable_incorrect
        lable_incorrect =Label(root,text="False", font=('arial', 30))
        lable_incorrect.place(relx=0.43,rely= 0.65)
        button1['state']=DISABLED
        button2['state']=DISABLED
        button3['state']=DISABLED

        my_cursor.execute("insert into marks values(1,0)")
        mydb.commit()

    global label1
    label1 = Label(root,text = '''Which of the following is the correct way
to assign a number to a variable? ''', font=('arial',25),bg = "green")
    label1.pack()
    
    global button1
    button1=Button(root, text="var = 8", command= correct , font=('arial', 20),height= 2, width=6)
    button1.place(relx=0.1,rely=0.4)
    global button2
    button2=Button(root, text="var = '8'", command=Not_correct,font=('arial', 20),height= 2, width=6 )
    button2.place(relx=0.4,rely=0.4)
    global button3
    button3=Button(root, text="var == 8", command= Not_correct, font=('arial', 20),height= 2, width=6)
    button3.place(relx=0.7,rely=0.4)

    global button4
    button4 = Button(root,text = 'Next', command= tab2, font=('arial', 20))
    button4.pack(side= BOTTOM)

lable_correct =Label(root)
lable_incorrect =Label(root)

def timer():
    draw.up()
    draw.hideturtle()
    draw.sety(-48)
    draw.setx(10)
    draw.fillcolor('#f04d75')
    draw.begin_fill()
    def new():
        draw.circle(60,extent=72)
        draw.left(90) 
        draw.forward(60)
    for i in range(5):
        new() 
        draw.end_fill()  
        draw.fillcolor('#f04d75')
        draw.begin_fill()
        draw.backward(60)  
        draw.right(90)

tab1()
root.mainloop()