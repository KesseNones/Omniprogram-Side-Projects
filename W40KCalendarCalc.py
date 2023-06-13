#Jesse A. Jones
#Version: 2023-06-13.10

from tkinter import *
import leapDetect
import datetime
import metricTime
import dateHandling

#Calculates imperial date from input date and time.
class FortyKCalendarCalc(object):
    """ THE EMPEROR PROTECTS """
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when clicked.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds input fields, conversion button, and calendar output.
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
    
        #Calculates imperial date stamp based 
        #   on input date and time when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert", 
            font = FONT, command = self.displayCal)
        self.convButton.grid(row = 6, column = 0)

        #Displays imperial date output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 30")
        self.tOutput.grid(row = 6, column = 1)

        #Used in detecting leap years, parsing input date 
        #   and time, and finding day number of year.
        self.leap = leapDetect.IsLeap()
        self.dateHandle = dateHandling.GetDate()
        self.metric = metricTime.MetricTime()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates and displays imperial calendar based on input date.
    def displayCal(self):
        #Fetches input date.
        year = self.dateHandle.getYear(self.year.get())
        month = self.dateHandle.getMonth(self.month.get())
        day = self.dateHandle.getDay(self.day.get())
        hour = self.dateHandle.getHour(self.hour.get())
        minute = self.dateHandle.getMinOrSec(self.minute.get())
        
        self.tOutput["text"] = self.calc40K(year, month, day, hour, minute, 0)

    #Caclulates current imperial date stamp and displays it.
    def calc40K(self, year, month, day, hour, minute, second):
        isLeap = self.leap.isLeapYear(year)
        
        #Finds number of days elapsed in decimal form.
        dayNum = self.metric.findDayNumOfYear(year, month, day)
        dayDec = ((hour * 3600) + (minute * 60) + second) / 86400
        dayNumDec = (dayNum - 1) + dayDec

        #Calculates year fraction based on input.
        yearFrac = str(int((dayNumDec / (365 + isLeap)) * 1000)).zfill(3)

        #Finds century portion of year, i.e. 2023 gives 023.
        centuryStamp = (str((year % 1000)).zfill(3))

        #Calculates current millennium in ordinal form 
        #   so it's currently M03 becasue 
        #   it's the 3rd millennium of the common era.
        milleniumOrd = str(((year // 1000) + 1)).zfill(2)

        #Returns Imperial time stamp.
        return f"0 {yearFrac} {centuryStamp}.M{milleniumOrd}"

def main():
    root = Tk()
    root.title("Warhammer 40K Imerial Calendar Calculator")
    metric = FortyKCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
