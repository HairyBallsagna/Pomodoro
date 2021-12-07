from tkinter import *
import math 


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    """Cancels the timer and resets the labels and reps"""
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0


def start_timer():
    """Starts the timer and changes the labels accordingly"""
    global reps
    reps += 1
    
    # convert the work and break minutes to seconds
    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60
    
    # if its the 8th rep i.e. after completing 4 work sessions, start a long break session
    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="Break", fg=RED)
    # after every rep start the short break session
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="Break", fg=PINK)
    # start the work session
    else:
        count_down(work_seconds)
        title_label.config(text="Work", fg=GREEN)
        
        
def count_down(count):
    """Starts the timer with the start_timer() function or the window.after() and 
        increase controls the check marks indicating when a rep is completed"""
        
    # converts the seconds to minutes
    count_minutes = math.floor(count / 60)
    # converts the seconds to the remaining seconds from the current minute
    count_seconds = count % 60
    
    # if the seconds/minutes are in single digits, then format them to display time correctly like: 05:02
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    if count_minutes < 10:
        count_minutes = f"0{count_minutes}"
    
    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after((75//2)//2, count_down, count - 1)
    else:
        # start the timer
        start_timer()
        marks = ""
        # update the checkmarks
        for _ in range(math.floor(reps / 2)):
            marks += "✔"
        check_marks.config(text=marks)
        
        
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", command=start_timer, highlightthickness=0, bg="black", fg="white", width=10)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, bg="black", fg="white", width=10)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)


window.mainloop()