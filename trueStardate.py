from tkinter import *
import leapDetect
import datetime
import metricTime

class SDate(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Times 100")
        self.tOutput.grid(row = 0, column = 0)

        self.leap = leapDetect.IsLeap()

        self.displaySDate()

    def quitButtonAction(self):
        self.window.destroy()

    def displaySDate(self):
        stardate = self.calcStardate()
        self.tOutput["text"] = stardate
        self.tOutput.after(1, self.displaySDate)

    def calcStardate(self):
        timeCurrent = datetime.datetime.utcnow()
        year = timeCurrent.year
        month = timeCurrent.month
        day = timeCurrent.day
        hour = timeCurrent.hour
        minute = timeCurrent.minute
        second = timeCurrent.second 

        isLeap = self.leap.isLeapYear(year)
        dayNum = metricTime.MetricTime().findDayNumOfYear(year, month, day)
        dayDec = self.findDayDec(hour, minute, second)
        dayNumDec = (dayNum - 1) + dayDec

        yearFrac = self.findYearFraction(dayNumDec, isLeap)

        displacement = year - 2323

        return f"{displacement}{yearFrac}"

    def findDayDec(self, hour, minute, second):
        hourSecs = hour * 3600
        minuteSecs = minute * 60

        totalSecs = hourSecs + minuteSecs + second

        return (totalSecs / 86400)

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
