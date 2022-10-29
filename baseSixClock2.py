import time
from tkinter import *
import math
import datetime
import baseConvertClass

class SixTime2(object):
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

        effyGrixTotal = secTotal // 400
        secTotal %= 400

        effyMillixTotal = int(secTotal / (400 / 216))

        base = baseConvertClass.BaseConvert()
        effyGrixPlace = base.baseConv(int(effyGrixTotal), 6).zfill(3)
        effyMillixPlace = base.baseConv(int(effyMillixTotal), 6).zfill(3)

        timeString = f"{effyGrixPlace}.{effyMillixPlace}"
        return timeString

def main():
    root = Tk()
    root.title("Base Six Clock Version II")
    metric = SixTime2(root)
    root.mainloop()

if __name__ == "__main__":
    main()
