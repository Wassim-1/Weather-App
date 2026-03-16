from tkinter import *
from tkinter import ttk
import weather

win= Tk()

win.geometry("750x250")
win.title("Test")

def display_text():
   global entry
   string= entry.get()
   x=weather.weather(string)
   temp=str(x["main"]["temp"])+"°C"
   label.configure(text=temp)

label=Label(win, text="", font=("Courier 22 bold"))
label.pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()



