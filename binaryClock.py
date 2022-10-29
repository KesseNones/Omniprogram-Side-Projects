from time import sleep
import time
from tkinter import *
import math
import datetime
import baseConvertClass

class BinarTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        # self.descButton = Button(self.frameTop, text = "Description",
        #     font = "Ariel 20", command = self.showDescription)
        # self.descButton.grid(row = 0, column = 1)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "test", font = "Times 100", anchor = "w")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        t = time.time()
        timeString = self.binConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def binConv(self, unix):
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        secTotal = (unix - (3600 * timeZoneDiff)) % 86400
        half = 86400 / 2
        quarter = 86400 / 4
        eighth = 86400 / 8
        sixteenth = 86400 / 16

        thirty = 86400 / 32
        sixty = 86400 / 64
        onehundred = 86400 / 128
        twohundred = 86400 / 256

        fivehundred = 86400 / 512
        onethousand = 86400 / 1024
        twothousand = 86400 / 2048
        fourK = 86400 / 4096

        eightK = 86400 / 8192
        sixteenK = 86400 / 16384
        thirtytwoK = 86400 / 32768
        sixtyfiveK = 86400 / 65536
        onethirtyOneK = 86400 / 131072


        halves = secTotal // half
        secTotalReduced = secTotal % half
        quarters = secTotalReduced // quarter
        secTotalReduced = secTotalReduced % quarter
        eighths = secTotalReduced // eighth
        secTotalReduced = secTotalReduced % eighth
        sixteenths = secTotalReduced // sixteenth
        secTotalReduced = secTotalReduced % sixteenth

        thrities = secTotalReduced // thirty
        secTotalReduced = secTotalReduced % thirty
        sixties = secTotalReduced // sixty
        secTotalReduced = secTotalReduced % sixty
        onehundreds = secTotalReduced // onehundred
        secTotalReduced = secTotalReduced % onehundred
        twohundreds = secTotalReduced // twohundred
        secTotalReduced = secTotalReduced % twohundred

        fivehundreds = secTotalReduced // fivehundred
        secTotalReduced = secTotalReduced % fivehundred
        onethousandths = secTotalReduced // onethousand
        secTotalReduced = secTotalReduced % onethousand
        twothousands = secTotalReduced // twothousand
        secTotalReduced = secTotalReduced % twothousand
        fourKs = secTotalReduced // fourK
        secTotalReduced = secTotalReduced % fourK

        eightKs = secTotalReduced // eightK
        secTotalReduced = secTotalReduced % eightK
        sixteenKs = secTotalReduced // sixteenK
        secTotalReduced = secTotalReduced % sixteenK
        thirtytwoKs = secTotalReduced // thirtytwoK
        secTotalReduced = secTotalReduced % thirtytwoK
        sixtyfiveKs = secTotalReduced // sixtyfiveK
        secTotalReduced = secTotalReduced % sixtyfiveK
        onethirtyOneKs = secTotalReduced // onethirtyOneK

        base = baseConvertClass.BaseConvert()
        first = base.baseConv(int(halves), 2)
        second = base.baseConv(int(quarters), 2)
        third = base.baseConv(int(eighths), 2)
        fourth = base.baseConv(int(sixteenths), 2)
        fifth = base.baseConv(int(thrities), 2)
        sixth = base.baseConv(int(sixties), 2)
        seventh = base.baseConv(int(onehundreds), 2)
        eight = base.baseConv(int(twohundreds), 2)
        ninth = base.baseConv(int(fivehundreds), 2)
        tenth = base.baseConv(int(onethousandths), 2)
        eleventh = base.baseConv(int(twothousands), 2)
        twelfth = base.baseConv(int(fourKs), 2)
        thirteenth = base.baseConv(int(eightKs), 2)
        fourteenth = base.baseConv(int(sixteenKs), 2)
        fifteenth = base.baseConv(int(thirtytwoKs), 2)
        sixteenth = base.baseConv(int(sixtyfiveKs), 2)
        seventeenth = base.baseConv(int(onethirtyOneKs), 2)

        #timeString = first + "." + second + third + fourth + fifth + sixth + seventh + eight + ninth + tenth + eleventh + twelfth + thirteenth + fourteenth + fifteenth + sixteenth + seventeenth
        #Old time string format.

        timeString = first + second + third + fourth + " " + fifth + sixth + seventh + eight + " " + ninth + tenth + eleventh + twelfth + " " + thirteenth + fourteenth + fifteenth + sixteenth
        #New time string format.

        return timeString

def main():
    root = Tk()
    root.title("Binary Clock")
    metric = BinarTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
