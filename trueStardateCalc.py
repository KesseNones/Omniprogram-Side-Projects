#Jesse A. Jones
#Version: 2023-06-11.21

from tkinter import *
import leapDetect
import datetime
import metricTime
import dateHandling

#Takes in an input date and calculates the true TNG stardate.
class SDateCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date and time input fields, 
        #   conversion button, and TNG stardate output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        FONT = "Ariel 20"

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter year:", font = FONT, anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = FONT)
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter month:", font = FONT, anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = FONT)
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter day:", font = FONT, anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = FONT)
        self.day.grid(row = 3, column = 1)

        #Hour input field.
        self.messageIV = Label(self.frameBottom, text = "Enter hour (UTC):", font = FONT, anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = FONT)
        self.hour.grid(row = 4, column = 1)

        #Minute input field.
        self.messageV = Label(self.frameBottom, text = "Enter minute (UTC):", font = FONT, anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = FONT)
        self.minute.grid(row = 5, column = 1)
    
        #Converts date and time to true TNG stardate when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert", 
            font = FONT, command = self.displaySDate)
        self.convButton.grid(row = 6, column = 0)

        #Displays converted true TNG stardate.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = FONT)
        self.tOutput.grid(row = 6, column = 1)

        self.leap = leapDetect.IsLeap()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates true TNG stardate and displays result.
    def displaySDate(self):
        stardate = self.calcStardate()
        self.tOutput["text"] = stardate

    #Calculates true TNG stardate and returns it.
    def calcStardate(self):
        dateHandle = dateHandling.GetDate()

        #Input date and time fetched.
        year = dateHandle.getYear(self.year.get())
        month = dateHandle.getMonth(self.month.get())
        day = dateHandle.getDay(self.day.get())
        hour = dateHandle.getHour(self.hour.get())
        minute = dateHandle.getMinOrSec(self.minute.get())
        second = 0 

        #Calendar information determined.
        isLeap = self.leap.isLeapYear(year)
        dayNum = metricTime.MetricTime().findDayNumOfYear(year, month, day)
        
        #Calculates total days elapsed.
        dayDec = self.findDayDec(hour, minute, second)
        dayNumDec = (dayNum - 1) + dayDec

        #Calculates fractional chunk of year.
        yearFrac = self.findYearFraction(dayNumDec, isLeap)

        #Stardate 0 is in the year 2323.
        displacement = year - 2323

        #Builds stardate string and returns it.
        return f"{displacement}{yearFrac}"

    #Determines day decimal based on time.
    def findDayDec(self, hour, minute, second):
        hourSecs = hour * 3600
        minuteSecs = minute * 60

        totalSecs = hourSecs + minuteSecs + second

        return (totalSecs / 86400)

    #Determines year fraction based 
    #   on day number decimal and if it's a leap year.
    def findYearFraction(self, dayNumDec, isLeap):
        div = 365 + isLeap
        frac = dayNumDec / div
        frac *= 10000
        frac = int(frac)
        frac /= 10.0
        return (str(frac).zfill(5))

def main():
    root = Tk()
    root.title("True TNG Stardate Calculator")
    metric = SDateCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
