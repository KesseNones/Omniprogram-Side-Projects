#Jesse A. Jones
#Version: 2022-12-31.9

from tkinter import *
import dateHandling
import leapDetect
import datetime
import metricTime
from time import time

#Contains the members and methods necessary to count down 
#   to a date or up from a date in terms of time units 
#   of years, months, days, hours, and minutes.
class CountDownAlt(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Contains time input fields, start countdown button, 
        #   and countdown clock.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year entry field.
        self.messageI = Label(self.frameBottom, text = "Enter year:", font = "Times 30", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Times 30")
        self.year.grid(row = 0, column = 1)

        #Month entry field.
        self.messageII = Label(self.frameBottom, text = "Enter month:", font = "Times 30", anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Times 30")
        self.month.grid(row = 2, column = 1)

        #Day entry field.
        self.messageIII = Label(self.frameBottom, text = "Enter day:", font = "Times 30", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Times 30")
        self.day.grid(row = 3, column = 1)

        #Hour entry field.
        self.messageIV = Label(self.frameBottom, text = "Enter hour:", font = "Times 30", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = "Times 30")
        self.hour.grid(row = 4, column = 1)

        #Minute entry field.
        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Times 30", anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = "Times 30")
        self.minute.grid(row = 5, column = 1)
    
        #Start countdown button.
        self.convButton = Button(self.frameBottom, text = "Start Countdown", 
            font = "Times 30", command = self.displayTimeDiff)
        self.convButton.grid(row = 6, column = 0)

        #Time output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Times 30")
        self.tOutput.grid(row = 6, column = 1)

        #Used in detecting leap years.
        self.leap = leapDetect.IsLeap()

    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()

    #Repeatedly calls the countdown calculation 
    #   and displays it to the user, making it a live countdown.
    def displayTimeDiff(self):
        nonMetricTimeString = self.calcTimeDelta()
        self.tOutput["text"] = nonMetricTimeString
        self.tOutput.after(1, self.displayTimeDiff)

    #Calculates the countdown time and returns the countdown string.
    #Returns a countdown/countup string.
    def calcTimeDelta(self):
        #Object instances used in input handling and metric time finding.
        date = dateHandling.GetDate()
        metric = metricTime.MetricTime()

        #Handles input fields.
        yearIn = date.getYear(self.year.get())
        monthIn = date.getMonth(self.month.get())
        dayIn = date.getDay(self.day.get())
        hourIn = date.getHour(self.hour.get())
        minuteIn = date.getMinOrSec(self.minute.get())

        #Used in calculation of metric dates.
        isOutOfRange = (yearIn < 1969 or yearIn > 3002)

        #Acquires local timezone and uses it 
        #   to calculate the timezone difference from UTC.
        unix = int(time())
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (unix % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = utcHour - localHr
        timeZoneUTCOffshift = timeZoneDiff

        #Calculates metric date based on input fields 
        #   and gets the current metric date. 
        #   The lengthy expression following 
        #   the function call for metricIn compensates for calculation 
        #   of metric dates for out of range years not being in range of UTC.
        metricIn = metric.metric_calc(yearIn, monthIn, dayIn, hourIn, minuteIn) + ( ( ((3600 * timeZoneUTCOffshift) * ( 0.864 ** (-1) )) / 100000000) * int(isOutOfRange))
        metricCurr = metric.metric_time()

        metricDelta = metricIn - metricCurr

        #Current date and time data fetched.
        yearCurr = local.year
        monthCurr = local.month
        dayCurr = local.day
        hourCurr = local.hour
        minuteCurr = local.minute

        #Calculates date and time deltas.
        deltaArr = self.dateFromDayDelta(yearCurr, monthCurr, dayCurr, int(metricDelta * 1000))
        timeArr = self.findTimeDelta(metricDelta)

        yearDelta = str(deltaArr[0]).zfill(4)
        monthDelta = str(deltaArr[1]).zfill(2)
        dayDelta = str(deltaArr[2]).zfill(2)

        hourDel = str(timeArr[0]).zfill(2)
        minDel = str(timeArr[1]).zfill(2)
        secDel = str(timeArr[2]).zfill(2)

        return f"{yearDelta}Y {monthDelta}M {dayDelta}D {hourDel}h {minDel}m {secDel}"

    #Calculates the date some number of days ago 
    #   or in the future based on the present date input 
    #   and the day delta.
    #Returns an array of time deltas of years, months, and days respectively.
    def dateFromDayDelta(self, year, month, day, dayDelta):
        monthDayArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        diff = dayDelta
        dayInit = day
        monthInit = month
        yearDelta = 0
        monthDelta = 0
        dayDelta = 0

        #Returns delta of 0 for all three 
        #   if there is no day difference between the dates.
        if diff == 0:
            return [yearDelta, monthDelta, dayDelta]

        #Handles case of date being in the future.
        elif diff > 0:
            #Generates part of the year delta for years more 
            #   than 800 years in the future, to avoid the linear 
            #   time component of this function becoming too problematic.
            if diff >= 292194:
                yearAdd = diff // 146097
                year += (yearAdd * 400)
                yearDelta += (yearAdd * 400)
                diff = diff % 146097

            #Calculates the remaining portion of the time delta 
            #   after potentially being shrunk by the above if statement.
            while diff > 0:
                #Checks for leap year.
                leap = self.leap.isLeapYear(year)
                monthDayArr[1] = 28 + leap
                
                day += 1
                dayDelta += 1

                #If the day is past 31 in a 31 day month, 
                #   increment month, and decrement day by 31.
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day > 31:
                    month += 1
                    day -= 31

                #If the day is past 30 in a 30 day month, 
                #   increment month, and decrement day by 30.
                if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                    month += 1
                    day -= 30

                #If the day is past 28 or 29 in Feburary, 
                #   increment month, and decrement day by 28 or 29.
                if (month == 2 and day > (28 + leap)):
                    month += 1
                    day -= (28 + leap)

                #If it's past New Year's Eve, 
                #   increment year and reset month and day.
                if month == 12 and day > 31:
                    year += 1
                    month -= 11
                    day -= 31

                index = ((monthInit - 1) + monthDelta) % 12

                #If the dayDelta has reached maximum size based 
                #   on a given month, reset day delta 
                #   and potentially other things.
                if (dayDelta == monthDayArr[index]):

                    #Reset dayDelta, monthDelta, and increment year delta 
                    #   if the months match and the day is sufficiently large.
                    #Otherwise just reset dayDelta and increment month Delta.
                    if (month == monthInit and day >= dayInit):
                        monthDelta = 0
                        dayDelta = 0
                        yearDelta += 1
                    else:
                        monthDelta += 1
                        dayDelta = 0

                diff -= 1

            return [yearDelta, monthDelta, dayDelta]

        #Covers case of date being in the past.
        else:
            #Generates part of the year delta for years more 
            #   than 800 years in the past, to avoid the linear 
            #   time component of this function becoming too problematic.
            if diff <= -292194:
                yearSub = (diff * -1) // 146097
                year -= (yearSub * 400)
                yearDelta += (yearSub * 400)
                diff = ((diff * -1) % 146097) * -1

            #Calculates the remaining portion of the time delta 
            #   after potentially being shrunk by the above if statement.
            while diff < 0:
                leap = self.leap.isLeapYear(year)
                monthDayArr[1] = 28 + leap

                day -= 1
                dayDelta += 1

                #If the day is less than 1 in March, 
                #   back the month off and increment 28 or 29 days.
                if month == 3 and day < 1:
                    month -= 1
                    day += (28 + leap)

                #If a time before a New Year's Day is reached, 
                #   decrement year and set month and day to maximum.
                if month == 1 and day < 1:
                    year -= 1
                    month += 11
                    day += 31

                #If a day before the start of a 30 day month, 
                #   add 31 days to day and decrement month.
                if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) and day < 1:
                    month -= 1
                    day += 31

                #If a day before the start of a 31 day month, 
                #   add 30 days to day and decrement month.
                if (month == 5 or month == 10 or month == 12 or month == 7) and day < 1:
                    month -= 1
                    day += 30

                #Increment 31 days and decrement month 
                #   if time traveled to before the start of August.
                if (month == 8) and day < 1:
                    month -= 1
                    day += 31

                index = ((monthInit - 2) - monthDelta) % 12
                
                #If the dayDelta has reached maximum size based 
                #   on a given month, reset day delta 
                #   and potentially other things.
                if (dayDelta == monthDayArr[index]):

                    #Reset dayDelta, monthDelta, and increment year delta 
                    #   if the months match and the day is sufficiently large.
                    #Otherwise just reset dayDelta and increment month Delta.
                    if (month == monthInit and dayInit <= day):
                        monthDelta = 0
                        dayDelta = 0
                        yearDelta += 1
                    else:
                        monthDelta += 1
                        dayDelta = 0

                diff += 1

            return [yearDelta, monthDelta, dayDelta]

    #Finds the time until or elapsed from 
    #   a point in time based 
    #   on the input metric time delta.
    #Returns an array of time deltas of hours, minutes, and seconds.
    def findTimeDelta(self, metricDelta):
        mecondDelta = abs(metricDelta) * 100000000
        secondDelta = (mecondDelta * 0.864)
        secondsOfDay = secondDelta % 86400
        hour = int(secondsOfDay // 3600)
        secondsOfDay %= 3600
        minute = int(secondsOfDay // 60)
        secondsOfDay %= 60
        second = int(secondsOfDay)
        return [hour, minute, second] 

def main():
    root = Tk()
    root.title("Regular Countdown Timer II")
    metric = CountDownAlt(root)
    root.mainloop()

if __name__ == "__main__":
    main()
