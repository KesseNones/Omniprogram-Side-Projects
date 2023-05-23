#Jesse A. Jones
#Version: 2023-05-23.15

import time
from tkinter import *
import datetime
import baseConvertClass

#This class displays the clock in hexadecimal time.
#   This version of hex time is 0x10000 units.
class HexTime(object):
    def __init__(self, window = None):
        self.window = window

        #Fixes window width to prevent text shifting the window size.
        self.window.geometry("400x200")

        #Contains quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds hex time display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays hex time.
        self.message = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.message.pack(side = TOP)
    
        self.base = baseConvertClass.BaseConvert()

        #Starts recursive time updating loop.
        self.timeUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Derives current hex time based on unix time, 
    #   displays it, and then recursively updates.
    def timeUpdate(self):
        self.message["text"] = self.hexTimeConv(time.time())
        self.message.after(1, self.timeUpdate)

    #Takes in a unix timestamp and converts it to hex time.
    def hexTimeConv(self, unix):
        #Uses the datetime library to determine 
        #   the local timezone offshift from UTC.
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        
        #Number of seconds in current day based on local timezone.
        secTotal = (unix - (3600 * timeZoneDiff)) % 86400
        
        #Fractions used in calculating places of hex clock.
        sixteenth = 86400 / 16
        twohundred = 86400 / 256
        fourK = 86400 / 4096
        sixtyFiveK = 86400 / 65536
        oneMil = 86400 / 1048576

        #Places of hex clock calculated. 
        sixteenths = secTotal // sixteenth
        secTotalReduced = secTotal % sixteenth
        twohundreds = secTotalReduced // twohundred
        secTotalReduced = secTotalReduced % twohundred
        fourKs = secTotalReduced // fourK
        secTotalReduced = secTotalReduced % fourK
        sixtyFiveKs = secTotalReduced // sixtyFiveK
        secTotalReduced = secTotalReduced % sixtyFiveK
        oneMils = secTotalReduced // oneMil

        #Converts each spot of hex clock to base 16.
        first = self.base.baseConv(int(sixteenths), 16)
        second = self.base.baseConv(int(twohundreds), 16)
        third = self.base.baseConv(int(fourKs), 16)
        fourth = self.base.baseConv(int(sixtyFiveKs), 16)
        fifth = self.base.baseConv(int(oneMils), 16)

        #Returns new time string.
        return f"{first}{second}{third}{fourth}.{fifth}"

def main():
    root = Tk()
    root.title("Hexadecimal Clock")
    metric = HexTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
