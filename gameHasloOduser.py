from tkinter import *
from tkinter import  ttk


class UserGame:
    def __init__(self, parent, title="Wisielca", resizable=(False, False)):
        # тут сделал по другому, потому что я дурак делал раньше сложнее((
        self.graUser = Toplevel(parent)
        self.graUser.title(title)
        self.canvas = Canvas(self.graUser, width=900, height=600)
        self.canvas.pack()
        self.graUser.resizable(resizable[0], resizable[1])
        self.graUser.wm_attributes("-topmost", 1)
        self.graUser.iconbitmap('filesImages/icon.ico')

        self.haslo_i_temat()
        self.line()
        self.start_pos_man()
        self.alphabet_start()




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

    def line(self):
        y = 0
        while y < 600:
            x = 0
            while x < 900:
                self.canvas.create_rectangle(x, y, x + 33, y + 27, fill="white", outline="blue")
                x = x + 33
            y = y + 27



    def start_pos_man(self):
        self.lin1 = self.canvas.create_line(100, 400, 100, 100, width=4)  # cлева 1
        self.lin2 = self.canvas.create_line(100, 100, 900 // 3, 100, width=4)  # сверху верхняя
        self.lin3 = self.canvas.create_line(900 // 3, 100, 900 // 3, 170, width=4)  # сбоку




    def start_pos_word(self):
        global label_under
        self.shift = 0

        for i in range(len(self.hasloUser)):
            self.text_czertoczki = self.canvas.create_text((500 + self.shift, 50), text='_', font='Arial 14',
                                                           fill="purple", tag='word')

            # label_under =  Label(self.canvas, text = '_', font = 'Arial 14', bg = 'silver', fg = 'purple' ).place(x = 500+ self.shift, y = 50)
            self.shift += 30

            self.label_word = []
            self.label_word.append(self.text_czertoczki)




    def randThems(self):

        self.canvas.create_text(200, 80, text='temat słowa: '+ self.tematUser, fill="black", font="Courier 18", tag = 'rand_temat')




    def delete_text(self):
        self.canvas.delete('rand_temat')
        self.canvas.delete('word')




    def alphabet_start(self):
        self.shift_x = self.shift_y = 0
        self.count = 0

        for c in range(ord("A"), ord("Z") + 1):
            self.btn_alphabet = Button(self.graUser, text=chr(c), width=2, height=1, fg='black', bg='silver',
                                       ).place(x=600 + self.shift_x, y=400 - self.shift_y)

            # self.btn_alphabet.bind('<Button-1>', lambda event : self.check_btn(event))

            btn_alpha = []
            btn_alpha.append(self.btn_alphabet)

            print(btn_alpha)

            self.shift_x += 40
            self.count += 1

            if self.count == 7:
                self.shift_x = self.count = 0
                self.shift_y -= 50








