from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
from patient_form import Patient
from room_form import Room
from employee_form import Employee
from appointment_form import Appointment
from billing_form import Billing
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
)

print("DATABASE CONNECTION SUCCESSFUL")

#root=Tk()

    
class Menu:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
       
        self.lblTitle = Label(self.frame,text = "MAIN MENU", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.button1 = Button(self.LoginFrame,text = "1.PATIENT REGISTRATION", width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Patient_Reg)       
        self.button1.grid(row=1,column=0,pady=10)
        
        self.button2 = Button(self.LoginFrame, text="2.ROOM ALLOCATION",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Room_Allocation)
        self.button2.grid(row=3,column=0,pady=10)
        
        self.button3 = Button(self.LoginFrame, text="3.EMPLOYEE REGISTRATION",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Employee_Reg)
        self.button3.grid(row=5,column=0,pady=10)
        
        self.button4 = Button(self.LoginFrame, text="4.BOOK APPOINTMENT",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Appointment_Form)
        self.button4.grid(row=7,column=0,pady=10)
        
        self.button5 = Button(self.LoginFrame, text="5.PATIENT BILL",width =30,font="Helvetica 14 bold",bg="cadet blue",command=self.Billing_Form)
        self.button5.grid(row=9,column=0,pady=10)
        
        self.button6 = Button(self.LoginFrame, text="6.EXIT",width =30,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=11,column=0,pady=10)
        
        #EXIT FOR MENU
    def Exit(self):
        self.master.destroy()
        
    def Patient_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Patient(self.newWindow)

    def Room_Allocation(self):
        self.newWindow = Toplevel(self.master)
        self.app = Room(self.newWindow)
        
    def Employee_Reg(self):
        self.newWindow = Toplevel(self.master)
        self.app = Employee(self.newWindow)

    def Appointment_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Appointment(self.newWindow)

    def Billing_Form(self):
        self.newWindow = Toplevel(self.master)
        self.app = Billing(self.newWindow)


#root.mainloop()