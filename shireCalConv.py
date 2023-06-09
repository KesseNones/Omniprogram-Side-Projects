#Jesse A. Jones
#Version: 2023-06-09.12

from tkinter import *
import leapDetect
import dateHandling
import weekCalculator
import metricTime

#This class takes in a date input 
#   and displays the resulting converted shire calendar.
class ShireCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button, tolkien name button, and shire name button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Converts date names to tolkien names (english)
        self.toTolkienButton = Button(self.frameTop, text = "To Tolkien Names", font = "Ariel 20", command = self.toTolkien)
        self.toTolkienButton.grid(row = 0, column = 1)

        #Converts date names to shire names.
        self.toShireButton = Button(self.frameTop, text = "To Shire Names", font = "Ariel 20", command = self.toShire)
        self.toShireButton.grid(row = 0, column = 2)

        #Holds date input, conversion button, and date output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Year input field.
        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.year = Entry(self.frameBottom, font = "Ariel 20")
        self.year.grid(row = 0, column = 1)

        #Month input field.
        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.month = Entry(self.frameBottom, font = "Ariel 20")
        self.month.grid(row = 2, column = 1)

        #Day input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 3, column = 1)
    
        #Converts input date to shire calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Shire Calendar", 
            font = "Ariel 20", command = self.shireCalCalc)
        self.convButton.grid(row = 4, column = 0)

        #Used to display shire calendar output.
        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT, bg = "#f0f0f0")
        self.cOutput.grid(row = 4, column = 1)

        #Used in determining if english names are used or not.
        self.tolkAte = False
        
        #Used in date parsing, leap year detection, 
        #   weekday finding, and day of year finding.
        self.date = dateHandling.GetDate()
        self.leap = leapDetect.IsLeap()
        self.week = weekCalculator.WeekFinder()
        self.metric = metricTime.MetricTime()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates shire calendar and displays result.
    def shireCalCalc(self):
        #Fetches user input for conversion.
        year = self.date.getYear(self.year.get())
        month = self.date.getMonth(self.month.get())
        day = self.date.getDay(self.day.get())

        #Finds shire calendar date and displays it.
        self.cOutput["text"] = self.findShire(year, month, day)

    #Enables tolkien names and recalculates date.
    def toTolkien(self):
        self.tolkAte = True
        self.shireCalCalc()

    #Disables tolkien names and recalculates date.
    def toShire(self):
        self.tolkAte = False
        self.shireCalCalc()

    #Calculates shire calendar and returns resulting date string.
    def findShire(self, year, month, day):
        #Calculates shire year.
        shireYear = year - 600
        
        #DESTROY HARD
        # #Finds week day of input date.
        # wkDay = self.week.weekFind(year, month, day)

        #Used to convert an english weekday name to a shire weekday name.
        engToShireDays = {"Sunday": "Sunday", "Monday": "Monday", 
                        "Tuesday": "Trewsday", "Wednesday": "Heavensday", 
                        "Thursday": "Mersday", "Friday": "Highday", 
                        "Saturday": "Sterday"}

        #Finds day of year in gregorian calendar and 
        gregDayOfYear = self.metric.findDayNumOfYear(year, month, day) - 1
        shireDay = gregDayOfYear + 10
        isLeap = self.leap.isLeapYear(shireYear)

        #Compensates for date going over threshold 
        #   due to ten day shift forward.
        shireYear += (shireDay > (364 + isLeap))
        shireDay %= (365 + isLeap)

        #Finds shire date, builds date string, and returns it.
        date = self.shireDateFind(shireYear, shireDay + 1, isLeap)
        shireWeek = self.week.weekFind(year, month, day)
        if not(self.tolkAte):
            shireWeek = engToShireDays[shireWeek]
        return f"{shireWeek} {date},\n{shireYear} Shire Reckoning"

    #Based on year, day number, and if it's 
    #   a leap year, the shire calendar date is found.
    def shireDateFind(self, shireYear, shireCode, isLeapYear):
        self.cOutput["bg"] = "#373737"
        
        #Yule case.
        if shireCode == 1:
            sDay = 2
            sMonth = "Yule"
            self.cOutput["fg"] = "#f0ffff"
        
        #Used in leap year math.
        leapAdd = 0
        leapSubtract = 0
        
        #Afteryule case.
        if 1 < shireCode < 32:
            if self.tolkAte == False:
                sMonth = "Afteryule"
            else:
                sMonth = "January"
            sDay = shireCode - 1
            self.cOutput["fg"] = "#87cefa"
        
        #Solmath case.
        if 32 <= shireCode < 62:
            if self.tolkAte == False:
                sMonth = "Solmath"
            else:
                sMonth = "February"
            sDay = shireCode - 31
            self.cOutput["fg"] = "#b0c4de"
        
        #Rethe case.
        if 62 <= shireCode < 92:
            if self.tolkAte == False:
                sMonth = "Rethe"
            else:
                sMonth = "March"
            sDay = shireCode - 61
            self.cOutput["fg"] = "#9acd32"
        
        #Astron case.
        if 92 <= shireCode < 122:
            if self.tolkAte == False:
                sMonth = "Astron"
            else:
                sMonth = "April"
            sDay = shireCode - 91
            self.cOutput["fg"] = "#228b22"

        #Thrimidge case.
        if 122 <= shireCode < 152:
            if self.tolkAte == False:
                sMonth = "Thrimidge"
            else:
                sMonth = "May"
            sDay = shireCode - 121
            self.cOutput["fg"] = "#e0ffff"
        
        #Forelithe case.
        if 152 <= shireCode < 182:
            if self.tolkAte == False:
                sMonth = "Forelithe"
            else:
                sMonth = "June"
            sDay = shireCode - 151
            self.cOutput["fg"] = "#fffacd"
        
        #Lithe, Midyear's and Lithe second for case of not leap year.
        if isLeapYear == False:
            if shireCode == 182:
                sMonth = "Lithe"
                sDay = 1
                self.cOutput["fg"] = "#f0ffff"
            if shireCode == 183:
                sMonth = ""
                sDay = "Midyear's Day"
                self.cOutput["fg"] = "#f0ffff"
            if shireCode == 184:
                sMonth = "Lithe"
                sDay = 2
                self.cOutput["fg"] = "#f0ffff"

        #Lithe, Midyear's and Lithe second for case of leap year.
        if isLeapYear:
            leapAdd = 1
            leapSubtract = 1
            if shireCode == 182:
                sMonth = "Lithe"
                sDay = 1
                self.cOutput["fg"] = "#f0ffff"
            if shireCode == 183:
                sMonth = ""
                sDay = "Midyear's Day"
                self.cOutput["fg"] = "#f0ffff"
            if shireCode == 184:
                sMonth = ""
                sDay = "Overlithe"
                self.cOutput["fg"] = "#f0ffff"
            if shireCode == 185:
                sMonth = "Lithe"
                sDay = 2
                self.cOutput["fg"] = "#f0ffff"

        #Afterlithe case.
        if 185 + leapAdd <= shireCode < 215 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Afterlithe"
            else:
                sMonth = "July"
            sDay = shireCode - 184 - leapSubtract
            self.cOutput["fg"] = "#008000"

        #Wedmath case.
        if 215 + leapAdd <= shireCode < 245 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Wedmath"
            else:
                sMonth = "August"
            sDay = shireCode - 214 - leapSubtract
            self.cOutput["fg"] = "#556b2f"
        
        #Halimath case.
        if 245 + leapAdd <= shireCode < 275 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Halimath"
            else:
                sMonth = "September"
            sDay = shireCode - 244 - leapSubtract
            self.cOutput["fg"] = "#b8860b"
        
        #Winterfilth case.
        if 275 + leapAdd <= shireCode < 305 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Winterfilth"
            else:
                sMonth = "October"
            sDay = shireCode - 274 - leapSubtract
            self.cOutput["fg"] = "#ffa500"
        
        #Blotmath case.
        if 305 + leapAdd <= shireCode < 335 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Blotmath"
            else:
                sMonth = "November"
            sDay = shireCode - 304 - leapSubtract
            self.cOutput["fg"] = "#a52a2a"
        
        #Foreyule case.
        if 335 + leapAdd <= shireCode < 365 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Foreyule"
            else:
                sMonth = "December"
            sDay = shireCode - 334 - leapSubtract
            self.cOutput["fg"] = "#6495ed"
        
        #First of Yule case.
        if shireCode == 365 + leapAdd:
            sMonth = "Yule"
            sDay = 1
            self.cOutput["fg"] = "#f0ffff"

        #Makes date string and returns it.
        dateString = str(sDay) + " " + sMonth
        return dateString
        
def main():
    root = Tk()
    root.title("Shire Calendar Calculator")
    calCalc = ShireCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
