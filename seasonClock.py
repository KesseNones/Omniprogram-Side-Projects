#Jesse A. Jones
#Version: 2023-06-08.92

import time
import datetime
from tkinter import *
import tkinter as tk
import math

#This class displays a season clock based on the northern hemisphere seasons.
class SeasonTime(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds season clock display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays season clock.
        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "white", highlightbackground = "black", highlightthickness = 2)
        self.draw.grid(row = 0, column = 0)

        #Creates initial time display.
        self.createSeasonSegments()
        self.createSeasonSymbols()
        self.outerCircle = self.draw.create_oval(5, 5, 795, 795, width = 6, outline = "black")
        self.moonMade = False
        self.seasonArrowDrawn = False
        self.drawSeasonArrow()
        self.createMoon()

        #Starts recursive time loop to update season clock.
        self.timeUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Creates the moon phase at the center of the clock.
    def createMoon(self):
        #Deletes old moon phase text if it exists.
        if self.moonMade:
            self.moonPhase = self.draw.delete(self.moonPhase)
            self.moonMade = False

        #Finds moon phase and displays resulting phase.
        moon = self.moonCalc()
        x = 400
        y = 400
        self.moonPhaseBack = self.draw.create_oval(370, 370, 430, 430, fill = "white")
        self.moonPhase = self.draw.create_text(x, y, text = moon, font  = "Times 50", fill = "black")
        self.moonMade = True
        
    #Calculates moon phase based on current metric date.
    def moonCalc(self):
        #🌑🌒🌓🌔🌕🌖🌗🌘 Moon phase emojis used.
        moonPhase = ""
        
        #Finds time delta used for finding current day in lunar cycle.
        metricDate = self.metric_time()
        moonBase = 4390.562679166
        metricDiff = metricDate - moonBase
        
        #Determines moon age.
        moonAge = (metricDiff * 1000) % 29.530588
        if moonAge < 0:
            moonAge += 29.530588
        
        #Moon phase found via moon age and returned.
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

    #Returns the current metric time.
    def metric_time(self):
        t = time.time()
        metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
        rounderI = metric_time * 1000000000
        rounderII = math.trunc(rounderI)
        rounderIII = rounderII / 1000000000
        return rounderIII

    #Used in determining if current year is leap year.
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
    
    #Generates a local unix time stamp based on the local time zone.
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

    #If midnight in local time is hit, 
    #   season arrow is updated and moon phase is updated.
    def timeUpdate(self):
        unix = self.localUnix()
        if unix % 86400 == 0:
            self.drawSeasonArrow()
            self.createMoon()
        self.window.after(1000, self.timeUpdate)

    #Creates the arrow that indicates the position in the seasonal cycle.
    def drawSeasonArrow(self):
        #Deletes old season arrow if already drawn.
        if self.seasonArrowDrawn:
            self.seasonArrow = self.draw.delete(self.seasonArrow)
            self.seasonArrowDrawn = False

        #Determines position in seasonal cycle.
        seasonPosition = self.findSeasonPos()

        #Starting coordinates of seasonal arm.
        seasonArmHyp = 350
        x = 400
        y = 400
        
        #Trig performed to find new coordinates for season arm.
        x2 = 400 + seasonArmHyp * math.cos(math.radians(seasonPosition - 90))
        y2 = 400 + seasonArmHyp * math.sin(math.radians(seasonPosition - 90))
        
        #Creates seasonal arrow based on input coordinates.
        self.seasonArrow = self.draw.create_line(400, 400, x2, y2, width = 10, 
            fill = "grey", arrow = tk.LAST, arrowshape = (10, 15, 10))
        self.seasonArrowDrawn = True

    #Determines the seasonal position based 
    #   on current day in seasonal calendar.
    def findSeasonPos(self):
        yearDayNum = self.calCalcI()
        if self.isLeap:
            div = 366
        else:
            div = 365
        yearDec = yearDayNum / div
        degOfYear = yearDec * 360
        return degOfYear

    #Calculates day in seasonal calendar.                   THIS CODE IS DISGUSTING AND OUTDATED. REPLACE WITH BETTER UPDATED VERSION
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

    #Creates the colored seasonal segments seen on the clock.
    def createSeasonSegments(self):
        seasonHyp = 395
        deg = 0
        
        #Creates spring segment.
        while deg < 91.726:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "green")
            deg += 1
        
        #Creates summer segment.
        while deg < 183.452:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "yellow")
            deg += 1

        #Creates autumn segment.
        while deg < 272.219:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "orange")
            deg += 1
        
        #Creates winter segment.
        while deg < 361:
            x2 = 400 + seasonHyp * math.cos(math.radians(deg - 90))
            y2 = 400 + seasonHyp * math.sin(math.radians(deg - 90))
            self.draw.create_line(400, 400, x2, y2, width = 8.5, fill = "blue")
            deg += 1
        
    #Creates the season symbols in their appropriate spots.
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
