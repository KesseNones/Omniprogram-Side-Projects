import random
from time import sleep
import time
from tkinter import *
import math

class StardateTOS(object):
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

        self.message = Label(self.frameBottom, text = "", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)
        
        self.tim = 1566431880
        
        self.starUpdate()


    def precGet(self, num):
        return int(self.prec.get())

    def quitButtonAction(self):
        self.window.destroy()

    def starUpdate(self):
        date = self.stardateTOS()
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
        self.message["text"] = str(date) + " " + "(" + str(int(self.superStar)) + ")"
        #self.tim += 1
        self.message.after(1, self.starUpdate)

    def stardateTOS(self):
        t = time.time()
        s = (6059232000 / 86400) - (t / 86400)
        s *= 5
        subStar = abs((s % 10000) - 10000)
        subStar = subStar * (10 ** self.precGet(1))
        subStar = math.trunc(subStar)
        subStar = subStar / (10 ** self.precGet(1))
        superStar = s // 10000
        self.superStar = (superStar * -1) - 1
        return subStar

def main():
    root = Tk()
    root.title("Stardate TOS Version")
    star = StardateTOS(root)
    root.mainloop()

if __name__ == "__main__":
    main()

