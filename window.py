import winsound
from  tkinter import *
from rejestracja import  Rejestracja
from logowanie import  Logowanie
from tkinter import ttk

from gra import  Gra


class StartWindow(Gra):   # начальное окно
    def __init__(self, width, height, title = "Wisielca", resizable = (False, False) ):
        self.window1 = Tk()
        self.window1.title(title)
        self.window1.geometry(f"{width}x{height}+500+150") # отступ от краев экрана + размеры
        self.window1.resizable(resizable[0], resizable[1])
        self.window1.iconbitmap('filesImages/icon.ico')
        self.window1.lift()
        self.image()
        self.btn()

        # self.dbrand()
        # self.json()


        """
        кнопки
        """
    def btn(self):  #кнопки

        # self.btn_rejestracja = Button(self.window1, text="rejestracja", width=10, height=1,command=self.okno_rejestracjiself).place(relx=0.45, rely=0.4)
        # self.btn_logowanie = Button(self.window1, text="zaloguj się", width=10, height=1,command = self.okno_logowaniaself).place(relx=0.45, rely=0.5)

        self.btn_rejestracja = ttk.Button(self.window1, text="rejestracja", command=self.okno_rejestracjiself).place(relx=0.45, rely=0.4)
        self.btn_logowanie = ttk.Button(self.window1, text="zaloguj się", command = self.okno_logowaniaself).place(relx=0.45, rely=0.5)
        # self.btn_gra = ttk.Button(self.window1, text = 'graj', command  = self.okno_gryself).place(relx=0.45, rely = 0.3)




        self.btn_musicoff = PhotoImage(file="filesImages/musicoff.png")
        self.btn_musicoff = self.btn_musicoff.subsample(5,5)
        Button(self.window1, text = 'stop music',image  = self.btn_musicoff,highlightthickness=0, bd=0, command  = self.stop_sound). place(relx =0, rely = 0.75)





        self.btn_music = PhotoImage(file="filesImages/musicon.png")
        self.btn_music = self.btn_music.subsample(5, 5)
        self.volume_btn = Button(self.window1, image=self.btn_music, highlightthickness=0, bd=0, command= lambda :[self.play_music()]) \
            .place(relx=0, rely=0.85)



    def stop_sound(self):
        winsound.PlaySound(None, winsound.SND_ALIAS)

    def play_music(self):
        winsound.PlaySound('filesImages/sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC| winsound.SND_LOOP )




    def run(self):
        self.window1.mainloop()


    def okno_rejestracjiself(self,  width = 500, height=400, title = "Okno rejestracji" , resizable = (False, False)):
        Rejestracja(self.window1, width, height, title ,resizable )

    def okno_logowaniaself(self , width = 400, height=300, title = "Logowanie" , resizable = (False, False)):
        Logowanie(self.window1, width, height, title ,resizable )


    # def okno_gryself(self,  title = "Gra" , resizable = (False, False)):
    #     Gra(self.window1, title ,resizable )




    def image(self):
        filename =PhotoImage(file ="filesImages/fon.png")
        filename = filename.subsample(1,1)
        filename_label = Label(self.window1)
        filename_label.image = filename
        filename_label['image'] = filename_label.image
        filename_label.place(x=0,y=0)




if __name__ == "__main__":
    startWindow= StartWindow(512,512)  # размер окна
    startWindow.run()















