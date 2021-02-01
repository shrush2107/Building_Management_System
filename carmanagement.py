import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import re
from matplotlib import pyplot as plt
from datetime import datetime
connection=sqlite3.connect('dbms.db')
cursor=connection.cursor()
class rental():      
    def __init__(self,t):
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        self.t=t
        self.t.title('Car Rental System')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')
        
        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()
        
        self.title=Label(self.frame,text='WELCOME to DYSJ Car Rental',font=('calibri',68,'bold'),bg='dodger blue4',fg='white')
        self.title.grid(row=0,column=0,columnspan=2,pady=8)

        self.frame1=Frame(self.frame,width=1350,height=600,bg='Steel blue1',relief='sunken',bd=19)
        self.frame1.grid(row=1,column=0,padx=6)
       
        self.button=Button(self.frame1,width=15,text='LOGIN',font=("arial",19,'bold'),bg='Steel blue1',fg='white',command=self.login)
        self.button.grid(row=2,column=0)
        self.button1=Button(self.frame1,width=15,text='SIGN UP',font=("arial",19,'bold'),bg='Steel blue1',fg='white',command=self.reg)
        self.button1.grid(row=2,column=1)
        self.button2 = Button(self.frame1, width=15, text='COMPANY SIGN IN', font=("arial", 19, 'bold'),bg='Steel blue1', fg='white', command=self.cons)
        self.button2.grid(row=2, column=2)
        self.button1 = Button(self.frame, width=12, text='CANCEL', font=("arial", 24, 'bold'), bg='Steel blue1',fg='white', command=self.rst)
        self.button1.grid(row=3, column=0)

    def rst(self):
        self.calls = Toplevel(self.t)
        self.obj = self.t.destroy()

    def cons(self):
        self.calls = Toplevel(self.t)
        self.obj = constant(self.calls)

    def login(self):
        self.calls=Toplevel(self.t)
        self.obj=login(self.calls)
        
    def reg(self):
        self.calls=Toplevel(self.t)
        self.obj=register(self.calls)


class constant:
    def ver(self):
        cursor.execute('select * from customer_dets where email_id = "driti@gmail.com"')
        p= cursor.fetchall()
        print(p)
        passw=self.e2.get()
        if p[0][1]==self.e2.get():
            self.call()
        else:
            self.te.delete(0.0,END)
            self.te.insert(INSERT,'Invalid Password')
            em.delete(first=0,last=100)
            self.ip2.delete(first=0,last=100)
            
    def __init__(self,t):
        self.t=t
        self.t.title('Company Sign In')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')

        self.frame = Frame(self.t, bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='COMPANY SIGN IN', font=('calibri', 68, 'bold'),bg='dodger blue4', fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)

        self.frame1 = Frame(self.frame, width=1350, height=600, bg='Steel blue1', relief='sunken', bd=19)
        self.frame1.grid(row=1, column=0, padx=6)

        self.l1 = Label(self.frame1, text='E-Mail:', font=("arial", 30, 'bold'), bg='Steel blue1', fg='white').grid(row=0,column=0)
        self.l2 = Label(self.frame1, text='driti@gmail.com', font=("arial", 30, 'bold'), bg='Steel blue1', fg='white').grid(row=0,column=1)

        
        self.l2 = tk.Label(self.frame1, text='Password', font=("arial", 30, 'bold'), bg='Steel blue1', fg='white').grid(row=1,column=0)
        self.e2 = tk.Entry(self.frame1, font=('calibri', 19, 'bold'), bg='white', fg='black',show='•')
        self.e2.grid(row=1, column=1)

        self.button=Button(self.frame1,width=15,text='PROCEED',font=("arial",19,'bold'),bg='Steel blue1',fg='white',command=self.ver)
        self.button.grid(row=2,column=0,columnspan=2)
        
        
    def call(self):
        dt=[]
        d=[]
        n=[]
        i=0
        x=('select count(*) from booking_details group by s_mnth order by s_mnth asc')
        y=cursor.execute(x)
        y=cursor.fetchall()
        for i in range(len(y)):
            for j in y[i]:
                n.append(j)
        e=('select distinct(s_mnth) from booking_details order by s_mnth asc')
        f=cursor.execute(e)
        f=cursor.fetchall()
        for h in range(len(f)):
            for k in f[h]:
                d.append(k)
        for u in range(len(d)):
            datetime_object = datetime.strptime(str(d[u]), "%m")
            dt.append(datetime_object.strftime("%B"))
        print(dt)
        print(n)
        plt.title("Bookings")
        plt.xlabel("MONTH")
        plt.ylabel("NO. OF CARS RENTED")
        plt.plot(dt,n,marker="o")
        plt.show()

