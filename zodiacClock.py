#Jesse A. Jones
#Version: 2022-11-23.4

import random
import time
import datetime
from tkinter import *
import math
import tkinter as tk
import metricTime

#This class is part of a program to display the current 
#   position in the commonly used Western Astrological system.
#I don't personally believe in this kind of stuff, 
#   I just made it because it's another time system I pay attention to for fun.
class Zodiac(object):
    #Makes all function calls to set up the initial astrological clock display.
    def __init__(self, window = None):
        self.window = window

        #Top frame contains quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Sets up frame bottom with appropriate background.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "white", highlightbackground = "black", highlightthickness = 2)
        self.draw.grid(row = 0, column = 0)

        self.backGroundColor = "white"
        #Hex code correlates to purple.
        self.outerCircle = self.draw.create_oval(5, 5, 795, 795, width = 6, fill = "#9d45b0")
        self.createSignSeperators()
        #Hex code correlates to very dark purple.
        self.innerCircle = self.draw.create_oval(85, 85, 715, 715, width = 6, fill = "#190020")
        self.createStars()
        self.createAstroSymbols()
        
        self.seasonArrowDrawn = False
        self.drawSeasonArrow()

        self.moonMade = False
        self.createMoon()

        self.timeUpdate()

    #Makes stars behind clock hand and moon phase.
    def createStars(self):
        #Hypotenuse length.
        hype = 310

        #Randomly makes stars in increasingly large circles, 
        #   filling up the background with a random set of stars.
        while hype > 0:
            starSize = random.choice(range(1, 4))
            starPos = random.choice(range(0, 360))
            x = 400 + hype * math.cos(math.radians(starPos - 90))
            y = 400 + hype * math.sin(math.radians(starPos - 90))
            self.draw.create_oval(x, y, x + starSize, y + starSize, width = 0, fill = "white")
            hype -= 2
            
    #Quits the program when quit button pressed.
    def quitButtonAction(self):
        self.window.destroy()
    
    #Draws background for moon phase and prints moon phase emoji based 
    #   on calculated moon phase. This was implemented 
    #   in Windows 10 originally. Running it in another OS might 
    #   either not work or have a moon phase with an off alignment background.
    def createMoon(self):
        #Delete old moon phase if moon already drawn before.
        if self.moonMade:
            self.moonPhase = self.draw.delete(self.moonPhase)
            self.moonMade = False

        #Gives moon phase character based on calculated moon phase. 
        moon = self.moonCalc()
        x = 400
        y = 400
        self.moonPhaseBack = self.draw.create_oval(370, 370, 430, 430, fill = "white")
        self.moonPhase = self.draw.create_text(x, y, text = moon, font  = "Times 50", fill = "black")
        self.moonMade = True
        
    #Calculates moon phase character to use based on metric date.
    def moonCalc(self):
        #🌑🌒🌓🌔🌕🌖🌗🌘 <- Moon phase emoji's used.
        moonPhase = ""
       
        #Gets current metric date and determines current moon 
        #   age decimal day from the offset from the base metric date.
        metric = metricTime.MetricTime()
        metricDate = metric.metric_time()
        moonBase = 4390.562679166
        metricDiff = metricDate - moonBase
        moonAge = (metricDiff * 1000) % 29.530588
        
        #Conditional chain used to determine current 
        #   moon phase character based on calculated moonAge.
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

    #Generates all twelve astrological symbols 
    #   used throughout the year in order, starting with Aries.
    def createAstroSymbols(self):
        degreeOffshift = 75
        x = 400 + 350 * math.cos(math.radians(0 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(0 - degreeOffshift))
        self.aries = self.draw.create_text(x, y, text = "♈", font  = "times 40", fill = "black")
        x = 400 + 350 * math.cos(math.radians(30 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(30 - degreeOffshift))
        self.taurus = self.draw.create_text(x, y, text = "♉", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(60 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(60 - degreeOffshift))
        self.gemini = self.draw.create_text(x, y, text = "♊", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(90 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(90 - degreeOffshift))
        self.cancer = self.draw.create_text(x, y, text = "♋", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(120 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(120 - degreeOffshift))
        self.leo = self.draw.create_text(x, y, text = "♌", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(150 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(150 - degreeOffshift))
        self.virgo = self.draw.create_text(x, y, text = "♍", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(180 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(180 - degreeOffshift))
        self.libra = self.draw.create_text(x, y, text = "♎", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(210 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(210 - degreeOffshift))
        self.scorpio = self.draw.create_text(x, y, text = "♏", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(240 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(240 - degreeOffshift))
        self.saggitarius = self.draw.create_text(x, y, text = "♐", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(270 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(270 - degreeOffshift))
        self.capricorn = self.draw.create_text(x, y, text = "♑", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(300 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(300 - degreeOffshift))
        self.aquarius = self.draw.create_text(x, y, text = "♒", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(330 - degreeOffshift))
        y = 400 + 350 * math.sin(math.radians(330 - degreeOffshift))
        self.pisces = self.draw.create_text(x, y, text = "♓", font  = "times 40")
        self.elementColors()

    #Sets each astrological symbol to its respective element color: 
    #   red for fire, green for earth, yellow for air, and blue for water.
    def elementColors(self):
        #Array of all twelve zodiac symbols.
        zodArr = [self.aries, self.taurus, self.gemini, self.cancer, self.leo, 
            self.virgo, self.libra, self.scorpio, self.saggitarius, 
            self.capricorn, self.aquarius, self.pisces]
        index = 0
        elementColorArr = ["red", "green", "#fff884", "blue"]
        
        #Colors each group of four signs in a specific color 
        #   order using modulo to discern which color goes where.
        for el in zodArr:
            elementColorArrIndex = index % 4
            self.draw.itemconfig(el, fill = elementColorArr[elementColorArrIndex])
            index += 1
        
    #Creates the lines seperating each sign segment of the clock.
    def createSignSeperators(self):
        delta = 0
        self.crazyArr = []
        while delta < 360:
            x = 400
            y = 400
            x2 = 400 + 395 * math.cos(math.radians(delta - 90))
            y2 = 400 + 395 * math.sin(math.radians(delta - 90))
            if delta % 30 == 1:
                self.draw.create_line(x, y, x2, y2, fill = "", width = 0)
            else:
                self.crazyArr.append(self.draw.create_line(x, y, x2, y2, fill = "black", width = 5))
            delta += 30

    #Detects if an input year is a leap year or not.
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
    
    #Gets a timezone shifted unix timestamp.
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

    #Updates the clock if midnight is hit.
    def timeUpdate(self):
        unix = self.localUnix()
        if unix % 86400 == 0:
            self.drawSeasonArrow()
            self.createMoon()
        self.window.after(1000, self.timeUpdate)

    #Creates arrow that indicates position in zodiac cycle.
    def drawSeasonArrow(self):
        #Deletes old arrow if one exists.
        if self.seasonArrowDrawn:
            self.seasonArrow = self.draw.delete(self.seasonArrow)
            self.seasonArrowDrawn = False

        #Calculates position in year and draws arrow appropriately.
        seasonPosition = self.findSeasonPos()
        seasonArmHyp = 350
        x = 400
        y = 400
        x2 = 400 + seasonArmHyp * math.cos(math.radians(seasonPosition - 90))
        y2 = 400 + seasonArmHyp * math.sin(math.radians(seasonPosition - 90))
        self.seasonArrow = self.draw.create_line(400, 400, x2, y2, width = 10, 
            fill = "grey", arrow = tk.LAST, arrowshape = (10, 15, 10))
        
        self.seasonArrowDrawn = True

    #Determines current degree number for the arrow to be on.
    def findSeasonPos(self):
        yearDayNum = self.calCalcI()
        if self.isLeap:
            div = 366
        else:
            div = 365
        yearDec = yearDayNum / div
        degOfYear = yearDec * 360
        return degOfYear

    #Calculates what day number to be on in the seasonal year cycle.
    def calCalcI(self):
        #Base date.
        yearB = 2001
        monthB = 3
        dayB = 19

        #Present date.
        local = datetime.datetime.now()
        yearC = local.year
        monthC = local.month
        dayC = local.day - 1

        leap_year = self.isLeapYear(yearB)
        leap_year = self.isLeapYear(yearC)
        
        #Giant block of ifs determine day number.
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

        #Calculates days elapsed in cycle.
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

        self.isLeap = self.isLeapYear(yearC)
        return Age_day

def main():
    root = Tk()
    root.title("Astrological Zodiac Clock")
    metric = Zodiac(root)
    root.mainloop()

if __name__ == "__main__":
    main()
