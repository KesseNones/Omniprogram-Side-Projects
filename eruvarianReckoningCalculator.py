from tkinter import *
import datetime
import time
import leapDetect
import metricTime
import dateHandling
import baseConvertClass

class EruCalc(object):
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
    
        self.convButton = Button(self.frameBottom, text = "Convert to Eru'varian Time", 
            font = "Ariel 55", command = self.calcEru)
        self.convButton.grid(row = 6, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 55")
        self.tOutput.grid(row = 6, column = 1)

        self.cOutputI = Label(self.frameBottom, text = "", 
            font = "Ariel 55")
        self.cOutputI.grid(row = 7, column = 1)

        self.cOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 55")
        self.cOutputII.grid(row = 8, column = 1)

        self.cOutputIII = Label(self.frameBottom, text = "", 
            font = "Ariel 55")
        self.cOutputIII.grid(row = 9, column = 1)

        self.isStupid = True

    def quitButtonAction(self):
        self.window.destroy()

    def unixTimeCompensator(self):
        mtrc = metricTime.MetricTime()
        date = dateHandling.GetDate()
        metricDate = mtrc.metric_calc(
            date.getYear(self.year.get()),
            date.getMonth(self.month.get()),
            date.getDay(self.day.get()),
            date.getHour(self.hour.get()),
            date.getMinOrSec(self.minute.get()))
        unixSim = ((metricDate - 4371.949) * 100000000) * 0.864 #Converts to simulated UNIX time.
        return unixSim

    def calcEru(self):
        time = self.eruCalc()
        self.tOutput["text"] = time
        self.cOutputI["text"] = self.otherTimeString
        self.cOutputII["text"] = self.subAge
        self.cOutputIII["text"] = self.age

    def eruCalc(self):
        date = dateHandling.GetDate()
        isStupid = True
        if isStupid:
            lower = 1969
            upper = 3002
        else:
            lower = 0
            upper = 10000
        year = date.getYear(self.year.get())
        month = date.getMonth(self.month.get())
        day = date.getDay(self.day.get())
        hour = date.getHour(self.hour.get())
        minute = date.getMinOrSec(self.minute.get())
        if lower < year < upper:
            dt = datetime.datetime(year, month, day, hour, minute)
            t = (time.mktime(dt.timetuple()))
        else:
            t = self.unixTimeCompensator()
        eruTime = self.eruConv(t)
        return eruTime

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

    def eruConv(self, unix):
        #659902464000 seconds per sub-age
        #-13916791159 Year of the beginning.
        #107884800991941 Year of the End (12 - 06)
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

        eruSecTotal = unix % 88400
        twelfth = 88400 / 12
        onefortyfourth = 88400 / 144
        oneseventeentwentyeigth = 88400 / 1728
        onetwentyK = 88400 / 20736
        onetwofiftyK = 88400 / 248832

        twelfths = eruSecTotal // twelfth
        reducedEruSecI = eruSecTotal % twelfth
        onefortyfourths = reducedEruSecI // onefortyfourth
        reducedEruSecII = reducedEruSecI % onefortyfourth
        oneseventeentwentyeigths = reducedEruSecII // oneseventeentwentyeigth
        reducedEruSecIII = reducedEruSecII % oneseventeentwentyeigth
        onetwentyKs = reducedEruSecIII // onetwentyK
        reducedEruSecIV = reducedEruSecIII % onetwentyK
        onetwofiftyKs = reducedEruSecIV // onetwofiftyK

        base = baseConvertClass.BaseConvert()
        firstPlace = base.baseConv(int(twelfths), 12)
        secondPlace = base.baseConv(int(onefortyfourths), 12)
        thirdPlace = base.baseConv(int(oneseventeentwentyeigths), 12)
        fourthPlace = base.baseConv(int(onetwentyKs), 12)
        fifthPlace = base.baseConv(int(onetwofiftyKs), 12)

        trueEruYear = base.baseConv(int(eruYear), 12)
        trueEruLunarCycle = base.baseConv(int(lunarCycle), 12)
        trueEruDay = base.baseConv(int(eruDay), 12)
        trueEruSubAge = base.baseConv(int(abs(eruSubAge)), 12)

        AGE = self.ageDeterminer(eruSubAge)

        if eruSubAge < 0:
            trueEruSubAge = "-" + trueEruSubAge
        if abs(eruSubAge) > 5159780351:
            trueEruSubAge = "Beyond Reckoning"
        self.otherTimeString = trueEruYear + "-" + trueEruLunarCycle + "-" + trueEruDay.zfill(2) + ", " + eruWeekday
        timeString = firstPlace + "." + secondPlace + thirdPlace + fourthPlace + fifthPlace
        self.subAge = "Sub-Age: " + str(trueEruSubAge)
        self.age = AGE
        return timeString
        # eruDec = eruSecTotal / 88400
        # return format(round(eruDec * 1000, 3), ".3f")

def main():
    root = Tk()
    root.title("Eru'varian Calendar and Time Calculator")
    star = EruCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