class login():
    def check(self):
        email=em.get()
        cursor.execute('select * from customer_dets where email_id=?',(email,))
        p=cursor.fetchall()
        if p==[]:
            self.te.delete(0.0,END)
            self.te.insert(INSERT,'Invalid E-Mail ID')
            em.delete(first=0,last=100)
            self.ip2.delete(first=0,last=100)
        elif p[0][1]==self.ip2.get():
            self.call()
        else:
            self.te.delete(0.0,END)
            self.te.insert(INSERT,'Invalid Password')
            em.delete(first=0,last=100)
            self.ip2.delete(first=0,last=100)
    def __init__(self,t):
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        self.t=t
        self.t.title('Login')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')
        
        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()
        
        self.title=Label(self.frame,text='ENTER LOGIN DETAILS',font=('calibri',68,'bold'),bg='dodger blue4',fg='white')
        self.title.grid(row=0,column=0,columnspan=2,pady=8)

        self.frame1=Frame(self.frame,width=1350,height=600,bg='dodger blue4',bd=19)
        self.frame1.grid(row=1,column=0,padx=6)
        self.frame2=Frame(self.frame,width=1000,height=600,bg='dodger blue4',bd=19)
        self.frame2.grid(row=2,column=0)

        self.title1=Label(self.frame1,text="EMAIL:",font=("arial",19,'bold'),bg='dodger blue4',fg='white',bd=23)
        self.title1.grid(row=0,column=0)
        em=Entry(self.frame1,font=("arial",19,'bold'))
        em.grid(row=0,column=1)
        self.title2=Label(self.frame1,text="PASSWORD:",font=("arial",19,'bold'),bg='dodger blue4',fg='white',bd=23)
        self.title2.grid(row=1,column=0)
        self.ip2=Entry(self.frame1,font=("arial",19,'bold'),show='•')
        self.ip2.grid(row=1,column=1)
        self.button=Button(self.frame2,width=15,text='PROCEED',font=("arial",19,'bold'),bg='Steel blue1',fg='white',command=self.check)
        self.button.grid(row=2,column=0)
        self.te=Text(self.frame2,width=15,height=1,font=("arial",19,'bold'),bg='dodger blue4',fg='red')
        self.te.grid(row=3,column=0)
    def call(self):
        self.calls=Toplevel(self.t)
        self.obj=choose(self.calls)
