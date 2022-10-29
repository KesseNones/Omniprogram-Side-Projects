from tkinter import *
import math
import time
import datetime
from tkinter import messagebox
import calendar

class CalendarDisp(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Times 55")
        self.messageI.grid(row = 0, column = 0)

        self.yearE = Entry(self.frameBottom, font = "Times 45")
        self.yearE.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Times 55")
        self.messageII.grid(row = 2, column = 0)

        self.monthE = Entry(self.frameBottom, font = "Times 45")
        self.monthE.grid(row = 2, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Show Month", 
            font = "Times 50", command = self.monthDisp)
        self.convButton.grid(row = 3, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Times 40", justify = LEFT, anchor = "w")
        self.cOutput.grid(row = 3, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def cal_disp(self, year, month):
        year = int(year)
        month = int(month)
        if month == 1:
            m = "January"
        if month == 2:
            m = "February"
        if month == 3:
            m = "March"
        if month == 4:
            m = "April"
        if month == 5:
            m = "May"
        if month == 6:
            m = "June"
        if month == 7:
            m = "July"
        if month == 8:
            m = "August"
        if month == 9:
            m = "September"
        if month == 10:
            m = "October"
        if month == 11:
            m = "November"
        if month == 12:
            m = "December"
        startingDay = self.week_fdn(year, month, 1)
        calDeeta = self.calCalc(year, month, startingDay)
        monthDisp = "   " + m + " " + str(year) + "\n Mo Tu We Th Fr Sa Su \n"
        for row in range(6):
            for day in range(7):
                monthDisp += ""  + calDeeta[row][day] + "  "
            monthDisp += "\n"
        return monthDisp

    def isLeapYear(self, year):
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True
        else:
            leap = False
        return leap

    def calCalc(self, year, month, weekDayStart):
        leap = self.isLeapYear(year)
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            dayMax = 31
        if month == month == 4 or month == 6 or month == 9 or month == 11:
            dayMax = 30
        if month == 2 and leap == False:
            dayMax = 28
        if month == 2 and leap:
            dayMax = 29
        monthMatrix = [["-", "-", "-", "-", "-", "-", "-"],["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],["-", "-", "-", "-", "-", "-", "-"]]
        if weekDayStart == "Monday":
            monthMatrix[0] = ["01", "02", "03", "04", "05", "06" , "07"]
        if weekDayStart == "Tuesday":
            monthMatrix[0] = ["    ", "01", "02", "03", "04", "05", "06"]
        if weekDayStart == "Wednesday":
            monthMatrix[0] = ["    ", "    ", "01", "02", "03", "04", "05"]
        if weekDayStart == "Thursday":
            monthMatrix[0] = ["    ", "    ", "    ", "01", "02", "03", "04"]
        if weekDayStart == "Friday":
            monthMatrix[0] = ["    ", "    ", "    ", "    ", "01 ", "02", "03"]
        if weekDayStart == "Saturday":
            monthMatrix[0] = ["    ", "    ", "    ", "    ", "    ", "01", "02"]
        if weekDayStart == "Sunday":
            monthMatrix[0] = ["    ", "    ", "    ", "    ", "    ", "    ", "01"]
        num = int(monthMatrix[0][6]) + 1
        for row in range(1, 6):
            for day in range(7):
                if num <= dayMax:
                    monthMatrix[row][day] = str(num).zfill(2)
                    num += 1
                else:
                    monthMatrix[row][day] = "    "
        return monthMatrix
        
    def week_fdn(self, year, month, day):
        subtract = 0
        if (month < 3) and ((year % 4) == 0 or (year % 400) == 0):
            subtract = -1
            if year % 100 == 0:
                subtract = 0
            if (year % 100 == 0) and (year % 400 == 0):
                subtract = -1
        if (month > 2):
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
        if net == 1:
            wk = "Monday"
        if net == 2:
            wk = "Tuesday"
        if net == 3:
            wk = "Wednesday"
        if net == 4:
            wk = "Thursday"
        if net == 5:
            wk = "Friday"
        if net == 6:
            wk = "Saturday"
        return wk

    def monthDisp(self):
        year = self.yearGet()
        month  = self.monthGet()
        cal = self.cal_disp(year, month)
        self.cOutput["text"] = cal

    def yearGet(self):
        if self.yearE.get() == "":
            messagebox.showerror("Empty Entry Error", "Be sure to enter a year!")
        else:
            return int(self.yearE.get())
    
    def monthGet(self):
        if self.monthE.get() == "":
            messagebox.showerror("Empty Entry Error", "Be sure to enter a month!")
        else:
            return int(self.monthE.get())

def main():
    root = Tk()
    root.title("Calendar Month Displayer")
    calCalc = CalendarDisp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
