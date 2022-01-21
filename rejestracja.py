from tkinter import *
from tkinter import  ttk
from tkinter import filedialog
import psycopg2 as ps
from tkinter import messagebox


class Rejestracja :
    def __init__(self, parent, width, height, title="Okno rejestracji", resizable=(False, False) ):
        """Function __init__ class Rejestracja

        Parameters
        ----------
         self.okno_rejestracji: Toplevel tkinter
        self.okno_rejestracji.iconbitmap: tkinter
            adds an icon to the application

        description
        -----------
        .lift()
            gives an advantage in the location of windows
        .iconbitmap
            adds an icon to the application
        .title()
            sets the title of the window



        :param parent:
        :param width: 500
        :param height: 400
        :param title: Okno rejestracji
        :param resizable: (False, False)
        """

        self.okno_rejestracji = Toplevel(parent)
        self.okno_rejestracji.title(title)
        self.okno_rejestracji.geometry(f"{width}x{height}+700+150") # размеры+ отступ от краев экрана
        self.okno_rejestracji.resizable (resizable[0], resizable [1])
        # self.window1.wm_attributes("-topmost",1)
        self.okno_rejestracji.lift()
        self.okno_rejestracji.iconbitmap('filesImages/icon.ico')
        self.rej()








    def rej(self):
        """ Function - rej (rejestracja (pl)) (registration)

            Parameters
            ----------
            self.nick: StringVar()
            self.adres_email: StringVar()
            self.plec: StringVar()
            self.haslo: StringVar()
            Label: tkinter.Label

            self.hi_rej : Label
                label with text - (okno dla rejestracji, wpisz swoje danne)

            self.nick_rejestracja: ttk.Entry
                place to enter a nickname

            self.adres_email_rejestracja: ttk.Entry
                place to enter a e-mail

            self.plec_rejestracja: ttk.Entry
                place to indicate gender

            self.avatar_rejestracja: ttk.Button
                opens a window for choosing an avatar

            self.save_dane_rejestracja: ttk.Button
                button for saving data to the database with the command -  self.sprawdzanie_nicknamu()

            Used libraries
            --------------
            tkinter import *
            tkinter import ttk

        :return: str
        """


        self.nick = StringVar()
        self.adres_email = StringVar()
        self.plec = StringVar()
        self.haslo = StringVar()




        self.hi_rej = Label(self.okno_rejestracji, text = "okno dla rejestracji, wpisz swoje danne").pack()
        #insertofftime это та палочка что бы видно было куда пишем (300 это 300 мс )
        #justify это положение текста
        self.nick_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER ,  textvariable =self.nick)\
            .place(relx=0.3, rely=0.1)
        self.label_nick_rejestracja = Label(self.okno_rejestracji,  text = "Wpisz swój nick: "). place(relx = 0.01, rely = 0.1)


        self.adres_email_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER , textvariable = self.adres_email)\
            .place(relx = 0.3, rely=0.20)
        self.label_adres_email_rejestracja = Label (self.okno_rejestracji, text = "Wpisz swój adres e-mail: ").place(relx = 0.01, rely = 0.20)


        self.plec_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER , textvariable = self.plec)\
            .place(relx = 0.3, rely= 0.30)
        self.label_plec_rejestracja = Label (self.okno_rejestracji, text = "Wpisz płeć (M/K): ").place(relx = 0.01, rely = 0.30)


        self.haslo_rejestracja = ttk.Entry(self.okno_rejestracji, width = 30,  justify = CENTER , show ="*", textvariable = self.haslo)\
            .place(relx = 0.3, rely = 0.40)
        self.label_haslo_rejestracja = Label(self.okno_rejestracji, text = "Wymyśł hasło: ").place(relx = 0.01, rely = 0.40)


        self.avatar_rejestracja = ttk.Button(self.okno_rejestracji, text="dodaj avatar",  command = self.avatar).place(relx=0.45, rely=0.5)

        self.save_dane_rejestracja = ttk.Button(self.okno_rejestracji, text="zapisać",
                                            command = lambda :[ self.sprawdzanie_nicknamu() ])\
            .place(relx = 0.45, rely = 0.6)


    def dodawanie_niku_do_bazy_points(self):
        """ Function - dodawanie_niku_do_bazy_points

            Parameters
            ----------
            self.newNickPoints.execute: database
                adding a nickname and points to the database points (initially 0 )

            Used libraries
            --------------
            import psycopg2 as ps

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
        """ Function  avatar
            Parameters
            ----------

            self.avatar:askopenfilename
                opens a window and asks the user to select a file

            Used libraries
                from tkinter import filedialog
        """
        self.avatar = filedialog.askopenfilename(parent=self.okno_rejestracji)




    def sprawdzanie_nicknamu(self):
        """ Function - sprawdzanie_nicknamu

            Parameters
            ----------
            self.sprawdzanieNik: database
                makes a query to the database and places the result in a variable self.niknameisbase

            self.niknameisbase: tuple


            description
            -----------
            checking whether the nickname entered by the user exists in the database,
            if it does not, it puts the entered data, and if it does, it throws an error



            Used libraries
            --------------
            import psycopg2 as ps

        :return: messagebox, tuple
        """



        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.sprawdzanieNik = self.conn.cursor()

        self.sprawdzanieNik.execute("SELECT nick  FROM bdgraczy WHERE nick = " + "'" + self.nick.get() +"'" )
        self.niknameisbase = self.sprawdzanieNik.fetchall()


        if not self.niknameisbase:
            self.conn = ps.connect(
                "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
            self.cur = self.conn.cursor()

            self.cur.execute("INSERT INTO bdgraczy (nick, email, plec, haslo, sciezka_do_avataru) VALUES " + \
                             "(" + "'" + self.nick.get() + "'" + "," + "'" + self.adres_email.get() +
                             "'" + "," + "'" + self.plec.get() + "'" + "," + "'" + self.haslo.get() + "'" + "," + "'" + self.avatar + "'" + ")")

            messagebox.showinfo('Crete', 'użytkownik zostal stworzony!')
            self.dodawanie_niku_do_bazy_points()
            self.okno_rejestracji.destroy()



            self.conn.commit()
            self.cur.close()
            self.conn.close()





        else:
            messagebox.showwarning('wiselca', 'Ten nickname jest zajęty')

        self.sprawdzanieNik.close()
        self.conn.close()





