#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
win=Tk()
win.title('EMPLOYEE MANAGEMENT SYSTEM')
win.minsize(width=800,height=600)
win.configure(bg='skyblue')
def show():
    conn=mysql.connector.connect(user='root',password='Python@123',host='localhost',database='project9')
    qur='select * from emp1'
    mycur=conn.cursor()
    mycur.execute(qur)
    list1=mycur.fetchall()
    for i in list1:
        treev.insert("",'end',values=(i[0],i[1],i[2],i[3]))
    mycur.close()
    conn.close()
    

def add():
    name=n1.get()
    mobno=m1.get()
    dept=d1.get()
    salary=s1.get()
    if (name=='' or mobno=='' or dept=='' or salary==''):
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Python@123',host='localhost',database='project9')
        qur='INSERT INTO emp1 VALUES("%s","%s","%s","%s")'%(name,mobno,dept,salary)
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is inserted successfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')


def salary():
    root=Tk()
    root.configure(bg='cyan')
    root.title('Salary Display')
    root.geometry('800x800')
    def disp():
        emp_name=e7.get()
        conn=mysql.connector.connect(user='root',password='Python@123',host='localhost',database='project9')
        qur='select salary from emp1 where name="%s"'%(emp_name)
        mycur=conn.cursor()
        mycur.execute(qur)
        result=mycur.fetchone()
        l9.config(text=result[0]+' Rs')
        mycur.close()
        conn.close()
    l8=Label(root,text='Name of Employee',width=20,bd=5,relief='ridge')
    l8.place(x=100,y=80)
    var3=StringVar()
    e7=Entry(root,textvariable=var3,bd=5,relief='ridge',width=40)
    e7.place(x=260,y=80)
    b8=Button(root,text='SHOW SALARY',width=20,command=disp)
    b8.place(x=260,y=120)
    l9=Label(root,text='Salary is here',width=20,height=4,bd=5,relief='ridge')
    l9.place(x=100,y=160)
    

    root.mainloop()

def delete():
    name=var1.get()
    if (name==''):
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Python@123',host='localhost',database='project9')
        qur='DELETE FROM emp1 WHERE name="%s"'%(name)
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is deleted successfully')
        var1.set('')
    

def select():
    name=var2.get()
    if (name==''):
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Python@123',host='localhost',database='project9')
        qur='select * from emp1 where name="%s"'%(name)
        mycur=conn.cursor()
        mycur.execute(qur)
        tup1=mycur.fetchone()
        e1.insert(0,tup1[0])
        e2.insert(0,tup1[1])
        e3.insert(0,tup1[2])
        e4.insert(0,tup1[3])
        mycur.close()
        conn.close()
        var2.set('')
    

def update():
    name=n1.get()
    mobno=m1.get()
    dept=d1.get()
    salary=s1.get()
    if (name=='' or mobno=='' or dept=='' or salary==''):
        messagebox.showinfo('info','All fields are compulsory')
    else:
        conn=mysql.connector.connect(user='root',password='Python@123',host='localhost',database='project9')
        qur='UPDATE emp1 SET mobno="%s",dept="%s",salary="%s" WHERE name="%s"'%(mobno,dept,salary,name)
        mycur=conn.cursor()
        mycur.execute(qur)
        conn.commit()
        mycur.close()
        conn.close()
        messagebox.showinfo('info','Data is updated successfully')
        n1.set('')
        m1.set('')
        d1.set('')
        s1.set('')
    

def clear():
    treev.delete(*treev.get_children())

# main label
lbl=Label(win,text='EMPLOYEE MANAGEMENT SYSTEM',bd=5,relief='ridge',bg='white',
         fg='black',width=40,font=('times new roman',16,'bold'))
lbl.place(x=268,y=40)

# name label and entry
l1=Label(win,text='EMPLOYEE NAME',bd=5,relief='ridge',bg='white',
         fg='black',width=20,font=('times new roman',12,'bold'))
l1.place(x=190,y=100)
n1=StringVar()
e1=Entry(win,textvariable=n1,bd=5,relief='ridge',bg='white',
         fg='black',width=40,font=('times new roman',12,'bold'))
e1.place(x=385,y=100)

# mob no label and entry
l2=Label(win,text='MOBILE NUMBER',bd=5,relief='ridge',bg='white',
         fg='black',width=20,font=('times new roman',12,'bold'))
l2.place(x=190,y=140)
m1=StringVar()
e2=Entry(win,textvariable=m1,bd=5,relief='ridge',bg='white',
         fg='black',width=40,font=('times new roman',12,'bold'))
e2.place(x=385,y=140)

# dept label and entry
l3=Label(win,text='DEPARTMENT',bd=5,relief='ridge',bg='white',
         fg='black',width=20,font=('times new roman',12,'bold'))
l3.place(x=190,y=180)
d1=StringVar()
e3=Entry(win,textvariable=d1,bd=5,relief='ridge',bg='white',
         fg='black',width=40,font=('times new roman',12,'bold'))
e3.place(x=385,y=180)

# salary label and entry
l4=Label(win,text='SALARY',bd=5,relief='ridge',bg='white',
         fg='black',width=20,font=('times new roman',12,'bold'))
l4.place(x=190,y=220)
s1=StringVar()
e4=Entry(win,textvariable=s1,bd=5,relief='ridge',bg='white',
         fg='black',width=40,font=('times new roman',12,'bold'))
e4.place(x=385,y=220)


# Add show exit salary button
b1=Button(win,text='SHOW',width=20,command=show)
b1.place(x=200,y=320)

b2=Button(win,text='ADD',width=20,command=add)
b2.place(x=500,y=320)

b3=Button(win,text='EXIT',width=20,command=win.destroy)
b3.place(x=200,y=360)

b4=Button(win,text='SALARY',width=20,command=salary)
b4.place(x=500,y=360)

# delete label entry button
l5=Label(win,text='Delete by Name>>',bd=5,relief='ridge',bg='white',
         fg='black',width=20,font=('times new roman',12,'bold'))
l5.place(x=190,y=400)
var1=StringVar()
e5=Entry(win,textvariable=var1,bd=5,relief='ridge',bg='white',
         fg='black',width=40,font=('times new roman',12,'bold'))
e5.place(x=385,y=400)

b5=Button(win,text='DELETE',width=20,command=delete)
b5.place(x=385,y=440)

# update label entry select and update button
l6=Label(win,text='Update by Name>>',bd=5,relief='ridge',bg='white',
         fg='black',width=20,font=('times new roman',12,'bold'))
l6.place(x=190,y=480)
var2=StringVar()
e6=Entry(win,textvariable=var2,bd=5,relief='ridge',bg='white',
         fg='black',width=40,font=('times new roman',12,'bold'))
e6.place(x=385,y=480)

b6=Button(win,text='SELECT',width=20,command=select)
b6.place(x=230,y=520)
b7=Button(win,text='UPDATE',width=20,command=update)
b7.place(x=385,y=520)

# treeview
treev = ttk.Treeview(win, selectmode ='browse',height=20)
treev.place(x=900,y=100,width=450)
treev["columns"] = ("1", "2", "3","4")
treev['show'] = 'headings'

treev.column("1", width = 90, anchor ='c')
treev.column("2", width = 90, anchor ='se')
treev.column("3", width = 90, anchor ='se')
treev.column("4", width = 90, anchor ='se')

treev.heading("1", text ="Name")
treev.heading("2", text ="Mobile No")
treev.heading("3", text ="Dept")
treev.heading("4", text ="Salary")

# clear button
b8=Button(win,text='CLEAR',width=20,command=clear)
b8.place(x=1080,y=560)



win.mainloop()

