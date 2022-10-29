import time
from tkinter import *
import math
import datetime
import baseConvertClass

class SixTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "", font = "Times 100", anchor = "w")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        t = time.time()
        timeString = self.sixTimeConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def sixTimeConv(self, unix):
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        secTotal = (unix - (3600 * timeZoneDiff)) % 86400
        hours = secTotal // 3600
        secTotal %= 3600
        sixth = secTotal // 600
        secTotal %= 600
        portion36 = secTotal // 100
        secTotal %= 100
        portion216 = secTotal // (100 / 6)
        secTotal %= (100 / 6)
        portion1296 = secTotal // (100 / 36)
        secTotal %= (100 / 36)
        portion7776 = secTotal // (100 / 216)

        base = baseConvertClass.BaseConvert()
        hourPlace = base.baseConv(int(hours), 6)
        sixthPlace = base.baseConv(int(sixth), 6)
        place36 = base.baseConv(int(portion36), 6)
        place216 = base.baseConv(int(portion216), 6)
        place1296 = base.baseConv(int(portion1296), 6)
        place7776 = base.baseConv(int(portion7776), 6)

        timeString = " " + hourPlace + "." + sixthPlace + place36 + place216 + place1296 + place7776 + " "
        return timeString

def main():
    root = Tk()
    root.title("Base Six Clock")
    metric = SixTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
