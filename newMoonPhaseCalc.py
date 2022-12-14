from tkinter import *
import math
import time
import datetime

class moonCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 75", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.year = Entry(self.frameBottom, font = "Times 69")
        self.year.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 75", anchor = "w")
        self.messageII.grid(row = 2, column = 0)

        self.month = Entry(self.frameBottom, font = "Times 69")
        self.month.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 75", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)

        self.day = Entry(self.frameBottom, font = "Times 69")
        self.day.grid(row = 3, column = 1)

        self.messageIV = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 75", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)

        self.hour = Entry(self.frameBottom, font = "Times 69")
        self.hour.grid(row = 4, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 75", anchor = "w")
        self.messageV.grid(row = 5, column = 0)

        self.minute = Entry(self.frameBottom, font = "Times 69")
        self.minute.grid(row = 5, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Calculate Moon Phase", 
            font = "Ariel 60", command = self.moonCalc)
        self.convButton.grid(row = 6, column = 0)

        self.mOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 69")
        self.mOutput.grid(row = 6, column = 1)

        self.mOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 69")
        self.mOutputII.grid(row = 7, column = 1)

        self.isStupid = True

    def quitButtonAction(self):
        self.window.destroy()
    def moonCalc(self):
        moonPhase = ""
        metricDateCalc = self.metric_calc()
        moonBase = 4390.562679166
        metricDiff = metricDateCalc - moonBase
        moonAge = (metricDiff * 1000) % 29.530588
        if moonAge < 0:
            moonAge += 29.530588
        moonAgeII = round(moonAge, 6)
        moonAgeII = format(moonAgeII, ".6f")
        self.mOutput["text"] = moonAgeII
        if 0.0 <= moonAge < 3.6913235:
            moonPhase = "New Moon ????"
        if 3.6913235 <= moonAge < 7.382647:
            moonPhase = "Waxing Crescent ????"
        if 7.382647 <= moonAge < 11.0739705:
            moonPhase = "First Quarter ????"
        if 11.0739705 <= moonAge < 14.765294:
            moonPhase = "Waxing Gibbous ????"
        if 14.765294 <= moonAge < 18.4566175:
            moonPhase = "Full Moon ????"
        if 18.4566175 <= moonAge < 22.147941:
            moonPhase = "Waning Gibbous ????"
        if 22.147941 <= moonAge < 25.8392645:
            moonPhase = "Third Quarter ????"
        if 25.8392645 <= moonAge < 29.530588:
            moonPhase = "Waning Crescent ????"
        self.mOutputII["text"] = moonPhase
        
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

    def metric_calc(self):
        if self.isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000
        year = int(self.year.get())
        month = int(self.month.get())
        day = int(self.day.get())
        hour = int(self.hour.get())
        minute = int(self.minute.get())
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
    root.title("Moon Phase Calculator")
    moon = moonCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
