#Jesse A. Jones
#Version: 2023-06-01.16

from tkinter import *
import dateHandling
import leapDetect
import metricTime

#This class takes in an input date 
#   and displays the resulting reformed calendar date, 
#   a calendar with 13 28 day periods and one or two days at the end.
class ReformedCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date input fields, conversion button, and date output field.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)
    
        #Converts to reformed calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Reformed Calendar", 
            font = "Ariel 20", command = self.rCalCalc)
        self.convButton.grid(row = 4, column = 0)

        #This is crappy labeling and needs to be redone.

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutput.grid(row = 4, column = 1)

        #Used in parsing input date, detecting leap years, 
        #   and finding day number in year.
        self.parse = dateHandling.GetDate()
        self.leap = leapDetect.IsLeap()
        self.metric = metricTime.MetricTime()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates reformed calendar date based on inputs 
    #   and converts it, displaying the result.
    def rCalCalc(self):
        #Input date fetched.
        year = self.parse.getYear(self.year.get())
        month = self.parse.getMonth(self.month.get())
        day = self.parse.getDay(self.day.get())

        self.cOutput["text"] = self.calc(year, month, day)

    #Takes in an input date and calculates the reformed calendar from it.
    def calc(self, year, month, day):
        #Finds reformed calendar year and calculates if it's a leap year.
        rYear = year + 10000
        isLeap = self.leap.isLeapYear(rYear)

        #Lists used in finding names based on calculations.
        refMonthList = ["Unuary", "Duotober", "Tres", "Quadtober", 
                        "Quintecember", "Sixril", "Septecember", "Octo", 
                        "Novembruary", "Decemptober", "Undecimer", "Dosdecimder", 
                        "Tridecimber", "Supplementary"]
        refWeekNameList = ["Solday", "Hermesday", "Venusday", "Terraday", 
                        "Lunaday", "Marsday", "Joviday"]
        suppWeekNameList = ["Yearday", "Leapday"]
        metaList = [refWeekNameList, suppWeekNameList]
        eraList = ["Human Era", "Before Human Era"]

        daysElapsed = self.metric.findDayNumOfYear(rYear, month, day) - 1
        monthIndex = daysElapsed // 28
        dayIndex = (daysElapsed % 28)

        #Calculates reformed calendar date string and returns it.
        return f"{metaList[monthIndex == 13][dayIndex % 7]} {dayIndex + 1} {refMonthList[monthIndex]}\n{rYear} {eraList[rYear < 0]}"

def main():
    root = Tk()
    root.title("Reformed Calendar Calculator")
    calCalc = ReformedCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
