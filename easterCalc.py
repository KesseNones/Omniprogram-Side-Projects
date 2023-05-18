#Jesse A. Jones
#Version: 2023-05-18.88

from tkinter import *
import weekCalculator
import dateHandling
import metricTime
import leapDetect


#This class takes in an input year 
#   and calculates the date easter occurs in the given year.
class EasterCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame has quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button that calls method to quit program.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame holds year input, conversion button, and date output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.message = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 1, column = 0)

        #Easter date finding button.
        self.convButton = Button(self.frameBottom, text = "Find Easter Date", 
            font = "Ariel 20", command = self.yearToCal)
        self.convButton.grid(row = 2, column = 0)

        #Easter date output
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)

        #Used in finding day of week, parsing year input, 
        #   finding metric dates, and if a year is a leap year.
        self.weekfind = weekCalculator.WeekFinder()
        self.yearParse = dateHandling.GetDate()
        self.tMetric = metricTime.MetricTime()
        self.findLeap = leapDetect.IsLeap()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls function calculate easter and displays result.
    def yearToCal(self):
        self.tOutput["text"] = self.eCal(self.year.get())

    #Calculates easter based on input year.
    def eCal(self, y):
        #Sets date to start of spring of given year.
        year = self.yearParse.getYear(y)
        month = 3
        day = 21

        newDate = None
        months = ["Jan", "Feb", "Mar",
                "Apr", "May", "Jun",
                "Jul", "Aug", "Sep",
                "Oct", "Nov", "Dec"]
        
        #Finds moon age of spring start.
        moonAge = self.moonCalc(year, month, day)

        #Finds weekday of spring start.
        wkDay = self.weekfind.weekFind(year, month, day)

        #Advances date forward until a full moon happens.
        while not (14.765294 < moonAge < 15.765294):
            #Moves date one day forward and updates date.
            newDate = self.dateCalc(1, year, month, day)
            year = newDate[0]
            month = newDate[1]
            day = newDate[2]

            #Calculates moon age of updated date.
            moonAge = self.moonCalc(year, month, day)

        #If full moon is on a sunday, date moves one day forward 
        #   in order to find the sunday *after* the full moon, 
        #   as the laws of easter dictate.
        if self.weekfind.weekFind(year, month, day) == "Sunday":
            newDate = self.dateCalc(1, year, month, day)
            year = newDate[0]
            month = newDate[1]
            day = newDate[2]

        #Moves date forward until a sunday is found.
        while self.weekfind.weekFind(year, month, day) != "Sunday":
            #Moves date one day forward and updates date.
            newDate = self.dateCalc(1, year, month, day)
            year = newDate[0]
            month = newDate[1]
            day = newDate[2]

        return f"{day} {months[month - 1]}, {year}"

    #Calculates date with input day offset. 
    #   This is modified for the easter calculator.
    def dateCalc(self, diff, year, month, day):
        #Fetches current date and day difference.
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
                leap = self.findLeap.isLeapYear(year)
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
                leap = self.findLeap.isLeapYear(year)
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

        return [year, month, day]

    #Finds moonphase from input date.
    def moonCalc(self, year, month, day):
        moonPhase = ""
        #Finds metric date of date.
        metricDateCalc = self.tMetric.metric_calc(year, month, day, 0, 0)

        #Using the metric date base, a day delta is found 
        #   which is modded by the number of days in a moon cycle.
        moonBase = 4390.562761805
        metricDiff = metricDateCalc - moonBase
        moonAge = (metricDiff * 1000) % 29.530588

        #Prevents negative moon age.
        if moonAge < 0:
            moonAge += 29.530588

        return moonAge

def main():
    root = Tk()
    root.title("Easter Date Calclator")
    temp = EasterCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
