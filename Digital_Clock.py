from time import strftime #for current time
from tkinter import Label, Tk # for GUI

#window config for clock
window = Tk() # create object
window.title("Digital Clock") #set Title
window.geometry('200x80') # set geometry
window.configure(bg = "black") # set background color
window.resizable(False,False)

#label config
clock_label = Label(window,bg = "black", fg = "orange", font = ("Times", 30, 'bold'), relief = 'flat')
clock_label.place(x = 20,y = 20)

def updating_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, updating_label)
updating_label()
window.mainloop()
