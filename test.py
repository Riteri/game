

from tkinter import  *
import time

root =Tk()

label = Label(root, text="Text on the screen", font=('Times New Roman',  '80'), fg="black", bg="white")
label.pack()


btn = Button(root, text = 'dell', command= lambda : label.destroy()).pack()


root.mainloop()
