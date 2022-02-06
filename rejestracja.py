from tkinter import *
from tkinter import  ttk
from tkinter import filedialog
import psycopg2 as ps
from tkinter import messagebox

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class Rejestracja :
    def __init__(self, parent, width, height, title="Registration window", resizable=(False, False) ):
        """
            :param self.okno_rejestracji: Toplevel tkinter
            :param self.okno_rejestracji.iconbitmap: tkinter

            :description:
                .lift()
                    gives an advantage in the location of windows
                .iconbitmap
                    adds an icon to the application
                .title()
                    sets the title of the window

            :param width: 500
            :param height: 400
            :param title: Okno rejestracji
            :param resizable: (False, False)
        """

        self.okno_rejestracji = Toplevel(parent)
        self.okno_rejestracji.title(title)
        self.okno_rejestracji.geometry(f"{width}x{height}+700+150") # размеры+ отступ от краев экрана
        self.okno_rejestracji.resizable (resizable[0], resizable [1])
        self.okno_rejestracji.lift()
        self.okno_rejestracji.iconbitmap('filesImages/icon.ico')
        self.rej()



    def rej(self):
        """
            :param self.nick: StringVar()
            :param self.adres_email: StringVar()
            :param self.plec: StringVar()
            :param self.haslo: StringVar()
            :param Label: tkinter.Label

            :param self.hi_rej: Label
                label with text - (okno dla rejestracji, wpisz swoje danne)

            :param self.nick_rejestracja: ttk.Entry
                place to enter a nickname

            :param self.adres_email_rejestracja: ttk.Entry
                place to enter a e-mail

            :param self.plec_rejestracja: ttk.Entry
                place to indicate gender

            :param self.avatar_rejestracja: ttk.Button
                opens a window for choosing an avatar

            :param self.save_dane_rejestracja: ttk.Button
                button for saving data to the database with the command -  self.sprawdzanie_nicknamu()

            :Used libraries:
                tkinter import *
                tkinter import ttk
        """

        self.nick = StringVar()
        self.adres_email = StringVar()
        self.plec = StringVar()
        self.haslo = StringVar()



        self.hi_rej = Label(self.okno_rejestracji, text = "Window for registration, enter your details").pack()
        #justify это положение текста
        self.nick_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER ,  textvariable =self.nick)\
            .place(relx=0.3, rely=0.1)
        self.label_nick_rejestracja = Label(self.okno_rejestracji,  text = "Enter your nickname: "). place(relx = 0.01, rely = 0.1)


        self.adres_email_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER , textvariable = self.adres_email)\
            .place(relx = 0.3, rely=0.20)
        self.label_adres_email_rejestracja = Label (self.okno_rejestracji, text = "Enter your e-mail address: ").place(relx = 0.01, rely = 0.20)


        self.plec_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER , textvariable = self.plec)\
            .place(relx = 0.3, rely= 0.30)
        self.label_plec_rejestracja = Label (self.okno_rejestracji, text = "Enter your gender (M/W): ").place(relx = 0.01, rely = 0.30)


        self.haslo_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER , show ="*", textvariable = self.haslo)\
            .place(relx = 0.3, rely = 0.40)
        self.label_haslo_rejestracja = Label(self.okno_rejestracji, text = "Enter the password: ").place(relx = 0.01, rely = 0.40)


        self.avatar_rejestracja = ttk.Button(self.okno_rejestracji, text="Add an avatar",  command = self.avatar).place(relx=0.45, rely=0.5)

        self.save_dane_rejestracja = ttk.Button(self.okno_rejestracji, text="Save",
                                            command = lambda :[ self.sprawdzanie_nicknamu() ])\
            .place(relx = 0.45, rely = 0.6)


    def dodawanie_niku_do_bazy_points(self):
        """
            :param self.newNickPoints.execute: database
                adding a nickname and points to the database points (initially 0 )

            :Used libraries: import psycopg2 as ps

        """
        self.com = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.newNickPoints = self.com.cursor()

        self.newNickPoints.execute("INSERT INTO points (nick, points) VALUES" + \
                         "(" + "'" + self.nick.get() + "'" + "," + '0' + ")")

        self.com.commit()
        self.cur.close()
        self.com.close()


    #Добавление аватарки
    def avatar(self):
        """
            :param self.avatar: askopenfilename
                opens a window and asks the user to select a file

            :Used libraries: from tkinter import filedialog
        """
        self.avatar = filedialog.askopenfilename(parent=self.okno_rejestracji)




    def sprawdzanie_nicknamu(self):
        """
            :param self.sprawdzanieNik: database
                makes a query to the database and places the result in a variable self.niknameisbase

            :param self.niknameisbase: tuple
            :param from_email: str
            :param recipient: str


            :description:
                checking whether the nickname entered by the user exists in the database,
                if it does not, it puts the entered data, and if it does, it throws an error
                sends a message to the mail

            :Used libraries: import psycopg2 as ps

        """



        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.sprawdzanieNik = self.conn.cursor()

        self.sprawdzanieNik.execute("SELECT nick  FROM bdgraczy WHERE nick = " + "'" + self.nick.get() +"'" )
        self.niknameisbase = self.sprawdzanieNik.fetchall()

        self.conn.commit()
        self.conn.close()
        self.sprawdzanieNik.close()


        if not self.niknameisbase:
            self.conn = ps.connect(
                "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
            self.sprawdzanieEmail = self.conn.cursor()

            self.sprawdzanieEmail.execute("SELECT email  FROM bdgraczy WHERE email = " + "'" +  self.adres_email.get() + "'")
            self.emailNot = self.sprawdzanieEmail.fetchall()

            self.conn.commit()
            self.conn.close()
            self.sprawdzanieEmail.close()

            if not self.emailNot:
                try:
                    """
                    wyslanie meila do gracza
                    
                    """
                    from_email = 'wisielcabyantondidytskyi@gmail.com'
                    password = 'zktn zfpc bcoi ecjd'

                    recipient = self.adres_email.get()


                    msg = MIMEMultipart()

                    msg['From'] = from_email
                    msg['To'] = recipient
                    msg['Subject'] = 'Wisielca. Successful registration!'


                    message = 'registration completed successfully!\n' \
                              '------------------------------------\n' \
                              '         account information        \n' \
                              '------------------------------------\n' \
                              'Nick: '+ self.nick.get()+ '\n' \
                              'Password: '+ self.haslo.get()+'\n' \
                              'E-mail address: ' +  self.adres_email.get() +'\n'\
                              'Gener: ' + self.plec.get()

                    msg.attach(MIMEText(message, 'plain'))

                    server = smtplib.SMTP('smtp.gmail.com: 587') # 587 = gmail
                    server.starttls()
                    server.login(from_email, password)
                    server.send_message(msg)
                    # server.sendmail(from_email, recipient, msg.as_string())
                    server.quit()

                    """"""

                    self.dodawanieDanych_do_bazy()


                except:
                    messagebox.showinfo('wrong data', 'you entered incorrect data, please try again\nbut the account was created')
                    self.dodawanieDanych_do_bazy()


            else:
                messagebox.showwarning('wiselca', 'This email is taken')


        else:
            messagebox.showwarning('wiselca', 'This nickname is taken')


    def dodawanieDanych_do_bazy(self):

        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.cur = self.conn.cursor()

        self.cur.execute("INSERT INTO bdgraczy (nick, email, plec, haslo, sciezka_do_avataru) VALUES " + \
                         "(" + "'" + self.nick.get() + "'" + "," + "'" + self.adres_email.get() +
                         "'" + "," + "'" + self.plec.get() + "'" + "," + "'" + self.haslo.get() + "'" + "," + "'" + self.avatar + "'" + ")")

        self.conn.commit()
        self.cur.close()
        self.conn.close()

        messagebox.showinfo('Crete', 'User has been created!')
        self.dodawanie_niku_do_bazy_points()
        self.okno_rejestracji.destroy()



