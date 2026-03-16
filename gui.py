from tkinter import *
import weather

window=Tk()
window.geometry("500x500")
window.title("Weather")
window.config(background="gray")
label=Label(window,text="Welcome to weather app",
            font=('Arial',20,'bold'),
            width=25,height=2,
            fg="#f30707",
            bg='#180e45',
            relief='sunken',
            bd=10
            )
label.pack()
window.mainloop()
