#Jesse A. Jones
#Version: 2023-05-25.85

from tkinter import *
import math
import time
import datetime
import leapDetect
import dateHandling

#Calculates a metric date based on input and displays result.
class OtherMetricCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date and time input fields as well 
        #   as conversion button and metric time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20", anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)

        #Hour input field.
        self.messageIV = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 20", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = "Ariel 20")
        self.hour.grid(row = 4, column = 1)

        #Minute input field.
        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 20", anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = "Ariel 20")
        self.minute.grid(row = 5, column = 1)
    
        #Converts to metric date when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Metric Date", 
            font = "Ariel 20", command = self.calcMetric)
        self.convButton.grid(row = 6, column = 0)

        #Metric date output.
        self.mOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.mOutput.grid(row = 6, column = 1)

        #Used to specify if OS is windows or not.
        self.isStupid = True

        #Used in leap year detection and date parsing.
        self.leap = leapDetect.IsLeap()
        self.date = dateHandling.GetDate()

    #Quits program when pressed.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates metric date and displays result.
    def calcMetric(self):
        self.mOutput["text"] = self.metric_calc()

    #Used to calculate metric date when year is out 
    #   of range where unix time stamp library works.
    def metricCalcII(self, year, dayNum, hour, minute):
        year += 10000

        #Takes out all 400 year cycles and adds them to total.
        fourCenturyCount = year // 400
        remainingYears = year % 400
        totalDays = fourCenturyCount * 146097

        #Takes down remaining years until no years remain.
        while remainingYears > 0:
            totalDays += (365 + self.leap.isLeapYear(remainingYears))
            remainingYears -= 1

        #Adds fractional chunk of year and turns it into a metric date.
        totalDays += dayNum - 1
        totalDays = totalDays / 1000
        totalDays = round(totalDays, 3)

        #Calculates day fraction and turns it into a metric decimal.
        secTotal = (hour * 3600) + (minute * 60)
        dayDec = secTotal / 86400
        dayDec *= 1000000
        dayDec = math.floor(dayDec)
        dayDec = dayDec / 1000000000

        #Adds day fraction to metric date and returns it.
        finalMetric = totalDays + dayDec
        return finalMetric 

    #Calculates metric date either using time library 
    #   or using the metricCalcII function.
    def metric_calc(self):
        #Year range set based on if it's on Windows or not.
        if self.isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000

        #Fetches date and time input.
        year = self.date.getYear(self.year.get())
        month = self.date.getMonth(self.month.get())
        day = self.date.getDay(self.day.get())
        hour = self.date.getHour(self.hour.get())
        minute = self.date.getMinOrSec(self.minute.get())
        
        #If the year is in the range, 
        #   calculate the metric time using datetime and do some quick maths.
        #   If it's out of range two helper functions are called 
        #   and metric date is calculated that way.
        if lower < year < upper:
            #Calculates unix time stamp from datetime.
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))

            #Uses unix time stamp to calculate metric date.
            metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
            metric_time = metric_time * 1000000000
            metric_time = math.trunc(metric_time)
            metric_time = metric_time / 1000000000 
        else:
            #Finds current day number of date.
            dayCount = self.findDayNumOfYear(year, month, day)

            #Uses day number, year, and time to calculate metric date.
            metric_time = self.metricCalcII(year, dayCount, hour, minute)

        return metric_time

    #Finds current day number of year.
    def findDayNumOfYear(self, year, month, day):
        leap_year = self.leap.isLeapYear(year)
        if month == 1:
                D_Code_MKI = 0
        if month == 2:
                D_Code_MKI = 31
        if month == 3:
                D_Code_MKI = 59
                if leap_year == True:
                    D_Code_MKI = 60
        if month == 4:
                D_Code_MKI = 90
                if leap_year == True:
                    D_Code_MKI = 91
        if month == 5:
                D_Code_MKI = 120
                if leap_year == True:
                    D_Code_MKI = 121
        if month == 6:
                D_Code_MKI = 151
                if leap_year == True:
                    D_Code_MKI = 152
        if month == 7:
                D_Code_MKI = 181
                if leap_year == True:
                    D_Code_MKI = 182
        if month == 8:
                D_Code_MKI = 212
                if leap_year == True:
                    D_Code_MKI = 213
        if month == 9:
                D_Code_MKI = 243
                if leap_year == True:
                    D_Code_MKI = 244
        if month == 10:
                D_Code_MKI = 273
                if leap_year == True:
                    D_Code_MKI = 274
        if month == 11:
                D_Code_MKI = 304
                if leap_year == True:
                    D_Code_MKI = 305
        if month == 12:
                D_Code_MKI = 334
                if leap_year == True:
                    D_Code_MKI = 335
        D_Code_MKII = D_Code_MKI + day
        return D_Code_MKII

def main():
    root = Tk()
    root.title("Metric Date Calculator")
    metric = OtherMetricCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
