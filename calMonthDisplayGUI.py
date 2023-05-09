#Jesse A. Jones
#Version: 2023-05-09.88

from tkinter import *
import math
import time
import datetime
import leapDetect
import dateHandling
import weekCalculator

#This class displays a calendar month page based 
#   on an input year and input month.
class CalendarDisp(object):
    #Sets up GUI.
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)

        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)

        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Show Month", 
            font = "Ariel 20", command = self.monthDisp)
        self.convButton.grid(row = 3, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT, anchor = "w")
        self.cOutput.grid(row = 3, column = 1)

        #Used for date parsing and leap detection.
        self.dateParse = dateHandling.GetDate()
        self.leaper = leapDetect.IsLeap()
        self.weekCalc = weekCalculator.WeekFinder()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Creates month display string based on input year and month.
    def calDisp(self, year, month):
        #Determines month name.
        monthNameArr = ["January", "February", "March",
                        "April", "May", "June",
                        "July", "August", "September",
                        "October", "November", "December"]
        m = monthNameArr[month - 1]

        startingDay = self.weekCalc.weekFind(year, month, 1)
        calDeeta = self.calCalc(year, month, startingDay)
        monthDisp = "   " + m + " " + str(year) + "\n Mo Tu We Th Fr Sa Su \n"
        for row in range(6):
            for day in range(7):
                monthDisp += ""  + calDeeta[row][day] + "  "
            monthDisp += "\n"
        return monthDisp

    #Creates the matrix that represents the calendar month page.
    def calCalc(self, year, month, weekDayStart):
        #Determines month length.
        leap = self.leaper.isLeapYear(year)
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            dayMax = 31
        if month == month == 4 or month == 6 or month == 9 or month == 11:
            dayMax = 30
        if month == 2 and leap == False:
            dayMax = 28
        if month == 2 and leap:
            dayMax = 29

        #Month matrix initialized.
        monthMatrix = [["-", "-", "-", "-", "-", "-", "-"],["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],["-", "-", "-", "-", "-", "-", "-"],
            ["-", "-", "-", "-", "-", "-", "-"],["-", "-", "-", "-", "-", "-", "-"]]
        
        #Determines what start of month looks like.
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
        
        #Calculates date to start week 2 and beyond of month with.
        num = int(monthMatrix[0][6]) + 1

        #Fills in the rest of the month matrix based on num.
        for row in range(1, 6):
            for day in range(7):
                if num <= dayMax:
                    monthMatrix[row][day] = str(num).zfill(2)
                    num += 1
                else:
                    monthMatrix[row][day] = "    "
        return monthMatrix

    #Called when display month button is pressed. 
    #   Actually displays the calendar month.
    def monthDisp(self):
        #Parses input year and month.
        year = self.dateParse.getYear(self.year.get())
        month  = self.dateParse.getMonth(self.month.get())
        
        #Calculates and displays month.
        self.cOutput["text"] = self.calDisp(year, month)

def main():
    root = Tk()
    root.title("Calendar Month Displayer")
    calCalc = CalendarDisp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
