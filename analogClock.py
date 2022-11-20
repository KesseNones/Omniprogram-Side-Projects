#Jesse A. Jones
#Version: 2022-11-20.0

import time
import datetime
from tkinter import *
import math
import tkinter as tk
import metricTime
import leapDetect

#This class contains methods necessary to display 
#   an analog clock and all the information contained on it.
class AnalogTime(object):
    #Creates initial clock members and elements.
    def __init__(self, window = None):
        self.window = window

        #Top frame created containing quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Bottom frame created to hold all the other elements of the clock.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Canvas used to display clock itself.
        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "white", highlightbackground = "black", highlightthickness = 2)
        self.draw.grid(row = 0, column = 0)

        #Sets up a the clock circle, initial background, 
        #   and moon phase and date.
        self.backGroundColor = "white"
        self.createMinDashes()
        self.outerCircle = self.draw.create_oval(5, 5, 795, 795, width = 6)
        self.dateCreated = False
        self.createDate()
        self.moonMade = False
        self.createMoon()
        self.createHourNums()
        self.createWeekDays()
        
        #Draws weekday hand of clock as well as sets some booleans.
        self.lineDrawn = False
        self.lineDrawnII = False
        self.lineDrawnIII = False
        self.lineDrawnIV = False
        self.drawWeek()

        #Sets up initial character colors.
        self.isPhaseII = False
        self.isLightLetters = False
        self.centerOvalColor = "black"
        self.initialCharColor()
        self.charColorHasNotRunOnce = True

        #Activates clock loop.
        self.timeUpdate()

    #Determines wheather the text on the clock is white 
    #   or black based on the time and sets the text as such.
    def initialCharColor(self):
        unix = self.localUnix()
        daySec = unix % 86400

        #Sets character color to white if seconds of local unix is 
        #   in specified range where it is dark in most places.
        #   Characters set to black otherwise.
        if 64800 < daySec or daySec < 21600:
            self.charColor("white")
            self.isLightLetters = True
            self.centerOvalColor = "white"
            self.draw.itemconfig(self.dayOfMonth, fill = "white")
        else:
            self.charColor("black")
        self.isPhaseII = True

    #Quits program if quit button pressed.
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
        x = 560
        y = 400

        #Moon phase background circle drawn and moon phase printed on top.
        self.moonPhaseBack = self.draw.create_oval(530, 370, 590, 430, fill = "white")
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

    #Creates the day of month number date on the clock.
    def createDate(self):
        #If an old date is already there, delete it, 
        #   in order for it to be replaced.
        if self.dateCreated:
            self.dayOfMonth = self.draw.delete(self.dayOfMonth)
            self.dateCreated = False 

        #Creates date from resulting date found from datetime.
        dateToday = datetime.date.today()
        date = str(dateToday.day).zfill(2)
        x = 225
        y = 400
        self.dayOfMonth = self.draw.create_text(x, y, text = date, font  = "Times 50", fill = "black")
        self.dateCreated = True

    #Creates appropriately placed two letter weekday names 
    #   around the clock from the 12hr position to the 6hr position.
    def createWeekDays(self):
        pixelsFromCenter = 275
        x = 400 + pixelsFromCenter * math.cos(math.radians(0 - 90))
        y = 400 + pixelsFromCenter * math.sin(math.radians(0 - 90))
        self.sunday = self.draw.create_text(x, y, text = "Su", font  = "times 40", fill = "black")
        x = 400 + pixelsFromCenter * math.cos(math.radians(30 - 90))
        y = 400 + pixelsFromCenter * math.sin(math.radians(30 - 90))
        self.monday = self.draw.create_text(x, y, text = "Mo", font  = "times 40", fill = "black")
        x = 400 + pixelsFromCenter * math.cos(math.radians(60 - 90))
        y = 400 + pixelsFromCenter * math.sin(math.radians(60 - 90))
        self.tuesday = self.draw.create_text(x, y, text = "Tu", font  = "times 40", fill = "black")
        x = 400 + pixelsFromCenter * math.cos(math.radians(90 - 90))
        y = 400 + pixelsFromCenter * math.sin(math.radians(90 - 90))
        self.wednesday = self.draw.create_text(x, y, text = "We", font  = "times 40", fill = "black")
        x = 400 + pixelsFromCenter * math.cos(math.radians(120 - 90))
        y = 400 + pixelsFromCenter * math.sin(math.radians(120 - 90))
        self.thursday = self.draw.create_text(x, y, text = "Th", font  = "times 40", fill = "black")
        x = 400 + pixelsFromCenter * math.cos(math.radians(150 - 90))
        y = 400 + pixelsFromCenter * math.sin(math.radians(150 - 90))
        self.friday = self.draw.create_text(x, y, text = "Fr", font  = "times 40", fill = "black")
        x = 400 + pixelsFromCenter * math.cos(math.radians(180 - 90))
        y = 400 + pixelsFromCenter * math.sin(math.radians(180 - 90))
        self.saturday = self.draw.create_text(x, y, text = "Sa", font  = "times 40", fill = "black")
        self.weekNameArr = [self.sunday, self.monday, self.tuesday, self.wednesday, self.thursday, self.friday, self.saturday]

    #Creates roman numeral style hour hands seen from numbers I to XII.
    def createHourNums(self):
        x = 400 + 350 * math.cos(math.radians(0 - 90))
        y = 400 + 350 * math.sin(math.radians(0 - 90))
        self.twelve = self.draw.create_text(x, y, text = "XII", font  = "times 40", fill = "black")
        x = 400 + 350 * math.cos(math.radians(30 - 90))
        y = 400 + 350 * math.sin(math.radians(30 - 90))
        self.one = self.draw.create_text(x, y, text = "I", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(60 - 90))
        y = 400 + 350 * math.sin(math.radians(60 - 90))
        self.two = self.draw.create_text(x, y, text = "II", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(90 - 90))
        y = 400 + 350 * math.sin(math.radians(90 - 90))
        self.three = self.draw.create_text(x, y, text = "III", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(120 - 90))
        y = 400 + 350 * math.sin(math.radians(120 - 90))
        self.four = self.draw.create_text(x, y, text = "IIII", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(150 - 90))
        y = 400 + 350 * math.sin(math.radians(150 - 90))
        self.five = self.draw.create_text(x, y, text = "V", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(180 - 90))
        y = 400 + 350 * math.sin(math.radians(180 - 90))
        self.six = self.draw.create_text(x, y, text = "VI", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(210 - 90))
        y = 400 + 350 * math.sin(math.radians(210 - 90))
        self.seven = self.draw.create_text(x, y, text = "VII", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(240 - 90))
        y = 400 + 350 * math.sin(math.radians(240 - 90))
        self.eight = self.draw.create_text(x, y, text = "VIII", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(270 - 90))
        y = 400 + 350 * math.sin(math.radians(270 - 90))
        self.nine = self.draw.create_text(x, y, text = "IX", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(300 - 90))
        y = 400 + 350 * math.sin(math.radians(300 - 90))
        self.ten = self.draw.create_text(x, y, text = "X", font  = "times 40")
        x = 400 + 350 * math.cos(math.radians(330 - 90))
        y = 400 + 350 * math.sin(math.radians(330 - 90))
        self.eleven = self.draw.create_text(x, y, text = "XI", font  = "times 40")
        
    #Creates the dashes representing the minutes 
    #   between the five minute chunks of the clock.
    def createMinDashes(self):
        delta = 0
        self.minLineArr = []
        while delta < 360:
            x = 400
            y = 400
            x2 = 400 + 395 * math.cos(math.radians(delta - 90))
            y2 = 400 + 395 * math.sin(math.radians(delta - 90))
            if delta % 30 == 0:
                self.draw.create_line(x, y, x2, y2, fill = "", width = 0)
            else:
                self.minLineArr.append(self.draw.create_line(x, y, x2, y2, fill = "black", width = 5))
            delta += 6
        self.coverOval = self.draw.create_oval(55, 55, 745, 745, fill = "white", width = 0)

    #Draws the second hand of the clock 
    #   in the appropriate position based on the time.
    def drawSecond(self, delta):
        if self.lineDrawn:
            self.secLine = self.draw.delete(self.secLine)
            self.centerOval = self.draw.delete(self.centerOval)
            self.lineDrawn = False
        secHyp = 390
        x2 = 400 + secHyp * math.cos(math.radians(delta - 90))
        y2 = 400 + secHyp * math.sin(math.radians(delta - 90))
        self.secLine = self.draw.create_line(400, 400, x2, y2, width = 6, fill = "red")
        self.centerOval = self.draw.create_oval(390, 390, 410, 410, fill = self.centerOvalColor, outline = self.centerOvalColor)
        self.lineDrawn = True

    #Creates the minute hand of the clock 
    #   in its position based on the current time.
    def drawMinute(self, delta):
        if self.lineDrawnII:
            self.minLine = self.draw.delete(self.minLine)
            self.lineDrawnII = False
        minHyp = 350
        x2 = 400 + minHyp * math.cos(math.radians(delta - 90))
        y2 = 400 + minHyp * math.sin(math.radians(delta - 90))
        self.minLine = self.draw.create_line(400, 400, x2, y2, width = 6, fill = "black")
        if self.isLightLetters:
            self.draw.itemconfig(self.minLine, fill = "white")
        self.lineDrawnII = True

    #Draws hour hand of clock in position based on current time.
    def drawHour(self, delta):
        if self.lineDrawnIII:
            self.hourLine = self.draw.delete(self.hourLine)
            self.lineDrawnIII = False
        hrHyp = 300
        x2 = 400 + hrHyp * math.cos(math.radians(delta - 90))
        y2 = 400 + hrHyp * math.sin(math.radians(delta - 90))
        self.hourLine = self.draw.create_line(400, 400, x2, y2, width = 6, fill = "black")
        if self.isLightLetters:
            self.draw.itemconfig(self.hourLine, fill = "white")
        self.lineDrawnIII = True

    #Draws weekday hand in its appropriate spot.
    def drawWeek(self):
        dateToday = datetime.date.today()
        weekNum = self.week_fdn(dateToday.year, dateToday.month, dateToday.day)
        weekHandAngle = weekNum * 30
        if self.lineDrawnIV:
            self.weekLine = self.draw.delete(self.weekLine)
            self.lineDrawnIV = False
        wkHyp = 175
        x2 = 400 + wkHyp * math.cos(math.radians(weekHandAngle - 90))
        y2 = 400 + wkHyp * math.sin(math.radians(weekHandAngle - 90))
        self.weekLine = self.draw.create_line(400, 400, x2, y2, width = 15, fill = "black", arrow = tk.LAST, arrowshape = (8, 12, 8))
        self.lineDrawnIV = True

    #Finds day of week based on input date.
    def week_fdn(self, year, month, day):
        #Determines if leap year, and the consequences of that.
        subtract = 0
        leapFind = leapDetect.IsLeap()
        leap = leapFind.isLeapYear(year)
        if leap and month < 3:
            subtract = -1
        else:
            subtract = 0
        
        #Determines year code.
        y = year % 100
        yII = int(y / 4)
        yIII = yII + y
        yC = yIII % 7

        #Determines century code.
        if (year - y) % 400 == 0:
            cC = 6
        if ((year - y) - 100) % 400 == 0:
            cC = 4
        if ((year - y) - 200) % 400 == 0:
            cC = 2
        if ((year - y) - 300) % 400 == 0:
            cC = 0

        net = yC + cC

        #Determines month code.
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

        #Calculates week day based on all the codes.
        net = net + mC
        net = net + int(day)
        net = net + subtract
        net = net % 7
        return net

    #Takes unix time stamp and alters it based 
    #   on timezone of user running this application.
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
    
    #Central driving function called in init that updates the clock, 
    #   so it's actually a live clock and not a static image.
    def timeUpdate(self):
        #Fetches local unix timestamp and hour.
        t = self.localUnix()
        localHr = ((t % 86400) // 3600)

        secDeltaAngle = self.secDeltaFind(t)
        minDeltaAngle = self.minDeltaFind(t)
        hrDeltaAngle = self.hrDeltaFind(t)
        self.colorBackground(localHr)
        secDay = t % 86400

        #Remakes date, moon phase, weekday, and text color if midnight is hit.
        if secDay == 0:
            self.createDate()
            self.createMoon()
            self.drawWeek()
            self.charColor("white")

        #If time reaches evening portion of day, text color changes.
        if secDay == 64800:
            self.charColor("white")
            self.isLightLetters = True

        #Color of text changed to lighter color if morning chunk hit.
        if secDay == 21600:
            self.charColor("black")
            self.isLightLetters = False

        #Hour, minute, and second hands drawn based on calculated angle deltas.
        self.drawHour(hrDeltaAngle)
        self.drawMinute(minDeltaAngle)
        self.drawSecond(secDeltaAngle)
        self.colorBackground(localHr)

        #Handles recoloring of text case.
        if self.charColorHasNotRunOnce:
            if self.isLightLetters:
                self.charColor("white")
            else:
                self.charColor("black")

        #Recursive call occurs every 100 miliseconds 
        #   to redisplay the clock, making it appear live.
        self.window.after(100, self.timeUpdate)

    #Changes background color throughout the day based on given hour.
    def colorBackground(self, hour):
        if 0 <= hour < 3:
            self.backGroundColor = "black"
        elif 3 <= hour < 6:
            self.backGroundColor = "#00857d" #Dark turqoise
        elif 6 <= hour < 9:
            self.backGroundColor = "#ffff3f" #Yellow
        elif 9 <= hour < 12:
            self.backGroundColor = "#00ff9b" #Greenish torquoise
        elif 12 <= hour < 15:
            self.backGroundColor = "#93ffd5" #Light blue
        elif 15 <= hour < 18:
            self.backGroundColor = "#b6ff54" #Yellowish green
        elif 18 <= hour < 21:
            self.backGroundColor = "#0e5efe" #Dark blue
        else:
            self.backGroundColor = "#03006a" #Very dark blue
        self.draw["bg"] = self.backGroundColor
        self.draw.itemconfig(self.coverOval, fill = self.backGroundColor)  

    #Colors characters of clock based on input color. 
    #   Black and white are common ones given.
    def charColor(self, color):
        self.draw.itemconfig(self.outerCircle, outline = color)
        self.draw.itemconfig(self.weekLine, fill = color)  
        if self.isPhaseII:
            self.draw.itemconfig(self.centerOval, fill = color, outline = color) #Fix this
            self.draw.itemconfig(self.dayOfMonth, fill = color)
            numberArr = [self.twelve, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine, self.ten, self.eleven]
            for el in numberArr:
                self.draw.itemconfig(el, fill = color)
            for i in self.minLineArr:
                self.draw.itemconfig(i, fill = color)
            for elem in self.weekNameArr:
                self.draw.itemconfig(elem, fill = color)
        self.charColorHasNotRunOnce = False 
    
    #Finds second hand angle based on local unix time stamp.
    def secDeltaFind(self, unix):
        second = unix % 60
        return second * 6

    #Finds minute hand angle based on local unix time stamp.
    def minDeltaFind(self, unix):
        minute = unix % 3600
        minute /= 60
        return int(minute) * 6

    #Finds four hand angle based on unix time stamp.
    def hrDeltaFind(self, unix):
        hour = unix % 86400
        hour /= 3600
        return hour * 30

#Starts the mainloop of the analog clock.
def main():
    root = Tk()
    root.title("Analog Clock")
    metric = AnalogTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
