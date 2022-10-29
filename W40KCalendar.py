from tkinter import *
import leapDetect
import datetime
import metricTime

class FortyKCalendar(object):
    """ THE EMPEROR PROTECTS """
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

        self.displayCal()

    def quitButtonAction(self):
        self.window.destroy()

    def displayCal(self):
        fortyKTimeString = self.calc40K()
        self.tOutput["text"] = fortyKTimeString
        self.tOutput.after(1, self.displayCal)

    def calc40K(self):
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

        centuryStamp = self.findCenturyStamp(year)

        milleniumOrd = self.findMillenium(year)

        return f"0{yearFrac}{centuryStamp}.M{milleniumOrd}"

    def findDayDec(self, hour, minute, second):
        hourSecs = hour * 3600
        minuteSecs = minute * 60

        totalSecs = hourSecs + minuteSecs + second

        return (totalSecs / 86400)

    def findYearFraction(self, dayNumDec, isLeap):
        div = 365 + isLeap
        return str(int( (dayNumDec / div) * 1000) ).zfill(3)

    def findCenturyStamp(self, year):
        return (str((year % 1000)).zfill(3))

    def findMillenium(self, year):
        return (str( ((year // 1000) + 1) ).zfill(2))

def main():
    root = Tk()
    root.title("Warhammer 40K Live Imerial Calendar")
    metric = FortyKCalendar(root)
    root.mainloop()

if __name__ == "__main__":
    main()
