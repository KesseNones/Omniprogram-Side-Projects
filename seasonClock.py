#Jesse A. Jones
#Version: 2023-06-08.93

import time
import datetime
from tkinter import *
import tkinter as tk
import math
import metricTime
import leapDetect

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

        #External classes used in finding current metric date 
        #   and detecting leap year respectively.
        self.metric = metricTime.MetricTime()
        self.leap = leapDetect.IsLeap()
        
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
        
    #Calculates moon phase based on metric date and displays results.
    def moonCalc(self):
        now = datetime.datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute

        #Finds current metric date and finds difference from base metric date.
        metricDateCalc = self.metric.metric_calc(year, month, day, hour, minute)
        moonBase = 4390.562679166
        metricDiff = metricDateCalc - moonBase
        
        #Metric delta used to find moon age.
        moonAge = (metricDiff * 1000) % 29.530588
        
        #Determines which moon phase the moon is currently in.
        if 0.0 <= moonAge < 3.6913235:
            moonPhase = "🌑"
        elif 3.6913235 <= moonAge < 7.382647:
            moonPhase = "🌒"
        elif 7.382647 <= moonAge < 11.0739705:
            moonPhase = "🌓"
        elif 11.0739705 <= moonAge < 14.765294:
            moonPhase = "🌔"
        elif 14.765294 <= moonAge < 18.4566175:
            moonPhase = "🌕"
        elif 18.4566175 <= moonAge < 22.147941:
            moonPhase = "🌖"
        elif 22.147941 <= moonAge < 25.8392645:
            moonPhase = "🌗"
        elif 25.8392645 <= moonAge < 29.530588:
            moonPhase = "🌘"
        else:
            moonPhase = "??"

        return moonPhase
    
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
        #Finds current date and uses it to calculate seasonal calendar day.
        now = datetime.datetime.now()
        yearDayNum = self.calcSeasonal(now.year, now.month, now.day)
        
        if self.leap.isLeapYear(now.year):
            div = 366
        else:
            div = 365
        yearDec = yearDayNum / div
        degOfYear = yearDec * 360
        return degOfYear

    #Given input year, month, and day, calculates seasonal calendar.
    def calcSeasonal(self, year, month, day):
        #Finds days elapsed in gregorian year and seasonal year.
        dayCount = self.metric.findDayNumOfYear(year, month, day) - 1
        seasonalDayCount = dayCount - 78

        #Accounts for if seasonal day count is negative.
        seasonalYear = year - (seasonalDayCount < 0)
        seasonalDayCount %= (365 + (self.leap.isLeapYear(year - 1)))

        return seasonalDayCount

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
