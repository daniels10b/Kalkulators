from cProfile import run
from distutils.archive_util import make_archive
from tkinter import*
mansLogs=Tk()
mansLogs.title("Kalkulators")
#mansLogs.geometry("400x300")#Loga izmers starp x nav astsartape
btn0=Button(mansLogs,text="0",padx="40",pady="20")
btn1=Button(mansLogs,text="1",padx="40",pady="20")
btn2=Button(mansLogs,text="2",padx="40",pady="20")
btn3=Button(mansLogs,text="3",padx="40",pady="20")
btn4=Button(mansLogs,text="4",padx="40",pady="20")
btn5=Button(mansLogs,text="5",padx="40",pady="20")
btn6=Button(mansLogs,text="6",padx="40",pady="20")
btn7=Button(mansLogs,text="7",padx="40",pady="20")
btn8=Button(mansLogs,text="8",padx="40",pady="20")
btn9=Button(mansLogs,text="9",padx="40",pady="20")
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
btn11=Button(mansLogs,text="C",padx="40",pady="20")
btn12=Button(mansLogs,text="=",padx="40",pady="20")
btn11.grid(row=4,column=1)
btn12.grid(row=4,column=2)
btn13=Button(mansLogs,text="/",padx="40",pady="20")
btn14=Button(mansLogs,text="x",padx="40",pady="20")
btn15=Button(mansLogs,text="+",padx="40",pady="20")
btn16=Button(mansLogs,text="-",padx="40",pady="20")
btn13.grid(row=1,column=3)
btn14.grid(row=2,column=3)
btn15.grid(row=3,column=3)
btn16.grid(row=4,column=3)




mansLogs.mainloop()
