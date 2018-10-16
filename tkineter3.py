import tkinter
from tkinter import ttk
import random


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    print_stuff_button = ttk.Button(frame1, text='Print stuff')
    print_stuff_button['command'] = (lambda: do_stuff())
    print_stuff_button.grid()

    root.mainloop()


def do_stuff():

    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z')
    random_word = ''
    for _ in range(10):
        letter = letters[random.randrange(26)]
        random_word = random_word + letter

    print(random_word)

main()
do_stuff()
