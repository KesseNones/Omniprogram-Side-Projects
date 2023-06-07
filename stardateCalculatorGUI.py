#Jesse A. Jones
#Version: 2023-06-07.13

from tkinter import *
import time
import datetime
import dateHandling
import metricTime

#This class takes in an input date and time 
#   and calculates the stardate based on it.
class StardateCalc(object):
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
        #   conversion button, and stardate output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20", anchor = "w")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)

        #Hour input field.
        self.messageIV = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 20", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)
        self.hour = Entry(self.frameBottom, font = "Ariel 20")
        self.hour.grid(row = 4, column = 1)

        #Minute input field.
        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 20", anchor = "w")
        self.messageV.grid(row = 5, column = 0)
        self.minute = Entry(self.frameBottom, font = "Ariel 20")
        self.minute.grid(row = 5, column = 1)
    
        #Converts input date to stardate when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Stardate", 
            font = "Ariel 20", command = self.calcStar)
        self.convButton.grid(row = 6, column = 0)

        #Stardate output field.
        self.sOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.sOutput.grid(row = 6, column = 1)

        #Used in finding metric date and parsing date and time inputs.
        self.metric = metricTime.MetricTime()
        self.date = dateHandling.GetDate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates a unix time like time stamp 
    #   from input date and time using the metric date.
    def unixTimeCompensator(self, year, month, day, hour, minute):
        metricDate = self.metric.metric_calc(year, month, day, hour, minute)
        
        #Converts metric date to unix time simulation and returns it.
        return ((metricDate - 4371.952) * 100000000) * 0.864

    #Calculates stardate and displays result.
    def calcStar(self):
        #Fetches date inputs.
        year = self.date.getYear(self.year.get())
        month = self.date.getMonth(self.month.get())
        day = self.date.getDay(self.day.get())
        hour = self.date.getHour(self.hour.get())
        minute = self.date.getMinOrSec(self.minute.get())

        self.sOutput["text"] = self.stardateCalc(year, month, day, hour, minute)

    #Calculates stardate and returns it.
    def stardateCalc(self, year, month, day, hour, minute):
        #If year is in range, unix time is calculated using actual library, 
        #   otherwise a simulated version of it is calculated.
        if 1969 < year < 3002:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
        else:
            t = self.unixTimeCompensator(year, month, day, hour, minute)
        
        #Uses the unix time to calculate stardate, round it and return it.
        s = (t / 31557.6) + (740583679.968 / 31557.6)
        RI = s * 100000
        RII = int(RI)
        RIII = RII / 100000
        return RIII

def main():
    root = Tk()
    root.title("Stardate Calculator")
    star = StardateCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
