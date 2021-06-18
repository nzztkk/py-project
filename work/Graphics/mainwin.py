from tkinter import *
import sys
#sys.path.append(1,'/lessons/project sem python/work/scripts')
#import const.py


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()
