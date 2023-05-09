#Jesse A. Jones
#Version: 2023-05-09.84

from tkinter import *
import math
import time
import datetime
import dateHandling
import leapDetect

#This class calculates a weekday from an 
#   input date and displays the result to the user.
class WeekCalc(object):
    #Sets up GUI and other useful items.
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

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)

        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Find Weekday", 
            font = "Ariel 20", command = self.wCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.output = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.output.grid(row = 4, column = 1)

        #Used for leap year detection and date parsing.
        self.leap = leapDetect.IsLeap()
        self.dateParse = dateHandling.GetDate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls calculation function and displays result to user.
    def wCalCalc(self):
        #Fetches input.
        year = self.dateParse.getYear(self.year.get())
        month = self.dateParse.getMonth(self.month.get())
        day = self.dateParse.getDay(self.day.get())

        #Finds week day and displays it.
        self.output["text"] = self.weekFind(year, month, day)

    #Finds day of week from input year, month, and day.
    def weekFind(self, year, month, day):
        #Determines if 1 needs to be subtracted from calculations or not.

        #Useful arrays for calculating week stuff.
        centuryCodeArr = [6, 4, 2, 0]
        monthCodeArr = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
        weekNameArr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        #Numbers used in the week calculation.
        leapSubtract = 0 - ((month < 3) and self.leap.isLeapYear(year))
        cenCode = centuryCodeArr[(year // 100) % 4]
        monthCode = monthCodeArr[month - 1]
        decAndYr = year % 100
        yearNum = decAndYr + (decAndYr // 4)

        #Performs final calculation and returns string representing week day.
        return weekNameArr[((cenCode + yearNum + monthCode + day + leapSubtract) % 7)]

def main():
    root = Tk()
    root.title("Day of Week Calculator")
    calCalc = WeekCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
