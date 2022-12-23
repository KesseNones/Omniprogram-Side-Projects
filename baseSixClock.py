#Jesse A. Jones
#Version: 2022-12-23.4

import time
from tkinter import *
import datetime
import baseConvertClass

#This class contains methods and members 
#   of a base six clock that expresses the time in 
#   a base six hour followed by five base six fractional places.
#This is effectively a base six equivalent of taking 
#   the hours in a day and expressing them as a decimal. 
class SixTime(object):
    def __init__(self, window = None):
        self.window = window

        #Top window holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Bottom frame holds time display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time output.
        self.message = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.message.pack(side = TOP)
        
        #Used for base conversions.
        self.base = baseConvertClass.BaseConvert()

        #Starts time updating loop.
        self.timeUpdate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Repeatedly converts a unix time stamp to base six time 
    #   and displays it to the user, 
    #   giving the impression of a live base six clock.
    def timeUpdate(self):
        t = time.time()
        timeString = self.sixTimeConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    #Converts a unix time stamp to the base six time format.
    def sixTimeConv(self, unix):
        #Uses datetime library to get a bearing on the local timezone 
        #   and add that as a distortion, from there 
        #   a total of seconds for a given day is found.
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        secTotal = (unix - (3600 * timeZoneDiff)) % 86400

        #Converts the second total to base six time.
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

        #Converts each chunk of the base six clock to base six. 
        #   Also ensures each clock element is a string.
        hourPlace = self.base.baseConv(int(hours), 6)
        sixthPlace = self.base.baseConv(int(sixth), 6)
        place36 = self.base.baseConv(int(portion36), 6)
        place216 = self.base.baseConv(int(portion216), 6)
        place1296 = self.base.baseConv(int(portion1296), 6)
        place7776 = self.base.baseConv(int(portion7776), 6)

        timeString = hourPlace.zfill(2) + "." + sixthPlace + place36 + place216 + place1296 + place7776
        return timeString

def main():
    root = Tk()
    root.title("Base Six Clock")
    metric = SixTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
