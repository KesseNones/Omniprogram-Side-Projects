from tkinter import *
import math
import time
import datetime
import dateHandling
import metricTime

class stardateCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.year = Entry(self.frameBottom, font = "Times 55")
        self.year.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 55", anchor = "w")
        self.messageII.grid(row = 2, column = 0)

        self.month = Entry(self.frameBottom, font = "Times 55")
        self.month.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 55", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)

        self.day = Entry(self.frameBottom, font = "Times 55")
        self.day.grid(row = 3, column = 1)

        self.messageIV = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 55", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)

        self.hour = Entry(self.frameBottom, font = "Times 55")
        self.hour.grid(row = 4, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 55", anchor = "w")
        self.messageV.grid(row = 5, column = 0)

        self.minute = Entry(self.frameBottom, font = "Times 55")
        self.minute.grid(row = 5, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Convert to Stardate", 
            font = "Ariel 55", command = self.calcStar)
        self.convButton.grid(row = 6, column = 0)

        self.sOutput = Label(self.frameBottom, text = "", 
            font = "Times 55")
        self.sOutput.grid(row = 6, column = 1)

        self.isStupid = True

    def quitButtonAction(self):
        self.window.destroy()

    def unixTimeCompensator(self, year, month, day, hour, min):
        metric = metricTime.MetricTime()
        metricDate = metric.metric_calc(year, month, day, hour, min)
        unixSim = ((metricDate - 4371.952) * 100000000) * 0.864 #Converts to simulated UNIX time.
        return unixSim

    def calcStar(self):
        stardate = self.stardate_calc()
        self.sOutput["text"] = stardate

    def stardate_calc(self):
        if self.isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000
        date = dateHandling.GetDate()
        year = date.getYear(self.year.get())
        month = date.getMonth(self.month.get())
        day = date.getDay(self.day.get())
        hour = date.getHour(self.hour.get())
        minute = date.getMinOrSec(self.minute.get())
        if lower < year < upper:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
        else:
            t = self.unixTimeCompensator(year, month, day, hour, minute)
        s = (t / 31557.59999999999999) + (740583679.968 / 31557.59999999999999)
        RI = s * 100000
        RII = math.trunc(RI)
        RIII = RII / 100000
        return RIII

def main():
    root = Tk()
    root.title("Stardate Calculator")
    star = stardateCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
