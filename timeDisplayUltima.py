#Jesse A. Jones
#Version: 2024-03-30.31

import time
from tkinter import *
import datetime
import metricTime
import weekCalculator
import leapDetect

#This class displays multiple time systems at once in a live widget.
class Date(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds time output fields.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        FONT = "Ariel 20"

        #Displays metric date.
        self.messageMetric = Label(self.frameBottom, text = "", font = FONT, anchor = "w")
        self.messageMetric.grid(row = 0, column = 0)

        #Displays TNG stardate.
        self.messageStardateTNG = Label(self.frameBottom, text = "", font = FONT, anchor = "w")
        self.messageStardateTNG.grid(row = 1, column = 0)

        #Displays TOS stardate.
        self.messageStardateTOS = Label(self.frameBottom, text = "", font = FONT, anchor = "w")
        self.messageStardateTOS.grid(row = 2, column = 0)

        #Displays current time.
        self.messageTime = Label(self.frameBottom, text = "", font = FONT, anchor = "w")
        self.messageTime.grid(row = 3, column = 0)

        #Displays current date and seasonal calendar.
        self.messageDate = Label(self.frameBottom, text = "", font = FONT, anchor = "w", bg = "#373737")
        self.messageDate.grid(row = 4, column = 0)

        #Displays week number and day number.
        self.messageWeeknumber = Label(self.frameBottom, text = "", font = FONT)
        self.messageWeeknumber.grid(row = 5, column = 0)

        #Displays moon age.
        self.messageMoonAge = Label(self.frameBottom, text = "", font = FONT)
        self.messageMoonAge.grid(row = 7, column = 0)

        #Displays moon phase.
        self.messageMoonPhase = Label(self.frameBottom, text = "", font = FONT)
        self.messageMoonPhase.grid(row = 8, column = 0)

        #Used in fetching metric date, finding day 
        #   of week from date, and determining if year is leap year.
        self.metric = metricTime.MetricTime()
        self.week = weekCalculator.WeekFinder()
        self.leap = leapDetect.IsLeap()

        #Starts recursive date update.
        self.dateUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates and displays all dates.
    def dateUpdate(self):
        #Finds and displays metric date.
        date = self.metric.metric_time()
        date = format(date, ".9f")
        self.messageMetric["text"] = f"MD: {date}"
        
        #Finds and displays TNG stardate.
        tngStar = self.stardate()
        tngStar = format(tngStar, ".5f")
        self.messageStardateTNG["text"] = f"TNG SD: {tngStar}"
        
        #Finds and displays TOS stardate.
        tosStar = self.stardateTOS()
        tosStar[0] = format(tosStar[0], ".5f")
        self.messageStardateTOS["text"] = f"TOS SD: {tosStar[0]} ({int(tosStar[1])})"
        
        #Finds local time.
        local = datetime.datetime.utcnow()
        timeNowLocal = local.strftime("%H:%M:%S")
        
        #Finds UTC time.
        UTC = datetime.datetime.utcnow()
        timeNowUTC = UTC.strftime("%H:%M:%S")
        
        #Finds ISO date.
        dateISO = datetime.datetime.now()
        currentYear = dateISO.year
        currentMonth = dateISO.month
        currentDay = dateISO.day
        currentHour = dateISO.hour
        currentMinute = dateISO.minute
        
        #Finds day of year.
        dayOfYear = dateISO.strftime("%j")

        #Finds UTC and local time, displaying them.
        self.messageTime["text"] = f"UTC: {timeNowUTC} | Local: {timeNowLocal}"
 
        #Finds day of week and shortens it to a three letter abreviation.
        week = self.week.weekFind(currentYear, currentMonth, currentDay)
        week = week[0] + week[1] + week[2] + "."

        #Finds date in seasonal calendar.
        seasonalStuff = self.calcSeasonal(currentYear, currentMonth, currentDay)

        #Finds current date as date string.
        readMonthISODate = self.textDate(currentYear, currentMonth, currentDay)

        #Displays current date, day of the week, and seasonal calendar date.
        self.messageDate["text"] = f"{readMonthISODate} {week}\n{seasonalStuff[0]}"
        self.messageDate["fg"] = seasonalStuff[1]
        
        #Finds current week number.
        weekNum = datetime.date.today().isocalendar()[1]
        weekNum = str(weekNum).zfill(2)
        
        #Displays week number and day number of year.
        self.messageWeeknumber["text"] = "Week: " + weekNum + " | " + "Day: " + dayOfYear
        
        #Finds and displays moon phase.
        moonInfo = self.moonCalc()
        self.messageMoonAge["text"] = f"Moon Age: {moonInfo[0]} Days"
        self.messageMoonPhase["text"] = moonInfo[1]
        
        self.window.after(1, self.dateUpdate)

    #Constructs ISO date string based on current date.
    def textDate(self, year, month, day):
        monthStrArr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthStr = monthStrArr[month - 1]
        dateString = str(year) + "-" + monthStr + "-" + str(day).zfill(2)
        return dateString

    #Calculates current stardate.
    def stardate(self):
        t = time.time()
        s = (t / 31557.6) + (740583679.968 / 31557.6)
        RI = s * 100000
        RII = int(RI)
        RIII = RII / 100000
        return RIII

    #Calculates TOS stardate.
    def stardateTOS(self):
        t = time.time()
        s = (6059232000 / 86400) - (t / 86400)
        s *= 5
        subStar = abs((s % 10000) - 10000)
        subStar = subStar * 100000
        subStar = int(subStar)
        subStar = subStar / 100000
        superStar = s // 10000
        superStar = (superStar * -1) - 1
        return [subStar, superStar]

    #Calculates moon phase based on metric date and displays results.
    def moonCalc(self):
        #Finds current metric date and finds difference from base metric date.
        metricDateCalc = self.metric.metric_time()
        moonBase = 4390.562679166
        metricDiff = metricDateCalc - moonBase
        
        #Metric delta used to find moon age.
        moonAge = (metricDiff * 1000) % 29.530588
        #Accounts for negative moon age edge case.
        if moonAge < 0:
            moonAge += 29.530588
        
        #Formats moon age decimal.
        moonAgeDisp = round(moonAge, 6)
        moonAgeDisp = format(moonAgeDisp, ".6f")
        
        #Determines which moon phase the moon is currently in.
        if 0.0 <= moonAge < 3.6913235:
            moonPhase = "New Moon 🌑"
        elif 3.6913235 <= moonAge < 7.382647:
            moonPhase = "Waxing Crescent 🌒"
        elif 7.382647 <= moonAge < 11.0739705:
            moonPhase = "First Quarter 🌓"
        elif 11.0739705 <= moonAge < 14.765294:
            moonPhase = "Waxing Gibbous 🌔"
        elif 14.765294 <= moonAge < 18.4566175:
            moonPhase = "Full Moon 🌕"
        elif 18.4566175 <= moonAge < 22.147941:
            moonPhase = "Waning Gibbous 🌖"
        elif 22.147941 <= moonAge < 25.8392645:
            moonPhase = "Third Quarter 🌗"
        elif 25.8392645 <= moonAge < 29.530588:
            moonPhase = "Waning Crescent 🌘"
        else:
            moonPhase = "WTF???"

        return [moonAgeDisp, moonPhase]

    #Given input year, month, and day, calculates seasonal calendar.
    def calcSeasonal(self, year, month, day):
        #Finds days elapsed in gregorian year and seasonal year.
        dayCount = self.metric.findDayNumOfYear(year, month, day) - 1
        seasonalDayCount = dayCount - 78

        #Accounts for if seasonal day count is negative.
        seasonalYear = year - (seasonalDayCount < 0)
        seasonalDayCount %= (365 + (self.leap.isLeapYear(year - 1)))

        #Finds seasonal date from seasonal day count.
        resArr = self.findSeasonAndDay(seasonalDayCount)
        sYear = year - 2000
        season = resArr[0]
        sDay = resArr[1]
        fgColor = resArr[2]

        #Date string and foreground color returned.
        return [f"{str(sDay).zfill(2)} {season} {sYear}", fgColor]

    #Calculates the seasonal date based on input year and day number.
    def findSeasonAndDay(self, dayNum):
        #Indicates how long each season is for the northern hemisphere.
        # Spring 93 days, Summer 93 days, Fall 90 days, Winter 89 days cm, 90 lpy

        fgColor = None
        seasonDay = None

        #Spring season case.
        if 0 <= dayNum < 93:
            seasonDay = dayNum + 1
            season = "Sp. 🌸"
            fgColor = "#38e838"

        #Summer season case.
        elif 93 <= dayNum < 186:
            seasonDay = (dayNum - 93) + 1
            season = "Su. 🔥"
            fgColor = "yellow"
        
        #Autumn season case.
        elif 186 <= dayNum < 276:
            seasonDay = (dayNum - 186) + 1
            season = "Fa. 🍂"
            fgColor = "orange"
        
        #Winter season case.
        else:
            seasonDay = (dayNum - 276) + 1
            season = "Wi. ❄"
            fgColor = "#1b6eff"

        return [season, seasonDay, fgColor]

def main():
    root = Tk()
    root.title("Time Display Ultima")
    dateAndTime = Date(root)
    root.mainloop()

if __name__ == "__main__":
    main()
