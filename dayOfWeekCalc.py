from tkinter import *
import math
import time
import datetime
import dateHandling
import leapDetect

class WeekCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.isStupid = True

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55")
        self.messageI.grid(row = 0, column = 0)

        self.yearE = Entry(self.frameBottom, font = "Times 45")
        self.yearE.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 55")
        self.messageII.grid(row = 2, column = 0)

        self.monthE = Entry(self.frameBottom, font = "Times 45")
        self.monthE.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 55")
        self.messageIII.grid(row = 3, column = 0)

        self.dayE = Entry(self.frameBottom, font = "Times 45")
        self.dayE.grid(row = 3, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Find Weekday", 
            font = "Ariel 50", command = self.wCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 65", justify = LEFT)
        self.cOutput.grid(row = 4, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def wCalCalc(self):
        day = self.cal_calc()
        self.cOutput["text"] = day

    def cal_calc(self):
        date = dateHandling.GetDate()
        year = date.getYear(self.yearE.get())
        month = date.getMonth(self.monthE.get())
        day = date.getDay(self.dayE.get())
        weekDay = self.week_fdn(year, month, day)
        print(year, month, day)
        return weekDay

    def week_fdn(self, year, month, day):
        leap = leapDetect.IsLeap()
        isLeap = leap.isLeapYear(year)
        if isLeap and month < 3:
            subtract = -1
        else:
            subtract = 0
        y = year % 100
        yII = int(y / 4)
        yIII = yII + y
        yC = yIII % 7
        if (year - y) % 400 == 0:
            cC = 6
        if ((year - y) - 100) % 400 == 0:
            cC = 4
        if ((year - y) - 200) % 400 == 0:
            cC = 2
        if ((year - y) - 300) % 400 == 0:
            cC = 0
        net = yC + cC
        if month == 1:
            mC = 0
        if month == 2:
            mC = 3
        if month == 3:
            mC = 3
        if month == 4:
            mC = 6
        if month == 5:
            mC = 1
        if month == 6:
            mC = 4
        if month == 7:
            mC = 6
        if month == 8:
            mC = 2
        if month == 9:
            mC = 5
        if month == 10:
            mC = 0
        if month == 11:
            mC = 3
        if month == 12:
            mC = 5
        net = net + mC
        net = net + int(day)
        net = net + subtract
        net = net % 7
        if net == 0:
            wk = "Sunday"
        elif net == 1:
            wk = "Monday"
        elif net == 2:
            wk = "Tuesday"
        elif net == 3:
            wk = "Wednesday"
        elif net == 4:
            wk = "Thursday"
        elif net == 5:
            wk = "Friday"
        else:
            wk = "Saturday"
        return wk

def main():
    root = Tk()
    root.title("Day of Week Calculator")
    calCalc = WeekCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
