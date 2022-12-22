#Jesse A. Jones
#Version: 2022-12-22.2

from tkinter import *
import math
import time
import datetime
import dateHandling
import metricTime
import leapDetect

#This class makes a GUI program that is used to calculate 
#   the age of something based on a start date and end date.
class AgeCalc(object):

    #Sets up window and necessary buttons.
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Birth Year:", font = "Times 20")
        self.messageI.grid(row = 0, column = 0)

        self.yearB = Entry(self.frameBottom, font = "Times 20")
        self.yearB.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Birth Month:", font = "Times 20")
        self.messageII.grid(row = 2, column = 0)

        self.monthB = Entry(self.frameBottom, font = "Times 20")
        self.monthB.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Birth Day:", font = "Times 20")
        self.messageIII.grid(row = 3, column = 0)

        self.dayB = Entry(self.frameBottom, font = "Times 20")
        self.dayB.grid(row = 3, column = 1)

        self.messageIV = Label(self.frameBottom, text = "Enter Current Year:", font = "Times 20")
        self.messageIV.grid(row = 4, column = 0)

        self.yearC = Entry(self.frameBottom, font = "Times 20")
        self.yearC.grid(row = 4, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter Current Month:", font = "Times 20")
        self.messageV.grid(row = 5, column = 0)

        self.monthC = Entry(self.frameBottom, font = "Times 20")
        self.monthC.grid(row = 5, column = 1)

        self.messageVI = Label(self.frameBottom, text = "Enter Current Day:", font = "Times 20")
        self.messageVI.grid(row = 6, column = 0)

        self.dayC = Entry(self.frameBottom, font = "Times 20")
        self.dayC.grid(row = 6, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Calculate Age", 
            font = "Times 20", command = self.ageCalc)
        self.convButton.grid(row = 7, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Times 20", justify = LEFT)
        self.cOutput.grid(row = 7, column = 1)

        self.cOutputII = Label(self.frameBottom, text = "", 
            font = "Times 20", justify = LEFT)
        self.cOutputII.grid(row = 8, column = 1)
        
        self.cOutputIII = Label(self.frameBottom, text = "", 
            font = "Times 20", justify = LEFT)
        self.cOutputIII.grid(row = 9, column = 1)
        
    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Displays age calculation information.
    def ageCalc(self):
        self.age_calc()
        self.cOutput["text"] = "Your age is: " + str(self.AGE) + " Year" + self.PII
        self.cOutputII["text"] = "OR"
        self.cOutputIII["text"] = str(self.ageAlt) + " Year" + self.PI + " and " + str(self.ageDay) + " day" + self.PIII

    #Calculates age based on input dates.
    def age_calc(self):
        dateGet = dateHandling.GetDate()
        dayNumFind = metricTime.MetricTime()
        isLeap = leapDetect.IsLeap()

        #Fetches birth date from input boxes.
        yearB = dateGet.getYear(self.yearB.get())
        monthB = dateGet.getMonth(self.monthB.get())
        dayB = dateGet.getDay(self.dayB.get())

        #Fetches "current" date from input boxes.
        yearC = dateGet.getYear(self.yearC.get())
        monthC = dateGet.getMonth(self.monthC.get())
        dayC = dateGet.getDay(self.dayC.get())

        #Converts dates to current day within year.
        birthDayNumber = dayNumFind.findDayNumOfYear(yearB, monthB, dayB)
        currentDayNumber = dayNumFind.findDayNumOfYear(yearC, monthC, dayC)
        
        #div is determined to be 365 or 366 days.
        div = 365 + isLeap.isLeapYear(yearB)

        #Calculates decimal age and years and days old separately.
        yearsOld = yearC - yearB
        if currentDayNumber > birthDayNumber:
                Age_day = currentDayNumber - birthDayNumber
        if currentDayNumber < birthDayNumber:
                Age_day = (currentDayNumber - birthDayNumber) + div
                yearsOld -= 1
        if currentDayNumber == birthDayNumber:
                Age_day = 0
        decimalAge = (currentDayNumber - birthDayNumber) / div
        age = yearsOld + decimalAge
        age = round(age, 3) 

        #Handles case of plural years and days vs not doing that.
        PI = ""
        if yearsOld == 0 or yearsOld > 1 or yearsOld < -1:
                PI = "s"
        else:
                PI = ""
        if age == 0 or age > 1 or age < -1 or 0 < age < 1:
                PII = "s"
        else:
                PII = ""
        if Age_day == 0 or Age_day > 1 or Age_day < -1:
                PIII = "s"
        else:
                PIII = ""

        #Sets instance variables to local variables for displaying age.
        self.AGE = age
        self.PII = PII
        self.ageAlt = yearsOld
        self.ageDay = Age_day
        self.PIII = PIII
        self.PI = PI
        return

def main():
    root = Tk()
    root.title("Age Calculator")
    age = AgeCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
