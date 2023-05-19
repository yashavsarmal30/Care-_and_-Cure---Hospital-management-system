from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "hospital"
)
#root = Tk()
cursor=conn.cursor()
print("DATABASE CONNECTION SUCCESSFUL")


#PATIENT FORM    
class Employee:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.emp_ID=StringVar()
        self.emp_name=StringVar()
        self.emp_sex=StringVar()
        self.emp_age=IntVar()
        self.emp_type=StringVar()
        self.emp_salary=IntVar()
        self.emp_exp=StringVar()
        self.emp_email=StringVar()
        self.emp_phno=IntVar()


        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblempid = Label(self.LoginFrame,text="EMPLOYEE ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempid.grid(row=0,column=0)
        self.lblempid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_ID)
        self.lblempid.grid(row=0,column=1)
        
        self.lblempname = Label(self.LoginFrame,text="EMPLOYEE NAME",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblempname.grid(row=1,column=0)
        self.lblempname  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_name)
        self.lblempname.grid(row=1,column=1)

        self.lblsex = Label(self.LoginFrame,text="SEX",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblsex.grid(row=2,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_sex)
        self.etype1.grid(row=2,column=1)
        

        self.lblage = Label(self.LoginFrame,text="AGE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblage.grid(row=3,column=0)
        self.lblage  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_age)
        self.lblage.grid(row=3,column=1)
        
        self.etype1=Label(self.LoginFrame,text="EMPLOYEE DESIGNATION [DOCTOR,NURSE,RECEPTIONIST] ",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.etype1.grid(row=4,column=0)
        self.etype1 =Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_type)
        self.etype1.grid(row=4,column=1)

        self.lblCon = Label(self.LoginFrame,text="SALARY",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblCon.grid(row=0,column=2)
        self.lblCon  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_salary)
        self.lblCon.grid(row=0,column=3)
        
        self.lblAlt = Label(self.LoginFrame,text="EXPERIENCE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblAlt.grid(row=1,column=2)
        self.lblAlt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_exp)
        self.lblAlt.grid(row=1,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="CONTACT NUMBER",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=2,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_phno)
        self.lbleid.grid(row=2,column=3)
        
        self.lbleid = Label(self.LoginFrame,text="EMAIL",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbleid.grid(row=3,column=2)
        self.lbleid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.emp_email)
        self.lbleid.grid(row=3,column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_EMP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_DISPLAY)
        self.button3.grid(row=3,column=2)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=3)

    def Exit(self):            
        self.master.destroy()
        
    def INSERT_EMP(self):
        global e1, e2, e3, e4, e5, e6, e7, e8, e9

        e1 = self.emp_ID.get()
        e2 = self.emp_name.get()
        e3 = self.emp_sex.get()
        e4 = self.emp_age.get()
        e5 = self.emp_type.get()
        e6 = self.emp_salary.get()
        e7 = self.emp_exp.get()
        e8 = self.emp_email.get()
        e9 = self.emp_phno.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employee WHERE EMP_ID = %s", (e1,))
        p = cursor.fetchall()
        x = len(p)

        if x != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE ID ALREADY EXISTS")
        else:
            cursor.execute("INSERT INTO employee VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",(e1, e2, e3, e4, e5, e6, e7, e8, e9))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")

        conn.commit()

    def DE_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_EMP(self.newWindow)


class D_EMP:
    def __init__(self,master):    
        global de1_emp,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_emp=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER EMPLOYEE ID TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_emp)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_EMP)
        self.DeleteB.grid(row=3,column=1)
        
    def DELETE_EMP(self):
        global inp_d
        inp_d = str(self.de1_emp.get())

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employee WHERE EMP_ID = %s", (inp_d,))
        p = cursor.fetchall()

        if len(p) != 0:
            cursor.execute("DELETE FROM employee WHERE EMP_ID = %s", (inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
        else:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")

        conn.commit()

#root.mainloop()