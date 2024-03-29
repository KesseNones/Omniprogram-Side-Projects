#Jesse A. Jones
#Version: 2024-03-11.21

from time import time
import datetime
from tkinter import *
import dateHandling
import metricTime

#Calculates the current metric date and time based 
#   on the format used in Isaac Asimov's books.
class AsimovCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program if clicked.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds time and date outputs.
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
        self.convButton = Button(self.frameBottom, text = "Determine Metric Time", 
            font = "Ariel 20", command = self.calcMetric)
        self.convButton.grid(row = 6, column = 0)

        #Displays date
        self.dateOutput = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.dateOutput.grid(row = 6, column = 1)
        
        #Displays time.
        self.timeOutput = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.timeOutput.grid(row = 7, column = 1)
        
        self.date = dateHandling.GetDate()
        self.metric = metricTime.MetricTime()

    #Quits program
    def quitButtonAction(self):
        self.window.destroy()
    
    #Gets user input and calculates metric date and time.
    def calcMetric(self):
        #Parses user input.
        year = self.date.getYear(self.year.get())
        month = self.date.getMonth(self.month.get())
        day = self.date.getDay(self.day.get())
        hour = self.date.getHour(self.hour.get())
        minute = self.date.getMinOrSec(self.minute.get())

        metricDate = self.metric.metric_calc(year, month, day, hour, minute)

        #Days elapsed since start of Common Era.
        daysSinceCEStart = (metricDate * 1000) - 3652425

        #Only accounts for timezone if necessary.
        #TURNED OFF CURRENTLY BECAUSE OF WACKINESS
        if False and year > 1969 and year < 3002:
            localDayDec = self.findLocalDayDec(daysSinceCEStart)
        else:
            localDayDec = daysSinceCEStart

        asimovLs = self.asimovCalc(localDayDec)

        self.dateOutput["text"] = asimovLs[0]
        self.timeOutput["text"] = asimovLs[1]

    #Finds local version of days elapsed decimal 
    #   to be thrown into the Asimov calendar.
    def findLocalDayDec(self, days):
        seconds = int(days * 86400)
        secondsElapsedInDay = seconds % 86400

        #Finds local and UTC hour.
        localHr = self.date.getHour(self.hour.get())
        utcHour = secondsElapsedInDay // 3600
        
        #Finds timezone difference between UTC and local time.
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        print(f"{localHr} {utcHour} FOUND TIMEZONE DIFF OF: {timeZoneDiff}")
        localSeconds = (seconds - (3600 * timeZoneDiff))
        
        return localSeconds / 86400

    #Determines the metric date 
    #   and metric time based on Isaac Asimov's format.
    def asimovCalc(self, daysElapsed):
        #Finds current metric date.
        currMetYear = int(daysElapsed) // 300
        daysElapsedInMetYear = int(daysElapsed) % 300
        currMetMonth = (daysElapsedInMetYear // 30) + 1
        currMetDay = (daysElapsedInMetYear % 30) + 1

        #Finds current metric time.
        timeOfDay = daysElapsed - int(daysElapsed)
        currMetHour = int(timeOfDay * 10)
        currMetMinute = int((timeOfDay * 1000) % 100)
        currMetSecond = int((timeOfDay * 100000) % 100)

        return [
            f"{currMetYear}-{str(currMetMonth).zfill(2)}-{str(currMetDay).zfill(2)}",
            f"{currMetHour}:{str(currMetMinute).zfill(2)}:{str(currMetSecond).zfill(2)}"
        ]



def main():
    root = Tk()
    root.title("Asimov Metric Time Calculator")
    metric = AsimovCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
