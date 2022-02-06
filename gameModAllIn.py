#-*- coding: utf-8 -*-
from tkinter import *
from dbslowa import DbRand
from tkinter import ttk, messagebox
import os
import psycopg2 as ps




class AllInGra(DbRand):

    def __init__(self, parent, title="Game mod allin", resizable=(False, False) ):
        """
            :description:
                .lift()
                    gives an advantage in the location of windows
                .iconbitmap
                    adds an icon to the application
                .title()
                    sets the title of the window


            :Used libraries:
                from tkinter import *
                from dbslowa import DbRand
                from tkinter import  ttk
                import os
                import psycopg2 as ps

            :param title: Game mod allin
            :param resizable: (False, False)
        """
        self.okienko_gryAllIn = Toplevel(parent)

        self.okienko_gryAllIn.title(title)
        self.okienko_gryAllIn.geometry('900x630')
        self.canvas = Canvas(self.okienko_gryAllIn,width = 900 , height = 630 )
        self.canvas.pack()
        self.okienko_gryAllIn.resizable(resizable[0], resizable[1])
        self.okienko_gryAllIn.lift()
        self.okienko_gryAllIn.iconbitmap('filesImages/icon.ico')

        self.start_pos_man()

        self.lifes()

        self.readtxt()
        self.dbpoints()
        self.nickIPointsIavatar()

        self.textHi = self.canvas.create_text(600, 300, font =('Futura PT Heave', 17), text = 'Welcome to the gameplay mode all-in\n'\
                                            'you can multiply your points\nor lose everything you have.\nPlay very carefully!',
                                              fill = 'blue', tag = 'HiText')




        self.topButton = ttk.Button(self.okienko_gryAllIn, text="\nnew word\n",  command = lambda :[ self.dbrand(), \
                                    self.delete_text(), self.randThems(),\
                                    self.start_pos_word(), self.lifes(), self.alphabet_start(), self.start_pos_man(),\
                                    self.dbpoints(), self.nickIPointsIavatar(),  self.posTimer() , self.timerStart(), self.disablebtn() ])
        self.topButton.place(relx=0.1, rely=0.8)


    def disablebtn(self):
        """
            :description: disabled button

        """
        self.topButton['state'] = 'disabled'

    def enabledBtn(self):
        """
            :description: enabled button, timer = 0 , delete label
        """
        self.stopTimer =0
        self.deleteLabel()
        self.topButton['state'] = 'enabled'



    def start_pos_man(self):
        """
            :description: draws the gallows

            :Used libraries:  from tkinter import *
        """

        self.lin1 = self.canvas.create_line(100, 460, 100, 90, width = 4  ) #cлева 1
        self.lin2 = self.canvas.create_line(90, 100, 900 //3, 100, width = 4) # сверху верхняя
        self.lin3 = self.canvas.create_line(900//3, 100, 900//3, 150, width =4) #сбоку
        self.lin4 = self.canvas.create_line(35,460, 300, 460, width=4)  #снизу

        self.lin5 = self.canvas.create_line(80,135,140,85, width =4 ) # косая сверху
        self.lin6 = self.canvas.create_line(100, 420, 50, 460, width = 4) # слева снизу косая
        self.lin7 = self.canvas.create_line(100,420, 150, 460, width = 4) # справа снизу косая



    def alphabet_start(self):
        """

            :param self.shift_x: int

            :param self.count: int
            :param buttons: list

            :description: places buttons with letters of the alphabet

            :Used libraries: from tkinter import *

        """


        global buttons
        self.shift_x = self.shift_y = 0
        self.count = 0

        buttons = []


        for c in range(ord("A"), ord("Z")+1):
            self.btn_alphabet = Button(self.okienko_gryAllIn, text = chr(c),  width=2, height=1, fg = 'black', bg = 'silver' )



            self.btn_alphabet.place( x =600+ self.shift_x, y = 400 - self.shift_y )
            self.btn_alphabet.bind('<Button-1>', lambda event: self.check_btn(event))



            self.shift_x +=40
            self.count +=1

            if self.count == 7:
                self.shift_x = self.count = 0
                self.shift_y -=50

            buttons.append(self.btn_alphabet)







    def randThems(self):
        """
            :description: displays the topic of the word

            :Used libraries: from tkinter import *
        """

        self.canvas.create_text(200, 30, text='Word theme: '+self.random_thems, fill="black", font=("Futura PT Heave ", 18), tag = 'rand_temat')





    def start_pos_word(self):
        """
            :param  label_word: list
            :param  label_under:  Label
            :param  self.shift: int

            :description: draws word length underscores

            :Used libraries: from tkinter import *
        """

        global  label_word, label_under
        label_word = []
        self.shift = 0

        for i in range(len(self.slowojoin)):

            label_under =  Label(self.canvas, text = '_', font = 'Arial 14', fg = 'purple')
            label_under.place(x = 400+ self.shift, y = 50)
            self.shift +=30

            label_word.append(label_under)


    def deleteLabel(self):
        """
            :description: delete label

        """

        for i in range(len(self.slowojoin)):
            label_word[i].destroy()

    # выводит на экран сколько у нас осталось жизни
    def lifes(self):
        """
            :param  lifes: int

            :description: displays the number of lives

            :Used libraries: from tkinter import *
        """


        global lifes_label, lifes
        lifes = 5

        lifes_text = Label(self.okienko_gryAllIn, text = 'lifes: ', font = ('Futura PT Heave ',20 ))
        lifes_text.place(x = 800,rely = 0.95)

        lifes_label = Label(self.okienko_gryAllIn, text = '{}'.format(lifes),font = ('Futura PT Heave ',20 ))
        lifes_label.place(x = 870, rely = 0.95)





    def posTimer(self):
        """
            :description: add timer

        """

        self.czas = 30
        self.stopTimer = 5
        self.labelTime = Label(self.okienko_gryAllIn, text = 'Time before line drawing: {}'.format(self.czas),
                               font = ('Futura PT Heave ',12 ), fg = 'purple')
        self.labelTime.place(relx = 0.68, rely = 0.55)



    def timerStart(self):
        """
            :param  self.czas: int
            :param  self.stopTimer: int
            :param  self.labelTime: Label

            :Used libraries: from tkinter import *
        """

        self.czas -=1

        if self.czas !=0:

            self.labelTime.config(text = 'Time before line drawing: {}'.format(self.czas))
            self.timerReload = self.okienko_gryAllIn.after(1000, self.timerStart)
        if self.czas == 0:
            # self.callBtn()
            self.testbtnclick()
            self.stopTimer -= 1

            self.czas = 30
            self.startTimer = self.okienko_gryAllIn.after(1000, self.timerStart)

        if self.stopTimer == 0:
            self.okienko_gryAllIn.after_cancel(self.timerReload)

        if self.czas == 10:
            self.labelTime.destroy()
            self.czas = 10
            self.labelTime = Label(self.okienko_gryAllIn, text='Time before line drawing: {}'.format(self.czas),
                                   font=('Futura PT Heave ', 12), fg='purple')
            self.labelTime.place(relx=0.68, rely=0.55)

    def testbtnclick(self):
        """
            :param check: str
            :param  pos: list
            :param licz_lifes: int
            :param life: int

            :description: checks if the user guessed the letter, if not, one life is taken away and the function of drawing human parts is called
        """



        global  life

        check = '/'
        pos = []

        for i in range(len(self.slowojoin)):
            if self.slowojoin[i] == check:
                pos.append(i)


        if pos:
            for i in pos:
                # self.canvas.itemconfig(label_word[i], text = '{}'.format(self.slowojoin[i]))
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
        """
            :param  check: str
            :param pos: list
            :param licz_lifes:  int
            :param life: int

            :description: checks if the user guessed the letter, if not, one life is taken away and the function of drawing human parts is called

        """

        global  life

        check = event.widget['text']
        pos = []

        for i in range(len(self.slowojoin)):
            if self.slowojoin[i] == check:
                pos.append(i)


        if pos:
            for i in pos:
                # self.canvas.itemconfig(label_word[i], text = '{}'.format(self.slowojoin[i]))
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
        """
            :param status: str
            :param punkty: int
            :description: in case of victory and defeat, it displays the corresponding inscription on the screen, also adds or subtracts points and calls the function for recording points in the table

            :Used libraries: from tkinter import *


        """

        global  punkty

        for btn in buttons:
            btn.destroy()

        if status == 'win':
            self.canvas.create_text(600, 300, font =('Futura PT Heave', 20), text = 'Congratulations on winning', fill = 'green', tag = 'winner')


            punkty = int(points_new) + abs(int(points_new)) +1
            self.newPunkty()
            print(punkty)
            self.enabledBtn()

        else:
            self.canvas.create_text(600, 300, font=('Futura PT Heave', 20), text='sorry you lost, try again ',
                                    fill='red', tag = 'loser')

            punkty = int(points_new)  - abs(int(points_new)) -1

            self.newPunkty()

            self.canvas.create_text(600, 30, text='search word :  ' + self.slowojoin, fill="black",
                                    font=("Futura PT Heave ", 18) \
                                    , tag='searchWord')

            self.enabledBtn()



    def draw(self, life):
        """

            :param life: int

            :description: checks the number of lives and draws lines according to their number

            :Used libraries: from tkinter import *

            :param life: int
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

            self.l_eye1 = self.canvas.create_line(285, 165, 290, 170, width=2 , tag = 'l_eye1')
            self.l_eye2 = self.canvas.create_line(290, 165, 285, 170, width = 2, tag = 'l_eye2')



            self.r_eye1 = self.canvas.create_line(310, 165, 315, 170, width=2, tag = 'r_eye1')
            self.r_eye2 = self.canvas.create_line(315, 165, 310, 170, width = 2, tag = 'r_eye2')

            self.gameOverr('lose')



    def readtxt(self):
        """

            :param f: File
            :param nick_is_points: str

            :description: reads txt file and gets values from there after reading it immediately deletes it
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
        """
            :param points_for_nick: tuple
            :param points_new: tuple

            :Used libraries: import psycopg2 as ps

            :return: tuple
        """


        global  points_for_nick, points_new

        # сделали обращение к базе points
        conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        nickname = conn.cursor()
        poin = conn.cursor()


        poin.execute("SELECT points FROM points WHERE nick = "+ "'"+  nick_is_points    +"'")

        points_for_nick =  " ".join(map(''.join, poin.fetchall()))

        #points_new - aktualna ilość punktów
        points_new = points_for_nick

        conn.commit()
        nickname.close()
        poin.close()

        conn.close()




    def nickIPointsIavatar(self):
        """

            :param self.labelNickGame: Label
            :param self.labelPoints: label

            :Description: displays nickname and number of points

            :Used libraries: from tkinter import *
        """


        self.labelNickGame = Label(self.okienko_gryAllIn, text = 'nick: ' + nick_is_points, font = ('Futura PT Heave ',20 ) )
        self.labelNickGame.place(relx = 0, rely = 0.95)



        self.labelPoints = Label(self.okienko_gryAllIn, text = 'points: '  ,  font  = ('Futura PT Heave ',20 ) ).place(relx = 0.4, rely =0.95)
        self.labelPointsNumber = self.canvas.create_text(520, 619, font=('Futura PT Heave', 20), text= points_new, tag = 'points')


    def newPunkty(self):
        """
            :param points.execute: database

            :Description: uploads the received points to the database

            :Used libraries: import psycopg2 as ps


        """
        conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        points = conn.cursor()

        points.execute("UPDATE points SET points =  "
                         + "'" +  str(punkty)  +"'" "WHERE nick = " + "'"+ nick_is_points  +"'"   )



        conn.commit()
        points.close()
        conn.close()


    def delete_text(self):
        """
            :description: clears the field after the end of the game

            :Used libraries: from tkinter import *
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
        self.canvas.delete('HiText')
        self.canvas.delete('points')
        self.canvas.delete('l_eye1')
        self.canvas.delete('l_eye2')
        self.canvas.delete('r_eye1')
        self.canvas.delete('r_eye2')
        self.canvas.delete('searchWord')





