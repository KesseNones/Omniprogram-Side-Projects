import random
from time import sleep
import time
from tkinter import *
import math

class Stardate(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.prec = Scale(self.frameTop, orient = HORIZONTAL, 
            from_ = 1, to = 5, length = 300,
            label = "SD Precision", font = "Ariel 20", command = self.precGet)
        self.prec.grid(row = 0, column = 1)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Click Update to Update", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)
    
        self.starUpdate()

    def precGet(self, num):
        return int(self.prec.get())

    def quitButtonAction(self):
        self.window.destroy()

    def starUpdate(self):
        date = self.stardate()
        prec = self.precGet(1)
        if prec == 1:
            date = format(date, ".1f")
        if prec == 2:
            date = format(date, ".2f")
        if prec == 3:
            date = format(date, ".3f")
        if prec == 4:
            date = format(date, ".4f")
        if prec == 5:
            date = format(date, ".5f")
        self.message["text"] = date
        self.message.after(1, self.starUpdate)

    def stardate(self):
        t = time.time()
        s = (t / 31557.59999999999999) + (740583679.968 / 31557.59999999999999)
        RI = s * (10 ** self.precGet(1))
        RII = math.trunc(RI)
        RIII = RII / (10 ** self.precGet(1))
        return RIII

def main():
    root = Tk()
    root.title("Stardate")
    star = Stardate(root)
    root.mainloop()

if __name__ == "__main__":
    main()

