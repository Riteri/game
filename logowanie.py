from tkinter import *
from tkinter import ttk
import psycopg2 as ps
from tkinter import messagebox
from gra import Gra
from gameHasloOduser import UserGame


class Logowanie:
    def __init__(self, parent, width, height, title="Wisielca", resizable=(False, False), ):

        self.okno_logowania = Toplevel(parent)
        self.okno_logowania.title(title)
        self.okno_logowania.geometry(f"{width}x{height}+300+150") # размеры+ отступ от краев экрана
        self.okno_logowania.resizable (resizable[0], resizable [1])
        # self.window1.wm_attributes("-topmost",1)
        self.okno_logowania.lift()
        self.okno_logowania.iconbitmap('filesImages/icon.ico')
        self.loguj()

        # Button(self.okno_logowania, text = 'graj', command = self.okno_gryself, width=10, height=1).place(relx = 0.45, rely = 0.4)



    def loguj(self):

        global nickname_logowanie_bd

        self.haslo_logowanie_bd = StringVar()
        nickname_logowanie_bd = StringVar()



        self.hi_loguj = Label(self.okno_logowania, text = "Okno dla logowania, zaloguj się i graj").pack()

        self.nick_logowanie = ttk.Entry(self.okno_logowania, width=30, justify=CENTER, textvariable = nickname_logowanie_bd).place(relx=0.3, rely=0.1)
        self.label_nick = Label(self.okno_logowania, text="Wpisz swój nick: ").place(relx=0.01, rely=0.1)

        # self.haslo_logowanie = Entry(self.okno_logowania, width=30, justify=CENTER, insertofftime=300, show="*", textvariable = self.haslo_logowanie_bd) \
        #     .place(relx=0.3, rely=0.2)
        # self.label_haslo = Label(self.okno_logowania, text="Wpisz hasło: ").place(relx=0.01, rely=0.2)

        self.graj_i_zalogujsie = ttk.Button(self.okno_logowania, text="zalogować się\nhaslo od komputera", command  = self.sprawdz_i_graj).place(relx=0.33, rely=0.3)
        self.graj_i_zalogujsie_userhaslo = ttk.Button(self.okno_logowania, text = "zalogować się\nhaslo od uzytkownika", command  = self.userGame).place(relx = 0.33, rely= 0.5)

    def sprawdz_i_graj(self):



        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.imie = self.conn.cursor()
        self.pswrd = self.conn.cursor()




        self.imie.execute("SELECT nick  FROM bdgraczy WHERE nick = " + "'" + nickname_logowanie_bd.get() + "'")

        self.niknamelogowaniedb = self.imie.fetchall()

        if not self.niknamelogowaniedb:

            messagebox.showwarning('wiselca', 'nie ma takiego użytkownika, sprobuj ponownie!')
        else:

            messagebox.showinfo('wiselca', 'możesz zaczynać gre!')
            #сделать лейбл на главном экране и отблокировать кнопку игры и в поле игры тоже добавить ник
            Gra(self.okno_logowania, title = 'Gra', resizable = (False,False))
            # self.okno_logowania.destroy()

            Label(self.okno_logowania, text=self.niknamelogowaniedb, font="Courier 20").place(relx=0.01, rely=0.9)


        self.conn.close()
        self.imie.close()
        self.pswrd.close()





    def userGame(self):

        self.conn = ps.connect(
            "host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        self.imie = self.conn.cursor()
        self.imie.execute("SELECT nick  FROM bdgraczy WHERE nick = " + "'" + nickname_logowanie_bd.get() + "'")

        self.niknamelogowaniedb = self.imie.fetchall()


        if not self.niknamelogowaniedb:

            messagebox.showwarning('wiselca', 'nie ma takiego użytkownika, sprobuj ponownie!')
        else:
            messagebox.showinfo('wiselca', 'możesz zaczynać gre!')
            # сделать лейбл на главном экране и отблокировать кнопку игры и в поле игры тоже добавить ник
            UserGame(self.okno_logowania, title = 'Gra', resizable = (False,False))
            Label(self.okno_logowania, text=self.niknamelogowaniedb, font="Courier 20").place(relx=0.01, rely=0.9)


        self.conn.close()
        self.imie.close()









