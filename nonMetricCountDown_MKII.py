from tkinter import *
import dateHandling
import leapDetect
import datetime
import metricTime

class CountDownAlt(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter year:", font = "Ariel 55", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.year = Entry(self.frameBottom, font = "Times 55")
        self.year.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter month:", font = "Ariel 55", anchor = "w")
        self.messageII.grid(row = 2, column = 0)

        self.month = Entry(self.frameBottom, font = "Times 55")
        self.month.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter day:", font = "Ariel 55", anchor = "w")
        self.messageIII.grid(row = 3, column = 0)

        self.day = Entry(self.frameBottom, font = "Times 55")
        self.day.grid(row = 3, column = 1)

        self.messageIV = Label(self.frameBottom, text = "Enter hour:", font = "Ariel 55", anchor = "w")
        self.messageIV.grid(row = 4, column = 0)

        self.hour = Entry(self.frameBottom, font = "Times 55")
        self.hour.grid(row = 4, column = 1)

        self.messageV = Label(self.frameBottom, text = "Enter minute:", font = "Ariel 55", anchor = "w")
        self.messageV.grid(row = 5, column = 0)

        self.minute = Entry(self.frameBottom, font = "Times 55")
        self.minute.grid(row = 5, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Start Countdown", 
            font = "Ariel 55", command = self.displayTimeDiff)
        self.convButton.grid(row = 6, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Times 55")
        self.tOutput.grid(row = 6, column = 1)

        self.leap = leapDetect.IsLeap()

    def quitButtonAction(self):
        self.window.destroy()

    def displayTimeDiff(self):
        nonMetricTimeString = self.calcTimeDelta()
        self.tOutput["text"] = nonMetricTimeString
        self.tOutput.after(1, self.displayTimeDiff)


    def calcTimeDelta(self):
        date = dateHandling.GetDate()
        metric = metricTime.MetricTime()

        yearIn = date.getYear(self.year.get())
        monthIn = date.getMonth(self.month.get())
        dayIn = date.getDay(self.day.get())
        hourIn = date.getHour(self.hour.get())
        minuteIn = date.getMinOrSec(self.minute.get())

        isOutOfRange = (yearIn < 1969 or yearIn > 3002)
        #isOutOfRange = False

        timeZoneUTCOffshift = -17

        metricIn = metric.metric_calc(yearIn, monthIn, dayIn, hourIn, minuteIn) + ( ( ((3600 * timeZoneUTCOffshift) * ( 0.864 ** (-1) )) / 100000000) * int(isOutOfRange))
        metricCurr = metric.metric_time()

        metricDelta = metricIn - metricCurr

        timeCurrent = datetime.datetime.now()
        yearCurr = timeCurrent.year
        monthCurr = timeCurrent.month
        dayCurr = timeCurrent.day
        hourCurr = timeCurrent.hour
        minuteCurr = timeCurrent.minute

        #convInArr = [yearIn, monthIn, dayIn, hourIn, minuteIn]
        #convCurrArr = [yearCurr, monthCurr, dayCurr, hourCurr, minuteCurr]

        deltaArr = self.dateFromDayDelta(yearCurr, monthCurr, dayCurr, int(metricDelta * 1000))
        timeArr = self.findTimeDelta(metricDelta)

        yearDelta = str(deltaArr[0]).zfill(4)
        monthDelta = str(deltaArr[1]).zfill(2)
        dayDelta = str(deltaArr[2]).zfill(2)

        hourDel = str(timeArr[0]).zfill(2)
        minDel = str(timeArr[1]).zfill(2)
        secDel = str(timeArr[2]).zfill(2)

        return f"{yearDelta}Y {monthDelta}M {dayDelta}D {hourDel}h {minDel}m {secDel}"


    def dateFromDayDelta(self, year, month, day, dayDelta):
        diff = dayDelta
        dayInit = day
        monthInit = month
        yearDelta = 0
        monthDelta = 0
        dayDelta = 0
        if diff == 0:
            return [yearDelta, monthDelta, dayDelta]
        elif diff > 0:
            if diff >= 300000:
                yearAdd = diff // 146097
                year += (yearAdd * 400)
                yearDelta += (yearAdd * 400)
                diff = diff % 146097
            while diff > 0:
                leap = self.leap.isLeapYear(year)
                day += 1
                dayDelta += 1
                if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10) and day > 31:
                    month += 1
                    day -= 31
                if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
                    month += 1
                    day -= 30
                if (month == 2 and day > (28 + leap)):
                    month += 1
                    day -= (28 + leap)
                if month == 12 and day > 31:
                    year += 1
                    month -= 11
                    day -= 31
                if (day == dayInit):
                    if (month == monthInit):
                        monthDelta = 0
                        dayDelta = 0
                        yearDelta += 1
                    else:
                        monthDelta += 1
                        dayDelta = 0
                diff -= 1
            return [yearDelta, monthDelta, dayDelta]
        else:
            if diff <= -300000:
                #print(dayDelta)
                yearSub = (diff * -1) // 146097
                year -= (yearSub * 400)
                yearDelta += (yearSub * 400)
                diff = ((diff * -1) % 146097) * -1
            while diff < 0:
                #print(dayDelta)
                leap = self.leap.isLeapYear(year)
                day -= 1
                dayDelta += 1
                if month == 3 and day < 1:
                    month -= 1
                    day += (28 + leap)
                if month == 1 and day < 1:
                    year -= 1
                    month += 11
                    day += 31
                if (month == 2 or month == 4 or month == 6 or month == 9 or month == 11) and day < 1:
                    month -= 1
                    day += 31
                if (month == 5 or month == 10 or month == 12 or month == 7) and day < 1:
                    month -= 1
                    day += 30
                if (month == 8) and day < 1:
                    month -= 1
                    day += 31
                if (day == dayInit):
                    if (month == monthInit):
                        monthDelta = 0
                        dayDelta = 0
                        yearDelta += 1
                    else:
                        monthDelta += 1
                        dayDelta = 0
                diff += 1
            return [yearDelta, monthDelta, dayDelta]

    def findTimeDelta(self, metricDelta):
        mecondDelta = abs(metricDelta) * 100000000
        secondDelta = (mecondDelta * 0.864)
        secondsOfDay = secondDelta % 86400
        hour = int(secondsOfDay // 3600)
        secondsOfDay %= 3600
        minute = int(secondsOfDay // 60)
        secondsOfDay %= 60
        second = int(secondsOfDay)
        return [hour, minute, second] 

def main():
    root = Tk()
    root.title("Regular Countdown Timer II")
    metric = CountDownAlt(root)
    root.mainloop()

if __name__ == "__main__":
    main()
