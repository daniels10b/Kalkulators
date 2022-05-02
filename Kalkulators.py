from ast import operator
from cProfile import run
from distutils.archive_util import make_archive
from tkinter import*
from math import *
mansLogs=Tk()
mansLogs.title("Kalkulators")
mansLogs.geometry("400x300")#Loga izmers starp x nav astsartape

mansLogs.configure(bg='teal')

#=================================================================

#=================================================================
def btnCommand(command):
    global num1#jāiegaumē skaitlis un darbība
    global mathOp#matemātiskais operators
    mathOp=command #+, -, /, *
    num1=float(e.get())
    e.delete(0,END)
    return 0
#=================================================================

#=================================================================
def btnClick(number):
    current=e.get()#nolasa esošo skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievieto displejā
    return 0
#=================================================================

#=================================================================
def vienads():
    global num2
    num2=(float(e.get()))
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2   
    elif mathOp=="/":
        result=num1/num2  
    elif mathOp=="%":
        result=num1*0.01*num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0
#=================================================================

#=================================================================
def notirit():
    e.delete(0,END)
    num1=0
    mathOp=''
    return 0
#=================================================================

#=================================================================
def sq_rt():
    global operator
    global num1
    num1=(float(e.get()))
    num1=sqrt(num1)
    e.delete(0,END)
    e.insert(0,num1)
    return 0
#=================================================================

#=================================================================
def kvadr():
    global operator
    global num1
    num1 =(float(e.get()))
    num1=num1**2
    e.delete(0,END)
    e.insert(0,num1)
    return 0
#=================================================================

#=================================================================
def loga():
    global operator
    global num1
    num1=(float(e.get()))
    num1=log(num1,81)
    e.delete(0,END)
    e.insert(0,num1)
    return 0
#=================================================================

    
#=================================================================
e=Entry(mansLogs,bg="pink",width=15,bd=20,font=("Arial Black",20))#veido display kur vadīs skaitļus
e.grid(row=0,column=0,columnspan=5)

btn0=Button(mansLogs,font="5",bg="yellow",text="0",padx="40",pady="20",command=lambda:btnClick(0))#funkcijais padod parametrus
btn1=Button(mansLogs,font="5",bg="yellow",text="1",padx="40",pady="20",command=lambda:btnClick(1))
btn2=Button(mansLogs,font="5",bg="yellow",text="2",padx="40",pady="20",command=lambda:btnClick(2))
btn3=Button(mansLogs,font="5",bg="yellow",text="3",padx="40",pady="20",command=lambda:btnClick(3))
btn4=Button(mansLogs,font="5",bg="yellow",text="4",padx="40",pady="20",command=lambda:btnClick(4))
btn5=Button(mansLogs,font="5",bg="yellow",text="5",padx="40",pady="20",command=lambda:btnClick(5))
btn6=Button(mansLogs,font="5",bg="yellow",text="6",padx="40",pady="20",command=lambda:btnClick(6))
btn7=Button(mansLogs,font="5",bg="yellow",text="7",padx="40",pady="20",command=lambda:btnClick(7))
btn8=Button(mansLogs,font="5",bg="yellow",text="8",padx="40",pady="20",command=lambda:btnClick(8))
btn9=Button(mansLogs,font="5",bg="yellow",text="9",padx="40",pady="20",command=lambda:btnClick(9))
btn11=Button(mansLogs,font="5",bg="yellow",text="C",padx="40",pady="20",command=notirit)
btn12=Button(mansLogs,font="5",bg="yellow",text="=",padx="40",pady="20",command=vienads)
btn13=Button(mansLogs,font="5",bg="cyan",text="/",padx="50",pady="20",command=lambda:btnCommand("/"))
btn14=Button(mansLogs,font="5",bg="cyan",text="x",padx="50",pady="20",command=lambda:btnCommand("*"))
btn15=Button(mansLogs,font="5",bg="cyan",text="+",padx="50",pady="20",command=lambda:btnCommand("+"))
btn16=Button(mansLogs,font="5",bg="cyan",text="-",padx="50",pady="20",command=lambda:btnCommand("-"))
btn17=Button(mansLogs,font="5",bg="cyan",text="√",padx="50",pady="20",command=sq_rt)
btn18=Button(mansLogs,font="5",bg="cyan",text="log",padx="50",pady="20",command=loga)
btn19=Button(mansLogs,font="5",bg="cyan",text="x²",padx="50",pady="20",command=kvadr)
btn20=Button(mansLogs,font="5",bg="cyan",text="%",padx="50",pady="20",command=lambda:btnCommand("%"))
#=================================================================

#=================================================================
btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)
btn0.grid(row=4,column=0)
btn11.grid(row=4,column=1)
btn12.grid(row=4,column=2)
btn13.grid(row=1,column=3)
btn14.grid(row=2,column=3)
btn15.grid(row=3,column=3)
btn16.grid(row=4,column=3)
btn17.grid(row=5,column=1)
btn18.grid(row=5,column=0)
btn19.grid(row=5,column=2)
btn20.grid(row=5,column=3)
#=================================================================


mansLogs.mainloop()