class register():
    def __init__(self,t):
        self.t=t
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        self.t.title('Car Rental System')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')
        
        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='SIGN UP', font=('calibri', 68, 'bold'), bg='dodger blue4',fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)

        self.frame1=Frame(self.frame,width=1350,height=600,bg='Steel blue1',relief='sunken',bd=19)
        self.frame1.grid(row=1,column=0,padx=6)
        
        self.l1=Label(self.frame1,text='Name',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=0,column=0)
        self.e1=tk.Entry(self.frame1,font=('calibri',19,'bold'),bg='white',fg='black')
        self.e1.grid(row=0,column=1)
        
        self.l2=tk.Label(self.frame1,text='E-Mail',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=1,column=0)
        em=tk.Entry(self.frame1,font=('calibri',19,'bold'),bg='white',fg='black')
        em.grid(row=1,column=1)
        
        self.l3=tk.Label(self.frame1,text='Contact Number',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=2,column=0)
        self.e3=tk.Entry(self.frame1,font=('calibri',19,'bold'),bg='white',fg='black')
        self.e3.grid(row=2,column=1)
        
        self.l5=tk.Label(self.frame1,text='Age',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=3,column=0)
        self.e4=tk.Entry(self.frame1,font=('calibri',19,'bold'),bg='white',fg='black')
        self.e4.grid(row=3,column=1)
        
        self.l4=tk.Label(self.frame1,text='Gender',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=4,column=0)
        self.c1 = ttk.Combobox(self.frame1, state='readonly',values=['Select Gender', 'Male', 'Female'],font=('calibri',19,'bold'),background='white',foreground='black')
        self.c1.current(0)
        self.c1.grid(row=4, column=1)
        
        self.l6=tk.Label(self.frame1,text='Password',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=8,column=0)
        self.e5=tk.Entry(self.frame1,show='•',font=('calibri',19,'bold'),bg='white',fg='black')
        self.e5.grid(row=8,column=1)
        self.l7=tk.Label(self.frame1,text='Confirm Password',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=9,column=0)
        self.e6=tk.Entry(self.frame1,show='•',font=('calibri',19,'bold'),bg='white',fg='black')
        self.e6.grid(row=9,column=1)
        
        self.l9=tk.Label(self.frame1,text='Street',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=10,column=0)
        self.e7=tk.Entry(self.frame1,font=('calibri',19,'bold'),bg='white',fg='black')
        self.e7.grid(row=10,column=1)
        
        self.l8=tk.Label(self.frame1,text='City',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=11,column=0)
        self.l10=tk.Label(self.frame1,text='Zip-Code',font=("arial",30,'bold'),bg='Steel blue1',fg='white').grid(row=12,column=0)
        self.e8=tk.Entry(self.frame1,font=('calibri',19,'bold'),bg='white',fg='black')
        self.e8.grid(row=12,column=1)
        self.c2=ttk.Combobox(self.frame1,state='readonly',values=['Select City','Mumbai','New Delhi','Kolkata','Chennai'],font=('calibri',19,'bold'),background='white',foreground='black')
        self.c2.current(0)
        self.c2.grid(row=11,column=1)

        self.b1=tk.Button(self.frame1,text='Submit',font=("arial",30,'bold'),bg='Steel blue1',fg='white',command=self.check).grid(row=13,column=0)
        self.b2=tk.Button(self.frame1,text='Cancel',font=("arial",30,'bold'),bg='Steel blue1',fg='white',command= self.lmn).grid(row=13,column=1)

        self.te=Text(self.frame1,height=1,font=("arial",19,'bold'),bg='Steel blue1',fg='red')
        self.te.grid(row=14,column=0,columnspan=2)
    def check(self):
        self.te.delete(0.0,END)
        if self.e5.get()==self.e6.get():
            if re.search('[a-z]+[0-9]*[a-z]*@[a-z]+[.]com',em.get())!=None:
                if re.search('[0-9]{10}',self.e3.get())!=None:
                    if re.search('[0-9]{4}',self.e5.get())!=None:
                        self.call()
                    else:
                        self.te.insert(INSERT,'Password should be 4 digits. Try Again')
                else:
                    self.e3.delete(first=0,last=100)
                    self.te.insert(INSERT,'Contact Number should be 10 digits. Try Again')
            else:
                self.e5.delete(first=0,last=100)
                self.e6.delete(first=0,last=100)
                self.te.insert(INSERT,'Invalid e-mail ID. Try Again')
                em.delete(first=0,last=100)
        else:
            self.e5.delete(first=0,last=100)
            self.e6.delete(first=0,last=100)
            self.te.insert(INSERT,'Paaswords Do not match. Try Again')
    def call(self):
        cursor.execute('Insert into customer_dets values (?,?,?,?,?,?,?,?,?,?)',(em.get(),self.e5.get(),random.randint(1000,100000),self.e1.get(),self.e3.get(),self.e7.get(),self.c2.get(),self.e8.get(),self.e4.get(),self.c1.get()))
        connection.commit()
        self.calls=Toplevel(self.t)
        self.obj=payment(self.calls)

    def lmn(self):
        self.calls = Toplevel(self.t)
        self.obj = self.t.destroy()

class choose():
    def __init__(self,t):
        self.t=t
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        self.t.title('Car Rental System')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')
        
        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()
        
        self.title=Label(self.frame,text='CHOOSE',font=('calibri',68,'bold'),bg='dodger blue4',fg='white')
        self.title.grid(row=0,column=0,columnspan=2,pady=8)

        self.frame1=Frame(self.frame,width=1350,height=600,bg='Steel blue1',relief='sunken',bd=19)
        self.frame1.grid(row=1,column=0,padx=6)
       
        self.button=Button(self.frame1,width=20,text='RENT A CAR',font=("arial",24,'bold'),bg='Steel blue1',fg='white',command=self.call)
        self.button.grid(row=2,column=0)
        self.button1 = Button(self.frame1,width=20,text='CHANGE PASSWORD',font=("arial", 24, 'bold'), bg='Steel blue1',fg='white',command=self.call1)
        self.button1.grid(row=4, column=0)
        self.button2 = Button(self.frame1,width=20,text='UPDATE INFORMATION',font=("arial", 24, 'bold'), bg='Steel blue1',fg='white',command=self.call2)
        self.button2.grid(row=5, column=0)
        self.button3=Button(self.frame1,width=20,text='BOOKING HISTORY',font=("arial",24,'bold'),bg='Steel blue1',fg='white',command=self.call3)
        self.button3.grid(row=3,column=0)
        
    def call(self):
        self.calls=Toplevel(self.t)
        self.obj=rent(self.calls)
    def call1(self):
        self.calls=Toplevel(self.t)
        self.obj=change(self.calls)
    def call2(self):
        self.calls=Toplevel(self.t)
        self.obj=upd_opt(self.calls)
    def call3(self):
        self.calls=Toplevel(self.t)
        self.obj=history(self.calls)
        
    
