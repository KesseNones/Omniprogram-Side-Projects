#Jesse A. Jones
#Version: 2022-12-22.4

import time
import datetime
from tkinter import *
import baseConvertClass

#This class contains members and methods necessary 
#   to generate a local time binary clock.
#This clock involves expressing a day in the form of four nibbles.
#   The furthest left bit is half a day, 
#   the bit to the right of that is a quarter of a day, etc. 
class BinarTime(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Bottom frame holds binary clock itself.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time output.
        self.message = Label(self.frameBottom, text = "test", font = "Times 50", anchor = "w")
        self.message.pack(side = TOP)
    
        #Starts time loop.
        self.timeUpdate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Updates the binary time every millisecond.
    def timeUpdate(self):
        #Fetches the unix time stamp and converts it to binary time.
        t = time.time()
        timeString = self.binConv(t)

        #Displays converted binary time in specified widget.
        self.message["text"] = timeString

        #Recursive call makes time live.
        self.message.after(1, self.timeUpdate)

    #Converts a passed in unix time stamp to a binary time string.
    def binConv(self, unix):
        #Acquires local timezone and uses it to generate 
        #   a local time based total of seconds ranging from 0 to 86399.
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        secTotal = (unix - (3600 * timeZoneDiff)) % 86400
        
        #First nibble of clock's factors.
        half = 86400 / 2
        quarter = 86400 / 4
        eighth = 86400 / 8
        sixteenth = 86400 / 16

        #Second nibble of clock's factors.
        thirty = 86400 / 32
        sixty = 86400 / 64
        onehundred = 86400 / 128
        twohundred = 86400 / 256

        #Third nibble of clock's factors.
        fivehundred = 86400 / 512
        onethousand = 86400 / 1024
        twothousand = 86400 / 2048
        fourK = 86400 / 4096

        #Fourth nibble of clock's factors.
        eightK = 86400 / 8192
        sixteenK = 86400 / 16384
        thirtytwoK = 86400 / 32768
        sixtyfiveK = 86400 / 65536
        onethirtyOneK = 86400 / 131072

        #Determines time elapsed in each bit of first nibble.
        halves = secTotal // half
        secTotalReduced = secTotal % half
        quarters = secTotalReduced // quarter
        secTotalReduced = secTotalReduced % quarter
        eighths = secTotalReduced // eighth
        secTotalReduced = secTotalReduced % eighth
        sixteenths = secTotalReduced // sixteenth
        secTotalReduced = secTotalReduced % sixteenth

        #Determines time elapsed in each bit of second nibble.
        thrities = secTotalReduced // thirty
        secTotalReduced = secTotalReduced % thirty
        sixties = secTotalReduced // sixty
        secTotalReduced = secTotalReduced % sixty
        onehundreds = secTotalReduced // onehundred
        secTotalReduced = secTotalReduced % onehundred
        twohundreds = secTotalReduced // twohundred
        secTotalReduced = secTotalReduced % twohundred

        #Determines time elapsed in each bit of third nibble.
        fivehundreds = secTotalReduced // fivehundred
        secTotalReduced = secTotalReduced % fivehundred
        onethousandths = secTotalReduced // onethousand
        secTotalReduced = secTotalReduced % onethousand
        twothousands = secTotalReduced // twothousand
        secTotalReduced = secTotalReduced % twothousand
        fourKs = secTotalReduced // fourK
        secTotalReduced = secTotalReduced % fourK

        #Determines time elapsed in each bit of fourth nibble.
        eightKs = secTotalReduced // eightK
        secTotalReduced = secTotalReduced % eightK
        sixteenKs = secTotalReduced // sixteenK
        secTotalReduced = secTotalReduced % sixteenK
        thirtytwoKs = secTotalReduced // thirtytwoK
        secTotalReduced = secTotalReduced % thirtytwoK
        sixtyfiveKs = secTotalReduced // sixtyfiveK
        secTotalReduced = secTotalReduced % sixtyfiveK
        onethirtyOneKs = secTotalReduced // onethirtyOneK

        #Converts each time elapse point to binary. 
        #   This isn't that necessary but ensures every 
        #   bit is indeed a string and is either a 0 or 1.
        base = baseConvertClass.BaseConvert()
        first = base.baseConv(int(halves), 2)
        second = base.baseConv(int(quarters), 2)
        third = base.baseConv(int(eighths), 2)
        fourth = base.baseConv(int(sixteenths), 2)
        fifth = base.baseConv(int(thrities), 2)
        sixth = base.baseConv(int(sixties), 2)
        seventh = base.baseConv(int(onehundreds), 2)
        eighth = base.baseConv(int(twohundreds), 2)
        ninth = base.baseConv(int(fivehundreds), 2)
        tenth = base.baseConv(int(onethousandths), 2)
        eleventh = base.baseConv(int(twothousands), 2)
        twelfth = base.baseConv(int(fourKs), 2)
        thirteenth = base.baseConv(int(eightKs), 2)
        fourteenth = base.baseConv(int(sixteenKs), 2)
        fifteenth = base.baseConv(int(thirtytwoKs), 2)
        sixteenth = base.baseConv(int(sixtyfiveKs), 2)
        seventeenth = base.baseConv(int(onethirtyOneKs), 2)

        timeString = f"{first}{second}{third}{fourth} {fifth}{sixth}{seventh}{eighth} {ninth}{tenth}{eleventh}{twelfth} {thirteenth}{fourteenth}{fifteenth}{sixteenth}"

        return timeString

def main():
    root = Tk()
    root.title("Binary Clock")
    metric = BinarTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
