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
class Appointment:
    def __init__(self,master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.pat_ID=IntVar()
        self.emp_ID=StringVar()
        self.ap_no=StringVar()
        self.ap_time=StringVar()
        self.ap_date=StringVar()
        self.des=StringVar()

        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "APPOINTMENT FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.emp_ID )
        self.lbldid.grid(row=1,column=1)

    
        self.lblap = Label(self.LoginFrame,text="APPOINTMENT NO",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblap.grid(row=2,column=0)
        self.lblap  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_no )
        self.lblap.grid(row=2,column=1)
            
        self.lblapt = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapt.grid(row=0,column=2)
        self.lblapt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_time )
        self.lblapt.grid(row=0,column=3)

        self.lblapd = Label(self.LoginFrame,text="APPOINTMENT DATE(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=1,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.ap_date)
        self.lblapd.grid(row=1,column=3)
        
        self.lbldes = Label(self.LoginFrame,text="DESCRIPTION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldes.grid(row=2,column=2)
        self.lbldes  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.des)
        self.lbldes.grid(row=2,column=3)
        

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_AP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_AP_DISPLAY)
        self.button3.grid(row=3,column=2)
        
        
        self.button3 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS",width =20,font="Helvetica 14 bold",bg="cadet blue",command= self.S_AP_DISPLAY)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=4)

    def Exit(self):            
        self.master.destroy()
        
    def INSERT_AP(self):
        global e1, e2, e3, e4, e5, e6
        e1 = self.pat_ID.get()
        e2 = self.emp_ID.get()
        e3 = self.ap_no.get()
        e4 = self.ap_time.get()
        e5 = self.ap_date.get()
        e6 = self.des.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM appointment WHERE AP_NO = %s", (e3,))
        p = cursor.fetchall()
        x = len(p)

        if x != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "APPOINTMENT ALREADY EXISTS")
        else:
            cursor.execute("INSERT INTO appointment VALUES (%s, %s, %s, %s, %s, %s)", (e1, e2, e3, e4, e5, e6))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "APPOINTMENT SET SUCCESSFULLY")

        conn.commit()

    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)

    def S_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)
           
     
class DEL_AP:
    def __init__(self,master):    
        global de1_ap,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_ap=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER APPOINTMENT NO TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_ap)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_AP)
        self.DeleteB.grid(row=3,column=1)
        
    def DELETE_AP(self):
        global inp_d
        inp_d = str(self.de1_ap.get())
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hospital"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM appointment WHERE AP_NO = %s", (inp_d,))
        v = cursor.fetchall()

        if len(v) == 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")
        else:
            cursor.execute('DELETE FROM APPOINTMENT WHERE AP_NO = %s', (inp_d,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")

        conn.commit()


class SEA_AP:
    def __init__(self,master):    
        global inp_s,entry,SearchB
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.entry=StringVar()
        self.lblTitle = Label(self.frame,text = "SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=25)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER DATE TO VIEW APPOINTMENTS(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.entry)
        self.lblpatid.grid(row=0,column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.SEARCH_AP)
        self.SearchB.grid(row=0,column=1)    

    def SEARCH_AP(self):
        global inp_s, entry, errorS, t, i, q, dis1, dis2, dis3, dis4, dis5, dis6, dis7, dis8, dis9, dis10, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10
        c1 = conn.cursor()
        ap = (self.entry.get())

        c1.execute("SELECT * FROM appointment WHERE AP_DATE = %s", (ap,))
        p = c1.fetchall()

        if len(p) == 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "NO APPOINTMENT FOR TODAY")
        else:
            c1.execute('SELECT PATIENT_ID, NAME, AP_NO, EMP_ID, AP_DATE, AP_TIME FROM PATIENT NATURAL JOIN appointment WHERE AP_DATE = %s', (ap,))
            t = c1.fetchall()

            self.l1 = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
            self.l1.grid(row=1, column=0)

            self.dis1 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=t[0][0])
            self.dis1.grid(row=1, column=1)

            self.l2 = Label(self.LoginFrame, text="PATIENT NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
            self.l2.grid(row=2, column=0)

            self.dis2 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=t[0][1])
            self.dis2.grid(row=2, column=1)

            self.l3 = Label(self.LoginFrame, text="APPOINTMENT NO", font="Helvetica 14 bold", bg="cadet blue", bd=22)
            self.l3.grid(row=3, column=0)

            self.dis3 = Label(self.LoginFrame, font="Helvetica 14 bold", bg="cadet blue", bd=2, text=t[0][2])
            self.dis3.grid(row=3, column=1)

            self.l4 = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
            self.l4.grid(row=4, column=0)

            self.dis4 = Label(self.LoginFrame, font="Helvetica 14 bold", bg="cadet blue", bd=2, text=t[0][3])
            self.dis4.grid(row=4, column=1)

            self.l5 = Label(self.LoginFrame, text="APPOINTMENT TIME(HH:MM:SS)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
            self.l5.grid(row=5, column=0)

            self.dis5 = Label(self.LoginFrame, font="Helvetica 14 bold", bg="cadet blue", bd=2, text=t[0][5])
            self.dis5.grid(row=5, column=1)

#root.mainloop()