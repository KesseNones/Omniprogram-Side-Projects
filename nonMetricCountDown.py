#Jesse A. Jones
#Version: 2023-05-13.14

from tkinter import *
import metricTime
import dateHandling
import leapDetect

#This class displays a countdown from a date or to a date 
#   in order of years, weeks, days, hours, minutes, and seconds.
class CountDown(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom field holds input fields, countdown start button, 
        #   and countdown output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter year:", font = "Ariel 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter month:", font = "Ariel 20", anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter day:", font = "Ariel 20", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)

        #Hour input field.
        self.messageIV = Label(self.frameBottom, text = "Enter hour:", font = "Ariel 20", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = "Ariel 20")
        self.hour.grid(row = 4, column = 1)

        #Minute input field.
        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 20", anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = "Ariel 20")
        self.minute.grid(row = 5, column = 1)
    
        #Countdown starting button.
        self.convButton = Button(self.frameBottom, text = "Start Countdown", 
            font = "Ariel 20", command = self.calcCount)
        self.convButton.grid(row = 6, column = 0)

        #Countdown output.
        self.mOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.mOutput.grid(row = 6, column = 1)

        #Used in leap year detection, 
        #   metric time conversions, and date parsing.
        self.leap = leapDetect.IsLeap()
        self.metric = metricTime.MetricTime()
        self.date = dateHandling.GetDate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls functions to calculate countdown string and displays result.
    def calcCount(self):
        #Calculates metric date from input date.
        metricDateFinal = self.metric.metric_calc(
            self.date.getYear(self.year.get()), self.date.getMonth(self.month.get()), 
            self.date.getDay(self.day.get()), self.date.getHour(self.hour.get()), 
            self.date.getMinOrSec(self.minute.get()))
        #Calculates current metric date.
        metricDateInitial = self.metric.metric_time()
        
        #Finds metric time delta in terms of days.
        metricCount = metricDateFinal - metricDateInitial
        metricCount = abs(metricCount) * 1000
        
        #Converts day delta to countdown string and displays result.
        nonMetricTimeString = self.metricToStandard(metricCount)
        self.mOutput["text"] = nonMetricTimeString

        #Recursively calls to display updated countdown.
        self.mOutput.after(1, self.calcCount)

    #Takes in an input day delta and turns it into a delta time string.
    def metricToStandard(self, metric):
        #Determines how many 400 year cycles are left or have happened.
        yearCycleCount = metric // 146097
        metric %= 146097

        #Determines how many years elapsed or are left.
        yearCount = int(self.determineYears(metric) + (400 * yearCycleCount))
        metric -= self.daysToSubtract

        #Determines how many weeks have elapsed or are left in the given year.
        weekCount = int(metric // 7)
        metric %= 7

        #"It just works" -Todd Howard
        dayCount = int(metric)
        metric -= dayCount

        #Determines time left or that has elapsed.
        daySec = metric * 86400
        hourCount = int(daySec // 3600)
        daySec %= 3600
        minCount = int(daySec // 60)
        daySec %= 60
        secCount = int(daySec)

        #Constructs final time string and returns it.
        string = str(yearCount).zfill(4) + "yr " + str(weekCount).zfill(2) + "wk " + str(dayCount) + "d " \
        + str(hourCount).zfill(2) + "h " + str(minCount).zfill(2) + "m " + str(secCount).zfill(2)
        return string

    #Determines how many years are contained in a given input day delta.
    def determineYears(self, metric):
        intMetric = int(metric)
        self.daysToSubtract = 0
        year = 0
        while intMetric > 365:
            leap = self.leap.isLeapYear(year)
            if leap:
                sub = 366
            else:
                sub = 365
            year += 1
            intMetric -= sub
            self.daysToSubtract += sub
        return year

def main():
    root = Tk()
    root.title("Regular Countdown Timer")
    metric = CountDown(root)
    root.mainloop()

if __name__ == "__main__":
    main()
