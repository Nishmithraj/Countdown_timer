import time
import subprocess
from tkinter import *

root = Tk()
root.title("Countdown")


# functions
def get_second():
    global secs
    global check
    hour = int(hr_entry.get())
    min = int(min_entry.get())
    sec = int(sec_entry.get())
    secs = (hour * 3600) + (min * 60) + sec
    check = 1
    start()


def start():
    global disp_label
    global secs
    global check
    if check == 1:
        #print("inside start :", secs)
        second = (secs % 60)
        if second < 10:
            second = str(0) + str(second)
        minute = "00"
        if secs >= 60:
            minute = (secs / 60) % 60
            minute = int(minute)
            if minute < 10:
                minute = str(0) + str(minute)
        hour = "00"
        if secs >= 3600:
            hour = (secs / 3600)
            hour = int(hour)
            if hour < 10:
                hour = "0" + str(hour)
        # if secs < 0:
        # print("INSIDE TIMEOUT")
        # stop()
        # print("Time is %s:%s:%s" % (hour, minut, second))

        secs = secs - 1
        disp_seconds.config(text=secs + 1)
        if secs >= 0:
            disp_label.config(text=str(hour) + ":" + str(minute) + ":" + str(second))
            disp_label.after(1000, start)
        else:
            subprocess.Popen(['start', 'Alarms1.wav'], shell=True)
            disp_label.config(text="TIME-OUT")
            pause()


def stop():
    global check
    disp_label.config(text="00:00:00")
    disp_seconds.config(text="STOPPED")
    check = 0
    start()


def pause():
    global secs
    #print("inside pause :", secs)
    global check
    check = 0
    start()


def resume():
    global secs
    global check
    check = 1
    #print("inside resume :", secs)
    start()


# Button's, Label's, Entry's
hr_entry = Entry(root, width=5, bg="white", fg="black", border=5, justify=CENTER)
min_entry = Entry(root, width=5, bg="white", fg="black", border=5, justify=CENTER)
sec_entry = Entry(root, width=5, bg="white", fg="black", border=5, justify=CENTER)

hr_label = Label(root, text="[HH]", font=('calibri', 8, 'bold')).grid(row=0, column=0)
min_label = Label(root, text="[MM]", font=('calibri', 8, 'bold')).grid(row=0, column=1)
sec_label = Label(root, text="[SS]", font=('calibri', 8, 'bold')).grid(row=0, column=2)

disp_label = Label(root, text="00:00:00", font=('calibri', 20, 'bold'), bg="black", fg="white")
disp_seconds = Label(root, text="remaining seconds", font=('calibri', 10, 'bold'), bg="black", fg="grey")


start_b = Button(root, text="START", font=('calibri', 8, 'bold'), command=get_second)
pause_b = Button(root, text="PAUSE", font=('calibri', 8, 'bold'), command=pause)
stop_b = Button(root, text="STOP", font=('calibri', 8, 'bold'), command=stop)
resume_b = Button(root, text="RESUME", font=('calibri', 8, 'bold'), command=resume)
close_b = Button(root, text="EXIT", font=('calibri', 7, 'bold'), command=root.destroy)


# placing
hr_entry.grid(row=1, column=0)
min_entry.grid(row=1, column=1)
sec_entry.grid(row=1, column=2)

disp_label.grid(row=2, column=0, columnspan=3, sticky=E + W)
disp_seconds.grid(row=3, column=0, columnspan=3, sticky=E + W)

start_b.grid(row=4, column=0,sticky=E + W)
pause_b.grid(row=4, column=1, sticky=E + W)
stop_b.grid(row=4, column=2, sticky=E + W)
resume_b.grid(row=5, column=0, columnspan=3,sticky=E + W)
close_b.grid(row=6, column=0, columnspan=3,sticky=E + W)

# Initialize the countdown
hr_entry.insert(0, "00")
min_entry.insert(0, "00")
sec_entry.insert(0, "00")

mainloop()
