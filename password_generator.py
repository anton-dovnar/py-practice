#!/usr/bin/env python3
from tkinter import *
import random
import string
import pyperclip


root = Tk()
root.geometry("600x400")
root.resizable(0, 0)
root.title("Password Generator")
f_left = Frame()
f_right = Frame()

heading = Label(root, text="Password Generator", font="fixedsys 15").pack(pady=16)
Label(root, text="fode4cun", font="fixedsys 10").pack(side=BOTTOM, pady=5)

# select password length

len_label = Label(f_left, text="LENGTH", font="fixedsys 15").pack()
pass_len = IntVar()
length = Spinbox(f_left, from_=8, to_=32, textvariable=pass_len, justify="center", width=21).pack()
pass_label = Label(f_right, text="PASSWORD", font="fixedsys 15").pack()
pass_str = StringVar()


def pass_gen():
    password = ""
    special_chars = string.ascii_letters + string.digits + string.punctuation
    for x in range(pass_len.get()):
        password += random.choice(special_chars)
    pass_str.set(password)

# button

Button(f_left, text="GENERATE PASSWORD", width=20, command=pass_gen).pack()
Entry(f_right, textvariable=pass_str, justify="center", width=22).pack()

# function to copy

def copy_pass():
    pyperclip.copy(pass_str.get())

Button(f_right, text="COPY TO CLIPBOARD", width=20, command=copy_pass).pack()

f_left.pack(side=LEFT, padx=45)
f_right.pack(side=RIGHT, padx=45)

root.mainloop()

