from tkinter import *
import metricTime
import dateHandling
import leapDetect

class CountDown(object):
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

        self.messageIV = Label(self.frameBottom, text = "Enter hour:", font = "Ariel 55", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)

        self.hour = Entry(self.frameBottom, font = "Times 55")
        self.hour.grid(row = 4, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 55", anchor = "w")
        self.messageV.grid(row = 5, column = 0)

        self.minute = Entry(self.frameBottom, font = "Times 55")
        self.minute.grid(row = 5, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Start Countdown", 
            font = "Ariel 55", command = self.calcMetric)
        self.convButton.grid(row = 6, column = 0)

        self.mOutput = Label(self.frameBottom, text = "", 
            font = "Times 55")
        self.mOutput.grid(row = 6, column = 1)

        self.leap = leapDetect.IsLeap()

    def quitButtonAction(self):
        self.window.destroy()

    def calcMetric(self):
        metric = metricTime.MetricTime()
        date = dateHandling.GetDate()
        metricDateFinal = metric.metric_calc(
            date.getYear(self.year.get()), date.getMonth(self.month.get()), 
            date.getDay(self.day.get()), date.getHour(self.hour.get()), 
            date.getMinOrSec(self.minute.get()))
        metricDateInitial = metric.metric_time()
        metricCount = metricDateFinal - metricDateInitial
        metricCount = abs(metricCount) * 1000
        nonMetricTimeString = self.metricToStandard(metricCount)
        self.mOutput["text"] = nonMetricTimeString
        self.mOutput.after(1, self.calcMetric)

    def metricToStandard(self, metric):
        yearCycleCount = metric // 146097
        metric %= 146097
        yearCount = int(self.determineYears(metric) + (400 * yearCycleCount))
        #metric = metric % 146097
        metric -= self.daysToSubtract
        weekCount = int(metric // 7)
        metric %= 7
        dayCount = int(metric)
        metric -= dayCount
        daySec = metric * 86400
        hourCount = int(daySec // 3600)
        daySec %= 3600
        minCount = int(daySec // 60)
        daySec %= 60
        secCount = int(daySec)

        string = str(yearCount).zfill(4) + "yr " + str(weekCount).zfill(2) + "wk " + str(dayCount) + "d " + str(hourCount).zfill(2) + "h " + str(minCount).zfill(2) + "m " + str(secCount).zfill(2)
        return string

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