class change():
    def __init__(self,t):
        self.t=t
        self.t.title('Change Password')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')

        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='CHANGE PASSWORD', font=('calibri', 68, 'bold'), bg='dodger blue4', fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)
        self.frame1 = Frame(self.frame, width=1350, height=600, bg='Steel blue1', relief='sunken', bd=19)
        self.frame1.grid(row=1, column=0, padx=6)
        self.l1=Label(self.frame1,text='Enter the Old Password: ',font=('calibri',24,'bold'),bg='Steel blue1',fg='white')
        self.l1.grid(row=0,column=0)
        self.e1=Entry(self.frame1,show='•')
        self.e1.grid(row=0,column=1)
        self.l2=Label(self.frame1,text='Enter the New Password: ',font=('calibri',24,'bold'),bg='Steel blue1',fg='white')
        self.l2.grid(row=1,column=0)
        self.e2=Entry(self.frame1,show='•')
        self.e2.grid(row=1,column=1)
        self.l3=Label(self.frame1,text='Confirm the New Password: ',font=('calibri',24,'bold'),bg='Steel blue1',fg='white')
        self.l3.grid(row=2,column=0)
        self.e3=Entry(self.frame1,show='•')
        self.e3.grid(row=2,column=1)
        self.button=Button(self.frame,text='CHANGE',font=("arial",19,'bold'),bg='Steel blue1',fg='white',command=self.check).grid(row=2,column=0)
        self.te=Text(self.frame,height=1,font=("arial",19,'bold'),bg='dodger blue4',fg='red')
        self.te.grid(row=3,column=0,columnspan=2)

        
    def check(self):
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        email=em.get()
        cursor.execute('select passw from customer_dets where email_id=?',(email,))
        dets=cursor.fetchall()
        if dets[0][0]==self.e1.get():
            if self.e2.get()==self.e3.get():
                cursor.execute('update customer_dets set passw=? where email_id=?',(self.e2.get(),email))
                connection.commit()
                self.call()
            else:
                self.te.insert(INSERT,'The new passwords entered do not match')
        else:
            self.te.insert(INSERT,'Old Password Incorrect')
    def call(self):
        self.calls = Toplevel(self.t)
        self.obj = self.t.destroy()

