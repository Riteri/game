import winsound
from  tkinter import *
from rejestracja import  Rejestracja
from logowanie import  Logowanie
from tkinter import ttk

from gra import  Gra


class StartWindow(Gra):   # начальное окно
    def __init__(self, width, height, title = "Wisielca", resizable = (False, False) ):
        """ function -  __init__ class StartWindow


        description
        -----------
        .lift()
            gives an advantage in the location of windows
        .iconbitmap
            adds an icon to the application
        .title()
            sets the title of the window

        :param width: 512
        :param height: 512
        :param title: Wisielca
        :param resizable: (False, False)
        """

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



    def btn(self):  #кнопки
        """Function - btn

        Parameters
        ----------
        self.btn_rejestracja : tkk.Button
            register button (opens the registration window)

         self.btn_logowanie: tkk.Button
            authorization button (opens authorization window)

        self.btn_musicoff: PhotoImage
            adds a photo to the button
            Button - button with text "stop music ",  to stop music

        self.btn_music: PhotoImage
            adds a photo to the button
            button  self.volume_btn -  turns on music

        Used libraries
        --------------
        tkinter import *
        """

        self.btn_rejestracja = ttk.Button(self.window1, text="rejestracja", command=self.okno_rejestracjiself).place(relx=0.45, rely=0.4)
        self.btn_logowanie = ttk.Button(self.window1, text="zaloguj się", command = self.okno_logowaniaself).place(relx=0.45, rely=0.5)


        self.btn_musicoff = PhotoImage(file="filesImages/musicoff.png")
        self.btn_musicoff = self.btn_musicoff.subsample(5,5)
        Button(self.window1, text = 'stop music',image  = self.btn_musicoff,highlightthickness=0, bd=0, command  = self.stop_sound). place(relx =0, rely = 0.75)


        self.btn_music = PhotoImage(file="filesImages/musicon.png")
        self.btn_music = self.btn_music.subsample(5, 5)
        self.volume_btn = Button(self.window1, image=self.btn_music, highlightthickness=0, bd=0, command= lambda :[self.play_music()]) \
            .place(relx=0, rely=0.85)



    def stop_sound(self):
        """function - stop_sound

        Parameters
        ----------
        winsound.SND_ALIAS: sound parameter
            The sound parameter is a sound association name from the registry.
            If the registry contains no such name, play the system default sound.

        Used libraries
        --------------
        winsound


        :return
            nothing
        """

        winsound.PlaySound(None, winsound.SND_ALIAS)

    def play_music(self):
        """function -  play_music

            Parameters
            ---------
            winsound.SND_ALIAS : sound parameter
                The sound parameter is a sound association name from the registry.
                If the registry contains no such name, play the system default sound.

            winsound.SND_ASYNC : sound parameter
                Return immediately, allowing sounds to play asynchronously.
            winsound.SND_LOOP: sound parameter
                Play the sound repeatedly. The SND_ASYNC flag must also be used to avoid blocking

            Used libraries
            --------------
            winsound

        :return: immediately

        """
        winsound.PlaySound('filesImages/sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC| winsound.SND_LOOP )




    def run(self):
        """ function  - run

            parameter
            ---------
             self.window1.mainloop()
                that service function will loop the window indefinitely,
                so the window will wait for any interaction with the user until it is closed
        :return:
        """
        self.window1.mainloop()


    def okno_rejestracjiself(self,  width = 500, height=400, title = "Okno rejestracji" , resizable = (False, False)):
        """ function -  okno_rejestracjiself


            description
            ----------
            opens the registration window

        :param width: 500
        :param height: 400
        :param title: Okno rejestracji
        :param resizable: (False, False)
        :return:
        """
        Rejestracja(self.window1, width, height, title ,resizable )

    def okno_logowaniaself(self , width = 400, height=300, title = "Logowanie" , resizable = (False, False)):
        """function okno_logowaniaself

            description
            -----------
            opens the authorization window

        :param width:
        :param height:
        :param title:
        :param resizable:
        :return:
        """
        Logowanie(self.window1, width, height, title ,resizable )





    def image(self):
        """ function - image

            description
            -----------
            adds a background image
        :return:
        """
        filename =PhotoImage(file ="filesImages/fon.png")
        filename = filename.subsample(1,1)
        filename_label = Label(self.window1)
        filename_label.image = filename
        filename_label['image'] = filename_label.image
        filename_label.place(x=0,y=0)




if __name__ == "__main__":
    startWindow= StartWindow(512,512)  # размер окна
    startWindow.run()















