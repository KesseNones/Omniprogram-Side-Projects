#Jesse A. Jones
#Version: 2022-12-28.1

import time
from tkinter import *
import datetime
import baseConvertClass

#This class contains the methods necessary to generate a different version 
#   of the base six clock that works in terms of fractions 
#   of the whole day, instead of a preassigned set of hours.
#This clock is equivalent to dividing the day into thousandths 
#   and then tracking the thousandths of the thousandths as a decimal. 
#   Of course, this is the base six equivalent so it tracks 216ths of the day.
class SixTime2(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Bottom frame holds time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time output message.
        self.message = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.message.pack(side = TOP)
    
        #Used in base conversions.
        self.base = baseConvertClass.BaseConvert()

        #Starts self updating time loop.
        self.timeUpdate()

    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()

    #Loops continuously, fetching the unix time stamp, 
    #   converting it to base six time, 
    #   and displaying it to user.
    def timeUpdate(self):
        t = time.time()
        timeString = self.sixTimeConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def sixTimeConv(self, unix):
        #Datetime library used to determine 
        #   the user's time zone offset from UTC.
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)

        #Second total of current day calculated.
        secTotal = (unix - (3600 * timeZoneDiff)) % 86400

        #Calculates number of 216ths of a day.
        effyGrixTotal = secTotal // 400
        secTotal %= 400

        #Calculates 6^6ths of a day.
        effyMillixTotal = int(secTotal / (400 / 216))

        #216ths and 6^6ths converted to base six 
        #   using home made base conversion libaray.
        effyGrixPlace = self.base.baseConv(int(effyGrixTotal), 6).zfill(3)
        effyMillixPlace = self.base.baseConv(int(effyMillixTotal), 6).zfill(3)

        timeString = f"{effyGrixPlace}.{effyMillixPlace}"
        return timeString

def main():
    root = Tk()
    root.title("Base Six Clock Version II")
    metric = SixTime2(root)
    root.mainloop()

if __name__ == "__main__":
    main()
