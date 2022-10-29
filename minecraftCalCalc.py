from tkinter import *
import math
from math import log
from tkinter import messagebox

class MinecraftCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter Day Number:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.dayE = Entry(self.frameBottom, font = "Times 55")
        self.dayE.grid(row = 1, column = 0)

        self.convButtonI = Button(self.frameBottom, text = "Convert to Minecraft Calendar", 
            font = "Ariel 60", command = self.dayToCal)
        self.convButtonI.grid(row = 2, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 60", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)
    
    def quitButtonAction(self):
        self.window.destroy()

    def dayToCal(self):
        self.mcCal()
        self.tOutput["text"] = self.dateString

    def mcCal(self):
        day = self.dayE.get()
        if day == "":
            messagebox.showerror("Empty Entry Error", "Enter something into the day box!")
            return
        day = int(day)
        year = (day // 96) + 1
        dayOfYear = day % 96
        month = dayOfYear // 8 + 1
        dayOfMonth = dayOfYear % 8 + 1
        ORD = dayOfMonth % 10
        if month == 1:
            monthString = "Silverfish (1)"
        if month == 2:
            monthString = "Cow (2)"
        if month == 3:
            monthString = "Ocelot (3)"
        if month == 4:
            monthString = "Rabbit (4)"
        if month == 5:
            monthString = "Ender (5)"
        if month == 6:
            monthString = "Skeleton (6)"
        if month == 7:
            monthString = "Horse (7)"
        if month == 8:
            monthString = "Sheep (8)"
        if month == 9:
            monthString = "Steve (9)"
        if month == 10:
            monthString = "Chicken (10)"
        if month == 11:
            monthString = "Wolf (11)"
        if month == 12:
            monthString = "Pig (12)"
        if ORD == 0:
            ORDII = 'th'
        if ORD == 1:
            ORDII = "st"
            if ORD == 1 and 20 > dayOfMonth > 10:
                ORDII = 'th'
        if ORD == 2:
            ORDII = "nd"
            if ORD == 2 and 20 > dayOfMonth > 10:
                ORDII = 'th'
        if ORD == 3:
            ORDII = "rd"
            if ORD == 3 and 20 > dayOfMonth > 10:
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
        self.dateString = str(dayOfMonth) + ORDII + " of " + monthString + ", " + "Year " + str(year)

def main():
    root = Tk()
    root.title("Minecraft Calendar Calclator")
    temp = MinecraftCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
