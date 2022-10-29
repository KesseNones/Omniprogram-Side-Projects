from tkinter import *
import math
import time
import datetime
from tkinter import messagebox

class LunisolarCalendarCalc(object):
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
    
        self.convButton = Button(self.frameBottom, text = "Convert to Luni-Solar Calendar", 
            font = "Ariel 50", command = self.RCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 55", justify = LEFT)
        self.cOutput.grid(row = 5, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def RCalCalc(self):
        date = self.cal_calc()
        self.cOutput["text"] = date

    def isShortCycle(self, cyNum):
        fourLoc = cyNum % 4
        shortCyArr = [True, False, False, False]
        isShort = shortCyArr[fourLoc]
        return isShort

    def yearGet(self):
        if self.yearE.get() == "":
            messagebox.showerror("Empty Entry Error", "Put a year in!")
            return
        else:
            return int(self.yearE.get())

    def monthGet(self):
        if self.monthE.get() == "":
            messagebox.showerror("Empty Entry Error", "Put a month in!")
            return
        if 1 > int(self.monthE.get()) > 12:
            messagebox.showerror("Out of Range Error", "Month must be in range 1-12!")
            return
        else:
            return int(self.monthE.get())

    def dayGet(self):
        if self.dayE.get() == "":
            messagebox.showerror("Empty Entry Error", "Put a day in!")
            return
        if 1 > int(self.dayE.get()) > 12:
            messagebox.showerror("Out of Range Error", "Day must be in range 1-31!")
            return
        else:
            return int(self.dayE.get())

    def cal_calc(self):
        year = self.yearGet()
        month = self.monthGet()
        day = self.dayGet()
        baseDayNum = 4388023
        currentDayNum = self.metric_calc()
        currentDayNum = math.trunc(currentDayNum * 1000)
        dayDelta = currentDayNum - baseDayNum
        #27759 in four cycle
        monthsElapsed = 0
        baseCycleCount = 106
        cyclesElapsedTotal = (dayDelta // 27759) * 4 + baseCycleCount
        remainingCycleDays = dayDelta % 27759
        cyDayArr = [6939, 6940, 6940, 6940]
        shortCy = False
        if 0 <= remainingCycleDays < self.cyDaySum(cyDayArr, 1):
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 0)
            cyclesElapsedTotal += 0
            shortCy = True
        elif self.cyDaySum(cyDayArr, 1) <= remainingCycleDays < self.cyDaySum(cyDayArr, 2):
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 1)
            cyclesElapsedTotal += 1
        elif self.cyDaySum(cyDayArr, 2) <= remainingCycleDays < self.cyDaySum(cyDayArr, 3):
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 2)
            cyclesElapsedTotal += 2
        else:
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 3)
            cyclesElapsedTotal += 3
        daySub = shortCy
        #print(daySub, dayNumOfCycle)
        #cyclesElapsedTotal = (dayDelta // 6940) + baseCycleCount
        #dayNumOfCycle = (dayDelta % 6940)
        currentDayOf28MonthCycle = dayNumOfCycle % 827 + 1
        monthsElapsed = (dayNumOfCycle // 827) * 28
        if dayNumOfCycle < 6616:
            monthArr = [29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30, 30]
            if 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 1) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 0)
                monthsElapsed += 0
            elif self.cyDaySum(monthArr, 1) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 2) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 1)
                monthsElapsed += 1
            elif self.cyDaySum(monthArr, 2) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 3) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 2)
                monthsElapsed += 2
            elif self.cyDaySum(monthArr, 3) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 4) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 3)
                monthsElapsed += 3
            elif self.cyDaySum(monthArr, 4) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 5) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 4)
                monthsElapsed += 4
            elif self.cyDaySum(monthArr, 5) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 6) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 5)
                monthsElapsed += 5
            elif self.cyDaySum(monthArr, 6) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 7) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 6)
                monthsElapsed += 6
            elif self.cyDaySum(monthArr, 7) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 8) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 7)
                monthsElapsed += 7
            elif self.cyDaySum(monthArr, 8) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 9) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 8)
                monthsElapsed += 8
            elif self.cyDaySum(monthArr, 9) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 10) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 9)
                monthsElapsed += 9
            elif self.cyDaySum(monthArr, 10) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 11) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 10)
                monthsElapsed += 10
            elif self.cyDaySum(monthArr, 11) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 12) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 11)
                monthsElapsed += 11
            elif self.cyDaySum(monthArr, 12) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 13) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 12)
                monthsElapsed += 12
            elif self.cyDaySum(monthArr, 13) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 14) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 13)
                monthsElapsed += 13
            elif self.cyDaySum(monthArr, 14) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 15) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 14)
                monthsElapsed += 14
            elif self.cyDaySum(monthArr, 15) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 16) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 15)
                monthsElapsed += 15
            elif self.cyDaySum(monthArr, 16) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 17) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 16)
                monthsElapsed += 16
            elif self.cyDaySum(monthArr, 17) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 18) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 17)
                monthsElapsed += 17
            elif self.cyDaySum(monthArr, 18) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 19) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 18)
                monthsElapsed += 18
            elif self.cyDaySum(monthArr, 19) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 20) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 19)
                monthsElapsed += 19
            elif self.cyDaySum(monthArr, 20) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 21) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 20)
                monthsElapsed += 20
            elif self.cyDaySum(monthArr, 21) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 22) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 21)
                monthsElapsed += 21
            elif self.cyDaySum(monthArr, 22) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 23) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 22)
                monthsElapsed += 22
            elif self.cyDaySum(monthArr, 23) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 24) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 23)
                monthsElapsed += 23
            elif self.cyDaySum(monthArr, 24) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 25) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 24)
                monthsElapsed += 24
            elif self.cyDaySum(monthArr, 25) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 26) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 25)
                monthsElapsed += 25
            elif self.cyDaySum(monthArr, 26) + 1 <= currentDayOf28MonthCycle < self.cyDaySum(monthArr, 27) + 1:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 26)
                monthsElapsed += 26
            else:
                currentDay = currentDayOf28MonthCycle - self.cyDaySum(monthArr, 27)
                monthsElapsed += 27
        else:
            monthArrII = [29, 30, 29, 30, 29, 30, 29, 30, 29, 30 - daySub, 29]
            dayOfExceptionCycle = (dayNumOfCycle - 6616) + 1
            if self.cyDaySum(monthArrII, 0) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 1) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 0)
                monthsElapsed += 0
            elif self.cyDaySum(monthArrII, 1) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 2) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 1)
                monthsElapsed += 1
            elif self.cyDaySum(monthArrII, 2) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 3) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 2)
                monthsElapsed += 2
            elif self.cyDaySum(monthArrII, 3) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 4) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 3)
                monthsElapsed += 3
            elif self.cyDaySum(monthArrII, 4) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 5) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 4)
                monthsElapsed += 4
            elif self.cyDaySum(monthArrII, 5) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 6) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 5)
                monthsElapsed += 5
            elif self.cyDaySum(monthArrII, 6) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 7) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 6)
                monthsElapsed += 6
            elif self.cyDaySum(monthArrII, 7) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 8) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 7)
                monthsElapsed += 7
            elif self.cyDaySum(monthArrII, 8) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 9) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 8)
                monthsElapsed += 8
            elif self.cyDaySum(monthArrII, 9) + 1 <= dayOfExceptionCycle < self.cyDaySum(monthArrII, 10) + 1:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 9)
                monthsElapsed += 9
            else:
                currentDay = dayOfExceptionCycle - self.cyDaySum(monthArrII, 10)
                monthsElapsed += 10
        currentMonth = monthsElapsed + 1
        dateString = str(cyclesElapsedTotal) + "-" + str(currentMonth) + "-" + str(currentDay)
        trueDateString = self.toLuniSolar(cyclesElapsedTotal, currentMonth, currentDay)
        return trueDateString
    
    def toLuniSolar(self, cycles, month, day):
        year = cycles * 19
        monthCountArr = [12, 12, 13, 12, 12, 13, 12, 13, 12, 12, 13, 12, 12, 13, 12, 12, 13, 12, 13]
        if self.cyDaySum(monthCountArr, 0) + 1 <= month < self.cyDaySum(monthCountArr, 1) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 0)
            year += 0
        elif self.cyDaySum(monthCountArr, 1) + 1 <= month < self.cyDaySum(monthCountArr, 2) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 1)
            year += 1
        elif self.cyDaySum(monthCountArr, 2) + 1 <= month < self.cyDaySum(monthCountArr, 3) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 2)
            year += 2
        elif self.cyDaySum(monthCountArr, 3) + 1 <= month < self.cyDaySum(monthCountArr, 4) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 3)
            year += 3
        elif self.cyDaySum(monthCountArr, 4) + 1 <= month < self.cyDaySum(monthCountArr, 5) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 4)
            year += 4
        elif self.cyDaySum(monthCountArr, 5) + 1 <= month < self.cyDaySum(monthCountArr, 6) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 5)
            year += 5
        elif self.cyDaySum(monthCountArr, 6) + 1 <= month < self.cyDaySum(monthCountArr, 7) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 6)
            year += 6
        elif self.cyDaySum(monthCountArr, 7) + 1 <= month < self.cyDaySum(monthCountArr, 8) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 7)
            year += 7
        elif self.cyDaySum(monthCountArr, 8) + 1 <= month < self.cyDaySum(monthCountArr, 9) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 8)
            year += 8
        elif self.cyDaySum(monthCountArr, 9) + 1 <= month < self.cyDaySum(monthCountArr, 10) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 9)
            year += 9
        elif self.cyDaySum(monthCountArr, 10) + 1 <= month < self.cyDaySum(monthCountArr, 11) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 10)
            year += 10
        elif self.cyDaySum(monthCountArr, 11) + 1 <= month < self.cyDaySum(monthCountArr, 12) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 11)
            year += 11
        elif self.cyDaySum(monthCountArr, 12) + 1 <= month < self.cyDaySum(monthCountArr, 13) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 12)
            year += 12
        elif self.cyDaySum(monthCountArr, 13) + 1 <= month < self.cyDaySum(monthCountArr, 14) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 13)
            year += 13
        elif self.cyDaySum(monthCountArr, 14) + 1 <= month < self.cyDaySum(monthCountArr, 15) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 14)
            year += 14
        elif self.cyDaySum(monthCountArr, 15) + 1 <= month < self.cyDaySum(monthCountArr, 16) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 15)
            year += 15
        elif self.cyDaySum(monthCountArr, 16) + 1 <= month < self.cyDaySum(monthCountArr, 17) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 16)
            year += 16
        elif self.cyDaySum(monthCountArr, 17) + 1 <= month < self.cyDaySum(monthCountArr, 18) + 1:
            currentMonth = month - self.cyDaySum(monthCountArr, 17)
            year += 17
        else:
            currentMonth = month - self.cyDaySum(monthCountArr, 18)
            year += 18
        nameOfMonth = self.monthName(currentMonth)
        date = str(day) + " " + nameOfMonth + "(" + str(currentMonth) + "), " + str(year)
        return date

    def monthName(self, monthNum):
        if monthNum == 1:
            name = "Wolf"
        elif monthNum == 2:
            name = "Snow"
        elif monthNum == 3:
            name = "Worm"
        elif monthNum == 4:
            name = "Pink"
        elif monthNum == 5:
            name = "Flower"
        elif monthNum == 6:
            name = "Strawberry"
        elif monthNum == 7:
            name = "Buck"
        elif monthNum == 8:
            name = "Sturgeon"
        elif monthNum == 9:
            name = "Corn"
        elif monthNum == 10:
            name = "Harvest"
        elif monthNum == 11:
            name = "Beaver"
        elif monthNum == 12:
            name = "Cold"
        else:
            name = "Blue"
        return name
        

    def isMetonicLeapYear(self, year):
        if year == 2 or year == 5 or year == 7 or year == 10 or year == 13 or year == 16 or year == 18:
            return True
        else:
            return False

    def cyDaySum(self, monthArr, index):
        if index == 0:
            return 0
        else:
            i = 0
            subTotal = 0
            while i < index:
                subTotal += monthArr[i]
                i += 1
            return subTotal

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

def main():
    root = Tk()
    root.title("Lunisolar Calendar Calculator")
    calCalc = LunisolarCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
