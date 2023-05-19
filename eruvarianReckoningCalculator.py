#Jesse A. Jones
#Version: 2023-05-19.85

from tkinter import *
import datetime
import time
import leapDetect
import metricTime
import dateHandling
import baseConvertClass

#This class takes in an input date and time 
#   in the Gregorian Calendar (our calnedar) 
#   and converts it to an Eru'varian date and time.
class EruCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program if pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date inputs and outputs.
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
    
        #If pressed input date is converted to Eru'varian date and time.
        self.convButton = Button(self.frameBottom, text = "Convert to Eru'varian Time", 
            font = "Ariel 20", command = self.calcEru)
        self.convButton.grid(row = 6, column = 0)

        #Eru'varian clock output field.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.tOutput.grid(row = 6, column = 1)

        #Eru'varian date field.
        self.cOutputI = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.cOutputI.grid(row = 7, column = 1)

        #Eru'varian sub-age field.
        self.cOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.cOutputII.grid(row = 8, column = 1)

        #Eru'varian Age field.
        self.cOutputIII = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.cOutputIII.grid(row = 9, column = 1)

        #Used in metric date operations, date input parsing, 
        #   and base conversions.
        self.mtrc = metricTime.MetricTime()
        self.date = dateHandling.GetDate()
        self.base = baseConvertClass.BaseConvert()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Generates a simulated unix time stamp if the input date field 
    #   is beyond the range of the usual function used 
    #   to generate the unix time stamp used 
    #   to calculate the Eru'varian calendar. Instead the metric date 
    #   is used to do this.
    def unixTimeCompensator(self):
        metricDate = self.mtrc.metric_calc(
            self.date.getYear(self.year.get()),
            self.date.getMonth(self.month.get()),
            self.date.getDay(self.day.get()),
            self.date.getHour(self.hour.get()),
            self.date.getMinOrSec(self.minute.get()))
        unixSim = ((metricDate - 4371.949) * 100000000) * 0.864 #Converts to simulated UNIX time.
        return unixSim

    #Calls the function to calculate the Eru'varian time 
    #   and calendar and displays the result.
    def calcEru(self):
        timeArr = self.eruCalc()
        self.tOutput["text"] = timeArr[0]
        self.cOutputI["text"] = timeArr[1]
        self.cOutputII["text"] = timeArr[2]
        self.cOutputIII["text"] = timeArr[3]

    #Calculates fetches the input date and creates a unix time stamp from 
    #   it before feeding it into the Eru'varian calendar calculator.
    def eruCalc(self):
        #Establishes the date range the time.mktime method works in.
        isWindows = True
        if isWindows:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000

        #Fetches input date and time.
        year = self.date.getYear(self.year.get())
        month = self.date.getMonth(self.month.get())
        day = self.date.getDay(self.day.get())
        hour = self.date.getHour(self.hour.get())
        minute = self.date.getMinOrSec(self.minute.get())

        #Uses better implemented method to calculate unix time 
        #   if year within range, otherwise the unix timestamp 
        #   is generated more manually.
        if lower < year < upper:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
        else:
            t = self.unixTimeCompensator()

        #Uses generated unix time stamp to calculate resulting calendar 
        #   and returns list of calendar and time strings.
        eruTime = self.eruConv(t)
        return eruTime

    #Based on the input sub age the age is calculated.
    def ageDeterminer(self, subAge):
        if subAge >= 0:
            age = "Age of Balance"
        if -2 < subAge <= -1:
            age = "Age of Chaos"
        if -20709 < subAge <= -2:
            age = "Age of Experimentation"
        if subAge <= -20709:
            age = "Age of Void"
        if subAge >= 5159780351:
            age = "Ragnerok/Unknown"
        return age

    #Takes in a unix time stamp and calculates 
    #   the Eru'varian calendar and time from it.
    def eruConv(self, unix):
        #Useful into used in calculating the numbers needed for the math.
        #659902464000 seconds per sub-age
        #-13916791159 Year of the beginning.
        #107884800991941 Year of the End (12 - 06)

        #Calculates Eru'varian date.
        eruYearsElapsed = unix // 31824000
        eruYear = 5376 + eruYearsElapsed
        eruSubAgeBase = 665509
        eruSubAgesElapsed = eruYear // 20736
        eruSubAge = eruSubAgesElapsed + eruSubAgeBase
        eruYear = eruYear % 20736
        secondsOfCurrentYear = unix % 31824000
        lunarCycle = secondsOfCurrentYear // 2652000
        secondsOfCurrentLunarCycle = secondsOfCurrentYear % 2652000
        eruDay = secondsOfCurrentLunarCycle // 88400
        eruWeekdayNum = int(eruDay) % 6
        weekArr = ["Torfung", "Solfung", "Varfung", "Melfung", "Orivfung", "T'rarfung"]
        eruWeekday =  weekArr[eruWeekdayNum]

        #Fractions used in calculating Eru'varian time.
        eruSecTotal = unix % 88400
        twelfth = 88400 / 12
        onefortyfourth = 88400 / 144
        oneseventeentwentyeigth = 88400 / 1728
        onetwentyK = 88400 / 20736
        onetwofiftyK = 88400 / 248832

        #Calculates places of Eru'varian time.
        twelfths = eruSecTotal // twelfth
        reducedEruSecI = eruSecTotal % twelfth
        onefortyfourths = reducedEruSecI // onefortyfourth
        reducedEruSecII = reducedEruSecI % onefortyfourth
        oneseventeentwentyeigths = reducedEruSecII // oneseventeentwentyeigth
        reducedEruSecIII = reducedEruSecII % oneseventeentwentyeigth
        onetwentyKs = reducedEruSecIII // onetwentyK
        reducedEruSecIV = reducedEruSecIII % onetwentyK
        onetwofiftyKs = reducedEruSecIV // onetwofiftyK

        #Converts time places to base 12.
        firstPlace = self.base.baseConv(int(twelfths), 12)
        secondPlace = self.base.baseConv(int(onefortyfourths), 12)
        thirdPlace = self.base.baseConv(int(oneseventeentwentyeigths), 12)
        fourthPlace = self.base.baseConv(int(onetwentyKs), 12)
        fifthPlace = self.base.baseConv(int(onetwofiftyKs), 12)

        #Converts date elements to base 12.
        trueEruYear = self.base.baseConv(int(eruYear), 12)
        trueEruLunarCycle = self.base.baseConv(int(lunarCycle), 12)
        trueEruDay = self.base.baseConv(int(eruDay), 12)
        trueEruSubAge = self.base.baseConv(int(abs(eruSubAge)), 12)

        #Finds age.
        AGE = self.ageDeterminer(eruSubAge)

        #Handles some age cases of large Eru'varian sub ages.
        if eruSubAge < 0:
            trueEruSubAge = "-" + trueEruSubAge
        if abs(eruSubAge) > 5159780351:
            trueEruSubAge = "Beyond Reckoning"

        #Builds time strings and returns a list of them.
        timeString = firstPlace + "." + secondPlace + thirdPlace + fourthPlace + fifthPlace
        dateString = trueEruYear + "-" + trueEruLunarCycle + "-" + trueEruDay.zfill(2) + ", " + eruWeekday
        subAge = "Sub-Age: " + str(trueEruSubAge)
        return [timeString, dateString, subAge, AGE]

def main():
    root = Tk()
    root.title("Eru'varian Calendar and Time Calculator")
    star = EruCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
