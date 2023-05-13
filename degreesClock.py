#Jesse A. Jones
#Version: 2023-05-13.18

import time
from tkinter import *
import datetime

#This class displays a clock in a degree format, 
#   with 360 degrees in a day, 60 arc minutes per degree,
#   and 60 arc seconds per arc minute.
class DegTime(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame contains quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time display.
        self.message = Label(self.frameBottom, text = "test", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)
    
        #Starts recursive looping.
        self.timeUpdate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates degree time and displays the result.
    def timeUpdate(self):
        #Fetches current unix time and local hour based on user time zone.
        t = time.time()
        local = datetime.datetime.now()
        localHr = local.hour

        #Uses local hour and UTC hour to find user time zone 
        #   and shifts the seconds accordingly.
        utcHour = (t % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        secTotal = (t - (3600 * timeZoneDiff)) % 86400
        
        #Converts the total second count to degree time 
        #   and displays the result.
        self.message["text"] = self.convToDeg(secTotal)
        self.message.after(1, self.timeUpdate)

    #Converts number of seconds to degree time.
    def convToDeg(self, secNet):
        #Finds degrees.
        degCount = secNet // 240
        secNet %= 240

        #Finds arc minutes
        arcMinCount = secNet // 4
        secNet %= 4

        #Finds arc seconds.
        arcSecondCount = int((secNet / (4 / 60)))

        #Builds elements of time string.
        degString = str(int(degCount)).zfill(3)
        arcMinString = str(int(arcMinCount)).zfill(2)
        arcSecString = str(arcSecondCount).zfill(2)

        #Creates and returns time string.
        return f"{degString}\u00B0{arcMinString}\'{arcSecString}\""

def main():
    root = Tk()
    root.title("Degree Clock")
    metric = DegTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
