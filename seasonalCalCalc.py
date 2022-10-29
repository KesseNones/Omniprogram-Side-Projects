from tkinter import *
import math
import time
import datetime
from tkinter import messagebox

class SeasonCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.isStupid = True

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55")
        self.messageI.grid(row = 0, column = 0)

        self.yearE = Entry(self.frameBottom, font = "Times 45")
        self.yearE.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 55")
        self.messageII.grid(row = 2, column = 0)

        self.monthE = Entry(self.frameBottom, font = "Times 45")
        self.monthE.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 55")
        self.messageIII.grid(row = 3, column = 0)

        self.dayE = Entry(self.frameBottom, font = "Times 45")
        self.dayE.grid(row = 3, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Convert to Season Calendar", 
            font = "Ariel 50", command = self.sCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 45", justify = LEFT, fg = "white", bg = "#f0f0f0")
        self.cOutput.grid(row = 5, column = 0)

        self.cOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 45", justify = LEFT, fg = "white", bg = "#f0f0f0")
        self.cOutputII.grid(row = 6, column = 0)
        
        self.cOutputIII = Label(self.frameBottom, text = "", 
            font = "Ariel 45", justify = LEFT, fg = "black", bg = "#f0f0f0")
        self.cOutputIII.grid(row = 7, column = 0)
        
        # self.cOutputIV = Label(self.frameBottom, text = "", 
        #     font = "Ariel 45", justify = LEFT)
        # self.cOutputIV.grid(row = 8, column = 0)

        # self.cOutputV = Label(self.frameBottom, text = "", 
        #     font = "Ariel 45", justify = LEFT)
        # self.cOutputV.grid(row = 9, column = 0)

        # self.cOutputVI = Label(self.frameBottom, text = "", 
        #     font = "Ariel 45", justify = LEFT)
        # self.cOutputVI.grid(row = 10, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def isLeapYear(self, year):
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True
        else:
            leap = False
        return leap

    def sCalCalc(self):
        self.calCalcI()
        self.moonCalc()
        if self.isStupid == False:
            self.moonCalc()
        date = self.calCalcII()
        weekDay = self.week_fdn()
        self.cOutput["text"] = weekDay + " " + date
        #self.cOutputII["text"] = ""
        # self.cOutputIII["text"] = self.Zy + " " + str(int(self.elmyr)) + ", " + self.Zce + ", " + str(self.ZE) + ", " + str(int(self.ZA)) + self.ORDII + " " + self.Eon
        # self.cOutputIV["text"] = "Luni-Solar Year: " + str(int(self.lunyr))
        # self.cOutputV["text"] = "Luni-Solar Mini Cycle: " + str(int(self.luncy))
        # self.cOutputVI["text"] = "Luni-Solar Mega Cycle: " + str(int(self.lunMcy))

    def calCalcI(self):
        if self.yearE.get() == "" or self.monthE.get() == "" or self.dayE.get() == "":
            messagebox.showerror("Empty Box Error", "Be sure all the boxes are filled!")
            return
        yearB = 2001
        monthB = 3
        dayB = 19
        yearC = int(self.yearE.get())
        monthC = int(self.monthE.get())
        dayC = int(self.dayE.get()) - 1
        if monthC > 12 or monthC < 1:
            messagebox.showerror("Out of Range Error", "Month must be smaller than 13 and larger than 0!")
            return
        if dayC + 1 > 31 or dayC + 1 < 1:
            messagebox.showerror("Out of Range Error", "Day must be smaller than 32 and larger than 0!")
            return
        leap_year = self.isLeapYear(yearB)
        leap_year = self.isLeapYear(yearC)
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
        self.isLeap = leap_year
        return

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
            season = "Spring 🌸"
            self.cOutput["fg"] = "#38e838"
            self.cOutput["bg"] = "#404040"
        if 93 <= self.ageDay < 186:
            seasonDay = (self.ageDay - 93) + 1
            season = "Summer 🔥"
            self.cOutput["fg"] = "yellow"
            self.cOutput["bg"] = "#404040"
        if 186 <= self.ageDay < 276:
            seasonDay = (self.ageDay - 186) + 1
            season = "Fall 🍂"
            self.cOutput["fg"] = "orange"
            self.cOutput["bg"] = "#404040"
        if 276 <= self.ageDay < 365 + leapYearBoost:
            seasonDay = (self.ageDay - 276) + 1
            season = "Winter ❄"
            self.cOutput["fg"] = "#1b6eff"
            self.cOutput["bg"] = "#404040"
        dateString = str(seasonDay) + " " + season + ", Year " + str(year)
        return dateString 

    def week_fdn(self):
        subtract = 0
        year = int(self.yearE.get())
        month = int(self.monthE.get())
        day = int(self.dayE.get())
        leaper = self.isLeapYear(year)
        if leaper and month < 3:
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

    def moonCalc(self):
        #🌑🌒🌓🌔🌕🌖🌗🌘
        moonPhase = ""
        metricDateCalc = self.metric_calc()
        moonBase = 4390.558679166
        metricDiff = metricDateCalc - moonBase
        moonAge = (metricDiff * 1000) % 29.530588
        if moonAge < 0:
            moonAge += 29.530588
        moonAgeII = round(moonAge, 6)
        moonAgeII = format(moonAgeII, ".6f")
        self.cOutputII["text"] = "Moon Age: " + str(moonAgeII)
        self.cOutputII["bg"] = "#6d6d6d"
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
        self.cOutputIII["bg"] = "#6d6d6d"
        self.cOutputIII["text"] = moonPhase

    def metricCalcII(self, year, dayNum, hour, minute):
        year += 10000
        fourCenturyCount = year // 400
        remainingYears = year % 400
        totalDays = fourCenturyCount * 146097
        while remainingYears > 0:
            leap = self.isLeapYear(remainingYears)
            if leap:
                totalDays += 366
            else:
                totalDays += 365
            remainingYears -= 1
        totalDays += dayNum - 1
        totalDays = totalDays / 1000
        totalDays = round(totalDays, 3)
        secTotal = (hour * 3600) + (minute * 60)
        dayDec = secTotal / 86400
        dayDec *= 1000000
        dayDec = math.floor(dayDec)
        dayDec = dayDec / 1000000000
        finalMetric = totalDays + dayDec
        return finalMetric 
        #4390.694 200 666

    def isLeapYear(self, year):
        if year % 4 == 0:
            leap = True
            if year % 100 == 0:
                leap = False
                if year % 400 == 0:
                    leap = True
        else:
            leap = False
        return leap

    def metric_calc(self):
        if self.isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000
        year = int(self.yearE.get())
        month = int(self.monthE.get())
        day = int(self.dayE.get())
        hour = 0
        minute = 0
        if lower < year < upper:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
            metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
            rounderI = metric_time * 1000000000
            rounderII = math.trunc(rounderI)
            rounderIII = rounderII / 1000000000
        if year >= upper or year <= lower:
            dayCount = self.findDayNumOfYear(year, month, day)
            rounderIII = self.metricCalcII(year, dayCount, hour, minute)
        return rounderIII

    def findDayNumOfYear(self, year, month, day):
        leap_year = self.isLeapYear(year)
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
    root.title("Seasonal Calendar Calculator")
    calCalc = SeasonCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
