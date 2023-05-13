#Jesse A. Jones
#Version: 2023-05-13.16

import time
from tkinter import *
import datetime

#This class displays a clock based 
#   on a clock reformation idea found here: 
#   https://www.youtube.com/watch?v=iHK-aN3XZqw
class DiffTime(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Bottom frame holds time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time output.
        self.message = Label(self.frameBottom, text = "test", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)
    
        #Called to start time display loop.
        self.timeUpdate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls function to calculate current alternate time 
    #   and displays result before recursively looping.
    def timeUpdate(self):
        timeString = self.timeConv(self.localUnix())
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    #Converts input unix time stamp to alternate clock.
    def timeConv(self, unix):
        #Calulates hours, minutes, and seconds of alternate time.
        daySecTotal = unix % 86400
        hourCount = (daySecTotal // 4320) + 1
        daySecTotal %= 4320
        minCount = daySecTotal // 216
        secCount = daySecTotal % 216
        
        #Creates string version of each time element.
        hourLabel = str(hourCount).zfill(2)
        minuteLabel = str(minCount).zfill(2)
        secLabel = str(secCount).zfill(3)

        #Returns properly formatted time string.
        return f"{hourLabel}:{minuteLabel}:{secLabel}"  

    #Generates a local version of the unix time stamp based 
    #   on the time zone of the user.
    def localUnix(self):
        #Fetches unix time and local hour.
        t = time.time()
        t = int(t)
        local = datetime.datetime.now()
        localHr = local.hour

        #Uses local hour to determine timezone offset from UTC.
        utcHour = ((t % 86400) // 3600)
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)

        #Returns a timezone shifted unix time.
        t = (t - (3600 * timeZoneDiff))
        return t

def main():
    root = Tk()
    root.title("Different Clock (Not My Idea)")
    metric = DiffTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
