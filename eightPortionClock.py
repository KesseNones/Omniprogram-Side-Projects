import random
from time import sleep
import time
from tkinter import *
import math
import datetime

class EightClock(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageTime = Label(self.frameBottom, text = "test", font = "Times 75", anchor = "w")
        self.messageTime.grid(row = 0, column = 0)

        self.messageTimeSeg = Label(self.frameBottom, text = "test", font = "Times 75", anchor = "w", bg = "#373737")
        self.messageTimeSeg.grid(row = 1, column = 0)

        self.dateUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def dateUpdate(self):
        time = self.convFunTime()
        self.messageTime["text"] = time
        self.messageTimeSeg["text"] = self.portion
        self.window.after(1, self.dateUpdate)

    def currentTime(self):
        self.local = datetime.datetime.now()
        self.hourUnalt = self.local.hour
        self.min = self.local.minute
        self.sec = self.local.second

    def convFunTime(self):
        self.currentTime()
        if 0 <= self.hourUnalt < 3:
            portion = "Late Night"
            hour = self.hourUnalt + 1
            self.messageTimeSeg["fg"] = "black"
        if 3 <= self.hourUnalt < 6:
            portion = "Pre-Morning"
            hour = (self.hourUnalt - 3) + 1
            self.messageTimeSeg["fg"] = "#00857d"
        if 6 <= self.hourUnalt < 9:
            portion = "Morning"
            hour = (self.hourUnalt - 6) + 1
            self.messageTimeSeg["fg"] = "#ffff3f"
        if 9 <= self.hourUnalt < 12:
            portion = "Late Morning"
            hour = (self.hourUnalt - 9) + 1
            self.messageTimeSeg["fg"] = "#00ff9b"
        if 12 <= self.hourUnalt < 15:
            portion = "Afternoon"
            hour = (self.hourUnalt - 12) + 1
            self.messageTimeSeg["fg"] = "#93ffd5"
        if 15 <= self.hourUnalt < 18:
            portion = "Late Afternoon"
            hour = (self.hourUnalt - 15) + 1
            self.messageTimeSeg["fg"] = "#b6ff54"
        if 18 <= self.hourUnalt < 21:
            portion = "Evening"
            hour = (self.hourUnalt - 18) + 1
            self.messageTimeSeg["fg"] = "#0e5efe"
        if 21 <= self.hourUnalt < 24:
            portion = "Night"
            hour = (self.hourUnalt - 21) + 1
            self.messageTimeSeg["fg"] = "#03006a"
        self.portion = portion
        timeString = str(hour) + ":" + str(self.min).zfill(2) + ":" + str(self.sec).zfill(2)
        return timeString

def main():
    root = Tk()
    root.title("Clock With Eight Day Portions")
    dateAndTime = EightClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
