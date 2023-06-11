#Jesse A. Jones
#Version: 2023-06-11.19

from tkinter import *
import leapDetect
import datetime
import metricTime

#This class expresses the current TNG stardate 
#   if it were following an absolute scale rather than based on the shows.
class SDate(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds True TNG stardate output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays stardate output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 50")
        self.tOutput.grid(row = 0, column = 0)

        #Used in leap year detection and day of year finding.
        self.leap = leapDetect.IsLeap()
        self.metric = metricTime.MetricTime()

        #Starts recursive display loop.
        self.displaySDate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates true stardate and displays result.
    def displaySDate(self):
        stardate = self.calcStardate()
        self.tOutput["text"] = stardate
        self.tOutput.after(1, self.displaySDate)

    #Calculates current stardate and returns a string representing it.
    def calcStardate(self):
        #Current date and time information fetched.
        timeCurrent = datetime.datetime.utcnow()
        year = timeCurrent.year
        month = timeCurrent.month
        day = timeCurrent.day
        hour = timeCurrent.hour
        minute = timeCurrent.minute
        second = timeCurrent.second 
        isLeap = self.leap.isLeapYear(year)
        
        #Finds day number and decimal of current day.
        dayNum = self.metric.findDayNumOfYear(year, month, day)
        dayDec = self.findDayDec(hour, minute, second)
        
        #Day num decimal is used to find year fraction.
        dayNumDec = (dayNum - 1) + dayDec
        yearFrac = self.findYearFraction(dayNumDec, isLeap)

        #2323 is stardate 0 in this system for some reason.
        displacement = year - 2323

        #Creates stardate string and returns it.
        return f"{displacement}{yearFrac}"

    #Finds the day decimal based on the time.
    def findDayDec(self, hour, minute, second):
        hourSecs = hour * 3600
        minuteSecs = minute * 60

        totalSecs = hourSecs + minuteSecs + second

        return (totalSecs / 86400)

    #Finds the fraction of the year based 
    #   on the days elapsed and if it's a leap year or not.
    def findYearFraction(self, dayNumDec, isLeap):
        div = 365 + isLeap
        frac = dayNumDec / div
        frac *= 10000
        frac = int(frac)
        frac /= 10.0
        return (str(frac).zfill(5))

def main():
    root = Tk()
    root.title("True TNG Stardate Live")
    metric = SDate(root)
    root.mainloop()

if __name__ == "__main__":
    main()
