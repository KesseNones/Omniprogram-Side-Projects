#Jesse A. Jones
#Version: 2023-06-08.13

from tkinter import *
import leapDetect
import dateHandling
import metricTime
import weekCalculator

#This class takes in an input date and converts it to the seasonal calendar.
class SeasonCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Fixes window width to prevent text shifting the window size.
        self.window.geometry("500x450")

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date input fields, conversion button, 
        #   and seasonal calendar output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 1, column = 0)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 3, column = 0)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 4, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 5, column = 0)
    
        #Seasonal calendar conversion button.
        self.convButton = Button(self.frameBottom, text = "Convert to Season Calendar", 
            font = "Ariel 20", command = self.sCalCalc)
        self.convButton.grid(row = 6, column = 0)

        #Outputs seasonal calendar date.
        self.seasonalDate = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT, fg = "white", bg = "#f0f0f0")
        self.seasonalDate.grid(row = 7, column = 0)

        #Outputs moon age.
        self.moonAge = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT, fg = "black", bg = "#f0f0f0")
        self.moonAge.grid(row = 8, column = 0)
        
        #Outputs moon phase.
        self.moonPhase = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT, fg = "black", bg = "#f0f0f0")
        self.moonPhase.grid(row = 9, column = 0)

        #Used in parsing user date, detecting if year is leap year, 
        #   finding day num of year, and determining day of week.
        self.parse = dateHandling.GetDate()
        self.leap = leapDetect.IsLeap()
        self.metric = metricTime.MetricTime()
        self.week = weekCalculator.WeekFinder()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    def sCalCalc(self):
        #Fetches input date from user.
        year = self.parse.getYear(self.year.get())
        month = self.parse.getMonth(self.month.get())
        day = self.parse.getDay(self.day.get())

        #Finds seasonal calendar date and displays result.
        seasonalList = self.calcSeasonal(year, month, day)
        self.seasonalDate["text"] = seasonalList[0]
        self.seasonalDate["fg"] = seasonalList[1]
        self.seasonalDate["bg"] = "#404040"

        #Finds moon phase and age of date and displays result.
        moonArr = self.moonCalc(year, month, day)
        self.moonAge["text"] = f"Moon Age: {moonArr[0]} Days"
        self.moonPhase["text"] = moonArr[1]

    #Given input year, month, and day, calculates seasonal calendar.
    def calcSeasonal(self, year, month, day):
        #Finds days elapsed in gregorian year and seasonal year.
        dayCount = self.metric.findDayNumOfYear(year, month, day) - 1
        seasonalDayCount = dayCount - 78

        #Accounts for if seasonal day count is negative.
        seasonalYear = year - (seasonalDayCount < 0)
        seasonalDayCount %= (365 + (self.leap.isLeapYear(year - 1)))

        #Finds seasonal date from seasonal day count.
        resArr = self.findSeasonAndDay(seasonalDayCount)
        sYear = year - 2000
        season = resArr[0]
        sDay = resArr[1]
        fgColor = resArr[2]
        weekDay = self.week.weekFind(year, month, day)

        #Date string and foreground color returned.
        return [f"{weekDay} {sDay} {season}, Year {sYear}", fgColor]

    #Calculates moon phase based on metric date and displays results.
    def moonCalc(self, year, month, day):
        #Finds current metric date and finds difference from base metric date.
        metricDateCalc = self.metric.metric_calc(year, month, day, 0, 0)
        moonBase = 4390.562679166
        metricDiff = metricDateCalc - moonBase
        
        #Metric delta used to find moon age.
        moonAge = (metricDiff * 1000) % 29.530588
        #Accounts for negative moon age edge case.
        if moonAge < 0:
            moonAge += 29.530588
        
        #Formats moon age decimal.
        moonAgeDisp = round(moonAge, 6)
        moonAgeDisp = format(moonAgeDisp, ".6f")
        
        #Determines which moon phase the moon is currently in.
        if 0.0 <= moonAge < 3.6913235:
            moonPhase = "New Moon 🌑"
        elif 3.6913235 <= moonAge < 7.382647:
            moonPhase = "Waxing Crescent 🌒"
        elif 7.382647 <= moonAge < 11.0739705:
            moonPhase = "First Quarter 🌓"
        elif 11.0739705 <= moonAge < 14.765294:
            moonPhase = "Waxing Gibbous 🌔"
        elif 14.765294 <= moonAge < 18.4566175:
            moonPhase = "Full Moon 🌕"
        elif 18.4566175 <= moonAge < 22.147941:
            moonPhase = "Waning Gibbous 🌖"
        elif 22.147941 <= moonAge < 25.8392645:
            moonPhase = "Third Quarter 🌗"
        elif 25.8392645 <= moonAge < 29.530588:
            moonPhase = "Waning Crescent 🌘"
        else:
            moonPhase = "WTF???"

        return [moonAgeDisp, moonPhase]

    #Calculates the seasonal date based on input year and day number.
    def findSeasonAndDay(self, dayNum):
        #Indicates how long each season is for the northern hemisphere.
        # Spring 93 days, Summer 93 days, Fall 90 days, Winter 89 days cm, 90 lpy

        fgColor = None
        seasonDay = None

        #Spring season case.
        if 0 <= dayNum < 93:
            seasonDay = dayNum + 1
            season = "Spring 🌸"
            fgColor = "#38e838"

        #Summer season case.
        elif 93 <= dayNum < 186:
            seasonDay = (dayNum - 93) + 1
            season = "Summer 🔥"
            fgColor = "yellow"
        
        #Autumn season case.
        elif 186 <= dayNum < 276:
            seasonDay = (dayNum - 186) + 1
            season = "Fall 🍂"
            fgColor = "orange"
        
        #Winter season case.
        else:
            seasonDay = (dayNum - 276) + 1
            season = "Winter ❄"
            fgColor = "#1b6eff"

        return [season, seasonDay, fgColor]

   

def main():
    root = Tk()
    root.title("Seasonal Calendar Calculator")
    calCalc = SeasonCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
