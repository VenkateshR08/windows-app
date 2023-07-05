import tkinter.messagebox
from tkinter import *
import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='', db='products')
cursor = db.cursor()

def calculate():
    pro_tot.set(pro_price.get() * pro_qty.get())

def add():
    id = pro_id.get()
    name = pro_name.get()
    price = pro_price.get()
    qty = pro_qty.get()
    tot = pro_tot.get()
    cursor.execute('insert into details values(%s, %s, %s, %s, %s)', [id, name, price, qty, tot])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Products Added')

def view():
    id = pro_id.get()
    cursor.execute('select * from details where ProId = %s', [id])
    data = cursor.fetchone()
    if data != None:
        pro_name.set(data[1])
        pro_price.set(data[2])
        pro_qty.set(data[3])
        pro_tot.set(data[4])
    else:
        tkinter.messagebox.showinfo('Access', 'No Data')

def update():
    id = pro_id.get()
    price = pro_price.get()
    qty = pro_qty.get()
    tot = pro_tot.get()
    cursor.execute('Update details set ProPrice = %s, ProQty = %s, TotalPrice = %s where ProId = %s', [price, qty, tot, id])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Products Updated')

def delete():
    id = pro_id.get()
    cursor.execute('Delete from details where ProId = %s', [id])
    db.commit()
    tkinter.messagebox.showinfo('Access', 'Product Deleted')

def clear():
    pro_id.set('')
    pro_name.set('')
    pro_price.set('')
    pro_qty.set('')
    pro_tot.set('')

def overall():
    global viewdetail
    viewdetail = Toplevel(access)
    viewdetail.geometry('800x400')
    viewdetail.title('Product List')
    viewdetail.configure(bg='aqua')
    cursor.execute('Select * from details')
    data = cursor.fetchall()
    rows = len(data)
    cols = len(data[0])
    Label(viewdetail, text='ProId', font=('calibri', 13, 'bold'), bg='aqua', fg='blue').grid(row=0, column=0)
    Label(viewdetail, text='ProName', font=('calibri', 13, 'bold'), bg='aqua', fg='blue').grid(row=0, column=1)
    Label(viewdetail, text='ProPrice', font=('calibri', 13, 'bold'), bg='aqua', fg='blue').grid(row=0, column=2)
    Label(viewdetail, text='ProQty', font=('calibri', 13, 'bold'), bg='aqua', fg='blue').grid(row=0, column=3)
    Label(viewdetail, text='TotalPrice', font=('calibri', 13, 'bold'), bg='aqua', fg='blue').grid(row=0, column=4)
    for i in range(rows):
        for j in range(cols):
            s = Entry(viewdetail, font=('TimesNewRoman', 14))
            s.grid(row=i+1, column=j)
            s.insert(END, data[i][j])


access = Tk()
access.geometry('700x600')
access.title('Access Control Matrix')
access.configure(bg='grey')

Label(access, text='Products Entry', font=('calibri', 25), fg='blue').place(x=260, y=20)

pro_id_label = Label(access, text='Product Id', font=('calibri', 20), bg='lightblue')
pro_id_label.place(x=100, y=90)
pro_id = StringVar()
pro_id_entry = Entry(access, textvariable=pro_id, font=('calibri', 17))
pro_id_entry.place(x=300, y=90)

pro_name_label = Label(access, text='Product Name', font=('calibri', 20), bg='lightblue')
pro_name_label.place(x=100, y=140)
pro_name = StringVar()
pro_name_entry = Entry(access, textvariable=pro_name, font=('calibri', 17))
pro_name_entry.place(x=300, y=140)

pro_price_label = Label(access, text='Product Price', font=('calibri', 20), bg='lightblue')
pro_price_label.place(x=100, y=190)
pro_price = IntVar()
pro_price_entry = Entry(access, textvariable=pro_price, font=('calibri', 17))
pro_price_entry.place(x=300, y=190)

pro_qty_label = Label(access, text='Product Quantity', font=('calibri', 20), bg='lightblue')
pro_qty_label.place(x=100, y=240)
pro_qty = IntVar()
pro_qty_entry = Entry(access, textvariable=pro_qty, font=('calibri', 17))
pro_qty_entry.place(x=300, y=240)

pro_tot_label = Label(access, text='Product Total', font=('calibri', 20), bg='lightblue')
pro_tot_label.place(x=100, y=290)
pro_tot = IntVar()
pro_tot_entry = Entry(access, textvariable=pro_tot, font=('calibri', 17))
pro_tot_entry.place(x=300, y=290)

but_cal = Button(access, text='Calculate', command=calculate, font=('calibri', 17), bg='blue', fg='white', width='8', height='1')
but_cal.place(x=560, y=240)

but_add = Button(access, text='Add', command=add, font=('calibri', 17), bg='green', fg='white', width='11', height='1')
but_add.place(x=100, y=370)

but_view = Button(access, text='View', command=view, font=('calibri', 17), bg='blue', fg='white', width='11', height='1')
but_view.place(x=270, y=370)

but_upd = Button(access, text='Update', command=update, font=('calibri', 17), bg='green', fg='white', width='11', height='1')
but_upd.place(x=440, y=370)

but_del = Button(access, text='Delete', command=delete, font=('calibri', 17), bg='red', fg='white', width='11', height='1')
but_del.place(x=100, y=450)

but_clr = Button(access, text='Clear', command=clear, font=('calibri', 17), bg='blue', fg='white', width='11', height='1')
but_clr.place(x=270, y=450)

but_ovr = Button(access, text='Overall', command=overall, font=('calibri', 17), bg='blue', fg='white', width='11', height='1')
but_ovr.place(x=440, y=450)
access.mainloop()