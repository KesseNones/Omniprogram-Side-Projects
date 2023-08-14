#Jesse A. Jones
#Version: 2023-08-14.91

from tkinter import *
import reformedCalendarCalcGUI
import romeNumConv
import relativityCalculator
import romanNumeralClock
import reformedCalendarLive
import reformedCalendarCalcII

#Holds all programs that start with the letter R.
class R(object):
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        FONT = "Ariel 20"

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = FONT, command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.calButton = Button(self.frameBottom, text = "Reformed Calendar Calculator", 
            font = FONT, command = self.refCalCalc)
        self.calButton.grid(row = 0, column = 0)

        self.romeButton = Button(self.frameBottom, text = "Roman Numeral Converter", 
            font = FONT, command = self.romanNum)
        self.romeButton.grid(row = 0, column = 1)

        self.relativeity = Button(self.frameBottom, text = "Relativity Calculator", 
            font = FONT, command = self.relative)
        self.relativeity.grid(row = 0, column = 2)
        
        self.romeClock = Button(self.frameBottom, text = "Roman Numeral Clock and Calendar", 
            font = FONT, command = self.romeCalClock)
        self.romeClock.grid(row = 1, column = 0)

        self.refLiveButton = Button(self.frameBottom, text = "Reformed Calendar Live Edition", 
            font = FONT, command = self.refCalLive)
        self.refLiveButton.grid(row = 1, column = 1)

        self.refCalIIButton = Button(self.frameBottom, text = "Reformed Calendar Calculator Mk II", 
            font = FONT, command = self.refCalCalcII)
        self.refCalIIButton.grid(row = 1, column = 2)

    def quitButtonAction(self):
        self.window.destroy()

    def refCalCalc(self):                                     
        reformedCalendarCalcGUI.main()

    def romanNum(self):                         
        romeNumConv.main()

    def relative(self):                         
        relativityCalculator.main()
        
    def romeCalClock(self):                     
        romanNumeralClock.main()

    def refCalLive(self):                       
        reformedCalendarLive.main()

    def refCalCalcII(self):
        reformedCalendarCalcII.main()

def main():
    root = Tk()
    root.title("Programs Starting With R")
    om = R(root)
    root.mainloop()

if __name__ == "__main__":
    main()