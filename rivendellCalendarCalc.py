from tkinter import *
import dateHandling
import leapDetect

class RivCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.engButton = Button(self.frameTop, text = "To English Names", font = "Ariel 20", command = self.toTolkien)
        self.engButton.grid(row = 0, column = 1)

        self.elfButton = Button(self.frameTop, text = "To Elvish Names", font = "Ariel 20", command = self.toShire)
        self.elfButton.grid(row = 0, column = 2)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55")
        self.messageI.grid(row = 0, column = 0)

        self.yearE = Entry(self.frameBottom, font = "Times 45")
        self.yearE.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 55")
        self.messageII.grid(row = 2, column = 0)

        self.monthE = Entry(self.frameBottom, font = "Times 45")
        self.monthE.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 55")
        self.messageIII.grid(row = 3, column = 0)

        self.dayE = Entry(self.frameBottom, font = "Times 45")
        self.dayE.grid(row = 3, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Convert to Elven Calendar", 
            font = "Times 50", command = self.shireCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Times 60", justify = LEFT, bg = "#f0f0f0")
        self.cOutput.grid(row = 5, column = 0)

        self.anglAte = False

    def quitButtonAction(self):
        self.window.destroy()

    def shireCalCalc(self):
        shireDate = self.cal_calc()
        self.cOutput["text"] = shireDate

    def toTolkien(self):
        self.anglAte = True
        self.shireCalCalc()

    def toShire(self):
        self.anglAte = False
        self.shireCalCalc()

    #5030 years later greg year
    def cal_calc(self):
        date = dateHandling.GetDate()
        leap = leapDetect.IsLeap()
        year = date.getYear(self.yearE.get())
        month = date.getMonth(self.monthE.get())
        day = date.getDay(self.dayE.get())
        rivYear = year + 5031
        leap_year = leap.isLeapYear(year)
        if month == 1:
            D_Code_MKI = 0
        if month == 2:
            D_Code_MKI = 31
        if month == 3:
            D_Code_MKI = 59
            if leap_year == True:
                D_Code_MKI = 60
        if month == 4:
            D_Code_MKI = 90
            if leap_year == True:
                D_Code_MKI = 91
        if month == 5:
            D_Code_MKI = 120
            if leap_year == True:
                D_Code_MKI = 121
        if month == 6:
            D_Code_MKI = 151
            if leap_year == True:
                D_Code_MKI = 152
        if month == 7:
            D_Code_MKI = 181
            if leap_year == True:
                D_Code_MKI = 182
        if month == 8:
            D_Code_MKI = 212
            if leap_year == True:
                D_Code_MKI = 213
        if month == 9:
            D_Code_MKI = 243
            if leap_year == True:
                D_Code_MKI = 244
        if month == 10:
            D_Code_MKI = 273
            if leap_year == True:
                D_Code_MKI = 274
        if month == 11:
            D_Code_MKI = 304
            if leap_year == True:
                D_Code_MKI = 305
        if month == 12:
            D_Code_MKI = 334
            if leap_year == True:
                D_Code_MKI = 335
        D_Code_MKII = D_Code_MKI + day
        elfWeekday = self.getElfWeekday(year, D_Code_MKII)
        rivCode = D_Code_MKII + 285
        if rivCode > 366 and leap_year:
            rivCode -= 366
            rivYear += 1
        elif rivCode > 365 and leap_year == False:
            rivCode -= 365
            rivYear += 1
        date = self.rivendellDateFind(rivYear, rivCode, leap_year)
        dateString = elfWeekday + ", " + date + ", " + str(rivYear)
        return dateString

    #146097 days per 400 year cycle
    def getElfWeekday(self, year, dayCount):
        fourCenturyCount = year // 400
        remainingYears = year % 400
        totalDays = fourCenturyCount * 146097
        leapNess = leapDetect.IsLeap()
        while remainingYears > 0:
            leap = leapNess.isLeapYear(remainingYears)
            if leap:
                totalDays += 366
            else:
                totalDays += 365
            remainingYears -= 1
        totalDays += dayCount
        elfWeekdayNum = totalDays % 6
        elfWeekDays = ["Elenya", "Anarya", "Isilya", "Aldúya", "Menelya", "Valanya"]
        englishElfWeekdays = ["Stars Day", "Sun Day", "Moon Day", 
            "Two Trees Day", "Heavens Day", "Valar Day"]
        if self.anglAte:
            elvishWeekDay = englishElfWeekdays[elfWeekdayNum]
        else:
            elvishWeekDay = elfWeekDays[elfWeekdayNum]
        return elvishWeekDay

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
