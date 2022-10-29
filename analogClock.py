import random
from time import sleep
import time
import datetime
from tkinter import *
import math
from tkinter import messagebox
import tkinter as tk

class AnalogTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        # self.descButton = Button(self.frameTop, text = "Description",
        #     font = "Ariel 20", command = self.showDescription)
        # self.descButton.grid(row = 0, column = 1)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        # self.message = Label(self.frameBottom, text = "test", font = "Times 100", anchor = "w")
        # self.message.pack(side = TOP)

        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "white", highlightbackground = "black", highlightthickness = 2)
        #self.mouseInput = self.draw.bind("<Button-1>", self.mouse)
        self.draw.grid(row = 0, column = 0)

        self.backGroundColor = "white"
        self.createMinDashes()
        self.outerCircle = self.draw.create_oval(5, 5, 795, 795, width = 6)
        self.dateCreated = False
        self.createDate()
        self.moonMade = False
        self.createMoon()
        self.createHourNums()
        self.createWeekDays()
        
        self.lineDrawn = False
        self.lineDrawnII = False
        self.lineDrawnIII = False
        self.lineDrawnIV = False
        self.drawWeek()

        self.isPhaseII = False
        self.isLightLetters = False
        self.centerOvalColor = "black"
        self.initialCharColor()
        self.charColorHasNotRunOnce = True

        self.timeUpdate()

    # def mouse(self, event):
    #     print(event.x, event.y)

    # def showDescription(self):
    #     messagebox.showinfo("E", 
    #     "E")

    def initialCharColor(self):
        unix = self.localUnix()
        daySec = unix % 86400
        if 64800 < daySec or daySec < 21600:
            self.charColor("white")
            self.isLightLetters = True
            self.centerOvalColor = "white"
            self.draw.itemconfig(self.dayOfMonth, fill = "white")
        else:
            self.charColor("black")
        self.isPhaseII = True

    def quitButtonAction(self):
        self.window.destroy()

    def createMoon(self):
        if self.moonMade:
            self.moonPhase = self.draw.delete(self.moonPhase)
            self.moonMade = False
        moon = self.moonCalc()
        x = 560
        y = 400
        self.moonPhaseBack = self.draw.create_oval(530, 370, 590, 430, fill = "white")
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

    def createDate(self):
        if self.dateCreated:
            self.dayOfMonth = self.draw.delete(self.dayOfMonth)
            self.dateCreated = False 
        dateToday = datetime.date.today()
        date = str(dateToday.day).zfill(2)
        x = 225
        y = 400
        self.dayOfMonth = self.draw.create_text(x, y, text = date, font  = "Times 50", fill = "black")
        self.dateCreated = True

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
        #self.draw.itemconfig(self.one, fill = "blue")
        #self.twelve["fill"] = "blue"
        
    def createMinDashes(self):
        delta = 0
        self.crazyArr = []
        while delta < 360:
            x = 400
            y = 400
            x2 = 400 + 395 * math.cos(math.radians(delta - 90))
            y2 = 400 + 395 * math.sin(math.radians(delta - 90))
            if delta % 30 == 0:
                self.draw.create_line(x, y, x2, y2, fill = "", width = 0)
            else:
                self.crazyArr.append(self.draw.create_line(x, y, x2, y2, fill = "black", width = 5))
            delta += 6
        self.coverOval = self.draw.create_oval(55, 55, 745, 745, fill = "white", width = 0)

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

    def week_fdn(self, year, month, day):
        subtract = 0
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
        return net

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
        t = time.time()
        t = int(t)
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = ((t % 86400) // 3600)
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        t = (t - (3600 * timeZoneDiff))
        secDeltaAngle = self.secDeltaFind(t)
        minDeltaAngle = self.minDeltaFind(t)
        hrDeltaAngle = self.hrDeltaFind(t)
        self.colorBackground(localHr)
        secDay = t % 86400
        if secDay == 0:
            self.createDate()
            self.createMoon()
            self.drawWeek()
            self.charColor("white")
        if secDay == 64800:
            self.charColor("white")
            self.isLightLetters = True
        if secDay == 21600:
            self.charColor("black")
            self.isLightLetters = False
        self.drawHour(hrDeltaAngle)
        self.drawMinute(minDeltaAngle)
        self.drawSecond(secDeltaAngle)
        self.colorBackground(localHr)
        if self.charColorHasNotRunOnce:
            if self.isLightLetters:
                self.charColor("white")
            else:
                self.charColor("black")
        self.window.after(100, self.timeUpdate)

    def colorBackground(self, hour):
        if 0 <= hour < 3:
            self.backGroundColor = "black"
        elif 3 <= hour < 6:
            self.backGroundColor = "#00857d"
        elif 6 <= hour < 9:
            self.backGroundColor = "#ffff3f"
        elif 9 <= hour < 12:
            self.backGroundColor = "#00ff9b"
        elif 12 <= hour < 15:
            self.backGroundColor = "#93ffd5"
        elif 15 <= hour < 18:
            self.backGroundColor = "#b6ff54"
        elif 18 <= hour < 21:
            self.backGroundColor = "#0e5efe"
        else:
            self.backGroundColor = "#03006a"
        self.draw["bg"] = self.backGroundColor
        self.draw.itemconfig(self.coverOval, fill = self.backGroundColor)  

    def charColor(self, color):
        self.draw.itemconfig(self.outerCircle, outline = color)
        self.draw.itemconfig(self.weekLine, fill = color)  
        if self.isPhaseII:
            self.draw.itemconfig(self.centerOval, fill = color, outline = color) #Fix this
            self.draw.itemconfig(self.dayOfMonth, fill = color)
            numberArr = [self.twelve, self.one, self.two, self.three, self.four, self.five, self.six, self.seven, self.eight, self.nine, self.ten, self.eleven]
            for el in numberArr:
                self.draw.itemconfig(el, fill = color)
            for i in self.crazyArr:
                self.draw.itemconfig(i, fill = color)
            for elem in self.weekNameArr:
                self.draw.itemconfig(elem, fill = color)
        self.charColorHasNotRunOnce = False 
        
    def secDeltaFind(self, unix):
        second = unix % 60
        return second * 6

    def minDeltaFind(self, unix):
        minute = unix % 3600
        minute /= 60
        return int(minute) * 6

    def hrDeltaFind(self, unix):
        hour = unix % 86400
        hour /= 3600
        return hour * 30

def main():
    root = Tk()
    root.title("Analog Clock")
    metric = AnalogTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
