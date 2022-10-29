from tkinter import *
import math
import time
import datetime
from random import choice

class bearimyCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.yearI = Entry(self.frameBottom, font = "Times 55")
        self.yearI.grid(row = 0, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 55", anchor = "w")
        self.messageIII.grid(row = 2, column = 0)

        self.dayI = Entry(self.frameBottom, font = "Times 55")
        self.dayI.grid(row = 2, column = 1)

        self.messageIV = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 55", anchor = "w")
        self.messageIV.grid(row = 3, column = 0)

        self.hourI = Entry(self.frameBottom, font = "Times 55")
        self.hourI.grid(row = 3, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 55", anchor = "w")
        self.messageV.grid(row = 4, column = 0)

        self.minuteI = Entry(self.frameBottom, font = "Times 55")
        self.minuteI.grid(row = 4, column = 1)
    
        self.messageVI = Label(self.frameBottom, text = "Enter Second:", font = "Ariel 55", anchor = "w")
        self.messageVI.grid(row = 5, column = 0)

        self.secondI = Entry(self.frameBottom, font = "Times 55")
        self.secondI.grid(row = 5, column = 1)

        self.convButton = Button(self.frameBottom, text = "Convert to Bearimies", 
            font = "Ariel 55", command = self.timeToBer)
        self.convButton.grid(row = 6, column = 0)

        self.bOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 45", wraplength = 600)
        self.bOutput.grid(row = 6, column = 1)

        self.messageVII = Label(self.frameBottom, text = "Enter Bearimies:", font = "Ariel 55", anchor = "w")
        self.messageVII.grid(row = 8, column = 0)

        self.ber = Entry(self.frameBottom, font = "Times 55")
        self.ber.grid(row = 8, column = 1)

        self.convButton = Button(self.frameBottom, text = "Convert to Relative Earth Time", 
            font = "Ariel 55", command = self.BerToTime)
        self.convButton.grid(row = 9, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 55", wraplength = 600)
        self.tOutput.grid(row = 9, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def timeToBer(self):
        self.berConv("2")
        self.bOutput["text"] = str(self.berimy) + " Jeremy Bearimies"

    def BerToTime(self):
        self.berConv("1")
        self.tOutput["text"] = str(self.year) + ":" + str(self.day) + ":" + str(self.hour) + ":" + str(self.minute) + ":" + str(self.sec)
         

    def berConv(self, ch):
        if ch == "1":
            ber = float(self.ber.get())
            mult = choice(range(0,3220))
            yr = ber * mult
            d = (yr - int(yr)) * 365
            hr = (d - int(d)) * 24
            m = (hr - int(hr)) * 60
            sec = (m - int(m)) * 60
            sec = round(sec, 3)
            year = int(yr)
            day = int(d)
            hour = int(hr)
            minute = int(m)
            self.year = year
            self.day = day
            self.hour = hour
            self.minute = minute
            self.sec = sec
        elif ch == "2":
            yr = int(self.yearI.get())
            d = int(self.dayI.get())
            hr = int(self.hourI.get())
            m = int(self.minuteI.get())
            sec = float(self.secondI.get())
            yrDec = yr + ((d + ((hr + (m / 60) + (sec / 3600))/24))/365)
            ber = yrDec / choice(range(3220))
            self.berimy = ber

def main():
    root = Tk()
    root.title("Jeremy Bearimy Calculator")
    star = bearimyCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
