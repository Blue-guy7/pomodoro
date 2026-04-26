from tkinter import *
import math
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    sys.exit(-1)
import sys
sys.excepthook = show_exception_and_exit
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps=0
timer=NONE
window=Tk()
window.title("Pomodoro app")
window.config(padx=100,pady=50,bg=YELLOW)

def count_down(count):
    global timer
    global window
    count_min=math.floor(count/60)
    count_sec= count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(var,text=f"{count_min}:{count_sec}")
    if count>0:
        timer=window.after(1000,count_down,count-1)
    if count==0:
        strt_()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)

def strt_():
    global reps
    global var3
    butt1["state"] = "disabled"
    reps+=1
    if reps%2!=0:
        text1.config(text="WORK TIME",fg=GREEN)
        count_down(WORK_MIN*60)
                  
    elif reps%8==0:
        text1.config(text="LONG BREAK",fg=RED)
        count_down(LONG_BREAK_MIN*60)
        reps=0
        var3=""
        text2.config(text=var3)
    elif reps%2==0:
        text1.config(text="SHORT BREAK",fg=PINK)
        count_down(SHORT_BREAK_MIN*60)
    if reps%2==1 and reps!=1:
        var3+=checkmark

        text2.config(text=var3)
def on_click():
    global reps
    global var3
    window.after_cancel(timer)
    butt1["state"] = "active"
    text1.config(text="TIMER",fg=GREEN)
    canvas.itemconfig(var,text="00:00")
    var3=""
    text2.config(text=var3)
    reps=0

    return


    

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
fg=GREEN
checkmark="✔"
var3=""
count="00:00"
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
var=canvas.create_text(103,130,text=count,fill="white",font=(FONT_NAME,35,"bold"))




canvas.grid(column=2,row=2)
text1=Label(text="Timer",font=("Arial",24,"bold"),foreground=fg,bg=YELLOW)
text1.grid(column=2,row=1)
text2=Label(text=var3,font=("Arial",24,"bold"),foreground=fg,bg=YELLOW)
text2.grid(column=2,row=3)
butt1=Button(text="Start",command=strt_)
butt1.grid(column=1,row=3)
butt2=Button(text="Reset",command=on_click)
butt2.grid(column=3,row=3)








window.mainloop( )