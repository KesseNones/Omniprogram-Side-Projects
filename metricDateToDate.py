#Jesse A. Jones
#Version: 2023-05-31.19

from tkinter import *
import datetime
import dateHandling
import leapDetect

#This class takes in a metric date and converts it to a date in standard time.
class MetricToDate(object):
    def __init__(self, window = None):
        self.window = window

        #Holds the quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds metric date input field, 
        #   metric date conversion button, and date output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Metric date input field.
        self.message = Label(self.frameBottom, text = "Enter Metric Date", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.metricDate = Entry(self.frameBottom, font = "Ariel 20")
        self.metricDate.grid(row = 1, column = 0)

        #Calculates date from metric time when pressed.
        self.convButtonI = Button(self.frameBottom, text = "Calculate Date", 
            font = "Ariel 20", command = self.metricToCal)
        self.convButtonI.grid(row = 2, column = 0)

        #Date output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)
    
    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates date from input metric date and displays result.
    def metricToCal(self):
        date = self.dateCalc()
        self.tOutput["text"] = date

    #Fetches metric date from input.
    def getMetric(self):
        metricGet = dateHandling.GetDate()
        return round(metricGet.getGeneral(self.metricDate.get()), 9)

    #Calculates date based on metric date.
    def dateCalc(self):
        isLeap = leapDetect.IsLeap()
        monthNameArr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        #Fetches input metric date * 1000 to be in day units.
        metric = self.getMetric() * 1000
        
        #Finds decimal fraction of day and day count. 
        metricDay = int(metric)
        metricDec = metric - metricDay
        
        #Determines how many years elapsed based 
        #   on the fixed number of days in 400 years.
        year = 0
        elapsed400YearCycles = metricDay // 146097 # Number of days in 400 years.
        year += elapsed400YearCycles * 400
        
        #Calculates through remaining years.
        remainingDays = metricDay % 146097
        while (remainingDays >= 366):
            if (isLeap.isLeapYear(year)):
                sub = 366
            else:
                sub = 365
            remainingDays -= sub
            year += 1
            
        #Based on leap year and remaining days, 
        #   calculates date from remaining days.
        leap = isLeap.isLeapYear(year)
        dateArr = self.findDateFromDay(remainingDays, leap)
        month = dateArr[0]
        day = dateArr[1]
        
        #Finds month name and day of week from date.
        year -= 10000
        monthString = monthNameArr[month - 1]
        weekDay = self.week_fdn(year, month, day)
        
        #Calculates time based on metric decimal. Time is in UTC.
        daySec = 86400 * metricDec
        hour = daySec // 3600
        daySec %= 3600
        minute = daySec // 60
        second = int(daySec % 60)

        #Creates time string and returns it.
        dateString = str(int(year)).zfill(4) + "-" + monthString + "-" + str(day).zfill(2) + " " + weekDay + ", " + str(int(hour)).zfill(2) + ":" + str(int(minute)).zfill(2) + ":" + str(int(second)).zfill(2)
        return dateString

    #Given day cound and if it's a leap year, the date is found from the day.
    def findDateFromDay(self, day, leapCondit):
        month = 0
        returnArr = [0, 0]
        
        #January case.
        if (0 <= day < 31):
            returnArr[0] = 1
            returnArr[1] = (day + 1)
        
        #Februrary case.
        elif (31 <= day < 59 + leapCondit):
            returnArr[0] = 2
            returnArr[1] = (day + 1) - 31
        
        #March case
        elif (59 + leapCondit <= day < 90 + leapCondit):
            returnArr[0] = 3
            returnArr[1] = (day + 1) - (59 + leapCondit)
        
        #April case
        elif (90 + leapCondit <= day < 120 + leapCondit):
            returnArr[0] = 4
            returnArr[1] = (day + 1) - (90 + leapCondit)
        
        #May case
        elif (120 + leapCondit <= day < 151 + leapCondit):
            returnArr[0] = 5
            returnArr[1] = (day + 1) - (120 + leapCondit)
        
        #June case
        elif (151 + leapCondit <= day < 181 + leapCondit):
            returnArr[0] = 6
            returnArr[1] = (day + 1) - (151 + leapCondit)
        
        #July case
        elif (181 + leapCondit <= day < 212 + leapCondit):
            returnArr[0] = 7
            returnArr[1] = (day + 1) - (181 + leapCondit)
        
        #August case
        elif (212 + leapCondit <= day < 243 + leapCondit):
            returnArr[0] = 8
            returnArr[1] = (day + 1) - (212 + leapCondit)
        
        #September case
        elif (243 + leapCondit <= day < 273 + leapCondit):
            returnArr[0] = 9
            returnArr[1] = (day + 1) - (243 + leapCondit)
        
        #October case
        elif (273 + leapCondit <= day < 304 + leapCondit):
            returnArr[0] = 10
            returnArr[1] = (day + 1) - (273 + leapCondit)
        
        #November case
        elif (304 + leapCondit <= day < 334 + leapCondit):
            returnArr[0] = 11
            returnArr[1] = (day + 1) - (304 + leapCondit)
        
        #December case
        else:
            returnArr[0] = 12
            returnArr[1] = (day + 1) - (334 + leapCondit)
            
        return returnArr

    #Finds day of the week from input.
    def week_fdn(self, year, month, day):
            leapIs = leapDetect.IsLeap()
            if leapIs.isLeapYear(year) and month < 3:
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
            weekArr = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
            wk = weekArr[net]
            return wk                
 
            
def main():
    root = Tk()
    root.title("Metric to Normal Date Calculator")
    temp = MetricToDate(root)
    root.mainloop()

if __name__ == "__main__":
    main()
