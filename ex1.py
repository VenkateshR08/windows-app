from tkinter import *
from tkinter import ttk
def Divide():
    num1 = value1.get()
    num2 = value2.get()
    value = num1/num2
    result.config(text='Result: %d' % value)
ob = Tk()
ob.geometry('400x400')
ob.title('Operations')
ob.configure(bg='green')
Label(ob, text='Enter Value A: ', bg='red').grid(row=1, column=1)
Label(ob, text='Enter Value B: ', bg='red').grid(row=2, column=1)
value1 = IntVar()
value2 = IntVar()
Entry(ob, textvariable=value1).grid(row=1, column=2)
Entry(ob, textvariable=value2).grid(row=2, column=2)
Button(ob, text='Divide', command=Divide, bg='grey', fg='white', width='10', height='1').grid(row=4, column=2)
result = Label(ob, fg='black', bg='yellow')
result.grid(row=5, column=2)
ob.mainloop()