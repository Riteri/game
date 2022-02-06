from tkinter import *
from tkinter import ttk, messagebox
import psycopg2 as ps

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Remind:
    def __init__(self, parent, title="remindWindow", resizable=(False, False) ):

        """
            :param title: remindWindow
            :param resizable: False, False
        """

        self.remindWindow = Toplevel(parent)

        self.remindWindow.title(title)
        self.remindWindow.geometry('400x200')
        # self.canvas = Canvas(self.remindWindow, width=400, height=400)
        # self.canvas.pack()
        self.remindWindow.resizable(resizable[0], resizable[1])
        self.remindWindow.lift()
        self.remindWindow.iconbitmap('filesImages/icon.ico')
        self.entryLabels()


    def entryLabels(self):
        """
             :param self.nickStr: StringVar()
             :param self.emailStr: StringVar()

        """

        self.nickStr = StringVar()
        self.emailStr = StringVar()

        Label(self.remindWindow, text = '      If you have forgotten your password, you can send it to your email', fg = 'black').place(x = 0, y = 0)

        Label(self.remindWindow, text = 'Enter your nickname: ').place(relx = 0, rely = 0.25)
        self.entryNick = ttk.Entry(self.remindWindow, width=30, textvariable=  self.nickStr)
        self.entryNick.place(relx = 0.4, rely = 0.25)

        Label(self.remindWindow, text= 'Enter your email address: ').place(relx = 0, rely = 0.4)
        self.entryEmail = ttk.Entry(self.remindWindow, width=30, textvariable=self.emailStr)
        self.entryEmail.place(relx = 0.4, rely = 0.4)

        ttk.Button(self.remindWindow, text = 'Send data by email', command = self.password_search).place(relx = 0.4, rely = 0.6)




    def password_search(self):
        """
            :description: sends an email with a password
        """

        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")

        self.pswsearch = self.conn.cursor()

        self.pswsearch.execute("SELECT  haslo  FROM bdgraczy WHERE nick = " + "'" + self.nickStr.get() + "'"
                                + "and email = "+ "'" +   self.emailStr.get()   +"'"    )

        self.listPsw = self.pswsearch.fetchall()

        self.conn.commit()
        self.conn.close()
        self.pswsearch.close()


        self.remindHaslo = "".join(map(''.join, self.listPsw))
        print(self.remindHaslo)



        if not self.listPsw:
            messagebox.showinfo('Wrong data', 'check the entered data\nor such user does not exist')
        else:
            from_email = 'wisielcabyantondidytskyi@gmail.com'
            password = 'zktn zfpc bcoi ecjd'

            recipient = self.emailStr.get()



            msg = MIMEMultipart()

            msg['From'] = from_email
            msg['To'] = recipient
            msg['Subject'] = 'Wisielca. Password reminder'

            message = 'Password reminder      \n' \
                      '------------------------------------\n' \
                      '         account information        \n' \
                      '------------------------------------\n' \
                      'Nick: ' + self.nickStr.get() + '\n' \
                      'Your password: ' + self.remindHaslo


            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')  # 587 = gmail
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)
            # server.sendmail(from_email, recipient, msg.as_string())
            server.quit()

            messagebox.showinfo('password reminder', 'the password has been sent to the specified email')

            self.remindWindow.destroy()



