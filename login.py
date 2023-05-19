from tkinter import *
import tkinter.messagebox
from menu import Menu

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("CARE & CURE NURSING")
        self.master.geometry("1600x800+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.create_widgets()

    def create_widgets(self):
        lbl_title = Label(self.frame, text="CARE & CURE NURSING", font="Helvetica 20 bold", bg="powder blue", fg="black")
        lbl_title.grid(row=0, column=0, columnspan=2, pady=40)

        login_frame1 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        login_frame1.grid(row=1, column=0)
        login_frame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        login_frame2.grid(row=2, column=0)

        lbl_username = Label(login_frame1, text="Username", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        lbl_username.grid(row=0, column=0)
        entry_username = Entry(login_frame1, font="Helvetica 14 bold", textvariable=self.Username, bd=2)
        entry_username.grid(row=0, column=1)

        lbl_password = Label(login_frame1, text="Password", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        lbl_password.grid(row=1, column=0)
        entry_password = Entry(login_frame1, font="Helvetica 14 bold", show="*", textvariable=self.Password, bd=2)
        entry_password.grid(row=1, column=1)

        btn_login = Button(login_frame2, text="Login", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.login_system)
        btn_login.grid(row=3, column=0)
        btn_exit = Button(login_frame2, text="Exit", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.exit)
        btn_exit.grid(row=3, column=1)

    def login_system(self):
        username = self.Username.get()
        password = self.Password.get()
        if username == 'admin' and password == '1234':
            self.open_menu()
        elif username == 'root' and password == '4321':
            self.open_menu()
        else:
            tkinter.messagebox.askretrycancel("CARE & CURE NURSING", "PLEASE ENTER VALID USERNAME AND PASSWORD")

    def open_menu(self):
        self.new_window = Toplevel(self.master)
        self.app = Menu(self.new_window)
        #self.withdraw()

    def exit(self):
        self.master.destroy()

def main():
    root = Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
