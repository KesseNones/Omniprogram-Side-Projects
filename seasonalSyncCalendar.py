from tkinter import *
import math
import dateHandling
import leapDetect

class SeasonCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageI = Label(self.frameBottom, text = "Enter Year:", font = "Ariel 55")
        self.messageI.grid(row = 0, column = 0)

        self.yearE = Entry(self.frameBottom, font = "Times 45")
        self.yearE.grid(row = 1, column = 0)

        self.messageII = Label(self.frameBottom, text = "Enter Month:", font = "Ariel 55")
        self.messageII.grid(row = 2, column = 0)

        self.monthE = Entry(self.frameBottom, font = "Times 45")
        self.monthE.grid(row = 3, column = 0)

        self.messageIII = Label(self.frameBottom, text = "Enter Day:", font = "Ariel 55")
        self.messageIII.grid(row = 4, column = 0)

        self.dayE = Entry(self.frameBottom, font = "Times 45")
        self.dayE.grid(row = 5, column = 0)
    
        self.convButton = Button(self.frameBottom, text = "Convert to Seasonal Synced Calendar", 
            font = "Times 45", command = self.SCalCalc)
        self.convButton.grid(row = 6, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 55", justify = LEFT)
        self.cOutput.grid(row = 7, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def SCalCalc(self):
        dateString = self.cal_calc()
        self.cOutput["text"] = dateString

    def cal_calc(self):
        date = dateHandling.GetDate()
        leap = leapDetect.IsLeap()

        year = date.getYear(self.yearE.get())
        month = date.getMonth(self.monthE.get())
        day = date.getDay(self.dayE.get())
        
        monthDayArr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        monthNameArr = ["January", "February", "March", "April", "May", "June", \
                "July", "August", "September", "October", "November", "December"]
        flag = 0
        day -= 19
        if month < 3:
            year -= 1
            flag += 1
        if day < 1:
            month -= 1
            if month < 3 and flag == 0:
                year -= 1
            if month < 1:
                month += 12
            if (leap.isLeapYear(year)):
                monthDayArr[1] += 1
            day += monthDayArr[(month - 1)]
        
        dateString = f"{day} {monthNameArr[month - 1]}, {year}"
        
        return dateString

def main():
    root = Tk()
    root.title("Seasonal Synced Calendar Converter")
    calCalc = SeasonCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
