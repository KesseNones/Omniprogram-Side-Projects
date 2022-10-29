from tkinter import *
import math
from math import log
from tkinter import messagebox
import datetime
import time

class EasterCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.yearE = Entry(self.frameBottom, font = "Times 55")
        self.yearE.grid(row = 1, column = 0)

        self.convButtonI = Button(self.frameBottom, text = "Find Easter Date", 
            font = "Ariel 60", command = self.yearToCal)
        self.convButtonI.grid(row = 2, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 60", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)
    
        self.isStupid = True

    def quitButtonAction(self):
        self.window.destroy()

    def yearToCal(self):
        date = self.eCal()
        self.tOutput["text"] = date 

    def yearGet(self):
        if self.yearE.get() == "":
            messagebox.showerror("Empty Entry Error", "Enter a year!")
            return
        else:
            return int(self.yearE.get())

    def eCal(self):
        year = self.yearGet()
        month = 3
        day = 21
        moonAge = self.moonCalc(year, month, day)
        wkDay = self.week_fdn(year, month, day)
        curDay = self.currentDate(year, month, day)
        adv = 0
        self.dateCalc(adv)
        while not (14.765294 < moonAge < 15.765294):
            adv += 1
            self.dateCalc(adv)
            moonAge = self.moonCalc(self.yearFinal, self.monthFinal, self.dayFinal)
        wkDayII = self.week_fdn(self.yearFinal, self.monthFinal, self.dayFinal)
        adv = 0
        self.currentDate(self.yearFinal, self.monthFinal, self.dayFinal)
        if wkDayII == "Sunday":
            self.dateCalc(1)
            wkDayII = self.week_fdn(self.yearFinal, self.monthFinal, self.dayFinal)
        while wkDayII != "Sunday":
            adv += 1
            self.dateCalc(adv)
            wkDayII = self.week_fdn(self.yearFinal, self.monthFinal, self.dayFinal)
        mth = self.wordMonth()
        dateString = str(self.dayFinal) + " " + str(mth) + ", " +  str(self.yearFinal)
        return dateString

    def wordMonth(self):
        if self.monthFinal == 1:
            monthWord = "Jan"
        if self.monthFinal == 2:
            monthWord = "Feb"
        if self.monthFinal == 3:
            monthWord = "Mar"
        if self.monthFinal == 4:
            monthWord = "Apr"
        if self.monthFinal == 5:
            monthWord = "May"
        if self.monthFinal == 6:
            monthWord = "Jun"
        if self.monthFinal == 7:
            monthWord = "Jul"
        if self.monthFinal == 8:
            monthWord = "Aug"
        if self.monthFinal == 9:
            monthWord = "Sep"
        if self.monthFinal == 10:
            monthWord = "Oct"
        if self.monthFinal == 11:
            monthWord = "Nov"
        if self.monthFinal == 12:
            monthWord = "Dec"
        return monthWord    

    def currentDate(self, year, month, day):
        self.dateISO = datetime.date.today()
        self.currentYear = year
        self.currentMonth = month
        self.currentDay = day

    def isLeapYear(self, year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        else:
            return False

    def dateCalc(self, diff):
        year = self.currentYear
        month = self.currentMonth
        day = self.currentDay
        if diff >= 3000000:
            yearAdd = diff // 146097
            year += (yearAdd * 400)
            diff = diff % 146097
        if diff > 0:
            while diff > 0:
                leap = self.isLeapYear(year)
                day += 1
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day > 31:
                    month += 1
                    day -= 31
                if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                    month += 1
                    day -= 30
                if (month == 2 and leap == False and day > 28):
                    month += 1
                    day -= 28
                if (month == 2 and leap == True and day > 29):
                    month += 1
                    day -= 29
                if month == 12 and day > 31:
                    year += 1
                    month -= 11
                    day -= 31
                diff -= 1
            self.yearFinal = year
            self.monthFinal = month
            self.dayFinal = day
            return
        if diff <= -3000000:
            yearSub = diff // -146097
            year -= (yearSub * 400)
            diff = diff % -146097
        if diff < 0:
            while diff < 0:
                leap = self.isLeapYear(year)
                day -= 1
                if month == 3 and leap == False and day < 1:
                    month -= 1
                    day += 28
                if month == 3 and leap == True and day < 1:
                    month -= 1
                    day += 29
                if month == 1 and day < 1:
                    year -= 1
                    month += 11
                    day += 31
                if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) and day < 1:
                    month -= 1
                    day += 31
                if (month == 5 or month == 10 or month == 12 or month == 7) and day < 1:
                    month -= 1
                    day += 30
                if (month == 8) and day < 1:
                    month -= 1
                    day += 31
                diff += 1
            self.yearFinal = year
            self.monthFinal = month
            self.dayFinal = day
            return
        if diff == 0:
            self.yearFinal = year
            self.monthFinal = month
            self.dayFinal = day
            return

    def week_fdn(self, year, month, day):
        subtract = 0
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


    def moonCalc(self, year, month, day):
        moonPhase = ""
        metricDateCalc = self.metric_calc(year, month, day)
        moonBase = 4390.559679166
        metricDiff = metricDateCalc - moonBase
        moonAge = (metricDiff * 1000) % 29.530588
        if moonAge < 0:
            moonAge += 29.530588
        moonAgeII = round(moonAge, 6)
        moonAgeII = format(moonAgeII, ".6f")
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
        return moonAge
        
    def print_metric_meme(self, year, month, day, hour, minute):
        if year % 4 == 0 or year % 400 == 0:
                leap_year = True
        if year % 4 != 0 or year % 100 == 0:
                leap_year = False
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
        if leap_year == False:
            divider = 365
        if leap_year == True:
            divider = 366
        H = hour
        M = minute
        year = year + 10000
        MEMEI = D_Code_MKII - 1
        MEMEII = MEMEI / divider
        MEMEIII = MEMEII + year
        MEMEIV = MEMEIII / 2.7379093307922614306961635510947
        MEMEV = MEMEIV * 1000
        MEMEVI = math.trunc(MEMEV)
        MEMEVII = MEMEVI / 1000
        MEMEVIII = M / 60
        MEMEIX = H + MEMEVIII
        MEMEX = MEMEIX / 24
        MEMEXI = MEMEX * 1000
        MEMEXII = math.trunc(MEMEXI)
        MEMEXIII = MEMEXII / 1000000
        MEMEXIV = MEMEVII + MEMEXIII
        MEMEXV = MEMEXIV * 1000000
        MEMEXVI = math.trunc(MEMEXV)
        MEMEXVII = MEMEXVI / 1000000
        return MEMEXVII

    def metric_calc(self, year, month, day):
        if self.isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000
        hour = 0
        minute = 0
        if lower < year < upper:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
            metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.949
            rounderI = metric_time * 1000000000
            rounderII = math.trunc(rounderI)
            rounderIII = rounderII / 1000000000
        if year >= upper or year <= lower:
            rounderIII = self.print_metric_meme(year, month, day, hour, minute)
        return rounderIII
        

def main():
    root = Tk()
    root.title("Easter Date Calclator")
    temp = EasterCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
