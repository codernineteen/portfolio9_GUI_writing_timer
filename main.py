from tkinter import *
from tkinter import ttk
from tkinter import messagebox

MINUTES = 300
MOVEMENT = 1.87
CURRENT_X = 0
multiplier = 0
stop_timer = 6
len2 = 0
#--------------------------
def calculate_word(): #단어 갯수 세는 함수
    global word_count
    list1 = text_input.get("1.0", END).split(" ")
    len1 = len(text_input.get("1.0", END))
    if len1 > 1:
        word_num = len(list1)
        word_count = Label(text=f"word: {word_num}")
        word_count.grid(column=0, row=3, sticky=("W"))

    else:
        pass
    window.after(100, calculate_word)


def timer():
    global MINUTES, CURRENT_X, MOVEMENT, multiplier
    len1 = len(text_input.get("1.0", END))
    if len1 > 1 and MINUTES > 0:
        MINUTES -= 1
        multiplier += 1
        canvas.create_line(CURRENT_X, 10, MOVEMENT*multiplier, 10, fill='#9fe6a0', width=15)

    elif MINUTES == 0:
        messagebox.askyesno("Completed", "You've completed writing a block\n Do you want to continue to writing?")
        if exit == True:
            pass
        else:
            window.destroy()

    window.after(1000, timer)


def stop():
    global stop_timer, stop_count, text_input, len2
    len1 = len(text_input.get("1.0", END))
    if len1 > 1 and stop_timer > 0:
        if len1 == len2:
            stop_timer -= 1
        else:
            stop_timer = 5
        stop_count = Label(text=f"stop: {stop_timer}")
        stop_count.grid(column=1, row=3, sticky=("E"))

    elif stop_timer == 0:
        text_input.delete("1.0", END)
        canvas.delete("all")
        restart = messagebox.askyesno("Done", "Do you want to restart writing?")
        stop_timer = 6

        if restart == False:
            window.destroy()

        else:
            pass

    else:
        pass
    window.after(1000, stop)
    len2 = len(text_input.get("1.0", END))


def byebye():
    exit = messagebox.askyesno("exit", "Quit?")
    if exit == True:
        window.destroy()
    else:
        pass



#-----------GUI settings---------------
window = Tk()
window.title("Explode your writing")
# window.resizable(False, False)

canvas = Canvas(width=560, height=20, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=3)

title = Label(text="The Most Dangerous Writing App(clone)")
title.grid(column=0, row=1, sticky=("W"))

button = ttk.Button(window, text="exit", command=byebye)
button.grid(column=2, row=1, sticky=("E"))

text_input = Text(window)
text_input.grid(column=0, row=2, columnspan=3)

word_count = Label(text=f"word: 0")
word_count.grid(column=0, row=3, sticky=("W"))

stop_count = Label(text=f"stop: ")
stop_count.grid(column=1, row=3, sticky=("E"))
#-------------execute functions

calculate_word()
timer()
stop()

window.mainloop()