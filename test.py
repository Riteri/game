from tkinter import *

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
MARGIN = 100
BG_COLOR = 'white'
label_word = []
btn_alpha = []

def start_pos_man():
    line_1 = canvas.create_line(MARGIN, WINDOW_HEIGHT - MARGIN, MARGIN, MARGIN, width = 4)
    line_2 = canvas.create_line(MARGIN, MARGIN, WINDOW_HEIGHT//3, MARGIN, width = 4)
    line_3 = canvas.create_line(WINDOW_HEIGHT//3, MARGIN, WINDOW_HEIGHT//3, MARGIN*2, width =4 )


def alphabet_start():


    shift_x = shift_y = 0
    count = 0

    for c in range(ord("A"), ord("Z")+1):
        global  btn_alphabet
        btn_alphabet = Button(window, text = chr(c),  width=2, height=1, fg = 'black', bg = 'silver', command =  lambda  event: chek_alpha(event, slowo))\
                            .place( x =600+ shift_x, y = 400 - shift_y )

        # btn_alphabet.bind ('<Button-1>', lambda  event: chek_alpha(event, slowo))
        btn_alpha.append(btn_alphabet)


        shift_x +=40
        count +=1

        if count == 7:
            shift_x = count = 0
            shift_y -=50






def start_pos_word():
    global  slowo

    slowo = 'PRIVET'

    shift  = 0

    for i in range(len(slowo)):
        label_under  = Label(window, text = '_', font  = ' Arial 16', bg = 'white').place(x = WINDOW_HEIGHT-MARGIN*2 + shift, y = MARGIN*3.5)

        shift +=50
        label_word.append(label_under)


def chek_alpha (event, slowo):
    alpha  = event.wiget['text']
    pos  = []

    for i in range(len(slowo)):
        if (slowo[i] == alpha):
            pos.append(i)

    if (len(pos) != 0):
        label_word[i].config(text = '{}'.format(slowo[i]))








window = Tk()

window.title ('Wiselca')

canvas  = Canvas(window, bg = BG_COLOR, height = WINDOW_HEIGHT, width = WINDOW_WIDTH )
canvas.place(x = 0, y = 0)

window.geometry ('1200x800')



alphabet_start()
start_pos_man()

start_pos_word()


window.mainloop()



