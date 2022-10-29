from tkinter import *
import leapDetect
import datetime
import metricTime
import dateHandling

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

        self.messageI = Label(self.frameBottom, text = "Enter year:", font = "Ariel 55", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.year = Entry(self.frameBottom, font = "Times 55")
        self.year.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter month:", font = "Ariel 55", anchor = "w")
        self.messageII.grid(row = 2, column = 0)

        self.month = Entry(self.frameBottom, font = "Times 55")
        self.month.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter day:", font = "Ariel 55", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)

        self.day = Entry(self.frameBottom, font = "Times 55")
        self.day.grid(row = 3, column = 1)

        self.messageIV = Label(self.frameBottom, text = "Enter hour (UTC):", font = "Ariel 55", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)

        self.hour = Entry(self.frameBottom, font = "Times 55")
        self.hour.grid(row = 4, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter minute (UTC):", font = "Ariel 55", anchor = "w")
        self.messageV.grid(row = 5, column = 0)

        self.minute = Entry(self.frameBottom, font = "Times 55")
        self.minute.grid(row = 5, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Convert", 
            font = "Ariel 55", command = self.displayCal)
        self.convButton.grid(row = 6, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Times 100")
        self.tOutput.grid(row = 6, column = 1)

        self.leap = leapDetect.IsLeap()

    def quitButtonAction(self):
        self.window.destroy()

    def displayCal(self):
        fortyKTimeString = self.calc40K()
        self.tOutput["text"] = fortyKTimeString

    def calc40K(self):
        dateHandle = dateHandling.GetDate()

        year = dateHandle.getYear(self.year.get())
        month = dateHandle.getMonth(self.month.get())
        day = dateHandle.getDay(self.day.get())
        hour = dateHandle.getHour(self.hour.get())
        minute = dateHandle.getMinOrSec(self.minute.get())
        second = 0 

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
    root.title("Warhammer 40K Imerial Calendar Calculator")
    metric = FortyKCalendar(root)
    root.mainloop()

if __name__ == "__main__":
    main()
