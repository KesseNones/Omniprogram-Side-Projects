#Jesse A. Jones
#Version: 2023-06-01.14

from tkinter import *
import math
import dateHandling
import leapDetect
                                                                                                                        # THIS WHOLE THING IS INCREDIBLY GROSS AND YUCKY. FIX THIS ASAP!
#This class takes in an input date 
#   and displays the resulting reformed calendar date, 
#   a calendar with 13 28 day periods and one or two days at the end.
class ReformedCalendarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds date input fields, conversion button, and date output field.
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
    
        #Converts to reformed calendar when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Reformed Calendar", 
            font = "Ariel 20", command = self.RCalCalc)
        self.convButton.grid(row = 4, column = 0)

        #This is crappy labeling and needs to be redone.

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutput.grid(row = 5, column = 0)

        self.cOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutputII.grid(row = 6, column = 0)
        
        self.cOutputIII = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutputIII.grid(row = 7, column = 0)
        
        self.cOutputIV = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutputIV.grid(row = 8, column = 0)

        self.cOutputV = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutputV.grid(row = 9, column = 0)

        self.cOutputVI = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.cOutputVI.grid(row = 10, column = 0)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates reformed calendar date based on inputs 
    #   and converts it, displaying the result.
    def RCalCalc(self):
        self.cal_calc()
        self.cOutput["text"] = str(self.wkIII) + (",") + " " + str(int(self.day)) + " " + self.mnth + str(",") + " " + str(abs(int(self.year))) + " " + self.EPC1 + " is: "
        self.cOutputII["text"] = self.Rweekday + ", " + str(int(self.Rday)) + " " + self.Rmonth + str(",") + " " + str(abs(int(self.Ryear))) + " " + self.EPC2
        self.cOutputIII["text"] = self.Zy + " " + str(int(self.elmyr)) + ", " + self.Zce + ", " + str(self.ZE) + ", " + str(int(self.ZA)) + self.ORDII + " " + self.Eon
        self.cOutputIV["text"] = "Luni-Solar Year: " + str(int(self.lunyr))
        self.cOutputV["text"] = "Luni-Solar Mini Cycle: " + str(int(self.luncy))
        self.cOutputVI["text"] = "Luni-Solar Mega Cycle: " + str(int(self.lunMcy))

    #Bruh
    def mult28(self, mult):
        return 28 * mult

    #Calculates dates and stuff based on input. 
    #   !!!!This is one large ugly function that should be refactored.
    def cal_calc(self):
        #Classes used in date handling and leap year detection.
        date = dateHandling.GetDate()
        leap = leapDetect.IsLeap()

        #Gets year, month, and day from date input fields.
        year = date.getYear(self.yearE.get())
        month = date.getMonth(self.monthE.get())
        day = date.getDay(self.dayE.get())

        #Pointless cast to float because Python is dynamically typed.
        #   Why, past me, why???
        year = float(year)
        month = float(month)
        day = float(day)

        #Sets a bunch of class variables that don't need to exist.
        self.Ryear = year + 10000
        self.year = year
        self.month = month
        self.day = day

        #Determines if leap subtraction needs 
        #   to happen in week day calculation.
        isLeap = leap.isLeapYear(year)
        if (month < 3) and isLeap:
            subtract = -1
        else:
            subtract = 0
        
        #Determines year code.
        y = year % 100
        yII = int(y / 4)
        yIII = yII + y
        yC = yIII % 7

        #Determines century code.
        if (year - y) % 400 == 0:
            cC = 6
        if ((year - y) - 100) % 400 == 0:
            cC = 4
        if ((year - y) - 200) % 400 == 0:
            cC = 2
        if ((year - y) - 300) % 400 == 0:
            cC = 0

        net = yC + cC
        
        #Calculates month code.
        if month == 1:
            mC = 0
        elif month == 2:
            mC = 3
        elif month == 3:
            mC = 3
        elif month == 4:
            mC = 6
        elif month == 5:
            mC = 1
        elif month == 6:
            mC = 4
        elif month == 7:
            mC = 6
        elif month == 8:
            mC = 2
        elif month == 9:
            mC = 5
        elif month == 10:
            mC = 0
        elif month == 11:
            mC = 3
        else:
            mC = 5

        #Uses information to calculate week day.
        net = net + mC
        net = net + int(day)
        net = net + subtract
        net = net % 7

        #Converts week day number to week name.
        if net == 0:
            wk = "Sunday"
        elif net == 1:
            wk = "Monday"
        elif net == 2:
            wk = "Tuesday"
        elif net == 3:
            wk = "Wednesday"
        elif net == 4:
            wk = "Thursday"
        elif net == 5:
            wk = "Friday"
        else:
            wk = "Saturday"
        self.wkIII = wk

        #Finds day number of year because it's dated and crappy.
        leap_year = isLeap
        if month == 1:
                D_Code_MKI = 0
        elif month == 2:
                D_Code_MKI = 31
        elif month == 3:
                D_Code_MKI = 59
                if leap_year == True:
                    D_Code_MKI = 60
        elif month == 4:
                D_Code_MKI = 90
                if leap_year == True:
                    D_Code_MKI = 91
        elif month == 5:
                D_Code_MKI = 120
                if leap_year == True:
                    D_Code_MKI = 121
        elif month == 6:
                D_Code_MKI = 151
                if leap_year == True:
                    D_Code_MKI = 152
        elif month == 7:
                D_Code_MKI = 181
                if leap_year == True:
                    D_Code_MKI = 182
        elif month == 8:
                D_Code_MKI = 212
                if leap_year == True:
                    D_Code_MKI = 213
        elif month == 9:
                D_Code_MKI = 243
                if leap_year == True:
                    D_Code_MKI = 244
        elif month == 10:
                D_Code_MKI = 273
                if leap_year == True:
                    D_Code_MKI = 274
        elif month == 11:
                D_Code_MKI = 304
                if leap_year == True:
                    D_Code_MKI = 305
        else:
                D_Code_MKI = 334
                if leap_year == True:
                    D_Code_MKI = 335

        #Calulcates day and month number.
        dayNum = D_Code_MKI + day
        monthNum = (dayNum - 1) // 28
        if monthNum == 0:
            self.Rmonth = "Unuary"
        elif monthNum == 1:
            self.Rmonth = "Duotober"
        elif monthNum == 2:
            self.Rmonth = "Tres"
        elif monthNum == 3:
            self.Rmonth = "Quadtober"
        elif monthNum == 4:
            self.Rmonth = "Quintecember"
        elif monthNum == 5:
            self.Rmonth = "Sixril"
        elif monthNum == 6:
            self.Rmonth = "Septecember"
        elif monthNum == 7:
            self.Rmonth = "Octo"
        elif monthNum == 8:
            self.Rmonth = "Novembuary"
        elif monthNum == 9:
            self.Rmonth = "Decemptober"
        elif monthNum == 10:
            self.Rmonth = "Undecimber"
        elif monthNum == 11:
            self.Rmonth = "Dosdecimber"
        elif monthNum == 12:
            self.Rmonth = "Tridecimber"
        else:
            self.Rmonth = "Supplementary"
        
        #Cursed chunk of code used to find reformed calendar day.
        if self.mult28(0) + 1 <= dayNum < self.mult28(1) + 1:
            refDay = dayNum - self.mult28(0)
        elif self.mult28(1) + 1 <= dayNum < self.mult28(2) + 1:
            refDay = dayNum - self.mult28(1)
        elif self.mult28(2) + 1 <= dayNum < self.mult28(3) + 1:
            refDay = dayNum - self.mult28(2)
        elif self.mult28(3) + 1 <= dayNum < self.mult28(4) + 1:
            refDay = dayNum - self.mult28(3)
        elif self.mult28(4) + 1 <= dayNum < self.mult28(5) + 1:
            refDay = dayNum - self.mult28(4)
        elif self.mult28(5) + 1 <= dayNum < self.mult28(6) + 1:
            refDay = dayNum - self.mult28(5)
        elif self.mult28(6) + 1 <= dayNum < self.mult28(7) + 1:
            refDay = dayNum - self.mult28(6)
        elif self.mult28(7) + 1 <= dayNum < self.mult28(8) + 1:
            refDay = dayNum - self.mult28(7)
        elif self.mult28(8) + 1 <= dayNum < self.mult28(9) + 1:
            refDay = dayNum - self.mult28(8)
        elif self.mult28(9) + 1 <= dayNum < self.mult28(10) + 1:
            refDay = dayNum - self.mult28(9)
        elif self.mult28(10) + 1 <= dayNum < self.mult28(11) + 1:
            refDay = dayNum - self.mult28(10)
        elif self.mult28(11) + 1 <= dayNum < self.mult28(12) + 1:
            refDay = dayNum - self.mult28(11)
        elif self.mult28(12) + 1 <= dayNum < self.mult28(13) + 1:
            refDay = dayNum - self.mult28(12)
        else:
            refDay = dayNum - self.mult28(13)
        self.Rday = refDay

        #Calculates reformed calendar week day for normal case.
        W_Code = self.Rday % 7
        if W_Code == 0:
            self.Rweekday = "Joviday"
        elif W_Code == 1:
            self.Rweekday = "Solday"
        elif W_Code == 2:
            self.Rweekday = "Hermesday"
        elif W_Code == 3:
            self.Rweekday = "Venusday"
        elif W_Code == 4:
            self.Rweekday = "Terraday"
        elif W_Code == 5:
            self.Rweekday = "Lunaday"
        else:
            self.Rweekday = "Marsday"

        #If last day or second to last day in leap year, 
        #   special weekday names are to be had.
        if self.Rmonth == "Supplementary":
            if W_Code == 1:
                self.Rweekday = "Yearday"
            else:
                self.Rweekday = "Leapday"

        #Because yes.
        if month == 1:
            self.mnth = "January"
        elif month == 2:
            self.mnth = "February"
        elif month == 3:
            self.mnth = "March"
        elif month == 4:
            self.mnth = "April"
        elif month == 5:
            self.mnth = "May"
        elif month == 6:
            self.mnth = "June"
        elif month == 7:
            self.mnth = "July"
        elif month == 8:
            self.mnth = "August"
        elif month == 9:
            self.mnth = "September"
        elif month == 10:
            self.mnth = "October"
        elif month == 11:
            self.mnth = "November"
        else:
            self.mnth = "December"

        #Used in year designations.
        if year > 0:
            self.EPC1 = "Anno Domini"
        if year <= 0:
            self.EPC1 = "Before Christ"
        if self.Ryear >= 0:
            self.EPC2 = "Human Era"
        if self.Ryear < 0:
            self.EPC2 = "Before Human Era"

        #Cursed code to determine spiritual cylce stuff. 
        #   This is not necessary in the context of this program and should be removed.
        century = self.Ryear - (self.Ryear % 100)
        Zc = (century // 400)
        ZA = (Zc // 4) + 1
        self.ZA = abs(ZA)
        ORD = self.ZA % 10
        if ORD == 0:
            self.ORDII = "th"
        if ORD == 1:
            self.ORDII = "st"
            if ORD == 1 and 20 > ZA > 10:
                self.ORDII = 'th'
        if ORD == 2:
            self.ORDII = "nd"
            if ORD == 2 and 20 > ZA > 10:
                self.ORDII = 'th'
        if ORD == 3:
            self.ORDII = "rd"
            if ORD == 3 and 20 > ZA > 10:
                self.ORDII = 'th'
        if ORD == 4:
            self.ORDII = "th"
        if ORD == 5:
            self.ORDII = "th"
        if ORD == 6:
            self.ORDII = "th"
        if ORD == 7:
            self.ORDII = "th"
        if ORD == 8:
            self.ORDII = "th"
        if ORD == 9:
            self.ORDII = "th"
        if self.Ryear < 0:
            self.Eon = "Before Age"
        if self.Ryear >= 0:
            self.Eon = "Age"
        if Zc % 4 == 0:
            self.ZE = "Fire Era"
        if Zc % 4 == 1:
            self.ZE = "Air Era"
        if Zc % 4 == 2:
            self.ZE = "Water Era"
        if Zc % 4 == 3:
            self.ZE = "Earth Era"
        if self.Ryear % 4 == 0:
            self.Zy = "Fire Year"
        if self.Ryear % 4 == 1:
            self.Zy = "Air Year"
        if self.Ryear % 4 == 2:
            self.Zy = "Water Year"
        if self.Ryear % 4 == 3:
            self.Zy = "Earth Year"
        if century % 400 == 0:
            self.Zce = "Air Century"
        if century % 400 == 100:
            self.Zce = "Water Century"
        if century % 400 == 200:
            self.Zce = "Earth Century"
        if century % 400 == 300:
            self.Zce = "Fire Century"
        self.elmyr = ((self.Ryear % 100) // 4) + 1
        self.lunMcy = (self.Ryear // 361) + 1
        self.luncy = ((self.Ryear % 361) // 19) + 1
        self.lunyr = ((self.Ryear) % 19) + 1
        return

def main():
    root = Tk()
    root.title("Reformed Calendar Calculator")
    calCalc = ReformedCalendarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
