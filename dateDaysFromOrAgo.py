#Jesse A. Jones
#Version: 2023-05-12.16

from tkinter import *
import datetime
import dateHandling
import weekCalculator
import leapDetect

#This class calculates the date after applying a day offshift.
class DayCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds the quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame holds day difference field, 
        #   date calculation button, and date output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Day offset field.
        self.message = Label(self.frameBottom, text = "Enter Day Difference", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.dayOffset = Entry(self.frameBottom, font = "Ariel 20")
        self.dayOffset.grid(row = 1, column = 0)

        #Date calculation button.
        self.convButtonI = Button(self.frameBottom, text = "Calculate Date", 
            font = "Ariel 20", command = self.dayToCal)
        self.convButtonI.grid(row = 2, column = 0)

        #Converted date output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)

        #Used in leap year detection, weekday 
        #   from date calculation, and date parsing.
        self.leapFind = leapDetect.IsLeap()
        self.weekFinder = weekCalculator.WeekFinder()
        #self.dateGet = dateHandling.GetDate()
    
    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()
        
    #Calls functions to convert input days to date and displays result.                                                             FIX THIS TRASH
    def dayToCal(self):
        self.dateCalc()
        monthArr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = monthArr[self.monthFinal - 1]
        self.tOutput["text"] = self.weekDay + " " + str(self.dayFinal) + " " + str(month) + ", " + str(self.yearFinal)

    #Fetches current date.
    def currentDate(self):
        self.dateISO = datetime.date.today()
        self.currentYear = int(self.dateISO.year)
        self.currentMonth = int(self.dateISO.month)
        self.currentDay = int(self.dateISO.day)

    #Fetches day difference 
    def getDifference(self):
        dateGet = dateHandling.GetDate()
        return dateGet.getYear(self.dayOffset.get())

    def isLeapYear(self, year):                                                                                             #GARBAGE
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        else:
            return False

    #Calculates date with input day offset.
    def dateCalc(self):
        #Fetches current date and day difference.
        self.currentDate()
        year = self.currentYear
        month = self.currentMonth
        day = self.currentDay
        diff = self.getDifference()
        
        #If the difference is too large, 
        #   cut down on the difference using some math.
        if diff >= 3000000:                 #REFACTOR THIS TO BE LESS ARBITRARY
            yearAdd = diff // 146097
            year += (yearAdd * 400)
            diff = diff % 146097

        #Finds date in the future to match this.
        if diff > 0:
            while diff > 0:
                leap = self.isLeapYear(year)
                day += 1
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day > 31:
                    month += 1
                    day -= 31
                if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                    month += 1
                    day -= 30
                if (month == 2 and leap == False and day > 28):
                    month += 1
                    day -= 28
                if (month == 2 and leap == True and day > 29):
                    month += 1
                    day -= 29
                if month == 12 and day > 31:
                    year += 1
                    month -= 11
                    day -= 31
                diff -= 1
            self.yearFinal = year
            self.monthFinal = month
            self.dayFinal = day
            self.weekDay = self.week_fdn()
            return

        #If date is too far back, shift it to be less far back.
        if diff <= -3000000:                    #REFACTOR THIS TO BE LESS ARBITRARY
            yearSub = diff // -146097
            year -= (yearSub * 400)
            diff = diff % -146097

        #Finds date in past.
        if diff < 0:
            while diff < 0:
                leap = self.isLeapYear(year)
                day -= 1
                if month == 3 and leap == False and day < 1:
                    month -= 1
                    day += 28
                if month == 3 and leap == True and day < 1:
                    month -= 1
                    day += 29
                if month == 1 and day < 1:
                    year -= 1
                    month += 11
                    day += 31
                if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) and day < 1:
                    month -= 1
                    day += 31
                if (month == 5 or month == 10 or month == 12 or month == 7) and day < 1:
                    month -= 1
                    day += 30
                if (month == 8) and day < 1:
                    month -= 1
                    day += 31
                diff += 1
            self.yearFinal = year
            self.monthFinal = month
            self.dayFinal = day
            self.weekDay = self.week_fdn()
            return

        #If there is no difference, current date and week day are returned.
        if diff == 0:
            self.yearFinal = year
            self.monthFinal = month
            self.dayFinal = day
            self.weekDay = self.week_fdn()
            return

    #Finds current day of week.
    def week_fdn(self):
            subtract = 0
            year = int(self.yearFinal)
            month = int(self.monthFinal)
            day = int(self.dayFinal)
            if self.isLeapYear(year) and month < 3:
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
            weekArr = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            wk = weekArr[net]
            return wk                    
 
            
def main():
    root = Tk()
    root.title("Date In Some Number of Days From Now or Ago")
    temp = DayCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
