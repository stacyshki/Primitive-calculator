"""CALCULATOR IN 1 WINDOW"""

from tkinter import *

EXPRESSION = ''
ANSWER_TEXT = None


def clicked():
    global EXPRESSION
    global ANSWER_TEXT
    EXPRESSION = ASK_FIELD.get()
    ANSWER_TEXT = Label(master=WINDOW, text=f'Your answer is {eval(EXPRESSION)}', font=('New Times Roman', 13, 'bold'))
    ANSWER_TEXT.place(x=100, y=200)
    CLOSE_BUTTON = Button(master=WINDOW, text='CLOSE', font=('New Times Roman', 11, 'bold'), command=WINDOW.destroy)
    CLOSE_BUTTON.place(x=125, y=250)
    CLEAR_BUTTON = Button(master=WINDOW, text='CLEAR', font=('New Times Roman', 11, 'bold'))
    CLEAR_BUTTON.configure(command=ANSWER_TEXT.destroy)
    CLEAR_BUTTON.place(x=225, y=250)


WINDOW = Tk()
WINDOW.title('CALCULATOR')
WINDOW.geometry('450x300')
WINDOW.resizable(True, True)
TEXT_GREET = Label(master=WINDOW, text='Hello! Enter your expression please:', font=('New Times Roman', 13, 'bold'), background='white')
TEXT_GREET.place(x=100, y=50)
ASK_FIELD = Entry(master=WINDOW, width=25, font=('New Times Roman',))
ASK_FIELD.place(x=100, y=70)
OK_BUTTON = Button(master=WINDOW, text='COUNT', font=('New Times Roman', 11, 'bold'), command=clicked)
OK_BUTTON.place(x=175, y=125)
WINDOW.mainloop()
