import webbrowser
import winsound
from  tkinter import *
from rejestracja import  Rejestracja
from logowanie import  Logowanie
from tkinter import ttk

class StartWindow():
    def __init__(self, width, height, title = "Wisielca", resizable = (False, False) ):
        """
            :description:
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
        # self.window1.lift()
        self.image()
        self.btn()
        self.urlDonation = 'https://www.donationalerts.com/r/antondiditsky'
        self.urlTikTok = 'https://www.tiktok.com/@riteri'
        self.urlGitHub = 'https://github.com/Riteri'




    def btn(self):
        """
            :param self.btn_rejestracja: tkk.Button - register button (opens the registration window)
            :param self.btn_logowanie: tkk.Button: authorization button -  (opens authorization window)
            :param self.btn_musicoff: PhotoImage - adds a photo to the button
            :param Button:  button with text "stop music ",  to stop music
            :param self.btn_music: PhotoImage adds a photo to the button
            :param button: self.volume_btn -  turns on music

            :Used libraries:  tkinter import *
        """

        self.btn_rejestracja = ttk.Button(self.window1, text="Registration", command=self.okno_rejestracjiself , width = 15).place(relx=0.45, rely=0.4)
        self.btn_logowanie = ttk.Button(self.window1, text="Authorization ", command = self.okno_logowaniaself , width = 15).place(relx=0.45, rely=0.5)




        self.btn_musicoff = PhotoImage(file="filesImages/musicoff.png")
        self.btn_musicoff = self.btn_musicoff.subsample(5,5)
        Button(self.window1, text = 'stop music',image  = self.btn_musicoff,highlightthickness=0, bd=0, command  = self.stop_sound). place(relx =0, rely = 0.75)


        self.btn_music = PhotoImage(file="filesImages/musicon.png")
        self.btn_music = self.btn_music.subsample(5, 5)
        self.volume_btn = Button(self.window1, image=self.btn_music, highlightthickness=0, bd=0, command= lambda :[self.play_music()]) \
            .place(relx=0, rely=0.85)

        self.btnTikTok = PhotoImage(file= "filesImages/Tik-Tok.png")
        self.btnTikTok = self.btnTikTok.subsample(13,13)
        self.btnTikTokBtn = Button(self.window1, image= self.btnTikTok,command= self.tokTok ).place(relx = 0.55, y =452)


        self.donationBtn = PhotoImage(file = 'filesImages/donationalerts.png')
        self.donationBtn = self.donationBtn.subsample(6,6)
        self.donationalertsBtn = Button(self.window1, image= self.donationBtn, command=self.donation).place(relx = 0.4, rely=0.89)


        self.gitHubBtn = PhotoImage(file = 'filesImages/githubImage.png')
        self.gitHubBtn = self.gitHubBtn.subsample(11,11)
        self.GitBtn = Button(self.window1, image= self.gitHubBtn, command=self.github).place(relx = 0.7, y = 450)


    def donation(self):
        """
            :description: open Donation

        """
        webbrowser.open_new(self.urlDonation)

    def tokTok(self):
        """
            :description: open TikTok

        """
        webbrowser.open_new(self.urlTikTok)

    def github(self):
        """
            :description: open Github

        """
        webbrowser.open_new(self.urlGitHub)

    def stop_sound(self):
        """
            :param winsound.SND_ALIAS: sound parameter
                The sound parameter is a sound association name from the registry.
                If the registry contains no such name, play the system default sound.

            :Used libraries: winsound
        """

        winsound.PlaySound(None, winsound.SND_ALIAS)

    def play_music(self):
        """
            :param winsound.SND_ALIAS: sound parameter
                The sound parameter is a sound association name from the registry.
                If the registry contains no such name, play the system default sound.

            :param winsound.SND_ASYNC: sound parameter
                Return immediately, allowing sounds to play asynchronously.
            :param winsound.SND_LOOP: sound parameter
                Play the sound repeatedly. The SND_ASYNC flag must also be used to avoid blocking

            :Used libraries: winsound


        """
        winsound.PlaySound('filesImages/sound.wav', winsound.SND_ALIAS | winsound.SND_ASYNC| winsound.SND_LOOP )




    def run(self):
        """
            :param self.window1.mainloop(): that service function will loop the window indefinitely, so the window will wait for any interaction with the user until it is closed
        """
        self.window1.mainloop()


    def okno_rejestracjiself(self,  width = 500, height=400, title = "Registration window" , resizable = (False, False)):
        """
            :description: opens the registration window
            :param width: 500
            :param height: 400
            :param title: Okno rejestracji
            :param resizable: (False, False)
        """
        Rejestracja(self.window1, width, height, title ,resizable )

    def okno_logowaniaself(self , width = 400, height=300, title = "Authorization window" , resizable = (False, False)):
        """
            :description: opens the authorization window
            :param width: 400
            :param height: 500
            :param title: Authorization window
            :param resizable: False, False
        """
        Logowanie(self.window1, width, height, title ,resizable )


    def image(self):
        """
            :description: adds a background image
        """
        filename =PhotoImage(file ="filesImages/fon.png")
        filename = filename.subsample(1,1)
        filename_label = Label(self.window1)
        filename_label.image = filename
        filename_label['image'] = filename_label.image
        filename_label.place(x=0,y=0)

if __name__ == "__main__":
    startWindow= StartWindow(512,512)
    startWindow.run()















