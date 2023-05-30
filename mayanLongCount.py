#Jesse A. Jones
#Version: 2023-05-30.91

from tkinter import *
import math
import time
import datetime
import leapDetect
import dateHandling

#This class takes in an input date 
#   and displays the resulting mayan long count, tzolkin, and haab.
class MayanCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Used in metric date calculations.
        self.isStupid = True

        #Holds date input fields, conversion button, and converted output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.yearE = Entry(self.frameBottom, font = "Ariel 20")
        self.yearE.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.monthE = Entry(self.frameBottom, font = "Ariel 20")
        self.monthE.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)
        self.dayE = Entry(self.frameBottom, font = "Ariel 20")
        self.dayE.grid(row = 3, column = 1)
    
        #Converts input date to mayan calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Mayan Calendar", 
            font = "Ariel 20", command = self.MCalCalc)
        self.convButton.grid(row = 4, column = 0)

        #Outputs the Mayan long count date.
        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutput.grid(row = 4, column = 1)

        #Outputs the Mayan Tzolkin, Haab, and Lord of the Night.
        self.cOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutputII.grid(row = 5, column = 1)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls function to convert input date 
    #   to mayan calendar and displays result.
    def MCalCalc(self):
        date = self.cal_calc()
        self.cOutput["text"] = date
        self.cOutputII["text"] = self.otherDateString

    #Pefroms the calculations and function 
    #   calls necessary to calculate mayan calendar.
    def cal_calc(self):
        #Fetches date input.
        dateGet = dateHandling.GetDate()
        year = dateGet.getYear(self.yearE.get())
        month = dateGet.getMonth(self.monthE.get())
        day = dateGet.getDay(self.dayE.get())
        
        #Calculates current day of mayan calendar in terms of raw day count.
        dayBase = 2515647
        currentDay = self.metric_calc(year, month, day)
        currentDay = math.floor(currentDay * 1000)
        dayDelta = currentDay - dayBase

        #The day delta is used to calculate 
        #   the mayan long count and tzolkin and haab. 
        #   Setting and returning the appropriate variables.
        dateString = self.toMayan(dayDelta)
        self.otherDateString = self.toTzolkinAndHaab(dayDelta)
        return dateString

    #Takes in day delta and calculates Tzolkin and Haab.
    def toTzolkinAndHaab(self, dayDelta):
        #8 Cumku haab base
        
        #God names used in Tzolkin.
        tzolGods = ["Imix", "Ik", "Akbal", "Kan", "Chicchan", "Cimi", "Manik", "Lamat", "Muluc", "Oc", "Chuen", "Eb", "Ben", "Ix", "Men", "Cib", "Caban", "Etznab", "Cauac", "Ahau"]
        
        #Month names of Haab.
        haabMonths = ["Pop", "Uo", "Zip", "Zotz", "Tzec", "Xul", "Yaxkin", "Mol", "Chen", "Yax", "Zac", "Ceh", "Mac", "Kankin", "Muan", "Pax", "Kayab", "Cumku", "Uayeb"]
        
        #Range of days in tzolkin.
        tzolDays = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        
        #The range of numbers who are lords of the night.
        lordOfNightArr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        #Base index for each Tzolkin.
        tzolDayIndex = 3
        tzolGodIndex = 19
        
        #Calculates current Tzolkin day.
        currentTzolDay = dayDelta % 260
        #Tzolkin base case.
        if currentTzolDay == 0:
            tzolDay = 4
            tzolGod = "Ahau"

        #Advances time until current Tzolkin is found.
        while currentTzolDay > 0:
            tzolDayIndex += 1
            tzolGodIndex += 1
            #Resets indexes.
            if tzolDayIndex > 12:
                tzolDayIndex %= 13
            if tzolGodIndex > 19:
                tzolGodIndex %= 20
            tzolDay = tzolDays[tzolDayIndex]
            tzolGod = tzolGods[tzolGodIndex]
            currentTzolDay -= 1

        #Calculates date in Haab.
        currentHaabDay = (dayDelta + 348) % 365
        haabMonthNum = currentHaabDay // 20
        haabDay = currentHaabDay % 20
        haabMonth = haabMonths[haabMonthNum]
        
        #Calculates lord of night and returns resulting time string.
        lordOfNightIndex = dayDelta % 9 - 1
        lordOfNightGod = lordOfNightArr[lordOfNightIndex]
        return str(tzolDay) + " " + tzolGod + ", " + str(haabDay) + " " + haabMonth + ", G" + str(lordOfNightGod)

    #Calculates the long count date based on the day delta.
    def toMayan(self, dayDelta):
        #Lengths of each mayan long count section in days.
        alauTunLength = 23040000000
        kinchilTunLength = 1152000000
        kalapTunLength = 57600000
        piktunLength = 2880000
        baktunLength = 144000
        katunLength = 7200
        tunLength = 360
        winalLength = 20
        kinLength = 1
        
        #Alautun calculated.
        alauTun = dayDelta // alauTunLength
        reducedDayDelta = dayDelta % alauTunLength
        
        #KinchilTun calculated.
        kinchilTun = reducedDayDelta // kinchilTunLength
        reducedDayDelta = reducedDayDelta % kinchilTunLength
        
        #Kalaptun calculated.
        kalapTun = reducedDayDelta // kalapTunLength
        reducedDayDelta = reducedDayDelta % kalapTunLength

        #Piktun calculated.
        piktun = reducedDayDelta // piktunLength
        reducedDayDelta = reducedDayDelta % piktunLength

        #Baktun calculated.
        baktun = (reducedDayDelta // baktunLength)
        reducedDayDelta = reducedDayDelta % baktunLength

        #Katun calculated.
        katun = reducedDayDelta // katunLength
        reducedDayDelta %= katunLength

        #Tun calculated.
        tun = reducedDayDelta // tunLength
        reducedDayDelta %= tunLength

        #Winal calculated.
        winal = reducedDayDelta // winalLength
        reducedDayDelta %= winalLength
        
        #Kin is days leftover.
        kin = reducedDayDelta

        #Builds longcount time string and returns it.
        dateString = str(alauTun) + "." + str(kinchilTun) + "." + str(kalapTun) + "." + str(piktun) + "." + str(baktun) + "." + str(katun) + "." + str(tun) + "." + str(winal) + "." + str(kin)
        return dateString


    #Calculates metric date based on year, dayNu, and time.
    def metricCalcII(self, year, dayNum, hour, minute):
        leapQuery = leapDetect.IsLeap()
        year += 10000
        fourCenturyCount = year // 400
        remainingYears = year % 400
        totalDays = fourCenturyCount * 146097
        while remainingYears > 0:
            leap = leapQuery.isLeapYear(remainingYears)
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

    #Calcualtes metric date using time or metricCalcII
    def metric_calc(self, year, month, day):
        if self.isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000
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
        leap = leapDetect.IsLeap()
        leap_year = leap.isLeapYear(year)
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
    root.title("Mayan Long Count Calendar Calculator")
    calCalc = MayanCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
