from tkinter import *
import leapDetect
import dateHandling

class ShireCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.toTolkienButton = Button(self.frameTop, text = "To Tolkien Names", font = "Ariel 20", command = self.toTolkien)
        self.toTolkienButton.grid(row = 0, column = 1)

        self.toShireButton = Button(self.frameTop, text = "To Shire Names", font = "Ariel 20", command = self.toShire)
        self.toShireButton.grid(row = 0, column = 2)

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
    
        self.convButton = Button(self.frameBottom, text = "Convert to Shire Calendar", 
            font = "Ariel 50", command = self.shireCalCalc)
        self.convButton.grid(row = 4, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 60", justify = LEFT, bg = "#f0f0f0")
        self.cOutput.grid(row = 5, column = 0)

        self.tolkAte = False

    def quitButtonAction(self):
        self.window.destroy()

    def shireCalCalc(self):
        shireDate = self.cal_calc()
        self.cOutput["text"] = shireDate

    def toTolkien(self):
        self.tolkAte = True
        self.shireCalCalc()

    def toShire(self):
        self.tolkAte = False
        self.shireCalCalc()

    def cal_calc(self):
        date = dateHandling.GetDate()
        leap = leapDetect.IsLeap()
        year = date.getYear(self.yearE.get())
        month = date.getMonth(self.monthE.get())
        day = date.getDay(self.dayE.get())

        shireYear = year - 600
        subtract = 0
        if (month < 3) and leap.isLeapYear(year):
            subtract = -1
        else:
            subtract = 0
        y = year % 100
        yII = int(y / 4)
        yIII = yII + y
        yC = yIII % 7
        if (year - y) % 400 == 0:
            cC = 6
        if ((year - y) - 100) % 400 == 0:
            cC = 4
        if ((year - y) - 200) % 400 == 0:
            cC = 2
        if ((year - y) - 300) % 400 == 0:
            cC = 0
        net = yC + cC
        if month == 1:
            mC = 0
        if month == 2:
            mC = 3
        if month == 3:
            mC = 3
        if month == 4:
            mC = 6
        if month == 5:
            mC = 1
        if month == 6:
            mC = 4
        if month == 7:
            mC = 6
        if month == 8:
            mC = 2
        if month == 9:
            mC = 5
        if month == 10:
            mC = 0
        if month == 11:
            mC = 3
        if month == 12:
            mC = 5
        net = net + mC
        net = net + int(day)
        net = net + subtract
        net = net % 7
        if net == 0:
            if self.tolkAte == False:
                wk = "Sunday"
            else:
                wk = "Sunday"
        if net == 1:
            if self.tolkAte == False:
                wk = "Monday"
            else:
                wk = "Monday"
        if net == 2:
            if self.tolkAte == False:
                wk = "Trewsday"
            else:
                wk = "Tuesday"
        if net == 3:
            if self.tolkAte == False:
                wk = "Hevensday"
            else:
                wk = "Wendesday"
        if net == 4:
            if self.tolkAte == False:
                wk = "Mersday"
            else:
                wk = "Thursday"
        if net == 5:
            if self.tolkAte == False:
                wk = "Highday"
            else:
                wk = "Friday"
        if net == 6:
            if self.tolkAte == False:
                wk = "Sterday"
            else:
                wk = "Saturday"
        shireWeekDay = wk
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
        shireCode = D_Code_MKII + 10
        if shireCode > 366 and leap_year:
            shireCode -= 366
            shireYear += 1
        elif shireCode > 365 and leap_year == False:
            shireCode -= 365
            shireYear += 1
        date = self.shireDateFind(shireYear, shireCode, leap_year)
        dateString = shireWeekDay + " " + date + ", " + str(shireYear)
        return dateString

    def shireDateFind(self, shireYear, shireCode, isLeapYear):
        self.cOutput["bg"] = "#373737"
        if shireCode == 1:
            sDay = 2
            sMonth = "Yule"
            self.cOutput["fg"] = "#f0ffff"
        leapAdd = 0
        leapSubtract = 0
        if 1 < shireCode < 32:
            if self.tolkAte == False:
                sMonth = "Afteryule"
            else:
                sMonth = "January"
            sDay = shireCode - 1
            self.cOutput["fg"] = "#87cefa"
        if 32 <= shireCode < 62:
            if self.tolkAte == False:
                sMonth = "Solmath"
            else:
                sMonth = "February"
            sDay = shireCode - 31
            self.cOutput["fg"] = "#b0c4de"
        if 62 <= shireCode < 92:
            if self.tolkAte == False:
                sMonth = "Rethe"
            else:
                sMonth = "March"
            sDay = shireCode - 61
            self.cOutput["fg"] = "#9acd32"
        if 92 <= shireCode < 122:
            if self.tolkAte == False:
                sMonth = "Astron"
            else:
                sMonth = "April"
            sDay = shireCode - 91
            self.cOutput["fg"] = "#228b22"
        if 122 <= shireCode < 152:
            if self.tolkAte == False:
                sMonth = "Thrimidge"
            else:
                sMonth = "May"
            sDay = shireCode - 121
            self.cOutput["fg"] = "#e0ffff"
        if 152 <= shireCode < 182:
            if self.tolkAte == False:
                sMonth = "Forelithe"
            else:
                sMonth = "June"
            sDay = shireCode - 151
            self.cOutput["fg"] = "#fffacd"
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
        if 185 + leapAdd <= shireCode < 215 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Afterlithe"
            else:
                sMonth = "July"
            sDay = shireCode - 184 - leapSubtract
            self.cOutput["fg"] = "#008000"
        if 215 + leapAdd <= shireCode < 245 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Wedmath"
            else:
                sMonth = "August"
            sDay = shireCode - 214 - leapSubtract
            self.cOutput["fg"] = "#556b2f"
        if 245 + leapAdd <= shireCode < 275 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Halimath"
            else:
                sMonth = "September"
            sDay = shireCode - 244 - leapSubtract
            self.cOutput["fg"] = "#b8860b"
        if 275 + leapAdd <= shireCode < 305 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Winterfilth"
            else:
                sMonth = "October"
            sDay = shireCode - 274 - leapSubtract
            self.cOutput["fg"] = "#ffa500"
        if 305 + leapAdd <= shireCode < 335 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Blotmath"
            else:
                sMonth = "November"
            sDay = shireCode - 304 - leapSubtract
            self.cOutput["fg"] = "#a52a2a"
        if 335 + leapAdd <= shireCode < 365 + leapAdd:
            if self.tolkAte == False:
                sMonth = "Foreyule"
            else:
                sMonth = "December"
            sDay = shireCode - 334 - leapSubtract
            self.cOutput["fg"] = "#6495ed"
        if shireCode == 365 + leapAdd:
            sMonth = "Yule"
            sDay = 1
            self.cOutput["fg"] = "#f0ffff"
        dateString = str(sDay) + " " + sMonth
        return dateString
        
def main():
    root = Tk()
    root.title("Shire Calendar Calculator")
    calCalc = ShireCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
