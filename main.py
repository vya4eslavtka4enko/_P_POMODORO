from tkinter import *
import math
import time

FONT_NAME = 'Courier'
BGCOLOR = '#6495ED'
reps = 0
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
window = Tk()
window.title("POMODORO")
window.config(padx=15, pady=20, bg=BGCOLOR)
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text='00:00')
    label.config(text = "Timer")
    label_chek.config(text="")
    global reps
    reps = 0

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += '✔'
        label_chek.config(text=marks)


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text='LONG BREAK')
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text='SHORT BREAK')
    else:
        count_down(work_sec)
        label.config(text='WORK')
    # count_down(long_break_sec)


label = Label()
label.config(text="TIMER", font=(FONT_NAME, 55, 'bold'), bg=BGCOLOR)
label.grid(column=2, row=0)

canvas = Canvas(width=300, height=300, bg=BGCOLOR, highlightthickness=0)
tomato_img = PhotoImage(file='pomodoro.png')
canvas.create_image(150, 152, image=tomato_img)

timer_text = canvas.create_text(152, 150, text='00:00', fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

button_start = Button()
button_start.config(text="Start", bg=BGCOLOR, fg=BGCOLOR, bd=0, relief=RIDGE, width=10, height=2, command=start_timer)
button_start.grid(column=1, row=3)

label_chek = Label()
label_chek.config(text='', font=(FONT_NAME, 35, "bold"), bg=BGCOLOR)
label_chek.grid(column=2, row=3)

button_reset = Button()
button_reset.config(text="RESET", bg=BGCOLOR, fg=BGCOLOR, bd=0, relief=RIDGE, width=10, height=2, command=reset_timer)
button_reset.grid(column=3, row=3)

window.mainloop()
