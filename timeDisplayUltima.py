#Jesse A. Jones
#Version: 2023-06-10.91

import time
from tkinter import *
import math
import datetime

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

        #Starts recursive date update.
        self.dateUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates and displays all dates.
    def dateUpdate(self):
        #Finds and displays metric date.
        date = self.metric_time()
        date = format(date, ".9f")
        self.messageMetric["text"] = "MD: " + date
        
        #Finds and displays TNG stardate.
        stardt = self.stardate()
        stardt = format(stardt, ".5f")
        self.messageStardateTNG["text"] = "TNG SD: " + stardt
        
        #Finds and displays TOS stardate.
        dateStar = self.stardateTOS()
        dateStar = format(dateStar, ".5f")
        self.messageStardateTOS["text"] = "TOS SD: " + str(dateStar) + " " + "(" + str(int(self.superStar)) + ")"
        
        #Finds UTC and local time, displaying them.
        self.currentTime()
        self.messageTime["text"] = "UTC " + self.timeNowUTC + " | Local " + self.timeNowLocal

        #Finds day of week and shortens it to a three letter abreviation.
        week = self.week_fdn()
        week = week[0] + week[1] + week[2] + "."

        #Finds date in seasonal calendar.
        self.calCalcI()
        seasonCalDate = self.calCalcII()
        
        #Finds current date as date string.
        readMonthISODate = self.textDate()

        #Displays current date, day of the week, and seasonal calendar date.
        self.messageDate["text"] = readMonthISODate + " " + week + " " + seasonCalDate
        
        #Finds current week number.
        weekNum = datetime.date.today().isocalendar()[1]
        weekNum = str(weekNum).zfill(2)
        
        #Displays week number and day number of year.
        self.messageWeeknumber["text"] = "Week: " + weekNum + " | " + "Day: " + self.dayOfYear
        
        #Finds and displays moon phase.
        self.moonCalc()
        
        self.window.after(1, self.dateUpdate)

    #Constructs ISO date string based on current date.
    def textDate(self):
        month = self.currentMonth
        monthStrArr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        monthStr = monthStrArr[int(month) - 1]
        dateString = str(self.currentYear) + "-" + monthStr + "-" + str(self.currentDay).zfill(2)
        return dateString

    #Calculates current metric time.
    def metric_time(self):
        t = time.time()
        metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
        rounderI = metric_time * 1000000000
        rounderII = math.trunc(rounderI)
        rounderIII = rounderII / 1000000000
        return rounderIII

    #Calculates current stardate.
    def stardate(self):
        t = time.time()
        s = (t / 31557.6) + (740583679.968 / 31557.6)
        RI = s * 100000
        RII = math.trunc(RI)
        RIII = RII / 100000
        return RIII

    #Calculates TOS stardate.
    def stardateTOS(self):
        t = time.time()
        s = (6059232000 / 86400) - (t / 86400)
        s *= 5
        subStar = abs((s % 10000) - 10000)
        subStar = subStar * (100000)
        subStar = math.trunc(subStar)
        subStar = subStar / (100000)
        superStar = s // 10000
        self.superStar = (superStar * -1) - 1
        return subStar

    #Fetches current time and saves it into a bunch of class variables.
    #THIS IS PRETTY GROSS. THIS SHOULD RETURN A LIST OF TIME STUFF, RATHER THAN SETTING A BUTTLOAD OF CLASS VARIABLES
    def currentTime(self):
        #Finds local time.
        self.local = datetime.datetime.now()
        self.timeNowLocal = self.local.strftime("%H:%M:%S")
        
        #Finds UTC time.
        self.UTC = datetime.datetime.utcnow()
        self.timeNowUTC = self.UTC.strftime("%H:%M:%S")
        
        #Finds ISO date.
        self.dateISO = datetime.date.today()
        self.currentYear = self.dateISO.year
        self.currentMonth = self.dateISO.month
        self.currentDay = self.dateISO.day
        
        #Finds day of year.
        self.dayOfYear = self.dateISO.strftime("%j")

    #Finds current day of week based on current date.
    def week_fdn(self):
        subtract = 0
        year = int(self.currentYear)
        month = int(self.currentMonth)
        day = int(self.currentDay)
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

    #Calculates current moon age and phase.
    def moonCalc(self):
        #🌑🌒🌓🌔🌕🌖🌗🌘
        moonPhase = ""
        metricDate = self.metric_time()
        moonBase = 4390.562679166
        metricDiff = metricDate - moonBase
        moonAge = (metricDiff * 1000) % 29.530588
        if moonAge < 0:
            moonAge += 29.530588
        moonAgePrint = round(moonAge, 6)
        moonAgePrint = format(moonAgePrint, ".6f")
        self.messageMoonAge["text"] = "Moon Age: " + moonAgePrint
        if 0.0 <= moonAge < 3.6913235:
            moonPhase = "New Moon 🌑"
        if 3.6913235 <= moonAge < 7.382647:
            moonPhase = "Waxing Crescent 🌒"
        if 7.382647 <= moonAge < 11.0739705:
            moonPhase = "First Quarter 🌓"
        if 11.0739705 <= moonAge < 14.765294:
            moonPhase = "Waxing Gibbous 🌔"
        if 14.765294 <= moonAge < 18.4566175:
            moonPhase = "Full Moon 🌕"
        if 18.4566175 <= moonAge < 22.147941:
            moonPhase = "Waning Gibbous 🌖"
        if 22.147941 <= moonAge < 25.8392645:
            moonPhase = "Third Quarter 🌗"
        if 25.8392645 <= moonAge < 29.530588:
            moonPhase = "Waning Crescent 🌘"
        self.messageMoonPhase["text"] = "Phase: " +  moonPhase

    #GROSS OUTDATED CODE USED TO FIND THE SEASONAL DATE.
    def calCalcI(self):
        yearB = 2001
        monthB = 3
        dayB = 19
        yearC = int(self.currentYear)
        monthC = int(self.currentMonth)
        dayC = int(self.currentDay) - 1
        if yearB % 4 != 0 or yearB % 100 == 0:
            leap_year = False
        if yearB % 4 == 0 or yearB % 400 == 0:
            leap_year = True
        if yearC % 4 != 0 or yearC % 100 == 0:
            leap_year = False
        if yearC % 4 == 0 or yearC % 400 == 0:
            leap_year = True
        if leap_year == False:
            div = 365
        if leap_year == True:
            div = 366
        if monthB == 1:
            D_Code_B = 0
        if monthB == 2:
            D_Code_B = 31
        if monthB == 3:
            D_Code_B = 59
            if leap_year == True:
                D_Code_B = 60
        if monthB == 4:
            D_Code_B = 90
            if leap_year == True:
                D_Code_B = 91
        if monthB == 5:
            D_Code_B = 120
            if leap_year == True:
                D_Code_B = 121
        if monthB == 6:
            D_Code_B = 151
            if leap_year == True:
                D_Code_B = 152
        if monthB == 7:
            D_Code_B = 181
            if leap_year == True:
                D_Code_B = 182
        if monthB == 8:
            D_Code_B = 212
            if leap_year == True:
                D_Code_B = 213
        if monthB == 9:
            D_Code_B = 243
            if leap_year == True:
                D_Code_B = 244
        if monthB == 10:
            D_Code_B = 273
            if leap_year == True:
                D_Code_B = 274
        if monthB == 11:
            D_Code_B = 304
            if leap_year == True:
                D_Code_B = 305
        if monthB == 12:
            D_Code_B = 334
            if leap_year == True:
                D_Code_B = 335
        if monthC == 1:
            D_Code_C = 0
        if monthC == 2:
            D_Code_C = 31
        if monthC == 3:
            D_Code_C = 59
            if leap_year == True:
                D_Code_C = 60
        if monthC == 4:
            D_Code_C = 90
            if leap_year == True:
                D_Code_C = 91
        if monthC == 5:
            D_Code_C = 120
            if leap_year == True:
                D_Code_C = 121
        if monthC == 6:
            D_Code_C = 151
            if leap_year == True:
                D_Code_C = 152
        if monthC == 7:
            D_Code_C = 181
            if leap_year == True:
                D_Code_C = 182
        if monthC == 8:
            D_Code_C = 212
            if leap_year == True:
                D_Code_C = 213
        if monthC == 9:
            D_Code_C = 243
            if leap_year == True:
                D_Code_C = 244
        if monthC == 10:
            D_Code_C = 273
            if leap_year == True:
                D_Code_C = 274
        if monthC == 11:
            D_Code_C = 304
            if leap_year == True:
                D_Code_C = 305
        if monthC == 12:
            D_Code_C = 334
            if leap_year == True:
                D_Code_C = 335
        D_Code_BII = D_Code_B + dayB
        D_Code_CII = D_Code_C + dayC
        Age_int = yearC - yearB
        age_alt = yearC - yearB
        if D_Code_CII > D_Code_BII:
                Age_day = D_Code_CII - D_Code_BII
        if D_Code_CII < D_Code_BII:
                Age_day = (D_Code_CII - D_Code_BII) + div
                age_alt -= 1
        if D_Code_CII == D_Code_BII:
                Age_day = 0
        Age_dec = (D_Code_CII - D_Code_BII) / div
        AGE = Age_int + Age_dec
        AGE = AGE * 1000
        AGE = round(AGE)
        AGE = AGE / 1000
        self.AGE = AGE
        self.ageAlt = age_alt 
        self.ageDay = Age_day
        self.isLeapYear = leap_year
        return

    #XTREME YUCKY
    def calCalcII(self):
        # Spring 93 days, Summer 93 days, Fall 90 days, Winter 89 days cm, 90 lpy
        leapYearBoost = 0
        season = "null"
        seasonDay = 0
        year = self.ageAlt + 1
        if self.isLeapYear:
            leapYearBoost = 1
        if 0 <= self.ageDay < 93:
            seasonDay = self.ageDay + 1
            season = "🌸"
            self.messageDate["fg"] = "#38e838"
        if 93 <= self.ageDay < 186:
            seasonDay = (self.ageDay - 93) + 1
            season = "🔥"
            self.messageDate["fg"] = "yellow"
        if 186 <= self.ageDay < 276:
            seasonDay = (self.ageDay - 186) + 1
            season = "🍂"
            self.messageDate["fg"] = "orange"
        if 276 <= self.ageDay < 365 + leapYearBoost:
            seasonDay = (self.ageDay - 276) + 1
            season = "❄"
            self.messageDate["fg"] = "#1b6eff"
        dateString = str(seasonDay) + season + str(year)
        return dateString 

def main():
    root = Tk()
    root.title("Time Display Ultima")
    dateAndTime = Date(root)
    root.mainloop()

if __name__ == "__main__":
    main()
