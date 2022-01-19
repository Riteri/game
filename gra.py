#-*- coding: utf-8 -*-
from tkinter import *
from dbslowa import DbRand
from tkinter import  ttk

class Gra(DbRand):
    def __init__(self, parent, title="Wisielca", resizable=(False, False) ):
        #тут сделал по другому, потому что я дурак делал раньше сложнее((
        self.okienko_gry = Toplevel(parent)
        self.okienko_gry.title(title)
        self.canvas = Canvas(self.okienko_gry,width = 900 , height = 600 )
        self.canvas.pack()
        self.okienko_gry.resizable(resizable[0], resizable [1])
        self.okienko_gry.wm_attributes("-topmost", 1)
        self.okienko_gry.iconbitmap('filesImages/icon.ico')

        self.line()
        self.alphabet_start()
        self.start_pos_man()
















        #новое слово и новая тема (идет функция по рандому темы и функция по выписыванию с рандомной темы букв  очищает предыдущее ))
        ttk.Button(self.okienko_gry, text="\nnowe slowo\n",  command = lambda :[self.dbrand() , self.delete_text(), self.randThems(),
                                                                                self.start_pos_word()]).place(relx=0.1, rely=0.9)

        # ttk.Button(self.okienko_gry, text="\nnowe slowo\n",
        #            command=lambda: [self.json(), self.delete_text(), self.randThems(), self.start_pos_word()]).place(
        #     relx=0.1, rely=0.9)

    def line(self):
        y = 0
        while y < 600:
            x = 0
            while x < 900:
                self.canvas.create_rectangle(x, y, x + 33, y + 27, fill="white", outline="blue")
                x = x + 33
            y = y + 27


    def start_pos_man(self):
        self.lin1 = self.canvas.create_line(100, 400, 100, 100, width = 4  ) #cлева 1
        self.lin2 = self.canvas.create_line(100, 100, 900 //3, 100, width = 4) # сверху верхняя
        self.lin3 = self.canvas.create_line(900//3, 100, 900//3, 170, width =4) #сбоку



    def alphabet_start(self):
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
            # buttons.append(self.btn_alphabet.cget('text'))












    def test(self):
        self.textbtn = self.btn_alphabet.cget('text')
        print(self.textbtn)





    def randThems(self):

        self.canvas.create_text(200, 30, text='temat słowa: '+self.random_thems, fill="black", font="Courier 18", tag = 'rand_temat')


    def delete_text(self):
        self.canvas.delete('rand_temat')
        self.canvas.delete('word')






    #self.randomslowa это рандомное слово
    #рисует черточки вместо слова
    def start_pos_word(self):
        global  label_word, label_under
        label_word = []
        self.shift = 0




        for i in range(len(self.slowojoin)):

            # self.text_czertoczki = self.canvas.create_text((500 + self.shift, 50 ), text='_', font = 'Arial 14',fill="purple", tag = 'word')


            label_under =  Label(self.canvas, text = '_', font = 'Arial 14', fg = 'purple')
            label_under.place(x = 500+ self.shift, y = 50)
            self.shift +=30

            label_word.append(label_under)
            # label_word.append(self.text_czertoczki)

            """ 
            сделать еще удаление по нажатию кнопки
            пока что работает только с перезаходом 
            """



    def check_btn(self, event):


        check = event.widget['text']
        pos = []

        for i in range(len(self.slowojoin)):
            if self.slowojoin[i] == check:
                pos.append(i)

        if len(pos) != 0:
            for i in pos:
                label_word[i].config(text = '{}'.format(self.slowojoin[i]))


















