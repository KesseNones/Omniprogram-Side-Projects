#Jesse A. Jones
#Version: 2023-06-11.17

from tkinter import *
import math
import time
import datetime
import dateHandling
import metricTime

#This class takes in date input and displays a TOS stardate as a result.
class StardateCalcTOS(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date and time input, 
        #   stardate conversion button, and resulting output stardate.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        FONT = "Ariel 20"

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = FONT, anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = FONT)
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = FONT, anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = FONT)
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = FONT, anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = FONT)
        self.day.grid(row = 3, column = 1)

        #Hour input field.
        self.messageIV = Label(self.frameBottom, text = "Enter Hour:", font = FONT, anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = FONT)
        self.hour.grid(row = 4, column = 1)

        #Minute input field.
        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = FONT, anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = FONT)
        self.minute.grid(row = 5, column = 1)
    
        #Converts input date and time to TOS stardate when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Stardate", 
            font = FONT, command = self.calcStar)
        self.convButton.grid(row = 6, column = 0)

        #Displays output stardate.
        self.sOutput = Label(self.frameBottom, text = "", 
            font = FONT)
        self.sOutput.grid(row = 6, column = 1)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Given input date and time, uses metric date library to create a simulated unix time stamp.
    def unixTimeCompensator(self, year, month, day, hour, minute):
        metric = metricTime.MetricTime()
        metricDate = metric.metric_calc(year, month, day, hour, minute)
        unixSim = ((metricDate - 4371.952) * 100000000) * 0.864 #Converts to simulated UNIX time.
        return unixSim

    #Calculates TOS stardate and displays result.
    def calcStar(self):
        stardate = self.stardateTOSCalc()
        self.sOutput["text"] = stardate

    #Calculates TOS stardate and returns it.
    def stardateTOSCalc(self):
        #Input date and time fetched.
        date = dateHandling.GetDate()
        year = date.getYear(self.year.get())
        month = date.getMonth(self.month.get())
        day = date.getDay(self.day.get())
        hour = date.getHour(self.hour.get())
        minute = date.getMinOrSec(self.minute.get())
        
        #If year is within range, library is used 
        #   to calculate unix time, otherwise simulator is used.
        if 1969 < year < 3002:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
        else:
            t = self.unixTimeCompensator(year, month, day, hour, minute)
        
        #Calculates total stardates.
        s = (6059232000 / 86400) - (t / 86400)
        s *= 5
        
        #Calculates current stardate, truncating to precision setting of 5.
        subStar = abs((s % 10000) - 10000)
        subStar = subStar * (10 ** 5)
        subStar = math.trunc(subStar)
        subStar = subStar / (10 ** 5)

        #Calculates number of issues elapsed.
        superStar = s // 10000
        superStar = (superStar * -1) - 1

        #Builds stardate string and returns it.
        starString = str(subStar) + " " + "(" + str(int(superStar)) + ")"
        return starString

def main():
    root = Tk()
    root.title("Stardate Calculator TOS Version")
    star = StardateCalcTOS(root)
    root.mainloop()

if __name__ == "__main__":
    main()