class rent():
    def __init__(self,t):
        self.t=t
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        self.t.title('Enter Preferences')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')
        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()
        self.title=Label(self.frame,text='Enter Preferences',font=('calibri',50,'bold'),bg='dodger blue4',fg='white')
        self.title.grid(row=0,column=0,columnspan=2,pady=8)

        self.frame1=Frame(self.frame,width=1350,height=600,bg='Steel blue1',relief='sunken',bd=19)
        self.frame1.grid(row=1,column=0,padx=6)

        self.l1=Label(self.frame1,text='PICKUP LOCATION',font=('calibri',19,'bold'),bg='Steel blue1',fg='white')
        self.l1.grid(row=2,column=0)
        pul=StringVar()
        self.cb1=ttk.Combobox(self.frame1,state='readonly',textvariable=pul,font=('calibri',19,'bold'),background='Steel blue1',foreground='black')
        self.cb1['values']=("MUMBAI","DELHI","KOLKATA","CHENNAI")
        self.cb1.grid(row=2,column=1)

    
        self.l3=Label(self.frame1,text='START DAY',font=('calibri',19,'bold'),bg='Steel blue1',fg='white')
        self.l3.grid(row=4,column=0)
        sd=IntVar()
        self.cb3=ttk.Combobox(self.frame1,state='readonly',textvariable=sd,font=('calibri',19,'bold'),background='Steel blue1',foreground='black')
        self.cb3['values']=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
        self.cb3.grid(row=4,column=1)

        self.l4=Label(self.frame1,text='START MONTH',font=('calibri',19,'bold'),bg='Steel blue1',fg='white')
        self.l4.grid(row=5,column=0)
        sm=IntVar()
        self.cb4=ttk.Combobox(self.frame1,state='readonly',textvariable=sm,font=('calibri',19,'bold'),background='Steel blue1',foreground='black')
        self.cb4['values']=('1','2','3','4','5','6','7','8','9','10','11','12')
        self.cb4.grid(row=5,column=1)

        self.l5=Label(self.frame1,text='NO OF DAYS',font=('calibri',19,'bold'),bg='Steel blue1',fg='white')
        self.l5.grid(row=6,column=0)
        nd=IntVar()
        self.cb5=ttk.Combobox(self.frame1,state='readonly',textvariable=nd,font=('calibri',19,'bold'),background='Steel blue1',foreground='black')
        self.cb5['values']=("1")
        self.cb5.grid(row=6,column=1)

        self.l6=Label(self.frame1,text='SELECT CAR TYPE',font=('calibri',19,'bold'),bg='Steel blue1',fg='white')
        self.l6.grid(row=7,column=0)
        ct=StringVar()
        self.cb6=ttk.Combobox(self.frame1,state='readonly',textvariable=ct,font=('calibri',19,'bold'),background='Steel blue1',foreground='black')
        self.cb6['values']=('MINI','ECONOMY','STANDARD','LUXURY')
        self.cb6.grid(row=7,column=1)
        self.button=Button(self.frame,width=15,text='PROCEED',font=("arial",19,'bold'),bg='Steel blue1',fg='white',command=self.call)
        self.button.grid(row=8,column=0)
        self.te=Text(self.frame,height=1,font=("arial",19,'bold'),bg='dodger blue4',fg='red')
        self.te.grid(row=9,column=0,columnspan=2)

    def call(self):
        cursor.execute('select * from booking_details natural join driver natural join cars where booking_details.DRIVER_LIC_NO=driver.LICENCE_NO and driver.CAR_NUMBER=cars.CAR_NUMBER and pickup_location=? and s_day=? and s_mnth=? and car_category=?',(pul.get(),sd.get(),sm.get(),ct.get()))
        p=cursor.fetchall()
        if(p==[]):
            self.te.delete(0.0,END)
            if(pul.get()=="MUMBAI"):
                if(ct.get()=="MINI"):
                    self.a=int(nd.get())*1000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),456436757,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                elif(ct.get()=="ECONOMY"):
                    self.a=int(nd.get())*1500
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),234567891,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                elif(ct.get()=="STANDARD"):
                    self.a=int(nd.get())*2000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),457634780,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                else:
                    self.a=int(nd.get())*6000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),867564498,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))

            elif(pul.get()=="DELHI"):
                if(ct.get()=="MINI"):
                    self.a=int(nd.get())*1000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),223441256,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                elif(ct.get()=="ECONOMY"):
                    self.a=int(nd.get())*1500
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),987654234,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                elif(ct.get()=="STANDARD"):
                    self.a=int(nd.get())*2000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),323535768,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                else:
                    self.a=int(nd.get())*6000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),888766780,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))

            elif(pul.get()=="KOLKATA"):
                if(ct.get()=="MINI"):
                    self.a=int(nd.get())*1000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),567890678,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                elif(ct.get()=="ECONOMY"):
                    self.a=int(nd.get())*1500
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),435678987,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                elif(ct.get()=="STANDARD"):
                    self.a=int(nd.get())*2000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),987123651,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                else:
                    self.a=int(nd.get())*6000
                    cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),777888560,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))

            else:
               if(ct.get()=="MINI"):
                   self.a=int(nd.get())*1000
                   cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),890876786,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
               elif(ct.get()=="ECONOMY"):
                   self.a=int(nd.get())*1500
                   cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),456787623,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
               elif(ct.get()=="STANDARD"):
                   self.a=int(nd.get())*2000
                   cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),456600990,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
               else:
                   self.a=int(nd.get())*6000
                   cursor.execute('Insert into booking_details values (?,?,?,?,?,?,?,?,?)',(random.randint(1000,9999),str(em.get()),6767998901,pul.get(),int(nd.get()),int(sd.get()),sm.get(),2020,int(self.a)))
                   
            connection.commit()
            self.te.insert(INSERT,'Your car has been booked')
            self.calls=Toplevel(self.t)
            self.obj=confirm(self.calls)
        else:
            self.te.insert(INSERT,'Please select another car or date')
            

