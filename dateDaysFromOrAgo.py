#Jesse A. Jones
#Version: 2023-05-12.19

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
        self.dateGet = dateHandling.GetDate()
    
    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()
        
    #Calls functions to convert input days to date and displays result.
    def dayToCal(self):
        self.tOutput["text"] = self.dateCalc()

    #Fetches current date.
    def currentDate(self):
        dateISO = datetime.date.today()
        currentYear = int(dateISO.year)
        currentMonth = int(dateISO.month)
        currentDay = int(dateISO.day)

        return [currentYear, currentMonth, currentDay]

    #Calculates date with input day offset.
    def dateCalc(self):
        #Fetches current date and day difference.
        dateArr = self.currentDate()
        year = dateArr[0]
        month = dateArr[1]
        day = dateArr[2]
        diff = self.dateGet.getYear(self.dayOffset.get())
        monthNameArr = ["Jan", "Feb", "Mar",
                        "Apr", "May", "Jun",
                        "Jul", "Aug", "Sep", 
                        "Oct", "Nov", "Dec"]

        #Finds date in the future to match this.
        if diff > 0:
            #Crunches difference down to less than 146097.
            yearAdd = diff // 146097
            year += (yearAdd * 400)
            diff = diff % 146097

            #Moves time forward while difference is not 0.
            while diff > 0:
                #Determines if year is currently leap year and moves day forward by 1.
                leap = self.leapFind.isLeapYear(year)
                day += 1

                #31 day month flip over case.
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day > 31:
                    month += 1
                    day -= 31
                
                #30 day month flip over case.
                if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                    month += 1
                    day -= 30

                #Non leap februrary flip over case.
                if (month == 2 and leap == False and day > 28):
                    month += 1
                    day -= 28

                #Leap year februrary flip over case.
                if (month == 2 and leap == True and day > 29):
                    month += 1
                    day -= 29

                #Year end flip over case.
                if month == 12 and day > 31:
                    year += 1
                    month -= 11
                    day -= 31

                #Diff subtracted once transactions completed.
                diff -= 1

        #Finds date in past.
        if diff < 0:
            #Crunches difference to be closer to 0 and avoid linear time iterations.
            yearSub = diff // -146097
            year -= (yearSub * 400)
            diff = diff % -146097

            #Keeps moving time backwards until difference is down to 0.
            while diff < 0:
                #Day moves backwards and it's determined if leap year exists.
                leap = self.leapFind.isLeapYear(year)
                day -= 1

                #March back to feb non leap case.
                if month == 3 and leap == False and day < 1:
                    month -= 1
                    day += 28

                #March back to feb leap year case.
                if month == 3 and leap == True and day < 1:
                    month -= 1
                    day += 29

                #Back to previous year case.
                if month == 1 and day < 1:
                    year -= 1
                    month += 11
                    day += 31

                #Back to previous 31 day month.
                if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) and day < 1:
                    month -= 1
                    day += 31

                #Back to previous 30 day month.
                if (month == 5 or month == 10 or month == 12 or month == 7) and day < 1:
                    month -= 1
                    day += 30

                #Back from august to july case.
                if (month == 8) and day < 1:
                    month -= 1
                    day += 31

                #Difference adjusted once all has occured.
                diff += 1

        return f"{self.weekFinder.weekFind(year, month, day)} {day} {monthNameArr[month - 1]}, {year}"
           
def main():
    root = Tk()
    root.title("Date +/- Offset")
    temp = DayCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
