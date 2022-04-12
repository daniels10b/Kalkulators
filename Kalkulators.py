from cProfile import run
from distutils.archive_util import make_archive
from tkinter import*
mansLogs=Tk()
mansLogs.title("Kalkulators")
#mansLogs.geometry("400x300")#Loga izmers starp x nav astsartape
def btnCommand(command):
    global num1#jāiegaumē skaitlis un darbība
    global mathOp#matemātiskais operators
    mathOp=command #+, -, /, *
    num1=int(e.get())
    e.delete(0,END)
    return 0


def btnClick(number):
    current=e.get()#nolasa esošo skaitli
    e.delete(0,END)
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievieto displejā
    return 0
    
    

e=Entry(mansLogs,width=15,font=("Arial Black",20))#veido display kur vadīs skaitļus
e.grid(row=0,column=0,columnspan=4)

btn0=Button(mansLogs,text="0",padx="40",pady="20",command=lambda:btnClick(0))#funkcijais padod parametrus
btn1=Button(mansLogs,text="1",padx="40",pady="20",command=lambda:btnClick(1))
btn2=Button(mansLogs,text="2",padx="40",pady="20",command=lambda:btnClick(2))
btn3=Button(mansLogs,text="3",padx="40",pady="20",command=lambda:btnClick(3))
btn4=Button(mansLogs,text="4",padx="40",pady="20",command=lambda:btnClick(4))
btn5=Button(mansLogs,text="5",padx="40",pady="20",command=lambda:btnClick(5))
btn6=Button(mansLogs,text="6",padx="40",pady="20",command=lambda:btnClick(6))
btn7=Button(mansLogs,text="7",padx="40",pady="20",command=lambda:btnClick(7))
btn8=Button(mansLogs,text="8",padx="40",pady="20",command=lambda:btnClick(8))
btn9=Button(mansLogs,text="9",padx="40",pady="20",command=lambda:btnClick(9))
btn11=Button(mansLogs,text="C",padx="40",pady="20")
btn12=Button(mansLogs,text="=",padx="40",pady="20",command=lambda:btnCommand("="))
btn13=Button(mansLogs,text="/",padx="40",pady="20",command=lambda:btnCommand("/"))
btn14=Button(mansLogs,text="x",padx="40",pady="20",command=lambda:btnCommand("*"))
btn15=Button(mansLogs,text="+",padx="40",pady="20",command=lambda:btnCommand("+"))
btn16=Button(mansLogs,text="-",padx="40",pady="20",command=lambda:btnCommand("-"))

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



mansLogs.mainloop()
