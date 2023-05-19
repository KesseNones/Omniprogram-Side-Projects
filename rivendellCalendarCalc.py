#Jesse A. Jones
#Version: 2023-05-19.90

from tkinter import *
import dateHandling
import leapDetect
import metricTime

class RivCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button, english name button, and elvish name button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program if pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Converts elf names to english names when pressed.
        self.engButton = Button(self.frameTop, text = "To English Names", font = "Ariel 20", command = self.toTolkien)
        self.engButton.grid(row = 0, column = 1)

        #Converts names to elvish when pressed.
        self.elfButton = Button(self.frameTop, text = "To Elvish Names", font = "Ariel 20", command = self.toShire)
        self.elfButton.grid(row = 0, column = 2)

        #Bottom frame holds date input fields, 
        #   conversion button, and date output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.yearE = Entry(self.frameBottom, font = "Ariel 20")
        self.yearE.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.monthE = Entry(self.frameBottom, font = "Ariel 20")
        self.monthE.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)
        self.dayE = Entry(self.frameBottom, font = "Ariel 20")
        self.dayE.grid(row = 3, column = 1)
    
        #Converts to Elven calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Elven Calendar", 
            font = "Ariel 20", command = self.elvenCalCalc)
        self.convButton.grid(row = 4, column = 0)

        #Resulting date of Elven calendar displayed here.
        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT, bg = "#f0f0f0")
        self.cOutput.grid(row = 4, column = 1)

        #Boolean used to toggle between displaying english names 
        #   and elvish names.
        self.anglAte = False

        #Used in date parsing and leap year detection.
        self.date = dateHandling.GetDate()
        self.leap = leapDetect.IsLeap()
        self.dayFind = metricTime.MetricTime()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls function to calculate elf calendar and displays result.
    def elvenCalCalc(self):
        self.cOutput["text"] = self.elfCalc()

    #When called, sets english boolean to true and recalculates date, 
    #   in order to redisplay it as english.
    def toTolkien(self):
        self.anglAte = True
        self.elvenCalCalc()

    #When called, sets english boolean to false and recalculates date, 
    #   in order to redisplay it as elfish.
    def toShire(self):
        self.anglAte = False
        self.elvenCalCalc()

    #Calculates the elven calendar based on input.
    def elfCalc(self):
        #Fetches date from input fields.
        year = self.date.getYear(self.yearE.get())
        month = self.date.getMonth(self.monthE.get())
        day = self.date.getDay(self.dayE.get())
        
        #5031 is an arbitrary addition to the year.
        rivYear = year + 5031

        #Finds if current year is leap year and current day in gregorian year.
        isLeap = self.leap.isLeapYear(year)
        dayOfGregorianYear = self.dayFind.findDayNumOfYear(year, month, day)

        #Finds elf day of the week.
        elfWeekday = self.getElfWeekday(year, dayOfGregorianYear)
        
        #Finds day of year in the elven calendar.
        rivCode = dayOfGregorianYear + 285
        if rivCode > 366 and isLeap:
            rivCode -= 366
            rivYear += 1
        elif rivCode > 365 and isLeap == False:
            rivCode -= 365
            rivYear += 1

        #Calls function to calculate date in rivendel calendar 
        #   and returns resulting date string.
        date = self.rivendellDateFind(rivYear, rivCode, isLeap)
        dateString = elfWeekday + ", " + date + ", " + str(rivYear)
        return dateString

    #Calculates elven week day based on current day count and year.
    def getElfWeekday(self, year, dayCount):
        #Finds initial day count based on number of elaspsed 400 year cycles.
        fourCenturyCount = year // 400
        remainingYears = year % 400
        totalDays = fourCenturyCount * 146097

        #Calculates the remaining days elapsed based on the years left.
        while remainingYears > 0:
            leap = self.leap.isLeapYear(remainingYears)
            if leap:
                totalDays += 366
            else:
                totalDays += 365
            remainingYears -= 1
        totalDays += dayCount

        #Uses modulo and indexing to return either 
        #   an elfish week day name or englsh week day name.
        elfWeekdayNum = totalDays % 6
        elfWeekDays = ["Elenya", "Anarya", "Isilya", "Aldúya", "Menelya", "Valanya"]
        englishElfWeekdays = ["Stars Day", "Sun Day", "Moon Day", 
            "Two Trees Day", "Heavens Day", "Valar Day"]
        if self.anglAte:
            elvishWeekDay = englishElfWeekdays[elfWeekdayNum]
        else:
            elvishWeekDay = elfWeekDays[elfWeekdayNum]
        return elvishWeekDay

    #Finds the elven calendar date based on the year, 
    #   day number and if it's a leap year.
    def rivendellDateFind(self, rivYear, rivCode, isLeapYear):
        self.cOutput["bg"] = "#373737"
        if rivCode == 1:
            rDay = ""
            season = "Yestarë"
            self.cOutput["fg"] = "#f0ffff"
            if self.anglAte:
                season = "New Year's Day"
        leapAdd = 0
        leapSubtract = 0
        if 1 < rivCode < 56:
            season = "Tuilë"
            rDay = rivCode - 1
            self.cOutput["fg"] = "#228b22"
            if self.anglAte:
                season = "Spring"
        if 56 <= rivCode < 128:
            season = "Lairë"
            rDay = rivCode - 55
            self.cOutput["fg"] = "#fffacd"
            if self.anglAte:
                season = "Summer"
        if 128 <= rivCode < 182:
            season = "Yávië"
            rDay = rivCode - 127
            self.cOutput["fg"] = "#556b2f"
            if self.anglAte:
                season = "Autumn"
        if isLeapYear:
            leapAdd = 1
            leapSubtract = 1
        if 182 <= rivCode < 185 + leapAdd:
            season = "Enderë"
            rDay = rivCode - 181
            self.cOutput["fg"] = "#f0ffff"
            if self.anglAte:
                season = "Middle Day"
        if 185 + leapAdd <= rivCode < 239 + leapAdd:
            season = "Quellë"
            rDay = rivCode - 184 - leapSubtract
            self.cOutput["fg"] = "#b8860b"
            if self.anglAte:
                season = "Fading"
        if 239 + leapAdd <= rivCode < 311 + leapAdd:
            season = "Hrívë"
            rDay = rivCode - 238 - leapSubtract
            self.cOutput["fg"] = "#87cefa"
            if self.anglAte:
                season = "Winter"
        if 311 + leapAdd <= rivCode < 365 + leapAdd:
            season = "Coirë"
            rDay = rivCode - 311 - leapSubtract
            self.cOutput["fg"] = "#9acd32"
            if self.anglAte:
                season = "Stirring"
        if rivCode == 365 + leapAdd:
            season = "Mettarë"
            rDay = ""
            self.cOutput["fg"] = "#f0ffff"
            if self.anglAte:
                season = "New Year's Eve"

        dateString = str(rDay) + " " + season
        return dateString
        
def main():
    root = Tk()
    root.title("Elven Calendar Calculator")
    calCalc = RivCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
