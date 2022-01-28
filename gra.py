#-*- coding: utf-8 -*-
from tkinter import *
from dbslowa import DbRand
from tkinter import ttk, messagebox
import os
import psycopg2 as ps
# import threading
# import schedule
# import time
# from threading import Timer



class Gra(DbRand):

    def __init__(self, parent, title="game mod normal", resizable=(False, False) ):
        """ Function - __init__

        description
        -----------
        .lift()
            gives an advantage in the location of windows
        .iconbitmap
            adds an icon to the application
        .title()
            sets the title of the window


        Used libraries
        --------------
        from tkinter import *
        from dbslowa import DbRand
        from tkinter import  ttk
        import os
        import psycopg2 as ps
        import threading
        import schedule
        import time
        from threading import Timer


        :param parent:
        :param title: Gra
        :param resizable: (False, False)
        """
        self.okienko_gry = Toplevel(parent)

        self.okienko_gry.title(title)
        self.okienko_gry.geometry('900x630')
        self.canvas = Canvas(self.okienko_gry,width = 900 , height = 630 )
        self.canvas.pack()
        self.okienko_gry.resizable(resizable[0], resizable[1])
        self.okienko_gry.lift()
        self.okienko_gry.iconbitmap('filesImages/icon.ico')

        self.start_pos_man()
        self.lifes()
        self.readtxt()
        self.dbpoints()
        self.nickIPointsIavatar()




        self.topButton = ttk.Button(self.okienko_gry, text="\nnew word\n",  command = lambda :[ self.dbrand(),\
                                    self.delete_text(), self.randThems(),\
                                    self.start_pos_word(), self.lifes(), self.alphabet_start(),\
                                    self.dbpoints(), self.nickIPointsIavatar(),self.posTimer() , self.timerStart(), self.disablebtn() ])
        self.topButton.place(relx=0.1, rely=0.8)




    def disablebtn(self):
        self.topButton['state'] = 'disabled'

    def enabledBtn(self):
        self.stopTimer =0

        self.deleteLabel()

        self.topButton['state'] = 'enabled'




    def line(self):
        """Function - line

        Parameters
        ----------
        y: int
        x: int

        description
        -----------
        draws lines creating a notebook effect

        Used libraries
        --------------
        from tkinter import *

        """
        y = 0
        while y < 680:
            x = 0
            while x < 900:
                self.canvas.create_rectangle(x, y, x + 33, y + 27, fill="white", outline="blue")
                x = x + 33
            y = y + 27


    def start_pos_man(self):
        """ Function start_pos_man

        description
        -----------
        draws the gallows

        Used libraries
        --------------
        from tkinter import *

        """
        self.lin1 = self.canvas.create_line(100, 460, 100, 100, width = 4  ) #cлева 1
        self.lin2 = self.canvas.create_line(100, 100, 900 //3, 100, width = 4) # сверху верхняя
        self.lin3 = self.canvas.create_line(900//3, 100, 900//3, 150, width =4) #сбоку
        self.lin4 = self.canvas.create_line(50,460, 300, 460, width=4)






    def alphabet_start(self):
        """ Function alphabet_start

        Parameters
        ----------
        self.shift_x: int
        self.count: int
        buttons: list

        description
        -----------
        places buttons with letters of the alphabet

        Used libraries
        --------------
        from tkinter import *

        """


        global buttons
        self.shift_x = self.shift_y = 0
        self.count = 0

        buttons = []


        for c in range(ord("A"), ord("Z")+1):
            self.btn_alphabet = Button(self.okienko_gry, text = chr(c),  width=2, height=1, fg = 'black', bg = 'silver')



            self.btn_alphabet.place( x =600+ self.shift_x, y = 400 - self.shift_y )
            self.btn_alphabet.bind('<Button-1>', lambda event: self.check_btn(event))


            self.shift_x +=40
            self.count +=1

            if self.count == 7:
                self.shift_x = self.count = 0
                self.shift_y -=50

            buttons.append(self.btn_alphabet)







    def randThems(self):
        """Function -  randThems

        description
        -----------
        displays the topic of the word

        Used libraries
        --------------
        from tkinter import *

        """

        self.canvas.create_text(200, 30, text='Word theme: '+self.random_thems, fill="black", font=("Futura PT Heave ", 18), tag = 'rand_temat')





    def start_pos_word(self):
        """ Function - start_pos_word

        Parameters
        ----------
        label_word: list
        label_under: Label
        self.shift: int

        description
        -----------
        draws word length underscores

        Used libraries
        --------------
        from tkinter import *

        """

        global  label_word, label_under
        label_word = []
        label_test_list = []
        self.shift = 0


        for i in range(len(self.slowojoin)):
            label_under =  Label(self.canvas, text = '_', font = 'Arial 14', fg = 'purple')
            label_under.place(x = 400+ self.shift, y = 50)
            self.shift +=30

            label_word.append(label_under)



    def deleteLabel(self):
        for i in range(len(self.slowojoin)):
            label_word[i].destroy()


    # выводит на экран сколько у нас осталось жизни
    def lifes(self):
        """Function lifes

        Parameters
        ----------
        lifes: int

        description
        -----------
        displays the number of lives

        Used libraries
        --------------
        from tkinter import *

        """


        global lifes_label, lifes
        lifes = 5

        lifes_text = Label(self.okienko_gry, text = 'lifes: ', font = ('Futura PT Heave ',20 ))
        lifes_text.place(x = 800,rely = 0.95)

        lifes_label = Label(self.okienko_gry, text = '{}'.format(lifes),font = ('Futura PT Heave ',20 ))
        lifes_label.place(x = 870, rely = 0.95)


    def posTimer(self):
        self.czas = 30
        self.stopTimer = 5
        self.labelTime = Label(self.okienko_gry, text = 'czas przed rysowaniem linii: {}'.format(self.czas),
                               font = ('Futura PT Heave ',12 ), fg = 'purple')
        self.labelTime.place(relx = 0.68, rely = 0.55)



    def timerStart(self):
        """ Function timerStart

        Parameters
        ----------
        self.czas: int
        self.stopTimer: int
        self.labelTime: Label

        Used libraries
        --------------
        from tkinter import *
        """


        self.czas -=1

        if self.czas !=0:

            self.labelTime.config(text = 'czas przed rysowaniem linii: {}'.format(self.czas))
            self.timerReload = self.okienko_gry.after(1000, self.timerStart)
        if self.czas == 0:
            # self.callBtn()
            self.testbtnclick()
            self.stopTimer -= 1

            self.czas = 30
            self.startTimer = self.okienko_gry.after(1000, self.timerStart)

        if self.stopTimer == 0:
            self.okienko_gry.after_cancel(self.timerReload)



    #
    # def callBtn(self):
    #     if self.czas == 0:
    #         self.testbtnclick()
    #     else:
    #         pass




    # костыли xd но работает , тут я сделал просто функцию
    def testbtnclick(self):
        """ Function - testbtnclick

        parameter
        ---------
        check: str
        pos: list
        licz_lifes: int
        life: int

        description
        -----------
        checks if the user guessed the letter, if not, one life is taken away and the function of drawing human parts is called
        """


        global  life

        check = '/'
        pos = []

        for i in range(len(self.slowojoin)):
            if self.slowojoin[i] == check:
                pos.append(i)

        if pos:
            for i in pos:
                label_word[i].config(text = '{}'.format(self.slowojoin[i]))

            licz_lifes = 0

            for i in label_word:
                if  i['text'].isalpha():
                    licz_lifes +=1

            if licz_lifes == len(self.slowojoin):
                self.gameOverr('win')

        else:
            life = int (lifes_label.cget('text') ) -1
            lifes_label.config(text = '{}'.format(life))

            if life != 0:
                lifes_label.config(text='{}'.format(life))

            self.draw(life)




    def check_btn(self, event):
        """Function - check_btn


        parameter
        ---------
        check: str
        pos: list
        licz_lifes: int
        life: int

        description
        -----------
        checks if the user guessed the letter, if not, one life is taken away and the function of drawing human parts is called


        :param event:
        :return:
        """

        global  life

        check = event.widget['text']
        pos = []

        for i in range(len(self.slowojoin)):
            if self.slowojoin[i] == check:
                pos.append(i)

        if pos:
            for i in pos:
                label_word[i].config(text = '{}'.format(self.slowojoin[i]))

            licz_lifes = 0

            for i in label_word:
                if  i['text'].isalpha():
                    licz_lifes +=1

            if licz_lifes == len(self.slowojoin):
                self.gameOverr('win')

        else:
            life = int (lifes_label.cget('text') ) -1
            lifes_label.config(text = '{}'.format(life))

            if life != 0:
                lifes_label.config(text='{}'.format(life))

            self.draw(life)





    def gameOverr(self, status):
        """ Function - game overr

        description
        -----------
        in case of victory and defeat, it displays the corresponding inscription on the screen,
        also adds or subtracts points and calls the function for recording points in the table

        Used libraries
        --------------
        from tkinter import *

        :param status: str
        """

        global  punkty

        for btn in buttons:
            btn.destroy()

        if status == 'win':
            self.canvas.create_text(600, 300, font =('Futura PT Heave', 20), text = 'Gratuluję z wygraniem', fill = 'green', tag = 'winner')


            punkty = len(self.slowojoin)*1+ int(points_new)
            self.newPunkty()
            print(punkty)
            self.enabledBtn()

        else:
            self.canvas.create_text(600, 300, font=('Futura PT Heave', 20), text='Niestety przegrałeś, \n sprobuj ponownie ',
                                    fill='red', tag = 'loser')

            punkty = len(self.slowojoin) * (-1)  + int(points_new)

            self.newPunkty()
            self.enabledBtn()




    def draw(self, life):
        """ Function - draw

        Parameters
        -----------
        life : int

        description
        -----------
        checks the number of lives and draws lines according to their number

        Used libraries
        --------------
        from tkinter import *

        :param life: int
        :return:
        """



        if life == 4:
            self.head  = self.canvas.create_oval(270, 150, 330, 210 , width=3, tag = 'head')
        elif life == 3:
            self.body = self.canvas.create_line(300, 208, 300, 320, width=3, tag = 'body')
        elif life == 2:
            self.l_hand = self.canvas.create_line(300, 220, 250,320, width = 3, tag = 'lhand' )
        elif life == 1:
            self.r_hand = self.canvas.create_line(300, 220, 350, 320, width=3, tag = 'rhand')

        elif life == 0:
            self.l_foot = self.canvas.create_line(300, 320, 250, 430, width=3, tag = 'lfoot')
            self.r_foot = self.canvas.create_line(300, 320, 350, 430, width=3, tag = 'rfoot')

            self.gameOverr('lose')



    def readtxt(self):
        """ Function -  readtxt

        Parameters
        -----------
        f: File
        nick_is_points: str

        description
        -----------
        reads txt file and gets values from there
        after reading it immediately deletes it

        """

        global nick_is_points

        f = open('points.txt', 'r')
        # теперь наш ник и очки в переменной nick_i_points
        nick_is_points = f.read()
        # print(nick_is_points)
        f.close()

        # и сразу удаляем файл
        os.remove('points.txt')


    # тут обращаюсь к 2м базам и достаю из них данные, с базы points достаю ник и очки
    def dbpoints(self):
        """ Function dbpoints

        Parameters
        ----------
        points_for_nick: tuple
        points_new: tuple


        Used libraries
        --------------
        import psycopg2 as ps

        :return: tuple
        """

        global  points_for_nick, points_new

        # сделали обращение к базе points
        conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        nickname = conn.cursor()
        poin = conn.cursor()


        poin.execute("SELECT points FROM points WHERE nick = "+ "'"+  nick_is_points    +"'")

        points_for_nick =  " ".join(map(''.join, poin.fetchall()))

        points_new = points_for_nick

        conn.commit()
        nickname.close()
        poin.close()

        conn.close()




    def nickIPointsIavatar(self):

        """ Function - nickIPointsIavatar

        Parameters
        ----------
          self.labelNickGame: Label
          self.labelPoints: label

        Description
        -----------
        displays nickname and number of points

        Used libraries
        --------------
        from tkinter import *

        """

        self.labelNickGame = Label(self.okienko_gry, text = 'nick: ' + nick_is_points, font = ('Futura PT Heave ',20 ) )
        self.labelNickGame.place(relx = 0, rely = 0.95)



        self.labelPoints = Label(self.okienko_gry, text = 'points: ' ,  font  = ('Futura PT Heave ',20 ) ).place(relx = 0.4, rely =0.95)
        self.labelPointsNumber = self.canvas.create_text(520, 619, font=('Futura PT Heave', 20), text=points_new, tag='points')



    # загружает в таблицу наши пункты
    def newPunkty(self):
        """ Function -  newPunkty

        Parameters
        ----------
         points.execute: database

         Description
         -----------
         uploads the received points to the database

         Used libraries
         --------------
         import psycopg2 as ps

        """
        conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        points = conn.cursor()

        points.execute("UPDATE points SET points =  "
                         + "'" +  str(punkty)  +"'" "WHERE nick = " + "'"+ nick_is_points  +"'"   )



        conn.commit()
        points.close()
        conn.close()





    def delete_text(self):
        """Function -  delete_text

        description
        -----------
        clears the field after the end of the game

        Used libraries
        --------------
        from tkinter import *

        """
        self.canvas.delete('rand_temat')
        self.canvas.delete('winner')
        self.canvas.delete('loser')
        self.canvas.delete('word')
        self.canvas.delete('head')
        self.canvas.delete('body')
        self.canvas.delete('lhand')
        self.canvas.delete('rhand')
        self.canvas.delete('lfoot')
        self.canvas.delete('rfoot')
        self.canvas.delete('points')





    # points_new


