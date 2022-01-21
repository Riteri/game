#-*- coding: utf-8 -*-
from tkinter import *
from tkinter import  ttk
import os
import psycopg2 as ps
import threading
import schedule
import time
from threading import Timer



class UserGame:

    def __init__(self, parent, title="Wisielca", resizable=(False, False) ):
        #тут сделал по другому, потому что я дурак делал раньше сложнее((
        self.graUser = Toplevel(parent)

        self.graUser.title(title)
        self.graUser.geometry('900x680')
        self.canvas = Canvas(self.graUser,width = 900 , height = 600 )
        self.canvas.pack()
        self.graUser.resizable(resizable[0], resizable[1])
        self.graUser.wm_attributes("-topmost", 1)
        self.graUser.iconbitmap('filesImages/icon.ico')

        # self.line()
        # self.alphabet_start()
        self.start_pos_man()

        self.lifes()

        self.readtxt()
        self.dbpoints()
        self.nickIPointsIavatar()

        self.haslo_i_temat()

        Label(self.graUser, text = 'haslo muśi być wielkimi literami!', font = ('Futura PT Heave ',15 )).place(relx= 0.35, rely = 0)



        #новое слово и новая тема (идет функция по рандому темы и функция по выписыванию с рандомной темы букв  очищает предыдущее ))
        ttk.Button(self.graUser, text="\nnowe slowo\n",  command = lambda :[ self.saveInput(), self.delete_text(), self.randThems(),
                                    self.start_pos_word(), self.lifes(), self.alphabet_start(), self.start_pos_man(),
                                                                  self.dbpoints(), self.nickIPointsIavatar(), self.test()])\
            .place(relx=0.1, rely=0.8)


    def start_pos_man(self):
        self.lin1 = self.canvas.create_line(100, 400, 100, 100, width = 4  ) #cлева 1
        self.lin2 = self.canvas.create_line(100, 100, 900 //3, 100, width = 4) # сверху верхняя
        self.lin3 = self.canvas.create_line(900//3, 100, 900//3, 150, width =4) #сбоку







    def alphabet_start(self):
        global buttons
        self.shift_x = self.shift_y = 0
        self.count = 0

        buttons = []


        for c in range(ord("A"), ord("Z")+1):
            self.btn_alphabet = Button(self.graUser, text = chr(c),  width=2, height=1, fg = 'black', bg = 'silver')



            self.btn_alphabet.place( x =600+ self.shift_x, y = 400 - self.shift_y )
            self.btn_alphabet.bind('<Button-1>', lambda event: self.check_btn(event))


            self.shift_x +=40
            self.count +=1

            if self.count == 7:
                self.shift_x = self.count = 0
                self.shift_y -=50

            buttons.append(self.btn_alphabet)







    def randThems(self):

        self.canvas.create_text(200, 75, text='temat słowa: '+self.tematUser, fill="black", font=("Futura PT Heave ", 18), tag = 'rand_temat')


    def delete_text(self):
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





    #self.randomslowa это рандомное слово
    #рисует черточки вместо слова
    def start_pos_word(self):
        global  label_word, label_under
        label_word = []
        self.shift = 0

        # testperemennaja = len(self.hasloUser)

        # for i in range(len(self.hasloUser)):
        for i in range(len(self.hasloUser)):

            # label_undertext = self.canvas.create_text((500 + self.shift, 50 ), text='_', font = 'Arial 14',fill="purple", tag = 'word')

            label_under =  Label(self.canvas, text = '_', font = 'Arial 14', fg = 'purple')
            label_under.place(x = 500+ self.shift, y = 50)
            self.shift +=30

            label_word.append(label_under)

            # label_word.append(self.text_czertoczki)

    # выводит на экран сколько у нас осталось жизни
    def lifes(self):
        global lifes_label, lifes
        lifes = 5

        lifes_text = Label(self.graUser, text = 'życie ', font = ('Futura PT Heave ',20 ))
        lifes_text.place(x = 800, y = 10)

        lifes_label = Label(self.graUser, text = '{}'.format(lifes),font = ('Futura PT Heave ',20 ))
        lifes_label.place(x = 870, y = 10)







    def test(self):

        threading.Timer(30.0, self.testbtnclick).start()
        threading.Timer(60.0, self.testbtnclick).start()
        threading.Timer(90.0, self.testbtnclick).start()
        threading.Timer(120.0, self.testbtnclick).start()
        threading.Timer(150.0, self.testbtnclick).start()


    # костыли xd но работает , тут я сделал просто функцию
    def testbtnclick(self):
        global  life

        check = '/'
        pos = []

        for i in range(len(self.hasloUser)):
            if self.hasloUser[i] == check:
                pos.append(i)

        # if len(pos) != 0:
        if pos:
            for i in pos:
                # self.canvas.itemconfig(label_word[i], text = '{}'.format(self.hasloUser[i]))
                label_word[i].config(text = '{}'.format(self.hasloUser[i]))

            licz_lifes = 0

            for i in label_word:
                if  i['text'].isalpha():
                    licz_lifes +=1

            if licz_lifes == len(self.hasloUser):
                self.gameOverr('win')

        else:
            life = int (lifes_label.cget('text') ) -1
            lifes_label.config(text = '{}'.format(life))

            if life != 0:
                lifes_label.config(text='{}'.format(life))

            self.draw(life)




    def check_btn(self, event):
        global  life

        check = event.widget['text']
        pos = []

        for i in range(len(self.hasloUser)):
            if self.hasloUser[i] == check:
                pos.append(i)

        # if len(pos) != 0:
        if pos:
            for i in pos:
                # self.canvas.itemconfig(label_word[i], text = '{}'.format(self.hasloUser[i]))
                label_word[i].config(text = '{}'.format(self.hasloUser[i]))

            licz_lifes = 0

            for i in label_word:
                if  i['text'].isalpha():
                    licz_lifes +=1

            if licz_lifes == len(self.hasloUser):
                self.gameOverr('win')

        else:
            life = int (lifes_label.cget('text') ) -1
            lifes_label.config(text = '{}'.format(life))

            if life != 0:
                lifes_label.config(text='{}'.format(life))

            self.draw(life)





    def gameOverr(self, status):

        global  punkty

        for btn in buttons:
            btn.destroy()

        if status == 'win':
            self.canvas.create_text(600, 300, font =('Futura PT Heave', 20), text = 'Gratuluję z wygraniem', fill = 'green', tag = 'winner')


            punkty = len(self.hasloUser)*1+ int(points_new)
            self.newPunkty()
            print(punkty)

        else:
            self.canvas.create_text(600, 300, font=('Futura PT Heave', 20), text='Niestety przegrałeś, \n sprobuj ponownie ',
                                    fill='red', tag = 'loser')

            punkty = len(self.hasloUser) * (-1)  + int(points_new)

            self.newPunkty()

            # print(punkty)



    def draw(self, life):



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
        global  all_points_nick, points_for_nick, points_new, sciezka_do_avataru

        # сделали обращение к базе points
        conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        nickname = conn.cursor()
        poin = conn.cursor()


        # тут у нас очки  points_new

        poin.execute("SELECT points FROM points WHERE nick = "+ "'"+  nick_is_points    +"'")

        points_for_nick =  " ".join(map(''.join, poin.fetchall()))

        points_new = points_for_nick




        conn.commit()
        nickname.close()
        poin.close()

        conn.close()




    def nickIPointsIavatar(self):

        self.labelNickGame = Label(self.graUser, text = 'nick: ' + nick_is_points, font = ('Futura PT Heave ',20 ) )
        self.labelNickGame.place(relx = 0, rely = 0.95)



        self.labelPoints = Label(self.graUser, text = 'points: ' + points_new ,  font  = ('Futura PT Heave ',20 ) ).place(relx = 0.4, rely =0.95)




    # загружает в таблицу наши пункты
    def newPunkty(self):
        conn = ps.connect("host = 212.182.24.105 port=15432 dbname = student28 user = student28 password = anton123")
        points = conn.cursor()

        points.execute("UPDATE points SET points =  "
                         + "'" +  str(punkty)  +"'" "WHERE nick = " + "'"+ nick_is_points  +"'"   )



        conn.commit()
        points.close()
        conn.close()






    def haslo_i_temat(self):
        self.hasloUserStringVar = StringVar()
        self.tematUserStringVar = StringVar()

        self.hasloUserLabelEntry = ttk.Entry(self.graUser, width=30, justify=CENTER, textvariable= self.hasloUserStringVar,  show ="*") \
            .place(x =100, y = 0)
        self.hasloUserLabel = ttk.Label(self.graUser, text="Wpisz haslo: ").place(x = 0, y = 0)


        self.tematUserEntry = ttk.Entry(self.graUser, width=30, justify=CENTER,
                                    textvariable=self.tematUserStringVar,  show ="*") \
            .place(x = 100, y = 30)
        self.tematUserLabel = ttk.Label(self.graUser, text="Wpisz temat: ").place(x = 0, y = 30)

        ttk.Button(self.graUser, text = 'Grać',  command = lambda :[self.saveInput(), self.delete_text(), self.start_pos_word(), self.randThems()])\
            .place(relx=0.05, rely=0.9)



    def saveInput(self):


        self.hasloUser = self.hasloUserStringVar.get()
        self.tematUser = self.tematUserStringVar.get()

        print(self.hasloUser)
        print(self.tematUser)

