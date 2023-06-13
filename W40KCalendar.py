#Jesse A. Jones
#Version: 2023-06-13.09

from tkinter import *
import leapDetect
import datetime
import metricTime

#Calculates the current imperial timestamp on Holy Terra. 
#   This is based on the current calendar date 
#   so it's the 3rd millennium and not the 42nd.
#   The checking number at the start is always 0 because 
#   this program was made on Holy Terra so it will always 
#   be zero (unless you run this on Mars or something 
#   in which case the checking number should then be changed to 1)
#The Emperor Protects; Imperator Vult.
class FortyKCalendar(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds the time display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays current Imperial Date as known on Holy Terra.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 50")
        self.tOutput.grid(row = 0, column = 0)

        #Used in leap year detection.
        self.leap = leapDetect.IsLeap()

        #Starts recursive loop.
        self.displayCal()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates Imperial Date stamp and displays it.
    def displayCal(self):
        fortyKTimeString = self.calc40K()
        self.tOutput["text"] = fortyKTimeString
        self.tOutput.after(1, self.displayCal)

    #Caclulates current imperial date stamp and displays it.
    def calc40K(self):
        #Fetches current date and time and relevant information.
        timeCurrent = datetime.datetime.utcnow()
        year = timeCurrent.year
        month = timeCurrent.month
        day = timeCurrent.day
        hour = timeCurrent.hour
        minute = timeCurrent.minute
        second = timeCurrent.second 
        isLeap = self.leap.isLeapYear(year)
        
        #Finds number of days elapsed in decimal form.
        dayNum = metricTime.MetricTime().findDayNumOfYear(year, month, day)
        dayDec = self.findDayDec(hour, minute, second)
        dayNumDec = (dayNum - 1) + dayDec

        #Calculates year fraction based on input.
        yearFrac = self.findYearFraction(dayNumDec, isLeap)

        #Finds century portion of year, i.e. 2023 gives 023.
        centuryStamp = self.findCenturyStamp(year)

        #Calculates current millennium in ordinal form 
        #   so it's currently M03 becasue 
        #   it's the 3rd millennium of the common era.
        milleniumOrd = self.findMillenium(year)

        #Returns Imperial time stamp.
        return f"0 {yearFrac} {centuryStamp}.M{milleniumOrd}"

    #Given input time, calculates the day fraction.
    def findDayDec(self, hour, minute, second):
        hourSecs = hour * 3600
        minuteSecs = minute * 60

        totalSecs = hourSecs + minuteSecs + second

        return (totalSecs / 86400)

    #Given the day number decimal, 
    #   finds the current year decimal at three places of precision.
    def findYearFraction(self, dayNumDec, isLeap):
        div = 365 + isLeap
        return str(int( (dayNumDec / div) * 1000) ).zfill(3)

    #Finds the current century stamp of the year.
    def findCenturyStamp(self, year):
        return (str((year % 1000)).zfill(3))

    #Finds ordinal millennium.
    def findMillenium(self, year):
        return (str( ((year // 1000) + 1) ).zfill(2))

def main():
    root = Tk()
    root.title("Warhammer 40K Live Imerial Calendar")
    metric = FortyKCalendar(root)
    root.mainloop()

if __name__ == "__main__":
    main()
