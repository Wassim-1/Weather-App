from tkinter import *
from tkinter import ttk
import weather

win= Tk()

win.geometry("750x500")
win.title("Weather")

def display_text():
   global entry
   string= entry.get()
   x=weather.weather(string)
   temp=str(x["main"]["temp"])+"°C"
   feels=str(x["main"]["feels_like"])+"°C"
   humidity=str(x["main"]["humidity"])+"%"
   weeather=x["weather"][0]["main"]
   details=x["weather"][0]["description"]
   templabel.configure(text="temperature:" +temp)
   weatherlabel.configure(text="weather: "+weeather)
   detailslabel.configure(text="in particular: "+ details)
   humiditylabel.configure(text="humidity: "+humidity)
   feelslabel.configure(text="feels like: "+feels)
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack(pady=10)
templabel=Label(win, text="Temperature: ", font=('Arial',12),width=18,height=2)
templabel.pack()
weatherlabel=Label(win, text="Weather: ", font=('Arial',12),width=18,height=2)
weatherlabel.pack()
feelslabel=Label(win, text="feels like: ", font=('Arial',12),width=18,height=2)
detailslabel=Label(win, text="in particular: ", font=('Arial',12),width=25,height=2)
detailslabel.pack()
feelslabel.pack()
humiditylabel=Label(win, text="humidity: ", font=('Arial',12),width=18,height=2)
humiditylabel.pack()
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)
win.mainloop()



