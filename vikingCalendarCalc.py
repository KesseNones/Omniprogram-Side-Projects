from tkinter import *
import math
import time
import datetime
from tkinter import messagebox

class VikingCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.engButton = Button(self.frameTop, text = "To English Names", font = "Ariel 20", command = self.toEng)
        self.engButton.grid(row = 0, column = 1)

        self.vikButton = Button(self.frameTop, text = "To Viking Names", font = "Ariel 20", command = self.toViking)
        self.vikButton.grid(row = 0, column = 2)

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
    
        self.convButton = Button(self.frameBottom, text = "Convert to Viking Calendar", 
            font = "Ariel 50", command = self.VCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.isStupid = True

        self.isViking = True

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 45", justify = LEFT)
        self.cOutput.grid(row = 5, column = 0)

        # self.cOutputII = Label(self.frameBottom, text = "", 
        #     font = "Ariel 45", justify = LEFT)
        # self.cOutputII.grid(row = 6, column = 0)
        
        # self.cOutputIII = Label(self.frameBottom, text = "", 
        #     font = "Ariel 45", justify = LEFT)
        # self.cOutputIII.grid(row = 7, column = 0)
        
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
    
    #29   +   30   +   29   +   30   +   29   +   30   +   29   +   30   +   29   +   30   +   29   +   30 = 354 13th month should be 30 days
    #The years 3, 6, 8, 11, 14, 17, and 19 are the long (13-month) years of the Metonic cycle.

    def toEng(self):
        self.isViking = False
        self.VCalCalc()

    def toViking(self):
        self.isViking = True
        self.VCalCalc()

    def VCalCalc(self):
        date = self.cal_calc()
        self.cOutput["text"] = date

    # def cal_calc(self):
    #     metricDate = self.metric_calc()
    #     baseMetric = self.print_metric_meme(793, 4, 14, 0, 0)
    #     elapsedMetric = int(metricDate * 1000) - int(baseMetric * 1000)
    #     metonicDayCount = 6939
    #     yearsElapsedFromBase = (elapsedMetric // metonicDayCount) * 19
    #     otherYearsElapsedFromBase = 0
    #     currentMetatonicDayNumber = elapsedMetric % metonicDayCount
    #     # if yearsElapsedFromBase < 0:
    #     #     yearsElapsedFromBase += 19
    #     while currentMetatonicDayNumber >= 384:
    #         if self.isMetatonicLeapYear(otherYearsElapsedFromBase):
    #             currentMetatonicDayNumber -= 384
    #         else:
    #             currentMetatonicDayNumber -= 354
    #         otherYearsElapsedFromBase += 1
    #     self.vikingYear = yearsElapsedFromBase + otherYearsElapsedFromBase
    #     currentDayOfYear = currentMetatonicDayNumber
    #     isLeap = self.isMetatonicLeapYear(otherYearsElapsedFromBase)
    #     dateString = self.dateDeterminer(currentDayOfYear, isLeap)
    #     fullDateString = dateString + ", " + str(self.vikingYear) + " Viking Age"
    #     return fullDateString

    # def dateDeterminer(self, dayNum, leap):
    #     if 0 <= dayNum < 29:
    #         month = "HARPA"
    #         day = dayNum
    #     if 29 <= dayNum < 59:
    #         month = "SKERPLA"
    #         day = dayNum - 29
    #     if 59 <= dayNum < 88:
    #         month = "SÓLMÁNUÐUR"
    #         day = dayNum - 59
    #     if 88 <= dayNum < 118:
    #         month = "Heyannir"
    #         day = dayNum - 88
    #     if 118 <= dayNum < 147:
    #         month = "TVÍMÁNUÐUR"
    #         day = dayNum - 118
    #     if 147 <= dayNum < 177:
    #         month = "HAUSTMÁNUÐUR"
    #         day = dayNum - 147
    #     if 177 <= dayNum < 206:
    #         month = "GORMÁNUÐUR"
    #         day = dayNum - 177
    #     if 206 <= dayNum < 236:
    #         month = "ÝLIR"
    #         day = dayNum - 206
    #     if 236 <= dayNum < 265:
    #         month = "MÖRSUGUR"
    #         day = dayNum - 236
    #     if 265 <= dayNum < 295:
    #         month = "ÞORRI"
    #         day = dayNum - 265
    #     if 295 <= dayNum < 324:
    #         month = "GÓI"
    #         day = dayNum - 295
    #     if 324 <= dayNum < 354:
    #         month = "EINMÁNUÐUR"
    #         day = dayNum - 324
    #     if dayNum >= 354 and leap == False:
    #         self.vikingYear += 1
    #         day = dayNum - 354
    #         month = "HARPA"
    #     if (384 > dayNum >= 354) and leap:
    #         month = "Silðimánuður"
    #         day = dayNum - 354
    #     monthChar = month[0]
    #     otherMonthChars = month[1:]
    #     otherMonthChars = otherMonthChars.lower()
    #     monthII = monthChar + otherMonthChars
    #     if 355 > dayNum >= 178:
    #         season = "Vetur"
    #     else:
    #         season = "Sumar"
    #     dateString = str(day + 1) + " " + monthII + " " + season
    #     return dateString

    # def isMetatonicLeapYear(self, year):
    #     if year == 2 or year == 5 or year == 7 or year == 10 or year == 13 or year == 16 or year == 18:
    #         return True
    #     else:
    #         return False
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
        baseDayNum = 3942165
        currentDayNum = self.metric_calc()
        currentDayNum = math.trunc(currentDayNum * 1000)
        dayDelta = currentDayNum - baseDayNum
        #27759 in four cycle
        monthsElapsed = 0
        baseCycleCount = 0
        # cyclesElapsedTotal = (dayDelta // 27759) * 4 + baseCycleCount
        # remainingCycleDays = dayDelta % 27759
        # while remainingCycleDays > 6939:
        #     shortCycle = self.isShortCycle(cyclesElapsedTotal)
        #     if shortCycle:
        #         sub = 6939
        #     else:
        #         sub = 6940
        #     remainingCycleDays -= sub
        #     cyclesElapsedTotal += 1
        # isShort = self.isShortCycle(cyclesElapsedTotal)
        # print(isShort)
        # dayNumArr = [6940, 6939]
        # dayNumOfCycle = (dayDelta % dayNumArr[isShort])
        #daySub = 0#isShort
        cyclesElapsedTotal = (dayDelta // 6940) + baseCycleCount
        dayNumOfCycle = (dayDelta % 6940)
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
            monthArrII = [29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29]
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
        week = self.week_fdn()
        season = self.seasonFinder(currentMonth)
        date = week + ", " + str(day) + " " + nameOfMonth + " (" + str(season) + "), " + str(year + 1)
        return date
    
    def seasonFinder(self, month):
        if 1 <= month < 7:
            if self.isViking:
                season = "Sumar"
            else:
                season = "Summer"
        else:
            if self.isViking:
                season = "Vetur"
            else:
                season = "Winter"
        return season

    def week_fdn(self):
        subtract = 0
        year = int(self.yearE.get())
        month = int(self.monthE.get())
        day = int(self.dayE.get())
        leap = self.isLeapYear(year)
        if leap and month < 3:
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
            if self.isViking:
                wk = "Sunnudagr"
            else:
                wk = "Sun Day"
        if net == 1:
            if self.isViking:
                wk = "Mánadagr"
            else:
                wk = "Moon Day"
        if net == 2:
            if self.isViking:
                wk = "Týsdagr"
            else:
                wk = "Tyr's Day"
        if net == 3:
            if self.isViking:
                wk = "Óðinsdagr"
            else:
                wk = "Odin's Day"
        if net == 4:
            if self.isViking:
                wk = "Þórsdagr"
            else:
                wk = "Thor's Day"
        if net == 5:
            if self.isViking:
                wk = "Frjádagr"
            else:
                wk = "Freya's Day"
        if net == 6:
            if self.isViking:
                wk = "Laugardagr"
            else:
                wk = "Bath Day"
        return wk

    def monthName(self, monthNum):
        if monthNum == 1:
            if self.isViking:
                name = "HARPA"
            else:
                name = "Harpa"
        elif monthNum == 2:
            if self.isViking:
                name = "SKERPLA"
            else:
                name = "Skerpla"
        elif monthNum == 3:
            if self.isViking:
                name = "SÓLMÁNUÐUR"
            else:
                name = "Sun's Month"
        elif monthNum == 4:
            if self.isViking:
                name = "Heyannir"
            else:
                name = "Haymaking"
        elif monthNum == 5:
            if self.isViking:
                name = "Kornskurðarmánuður"
            else:
                name = "Corn Cutting"
        elif monthNum == 6:
            if self.isViking:
                name = "HAUSTMÁNUÐUR"
            else:
                name = "Autumn"
        elif monthNum == 7:
            if self.isViking:
                name = "GORMÁNUÐUR"
            else:
                name = "Slaughter"
        elif monthNum == 8:
            if self.isViking:
                name = "ÝLIR"
            else:
                name = "Yule"
        elif monthNum == 9:
            if self.isViking:
                name = "MÖRSUGUR"
            else:
                name = "Bone Marrow"
        elif monthNum == 10:
            if self.isViking:
                name = "ÞORRI"
            else:
                name = "Black Frost"
        elif monthNum == 11:
            if self.isViking:
                name = "GÓI"
            else:
                name = "Thorri Daughter"
        elif monthNum == 12:
            if self.isViking:
                name = "EINMÁNUÐUR"
            else:
                name = "One-Month"
        else:
            if self.isViking:
                name = "Silðimánuður"
            else:
                name = "Late Month"
        if self.isViking:
            nameFirst = name[0].upper()
            nameOther = name[1:].lower()
            name = nameFirst + nameOther
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
    root.title("Viking Calendar Calculator")
    calCalc = VikingCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
