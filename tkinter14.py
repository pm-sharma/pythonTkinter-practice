import tkinter
from tkinter import ttk


def main():
    root = tkinter.Tk()

    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    print_entry_button = ttk.Button(frame1, text='Print entry')
    print_entry_button['command'] = (lambda:
                                     print_contents(my_entry_box))
    print_entry_button.grid()

    root.mainloop()


def print_contents(entry_box):
   
    contents_of_entry_box = entry_box.get()
    print(contents_of_entry_box)
main()
print_contents()
