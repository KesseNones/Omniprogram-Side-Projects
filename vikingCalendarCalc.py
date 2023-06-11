#Jesse A. Jones
#Version: 2023-06-11.24

from tkinter import *
import time
import datetime
import metricTime 
import leapDetect
import dateHandling
import weekCalculator

#Takes in an input date and calculates the viking calendar date.
#   The translations and names are likely quite inaccurate 
#   because they're based on some quick googling.
class VikingCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button, english names button, and viking names button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Converts output calendar to english names.
        self.engButton = Button(self.frameTop, text = "To English Names", font = "Ariel 20", command = self.toEng)
        self.engButton.grid(row = 0, column = 1)

        #Converts output calendar to viking names.
        self.vikButton = Button(self.frameTop, text = "To Viking Names", font = "Ariel 20", command = self.toViking)
        self.vikButton.grid(row = 0, column = 2)

        #Holds time input fields.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        FONT = "Ariel 20"

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = FONT)
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = FONT)
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = FONT)
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = FONT)
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = FONT)
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = FONT)
        self.day.grid(row = 3, column = 1)
    
        #Converts to viking calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Viking Calendar", 
            font = FONT, command = self.VCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.isViking = True

        #Outputs viking calendar string.
        self.cOutput = Label(self.frameBottom, text = "", 
            font = FONT, justify = LEFT)
        self.cOutput.grid(row = 4, column = 1)

        #Used to parse input date, find day number of year, and find day of week.
        self.parse = dateHandling.GetDate()
        self.metric = metricTime.MetricTime()
        self.week = weekCalculator.WeekFinder()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()
    
    #Epik maths
    #29   +   30   +   29   +   30   +   29   +   30   +   29   +   30   +   29   +   30   +   29   +   30 = 354 13th month should be 30 days
    #The years 3, 6, 8, 11, 14, 17, and 19 are the long (13-month) years of the Metonic cycle.

    #Recalculates date with english names.
    def toEng(self):
        self.isViking = False
        self.VCalCalc()

    #Recalculates date with viking names.
    def toViking(self):
        self.isViking = True
        self.VCalCalc()

    #Calculates viking calendar and displays result.
    def VCalCalc(self):
        #Gets input date.
        year = self.parse.getYear(self.year.get())
        month = self.parse.getMonth(self.month.get())
        day = self.parse.getDay(self.day.get())

        self.cOutput["text"] = self.vikingCalCalc(year, month, day)

    #Calculates viking calendar.
    def vikingCalCalc(self, year, month, day):
        #Calculates metric time delta measured in days.
        baseDayNum = 3942165
        currentDayNum = self.metric.metric_calc(year, month, day, 0, 0)
        currentDayNum = int(currentDayNum * 1000)
        dayDelta = currentDayNum - baseDayNum

        #27759 in four cycle (useful????)
        monthsElapsed = 0
        baseCycleCount = 0
        
        #Finds total cycles elapsed, current day in cycle and current day 
        #   in 28 month cycle. Useful in doing the calendar stuff.
        cyclesElapsedTotal = (dayDelta // 6940) + baseCycleCount
        dayNumOfCycle = (dayDelta % 6940)
        currentDayOf28MonthCycle = dayNumOfCycle % 827 + 1
        monthsElapsed = (dayNumOfCycle // 827) * 28

        #"God, forgive me." -Tommy Wiseau
        #Gross yucky thing that determines the current day 
        #   in this gigantic cycle of years because yucky gross calendar math.
        if dayNumOfCycle < 6616:
            monthArr = [29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30, 30]
            
            #This gigantic block determines how many months 
            #   have elapsed and the current day in the cycle.
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
            #Smaller case for at the end of the cycle I think.
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

        #Builds the date string and returns it.
        currentMonth = monthsElapsed + 1
        dateString = str(cyclesElapsedTotal) + "-" + str(currentMonth) + "-" + str(currentDay)
        trueDateString = self.toLuniSolar(cyclesElapsedTotal, currentMonth, currentDay)
        return trueDateString
    
    #Finds precise date of viking calendar after cycles have been calculated.
    def toLuniSolar(self, cycles, month, day):
        year = cycles * 19
        monthCountArr = [12, 12, 13, 12, 12, 13, 12, 13, 12, 12, 13, 12, 12, 13, 12, 12, 13, 12, 13]
        
        #Determines how many years have elapsed in current metonic cycle.
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

        #Finds names and builds date string based on input.
        nameOfMonth = self.monthName(currentMonth)
        
        #Input to find the weekday here.
        inputYear = self.parse.getYear(self.year.get())
        inputMonth = self.parse.getMonth(self.month.get())
        inputDay = self.parse.getDay(self.day.get())

        #Finds week day and sets up dictionary 
        #   to translate weekday into viking version.
        week = self.week.weekFind(inputYear, inputMonth, inputDay)
        engToVikingWeeks = {"Sunday": ["Sun Day", "Sunnudagr"], 
                            "Monday": ["Moon Day", "Mánadagr"], 
                            "Tuesday": ["Tyr's Day", "Týsdagr"], 
                            "Wednesday": ["Odin's Day", "Óðinsdagr"], 
                            "Thursday": ["Thor's Day", "Þórsdagr"], 
                            "Friday": ["Freya's Day", "Frjádagr"], 
                            "Saturday": ["Bath Day", "Laugardagr"]}
        
        season = self.seasonFinder(currentMonth)
        return f"{engToVikingWeeks[week][self.isViking]}, {day} {nameOfMonth} ({season}), {year + 1}"

    #Determines viking season.
    def seasonFinder(self, month):
        seasonList = [["Summer", "Sumar"], ["Winter", "Vetur"]]
        return seasonList[(month - 1) // 6][self.isViking]

    #Used to find the month name.
    def monthName(self, monthNum):
        nameList = [["Harpa", "HARPA"], ["Skerpla", "SKERPLA"], 
                    ["Sun's Month", "SÓLMÁNUÐUR"], ["Haymaking", "Heyannir"], 
                    ["Corn Cutting", "Kornskurðarmánuður"], ["Autumn", "HAUSTMÁNUÐUR"], 
                    ["Slaughter", "GORMÁNUÐUR"], ["Yule", "ÝLIR"], 
                    ["Bone Marrow", "MÖRSUGUR"], ["Black Frost", "ÞORRI"], 
                    ["Thorri Daughter", "GÓI"], ["One-Month", "EINMÁNUÐUR"], 
                    ["Late Month", "Silðimánuður"]]
        
        name = nameList[monthNum - 1][self.isViking]

        #Removes the all caps thing going on.
        if self.isViking:
            nameFirst = name[0].upper()
            nameOther = name[1:].lower()
            name = nameFirst + nameOther

        return name
        
    #Determines if the year is a 13 month long year.
    def isMetonicLeapYear(self, year):
        return year in [2, 5, 7, 10, 13, 16, 18]

    #Adds up cycle days based on index into month list.
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

def main():
    root = Tk()
    root.title("Viking Calendar Calculator")
    calCalc = VikingCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
