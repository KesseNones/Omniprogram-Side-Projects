import random
from time import sleep
import time
from tkinter import *
import math
import datetime
from tkinter import messagebox
import baseConvertClass

class HexTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "test", font = "Times 100", anchor = "w")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        t = time.time()
        timeString = self.hexTimeConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def hexTimeConv(self, unix):
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        secTotal = (unix - (3600 * timeZoneDiff)) % 86400
        sixteenth = 86400 / 16
        twohundred = 86400 / 256
        fourK = 86400 / 4096
        sixtyFiveK = 86400 / 65536
        oneMil = 86400 / 1048576

        sixteenths = secTotal // sixteenth
        secTotalReduced = secTotal % sixteenth
        twohundreds = secTotalReduced // twohundred
        secTotalReduced = secTotalReduced % twohundred
        fourKs = secTotalReduced // fourK
        secTotalReduced = secTotalReduced % fourK
        sixtyFiveKs = secTotalReduced // sixtyFiveK
        secTotalReduced = secTotalReduced % sixtyFiveK
        oneMils = secTotalReduced // oneMil

        base = baseConvertClass.BaseConvert()
        first = base.baseConv(int(sixteenths), 16)
        second = base.baseConv(int(twohundreds), 16)
        third = base.baseConv(int(fourKs), 16)
        fourth = base.baseConv(int(sixtyFiveKs), 16)
        fifth = base.baseConv(int(oneMils), 16)

        #timeString = " " + first + "." + second + third + fourth + fifth + " "
        #Old time string.

        timeString = " " + first + second + third + fourth + "." + fifth + " "
        #New time string.
        return timeString

def main():
    root = Tk()
    root.title("Hexadecimal Clock")
    metric = HexTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
