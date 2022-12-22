#Jesse A. Jones
#Version: 2022-12-22.2

from tkinter import *
import metricTime
import dateHandling
from math import trunc

class LunisolarCalendarCalc(object):
    """
    This class contains all the methods necessary to convert a 
        Gregorian Calendar date to a homemade lunisolar calendar's date.
    """

    #This function initializes all the fields of input for the converter.
    def __init__(self, window = None):
        
        #Top frame established.
        self.window = window
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame created.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Times 20")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Times 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Times 20")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Times 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Times 20")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Times 20")
        self.day.grid(row = 3, column = 1)
    
        #Conversion button and output.
        self.convButton = Button(self.frameBottom, text = "Convert to Luni-Solar Calendar", 
            font = "Times 20", command = self.RCalCalc)
        self.convButton.grid(row = 4, column = 0)
        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Times 20", justify = LEFT)
        self.cOutput.grid(row = 5, column = 0)

        #Used in time calculations.
        self.metricStuph = metricTime.MetricTime()

    #This function quits the given program.
    def quitButtonAction(self):
        self.window.destroy()

    #Displays the resulting lunisolar calendar date to cOutput label.
    def RCalCalc(self):
        date = self.cal_calc()
        self.cOutput["text"] = date

    #Converts date from input fields to the equivalent lunisolar calendar date.
    def cal_calc(self):
        #Parses date field input. Accounts 
        #   for empty fields and out of bounds inputs.
        dateGet = dateHandling.GetDate()
        year = dateGet.getYear(self.year.get())
        month = dateGet.getMonth(self.month.get())
        day = dateGet.getDay(self.day.get())
        
        #Fetches current metric date and calculates date change from base date.
        baseDayNum = 4388023
        currentDayNum = self.metricStuph.metric_calc(year, month, day, 0, 0)
        currentDayNum = trunc(currentDayNum * 1000)
        dayDelta = currentDayNum - baseDayNum
        #27759 in four cycle

        monthsElapsed = 0
        baseCycleCount = 106
        cyclesElapsedTotal = (dayDelta // 27759) * 4 + baseCycleCount
        remainingCycleDays = dayDelta % 27759
        cyDayArr = [6939, 6940, 6940, 6940]
        shortCy = False

        #Determines if the given metonic cycle is a 
        #   short one as well as how many cycles have gone by.
        if 0 <= remainingCycleDays < self.cyDaySum(cyDayArr, 1):
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 0)
            cyclesElapsedTotal += 0
            shortCy = True
        elif self.cyDaySum(cyDayArr, 1) <= remainingCycleDays < self.cyDaySum(cyDayArr, 2):
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 1)
            cyclesElapsedTotal += 1
        elif self.cyDaySum(cyDayArr, 2) <= remainingCycleDays < self.cyDaySum(cyDayArr, 3):
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 2)
            cyclesElapsedTotal += 2
        else:
            dayNumOfCycle = remainingCycleDays - self.cyDaySum(cyDayArr, 3)
            cyclesElapsedTotal += 3

        #Calculates days and months elapsed in 28 month cycle.
        daySub = shortCy
        currentDayOf28MonthCycle = dayNumOfCycle % 827 + 1
        monthsElapsed = (dayNumOfCycle // 827) * 28

        #Handles case that covers most of the 28 month cycle.
        if dayNumOfCycle < 6616:
            monthArr = [29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 29, 30, 30, 30]

            #Determines current day and months elapsed within the cycle. 
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

        #Handles later chunk of the 28 month cycle.
        else:
            monthArrII = [29, 30, 29, 30, 29, 30, 29, 30, 29, 30 - daySub, 29]
            dayOfExceptionCycle = (dayNumOfCycle - 6616) + 1
            
            #Finds day and months elapsed of later part of 28 month cycle.
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

        #Calculates current month and calls function 
        #   to transform cycles elapsed, current month of cycle, 
        #   and day of cycle into a proper lunisolar datestamp.
        currentMonth = monthsElapsed + 1
        trueDateString = self.toLuniSolar(cyclesElapsedTotal, currentMonth, currentDay)
        return trueDateString
    
    #Calculates lunisolar datestamp from input cycles elapsed, 
    #   month of cycle, and day of month.
    def toLuniSolar(self, cycles, month, day):
        year = cycles * 19
        monthCountArr = [12, 12, 13, 12, 12, 13, 12, 13, 12, 12, 13, 12, 12, 13, 12, 12, 13, 12, 13]

        #Derives current year from leftover year count in Metonic cycle.
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

        #Constructs date string for lunisolar calendar to be returned.
        nameOfMonth = self.monthName(currentMonth)
        date = str(day) + " " + nameOfMonth + "(" + str(currentMonth) + "), " + str(year)
        return date

    #Derives month name from month number. 
    #   Names based on the Farmer's Almanac moon names.
    def monthName(self, monthNum):
        if monthNum == 1:
            name = "Wolf"
        elif monthNum == 2:
            name = "Snow"
        elif monthNum == 3:
            name = "Worm"
        elif monthNum == 4:
            name = "Pink"
        elif monthNum == 5:
            name = "Flower"
        elif monthNum == 6:
            name = "Strawberry"
        elif monthNum == 7:
            name = "Buck"
        elif monthNum == 8:
            name = "Sturgeon"
        elif monthNum == 9:
            name = "Corn"
        elif monthNum == 10:
            name = "Harvest"
        elif monthNum == 11:
            name = "Beaver"
        elif monthNum == 12:
            name = "Cold"
        else:
            name = "Blue"
        return name
        
    #Determines if a given metonic cycle year needs a leap month.
    def isMetonicLeapYear(self, year):
        if year == 2 or year == 5 or year == 7 or year == 10 or year == 13 or year == 16 or year == 18:
            return True
        else:
            return False

    #Returns a sum of days elapsed from a position in a month array.
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

#Creates tkinter root and main loop that makes GUI work.
def main():
    root = Tk()
    root.title("Lunisolar Calendar Calculator")
    calCalc = LunisolarCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
