from tkinter import *
import math
from math import log

class dstCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter Day Number:", font = "Ariel 75", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.dayE = Entry(self.frameBottom, font = "Times 69")
        self.dayE.grid(row = 1, column = 0)

        self.convButtonI = Button(self.frameBottom, text = "Convert to Don't Starve Calendar", 
            font = "Ariel 60", command = self.dayToCal)
        self.convButtonI.grid(row = 2, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 69", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)

        self.tOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 69")
        self.tOutputII.grid(row = 4, column = 0)

        self.tOutputIII = Label(self.frameBottom, text = "", 
            font = "Ariel 69")
        self.tOutputIII.grid(row = 5, column = 0)
    
    def quitButtonAction(self):
        self.window.destroy()

    def dayToCal(self):
        self.dstCalCalc()
        self.tOutput["text"] = str(self.D) + self.ORDII + " of " + str(self.season) + ", Year " + str(self.year)
        self.tOutputII["text"] = str(self.daysRemain) + " Day" + self.ap1 + " Remain" + self.ap2 + " in the Season"
        self.tOutputIII["text"] = self.lunPhase

    def dstCalCalc(self):
        day = int(self.dayE.get())
        year = (day // 70) + 1
        dayOfYear = day % 70
        if dayOfYear == 0:
            dayOfYear = 70
            year -= 1
        if day == 0:
            D = 15
            ORDII = "th"
            season = "summer"
            year = 0
            daysRemain = 1
            ap1 = ""
            ap2 = "s"
            lunPhase = "Waning Crescent [(]"
            self.D = D
            self.ORDII = ORDII
            self.season = season
            self.year = year
            self.daysRemain = daysRemain
            self.ap1 = ap1
            self.ap2 = ap2
            self.lunPhase = lunPhase
        if 1 <= dayOfYear <= 21:
            season = "Autumn"
            D = dayOfYear
            daysRemain = abs(D - 20) + 1
        if 21 <= dayOfYear <= 35:
            season = "Winter"
            D = (dayOfYear) - 20
            daysRemain = abs(D - 15) + 1
        if 36 <= dayOfYear <= 55:
            season = "Spring"
            D = (dayOfYear) - 35
            daysRemain = abs(D - 20) + 1
        if 56 <= dayOfYear <= 70:
            season = "Summer"
            D = (dayOfYear) - 55
            daysRemain = abs(D - 15) + 1
        if daysRemain == 1:
            ap1 = ""
            ap2 = "s"
        if daysRemain != 1:
            ap1 = "s"
            ap2 = ""
        ORD = D % 10
        if ORD == 0:
            ORDII = 'th'
        if ORD == 1:
            ORDII = "st"
            if ORD == 1 and 20 > D > 10:
                ORDII = 'th'
        if ORD == 2:
            ORDII = "nd"
            if ORD == 2 and 20 > D > 10:
                ORDII = 'th'
        if ORD == 3:
            ORDII = "rd"
            if ORD == 3 and 20 > D > 10:
                ORDII = 'th'
        if ORD == 4:
            ORDII = "th"
        if ORD == 5:
            ORDII = "th"
        if ORD == 6:
            ORDII = "th"
        if ORD == 7:
            ORDII = "th"
        if ORD == 8:
            ORDII = "th"
        if ORD == 9:
            ORDII = "th"
        lun = day % 20
        if lun == 0:
            lunPhase = "Waning Crescent 🌘"
        if lun == 1:
            lunPhase = "New Moon 🌑"
        if 1 < lun <= 4:
            lunPhase = "Waxing Crescent 🌒"
        if 4 < lun <= 7:
            lunPhase = "First Quarter 🌓"
        if 7 < lun <= 10:
            lunPhase = "Waxing Gibbous 🌔"
        if lun == 11:
            lunPhase = "Full Moon 🌕"
        if 11 < lun <= 14:
            lunPhase = "Waning Gibbous 🌖"
        if 14 < lun <= 17:
            lunPhase = "Third Quarter 🌗"
        if 17 < lun < 21:
            lunPhase = "Waning Crescent 🌘"
        self.D = D
        self.ORDII = ORDII
        self.season = season
        self.year = year
        self.daysRemain = daysRemain
        self.ap1 = ap1
        self.ap2 = ap2
        self.lunPhase = lunPhase

def main():
    root = Tk()
    root.title("Dst Calendar Calclator")
    temp = dstCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