class payment():
    def __init__(self,t):
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        self.t=t
        self.t.title('Payment')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')

        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='CARD DETAILS', font=('calibri', 68, 'bold'), bg='dodger blue4', fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)

        self.frame1 = Frame(self.frame, width=1350, height=600, bg='Steel blue1', relief='sunken', bd=19)
        self.frame1.grid(row=1, column=0, padx=6)
        self.frame2 = Frame(self.frame, width=1000, height=600, bg='Steel blue1', relief='ridge', bd=19)
        self.frame2.grid(row=2, column=0)

        self.title1 = Label(self.frame1, text="CARD NUMBER:", font=("arial", 19, 'bold'), bg='Steel blue1', fg='white',bd=23)
        self.title1.grid(row=0, column=0)
        self.ip1 = Entry(self.frame1, font=("arial", 19, 'bold'))
        self.ip1.grid(row=0, column=1,columnspan=2)

        self.title2 = Label(self.frame1, text="NAME ON CARD:", font=("arial", 19, 'bold'), bg='Steel blue1', fg='white',bd=23)
        self.title2.grid(row=1, column=0)
        self.ip2 = Entry(self.frame1, font=("arial", 19, 'bold'))
        self.ip2.grid(row=1, column=1,columnspan=2)


        self.title3 = Label(self.frame1, text="EXPIRY DATE:", font=("arial", 19, 'bold'), bg='Steel blue1',fg='white',bd=23)
        self.title3.grid(row=2, column=0)
        self.c1=ttk.Combobox(self.frame1,state='readonly',values=['1','2','3','4','5','6','7','8','9','10','11','12'])
        self.c1.grid(row=2,column=1)
        self.c2 = ttk.Combobox(self.frame1,state='readonly',values=['2021','2022','2023','2024'])
        self.c2.grid(row=2,column=2)


        self.title4 = Label(self.frame1, text="CVV:", font=("arial", 19, 'bold'), bg='Steel blue1', fg='white',bd=23)
        self.title4.grid(row=3, column=0)
        self.ip4 = Entry(self.frame1, font=("arial", 19, 'bold'),show='•')
        self.ip4.grid(row=3, column=1,columnspan=2)

        self.button = Button(self.frame2, width=15, text='PROCEED', font=("arial", 19, 'bold'), bg='Steel blue1',fg='white',command=self.check)
        self.button.grid(row=4, column=0,columnspan=3)
        self.te=Text(self.frame2,height=2,width=45,font=("arial",13,'bold'),bg='Steel blue1',fg='red')
        self.te.grid(row=5,column=0,columnspan=2)                                                         

    def check(self):
        self.x='[0-9]'
        self.a=(self.ip4.get())
        if (re.findall(self.x,self.a) and len(self.a)== 3):
                   self.call()
                   
        else:
            self.ip4.delete(first=0,last=100)
            self.te.insert(INSERT,'CVV should be a numerical value of 3 digits')
        
        

                                                                  

    def call(self):
        cursor.execute('Insert into cust_card_dets values(?,?,?,?,?)',(em.get(),int(self.ip1.get()),self.c1.get(),self.c2.get(),self.ip4.get()))
        connection.commit()
        self.calls=Toplevel(self.t)
        self.obj=choose(self.calls)
        

class upd_opt:
    def __init__(self, t):
        global em
        self.t=t

        self.t.title('Update Info')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')

        self.frame = Frame(self.t, bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='UPDATE INFO', font=('calibri', 68, 'bold'), bg='dodger blue4', fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)

        self.frame1 = Frame(self.frame, width=1500, height=600, bg='Steel blue1', relief='sunken', bd=19)
        self.frame1.grid(row=1, column=0, padx=6)

        self.button1 = Button(self.frame1, width=24, text='UPDATE CONTACT NUMBER', font=("arial", 24, 'bold'),bg='Steel blue1', fg='white',command=self.selectcon)
        self.button1.grid(row=1, column=0)
        self.button4 = Button(self.frame1, width=24, text='UPDATE CARD DETAILS', font=("arial", 24, 'bold'), bg='Steel blue1',fg='white',command= self.select)
        self.button4.grid(row=3, column=0)

    def select(self):
        self.calls = Toplevel(self.t)
        self.obj = updatecard(self.calls)

    def selectcon(self):
        self.calls = Toplevel(self.t)
        self.obj = updatecontact(self.calls)


class updatecontact:
    def __init__(self, t):
        global em
        self.t = t

        self.t.title('Update Contact Details')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')

        self.frame = Frame(self.t, bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='UPDATE CONTACT NUMBER', font=('calibri', 68, 'bold'), bg='dodger blue4',fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)

        self.frame1 = Frame(self.frame, width=1500, height=600, bg='Steel blue1', relief='sunken', bd=19)
        self.frame1.grid(row=1, column=0, padx=6)

       
        self.l2 = Label(self.frame1, text='Enter new Contact Number: ', font=('calibri', 24, 'bold'),bg='Steel blue1', fg='white')
        self.l2.grid(row=3, column=0)
        self.e2 = Entry(self.frame1)
        self.e2.grid(row=3, column=1)
        
        self.button = Button(self.frame, text='Update Contact', font=("arial", 24, 'bold'), bg='Steel blue1',fg='white',command= self.up1)
        self.button.grid(row=4, column=0, columnspan=1)
        
        self.button1=Button(self.frame,text='Go to Home Page',font=('arial',24,'bold'),fg='white',bg='Steel blue1',command=self.call1)
        self.button1.grid(row=5,column=0)

        self.te = Text(self.frame, height=1, font=("arial", 19, 'bold'), bg='Steel blue1', fg='red')
        self.te.grid(row=6, column=0, columnspan=2)

    def call1(self):
        self.calls=Toplevel(self.t)
        self.obj=choose(self.calls)
    
    def up1(self):
        self.te.delete(0.0, END)
        if re.search('[0-9]{10}', self.e2.get()) != None:
            email = em.get()
            con = self.e2.get()
            cursor.execute('update customer_dets set phone_number=? where email_id=?', (con, email,))
            connection.commit()
        else:
            self.te.insert(INSERT, 'Contact Number should be 10 digits. Try Again')
            self.e2.delete(first=0, last=100)
         
