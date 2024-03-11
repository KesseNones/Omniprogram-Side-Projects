#Jesse A. Jones
#Version: 2024-03-11.18

from time import time
import datetime
from tkinter import *

#Calculates the current metric date and time based 
#   on the format used in Isaac Asimov's books.
class AsimovCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program if clicked.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds time and date outputs.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays time.
        self.message = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.message.grid(row = 0, column = 0)
        
        #Displays date
        self.messageII = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.messageII.grid(row = 1, column = 0)

        #Finds timezone once for given program runtime.
        tTemp = time()
        self.timeZoneDiff = (self.findTimeZoneDiff(tTemp) * 3600)

        #Starts the recursive time update loop.
        self.timeUpdate()

    #Quits program
    def quitButtonAction(self):
        self.window.destroy()

    #Finds current time and date in Asimov metric calendar.
    def timeUpdate(self):
        timeArr = self.asimovCalc(time() - self.timeZoneDiff)
        self.message["text"] = timeArr[0]
        self.messageII["text"] = timeArr[1]
        self.message.after(1, self.timeUpdate)

    #Finds timezone difference between local and UTC.
    def findTimeZoneDiff(self, utcUnix):
        t = int(utcUnix)
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = ((t % 86400) // 3600)
        if utcHour < localHr:
            utcHour += 24
        return abs(utcHour - localHr)

    #Determines the metric date 
    #   and metric time based on Isaac Asimov's format.
    def asimovCalc(self, unix):
        #Number of days from start of CE to start of Unix epoch.
        baseDays = 719527

        #Finds current metric date.
        totalDays = baseDays + (unix / 86400)
        currMetYear = int(totalDays) // 300
        daysElapsedInMetYear = int(totalDays) % 300
        currMetMonth = (daysElapsedInMetYear // 30) + 1
        currMetDay = (daysElapsedInMetYear % 30) + 1

        #Finds current metric time.
        timeOfDay = totalDays % 1
        totalMetSeconds = int(timeOfDay * 100000)
        currMetHour = totalMetSeconds // 10000
        totalMetSeconds %= 10000
        currMetMinute = totalMetSeconds // 100
        totalMetSeconds %= 100
        currMetSecond = totalMetSeconds

        return [
            f"{currMetYear}-{str(currMetMonth).zfill(2)}-{str(currMetDay).zfill(2)}",
            f"{currMetHour}:{str(currMetMinute).zfill(2)}:{str(currMetSecond).zfill(2)}"
        ]



def main():
    root = Tk()
    root.title("Asimov Metric Time and Calendar")
    metric = AsimovCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
