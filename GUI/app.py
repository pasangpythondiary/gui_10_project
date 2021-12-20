from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("Python project gui program")

icon=PhotoImage(file="logo.png")
window.iconphoto(True,icon)

window.config(background="red")

window.mainloop()