class updatecard:
    def __init__(self, t):
        global em
        self.t=t

        self.t.title('Update Card Details')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')

        self.frame = Frame(self.t, bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='UPDATE CARD DETAILS', font=('calibri', 68, 'bold'), bg='dodger blue4', fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)

        self.frame1 = Frame(self.frame, width=1500, height=600, bg='Steel blue1', relief='sunken', bd=19)
        self.frame1.grid(row=1, column=0, padx=6)

        self.l1 = Label(self.frame1, text='Enter Name on Card: ', font=('calibri', 24, 'bold'), bg='Steel blue1',fg='white').grid(row=2, column=0)
        self.e1 = Entry(self.frame1)
        self.e1.grid(row=2, column=1)

        self.l2 = Label(self.frame1, text='Enter the Card Number: ', font=('calibri', 24, 'bold'), bg='Steel blue1',fg='white').grid(row=3, column=0)
        self.e2 = Entry(self.frame1)
        self.e2.grid(row=3,column=1)

        self.l3 = Label(self.frame1, text="Enter the Expiry Date:", font=('calibri', 24, 'bold'),bg='Steel blue1', fg='white').grid(row=4, column=0)
        self.c1 = ttk.Combobox(self.frame1, state='readonly',values=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10','11', '12'])
        self.c1.grid(row=4, column=1)
        self.c2 = ttk.Combobox(self.frame1, state='readonly',values=['2021', '2022', '2023', '2024', '2025', '2026', '2027', '2028', '2029','2030'])
        self.c2.grid(row=4, column=2)

        self.l4 = Label(self.frame1, text='Enter CVV: ', font=('calibri', 24, 'bold'), bg='Steel blue1',fg='white').grid(row=5, column=0)
        self.e3 = Entry(self.frame1,show='•')
        self.e3.grid(row=5,column=1)

        self.button = Button(self.frame, text='Update Contact', font=("arial", 24, 'bold'), bg='Steel blue1',fg='white', command=self.up2).grid(row=2, column=0)

        self.button1 = Button(self.frame,text='GO TO HOME PAGE', font=('arial', 24, 'bold'), fg='white',bg='Steel blue1', command=self.call2)
        self.button1.grid(row=3, column=0)

    def up2(self):
        email=em.get()
        cursor.execute('update cust_card_dets set card_no = ?,exp_mnth = ?,exp_yr = ?, cvv = ? where cust_email = ?',(int(self.e2.get()),int(self.c1.get()),int(self.c2.get()),int(self.e3.get()),email))
        connection.commit()

    def call2(self):
        self.calls = Toplevel(self.t)
        self.obj = choose(self.calls)


class history():
    def __init__(self,t):
        self.t=t
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        
        self.t.title('Booking History')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')
        
        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()


        self.frame1=Frame(self.frame,width=650,height=750,bg='Steel blue1',relief='sunken',bd=18)
        self.frame1.grid(row=1,column=0)
        

        self.title=Label(self.frame1,text='Booking history:',font=('calibri',30,'bold'),bg='Steel blue1',fg='white')
        self.title.grid(row=0,column=0,columnspan=2,pady=8)
        self.txt2=Text(self.frame1,height=20,width=100,bg='Steel blue1',fg='white',bd=10,font=('calibri',15,'bold'))
        self.txt2.grid(row=1,column=0,columnspan=2)
        
        email=em.get()
        fetch=('select booking_details.booking_id,booking_details.s_day,booking_details.s_mnth,driver.name,driver.contact_no,cars.car_number,cars.model_name,booking_details.amount from booking_details natural join driver natural join cars where booking_details.driver_lic_no= driver.licence_no and driver.car_number=cars.car_number and booking_details.cust_email=?')
        cursor.execute(fetch,[(em.get())])
        con=cursor.fetchall()
        self.i=0

        for row in con:
            s='BOOKING ID: '+str(con[self.i][0])+"\n"
            self.txt2.insert(INSERT,s)
            t='START DATE: '+str(con[self.i][1])+"/"+str(con[self.i][2])+"\n"
            self.txt2.insert(INSERT,t)
            u='DRIVER NAME: '+(con[self.i][3])+"\n"
            self.txt2.insert(INSERT,u)
            v='DRIVER CONTACT NUMBER: '+str(con[self.i][4])+"\n"
            self.txt2.insert(INSERT,v)
            w='CAR NUMBER: '+str(con[self.i][5])+"\n"
            self.txt2.insert(INSERT,w)
            x='CAR MODEL: '+(con[self.i][6])+"\n"
            self.txt2.insert(INSERT,x)
            y='AMOUNT: '+str(con[self.i][7])+"\n"
            self.txt2.insert(INSERT,y)
            self.txt2.insert(INSERT,'\n')
            self.i+=1
        
        self.button1=Button(self.frame,width=15,text='LOGOUT',font=('arial',12,'bold'),fg='white',bg='Steel blue1',command=self.call2)
        self.button1.grid(row=5,column=0)
        self.button1=Button(self.frame,width=15,text='GO TO HOME PAGE',font=('arial',12,'bold'),fg='white',bg='Steel blue1',command=self.call1)
        self.button1.grid(row=6,column=0)
        self.ploting()


    def call1(self):
        self.calls=Toplevel(self.t)
        self.obj=choose(self.calls)
    def call2(self):
        self.calls=Toplevel(self.t)
        self.obj=rental(self.calls)
    def ploting(self):
        cbmnth=[]
        x=('select count(*) from booking_details where cust_email=? group by s_mnth order by s_mnth asc')
        y=cursor.execute(x,[(em.get())])
        y=cursor.fetchall()
        for i in range(len(y)):
            for j in y[i]:
                cbmnth.append(j)
        print(cbmnth)
        mnth=[]
        e=('select distinct(s_mnth) from booking_details where cust_email=?order by s_mnth asc ')
        f=cursor.execute(e,[(em.get())])
        f=cursor.fetchall()
        for h in range(len(f)):
            for k in f[h]:
                mnth.append(k)
        print(mnth)
        month_name=[]
        for u in range(len(mnth)):
            datetime_object = datetime.strptime(str(mnth[u]), "%m")
            month_name.append(datetime_object.strftime("%B"))
        print(month_name)
        plt.title("NO OF CARS BOOKED")
        plt.xlabel("MONTHS")
        plt.ylabel("No of bookings")
        plt.bar(month_name,cbmnth)
        r=plt.show()
        

class confirm():
    def __init__(self,t):
        self.t=t
        global em
        global pul
        global dp
        global sd
        global sm
        global nd
        global ct
        
        self.t.title('Booking Confirmation')
        self.t.geometry('1350x750+0+0')
        self.t.config(bg='dodger blue4')
        
        self.frame=Frame(self.t,bg='dodger blue4')
        self.frame.pack()

        self.title = Label(self.frame, text='BOOKING DETAILS', font=('calibri', 68, 'bold'), bg='dodger blue4',fg='white')
        self.title.grid(row=0, column=0, columnspan=2, pady=8)

        self.frame1=Frame(self.frame,width=650,height=750,bg='Steel blue1',relief='sunken',bd=18)
        self.frame1.grid(row=1,column=0)

        self.txt=Text(self.frame1,height=5,width=50,bg='Steel blue1',fg='white',bd=10,font=('calibri',15,'bold'))
        self.txt.grid(row=1,column=0,columnspan=2)

        day= sd.get()
        mon= sm.get()
        pl= pul.get()
        nod= nd.get()
        email=em.get()
        
        cursor.execute('select booking_id, no_of_days_hired_for, pickup_location, s_day, s_mnth,amount from booking_details where cust_email=? and s_day=? and s_mnth=?',(email, day, mon,))
        con=cursor.fetchall()
        s='BOOKING ID: '+str(con[0][0])+"\n"

        self.txt.insert(INSERT,s)

        t='START DATE: '+str(sd.get())+"/"+str(sm.get())+"\n"
        self.txt.insert(INSERT,t)

        u='NO. OF DAYS: '+str(nd.get())+"\n"

        self.txt.insert(INSERT,u)

        v='PICKUP LOCATION: '+(pul.get())+"\n"

        self.txt.insert(INSERT,v)
        
        amt='AMOUNT: ₹'+str(con[0][5])

        self.txt.insert(INSERT,amt)
        
        self.button1=Button(self.frame,width=15,text='LOGOUT',font=('arial',15,'bold'),fg='white',bg='Steel blue1',command=self.call2)
        self.button1.grid(row=2,column=0)
        self.button1=Button(self.frame,width=15,text='GO TO HOME PAGE',font=('arial',15,'bold'),fg='white',bg='Steel blue1',command=self.call1)
        self.button1.grid(row=3,column=0)


    def call1(self):
        self.calls=Toplevel(self.t)
        self.obj=choose(self.calls)
    def call2(self):
        self.calls=Toplevel(self.t)
        self.obj=rental(self.calls)


t=tk.Tk()
ob=rental(t)
t.mainloop()
