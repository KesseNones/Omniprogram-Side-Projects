import random
from time import sleep
import time
import datetime
from tkinter import *
import tkinter as tk
import math
from tkinter import messagebox

class SeasonTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "white", highlightbackground = "black", highlightthickness = 2)
        self.draw.grid(row = 0, column = 0)

        self.createSeasonSegments()
        self.createSeasonSymbols()
        self.outerCircle = self.draw.create_oval(5, 5, 795, 795, width = 6, outline = "black")
        self.moonMade = False
        self.seasonArrowDrawn = False
        self.drawSeasonArrow()
        self.createMoon()

        self.timeUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def createMoon(self):
        if self.moonMade:
            self.moonPhase = self.draw.delete(self.moonPhase)
            self.moonMade = False
        moon = self.moonCalc()
        x = 400
        y = 400
        self.moonPhaseBack = self.draw.create_oval(370, 370, 430, 430, fill = "white")
        self.moonPhase = self.draw.create_text(x, y, text = moon, font  = "Times 50", fill = "black")
        self.moonMade = True
        
    def moonCalc(self):
        #🌑🌒🌓🌔🌕🌖🌗🌘
        moonPhase = ""
        metricDate = self.metric_time()
        moonBase = 4390.562679166
        metricDiff = metricDate - moonBase
        moonAge = (metricDiff * 1000) % 29.530588
        if moonAge < 0:
            moonAge += 29.530588
        if 0.0 <= moonAge < 3.6913235:
            moonPhase = "🌑"
        if 3.6913235 <= moonAge < 7.382647:
            moonPhase = "🌒"
        if 7.382647 <= moonAge < 11.0739705:
            moonPhase = "🌓"
        if 11.0739705 <= moonAge < 14.765294:
            moonPhase = "🌔"
        if 14.765294 <= moonAge < 18.4566175:
            moonPhase = "🌕"
        if 18.4566175 <= moonAge < 22.147941:
            moonPhase = "🌖"
        if 22.147941 <= moonAge < 25.8392645:
            moonPhase = "🌗"
        if 25.8392645 <= moonAge < 29.530588:
            moonPhase = "🌘"
        return moonPhase

    def metric_time(self):
        t = time.time()
        metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
        rounderI = metric_time * 1000000000
        rounderII = math.trunc(rounderI)
        rounderIII = rounderII / 1000000000
        return rounderIII

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
    
    def localUnix(self):
        t = time.time()
        t = int(t)
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = ((t % 86400) // 3600)
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        t = (t - (3600 * timeZoneDiff))
        return t

    def timeUpdate(self):
        unix = self.localUnix()
        if unix % 86400 == 0:
            self.drawSeasonArrow()
            self.createMoon()
        self.window.after(1000, self.timeUpdate)

    def drawSeasonArrow(self):
        if self.seasonArrowDrawn:
            self.seasonArrow = self.draw.delete(self.seasonArrow)
            self.seasonArrowDrawn = False
        seasonPosition = self.findSeasonPos()
        seasonArmHyp = 350
        x = 400
        y = 400
        x2 = 400 + seasonArmHyp * math.cos(math.radians(seasonPosition - 90))
        y2 = 400 + seasonArmHyp * math.sin(math.radians(seasonPosition - 90))
        self.seasonArrow = self.draw.create_line(400, 400, x2, y2, width = 10, fill = "grey", arrow = tk.LAST, arrowshape = (10, 15, 10))
        
        self.seasonArrowDrawn = True

    def findSeasonPos(self):
        yearDayNum = self.calCalcI()
        if self.isLeap:
            div = 366
        else:
            div = 365
        yearDec = yearDayNum / div
        degOfYear = yearDec * 360
        return degOfYear

    def calCalcI(self):
        yearB = 2001
        monthB = 3
        dayB = 19
        local = datetime.datetime.now()
        yearC = local.year
        monthC = local.month
        dayC = local.day - 1
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
        self.year = yearC
        self.isLeap = self.isLeapYear(yearC)
        print(Age_day)
        return Age_day

    def createSeasonSegments(self):
        seasonHyp = 395
        deg = 0
        while deg < 91.726:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "green")
            deg += 1
        while deg < 183.452:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "yellow")
            deg += 1
        while deg < 272.219:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "orange")
            deg += 1
        while deg < 361:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "blue")
            deg += 1
        
    def createSeasonSymbols(self):
        self.draw.create_text(250, 250, text = "❄", font  = "times 150", fill = "white")
        self.draw.create_text(560, 250, text = "🌸", font  = "times 130", fill = "pink")
        self.draw.create_text(550, 550, text = "🔥", font  = "times 130", fill = "black")
        self.draw.create_text(250, 550, text = "🍂", font  = "times 130", fill = "brown")

def main():
    root = Tk()
    root.title("Season Clock")
    metric = SeasonTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
