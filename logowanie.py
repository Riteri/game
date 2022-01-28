from tkinter import *
from tkinter import ttk
import psycopg2 as ps
from tkinter import messagebox

from gameModAllIn import AllInGra
from gra import  Gra
from remind import Remind



class Logowanie(Gra, AllInGra):
    def __init__(self, parent, width, height, title="Authorization", resizable=(False, False) ):
        """ Function - __init__

        Parameters
        ----------
        self.okno_logowania.iconbitmap: tkinter
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
        :param width: 400
        :param height: 300
        :param title: Logowanie
        :param resizable: (False, False)
        """

        self.okno_logowania = Toplevel(parent)
        self.okno_logowania.title(title)
        self.okno_logowania.geometry(f"{width}x{height}+300+150") # размеры+ отступ от краев экрана
        self.okno_logowania.resizable (resizable[0], resizable [1])
        self.okno_logowania.lift()
        self.okno_logowania.iconbitmap('filesImages/icon.ico')
        self.loguj()







    def loguj(self):
        """ Function - loguj

        Parameters
        ----------
        self.haslo_logowanie_bd: StringVar()
        nickname_logowanie_bd: StringVar()

        self.hi_loguj: Label
        self.nick_logowanie: ttk.Entry
            place to enter a nickname

        self.graj_i_zalogujsie: ttk.Button
            login button (word for game is  database )
        self.graj_i_zalogujsie_userhaslo: ttk.Button
            login button(the word for the game is entered by the user)

        Used libraries
        -------------
        tkinter import *
        tkinter import ttk
        """

        global nickname_logowanie_bd

        self.haslo_logowanie_bd = StringVar()
        nickname_logowanie_bd = StringVar()





        self.hi_loguj = Label(self.okno_logowania, text = "Login window, log in and play").pack()

        self.nick_logowanie = ttk.Entry(self.okno_logowania, width=30, justify=CENTER, textvariable = nickname_logowanie_bd).place(relx=0.3, rely=0.1)
        self.label_nick = Label(self.okno_logowania, text="Enter your nickname: ").place(relx=0.01, rely=0.1)

        self.haslo_logowanie = ttk.Entry(self.okno_logowania, width=30,justify=CENTER, textvariable= self.haslo_logowanie_bd, show ="*" ).place(relx= 0.3, rely = 0.2)
        self.haslo_logowanie_Label = Label(self.okno_logowania, text = 'Enter your password: ').place(relx= 0.01, rely = 0.2)



        self.graj_i_zalogujsie = ttk.Button(self.okno_logowania, text="Game mode: normal", command  = self.sprawdz_i_graj,  width = 20)\
            .place(relx=0.33, rely=0.3)
        self.graj_i_zalogujsie_userhaslo = ttk.Button(self.okno_logowania, text = "Game mode: All-in", command  = self.userGame,  width = 20)\
            .place(relx = 0.33, rely= 0.45)


        self.remind_password = ttk.Button(self.okno_logowania, text = 'Remind password', command = self.openWindowRemind)
        self.remind_password.place(relx = 0.7, rely = 0.9)


    def openWindowRemind(self):
        Remind(self.okno_logowania, title='remind password', resizable=(False, False))



    def points(self):
        """ Function points

        Parameters
        ----------
        self.nickpoints: database

        f: File

        description
        -----------
            writes nickname and points to txt file

        :return: tuple
        """

        # self.conn = ps.connect(
        #     "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        #
        # self.nickpoints = self.conn.cursor()
        #
        # self.nickpoints.execute("SELECT *  FROM points WHERE nick = " + "'" + nickname_logowanie_bd.get() + "'")
        #
        # self.pointsNickname  = self.nickpoints.fetchall()
        #
        #
        #
        # self.nicknamepointsjoin = " ".join(map(''.join, self.niknamelogowaniedb))

        #открываем файл и записываем туда ник и очки
        f = open('points.txt', 'w')
        f.write(str( nickname_logowanie_bd.get()))
        f.close()



    def sprawdz_i_graj(self):
        """ Function - sprawdz_i_graj

        Parameters
        ----------
        self.imie.execute: database
        self.niknamelogowaniedb: tuple

        description
        -----------
        checking if the entered nickname is in the database, if it matches,
        a window with the game opens, if the user is not found, an error is displayed

        :return: tuple, messagebox
        """

        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.imie = self.conn.cursor()
        self.pswrd = self.conn.cursor()




        self.imie.execute("SELECT nick, haslo  FROM bdgraczy WHERE nick = " + "'" + nickname_logowanie_bd.get() + "'"+
                    "and haslo= " + "'"+ self.haslo_logowanie_bd.get() + "'")

        self.niknamelogowaniedb = self.imie.fetchall()

        if not self.niknamelogowaniedb:

            messagebox.showwarning('wiselca', 'there is no such user, try again!')
        else:
            self.points()
            messagebox.showinfo('wiselca', 'you can start the game!\nAll words in English')


            Gra(self.okno_logowania, title = 'Gra', resizable = (False,False))



            Label(self.okno_logowania, text=self.niknamelogowaniedb, font="Courier 20").place(relx=0.01, rely=0.9)


        self.conn.close()
        self.imie.close()
        self.pswrd.close()





    def userGame(self):
        """ Function - userGame

        Parameters
        ----------
        self.imie.execute: database
        self.niknamelogowaniedb: tuple

        description
        -----------
        checking if the entered nickname is in the database, if it matches,
        a window with the game opens, if the user is not found, an error is displayed


        :return: tuple
        """


        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.imie = self.conn.cursor()
        self.imie.execute("SELECT nick, haslo  FROM bdgraczy WHERE nick = " + "'" + nickname_logowanie_bd.get() + "'"+
                    "and haslo= " + "'"+ self.haslo_logowanie_bd.get() + "'")

        self.niknamelogowaniedb = self.imie.fetchall()


        if not self.niknamelogowaniedb:

            messagebox.showwarning('wiselca', 'there is no such user, try again!')
        else:
            self.points()
            messagebox.showinfo('wiselca', 'you can start the game!\nAll words in English')
            AllInGra(self.okno_logowania, title = 'Gra', resizable = (False,False))
            Label(self.okno_logowania, text=self.niknamelogowaniedb, font="Courier 20").place(relx=0.01, rely=0.9)


        self.conn.close()
        self.imie.close()










