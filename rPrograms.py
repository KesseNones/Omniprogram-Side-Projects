#Jesse A. Jones
#Version: 2023-06-01.27

from tkinter import *

#Holds all programs that start with the letter R.
class R(object):
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 30", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.calButton = Button(self.frameBottom, text = "Reformed Calendar Calculator", 
            font = "Ariel 30", command = self.refCalCalc)
        self.calButton.grid(row = 0, column = 0)

        self.romeButton = Button(self.frameBottom, text = "Roman Numeral Converter", 
            font = "Ariel 30", command = self.romanNum)
        self.romeButton.grid(row = 0, column = 1)

        self.relativeity = Button(self.frameBottom, text = "Relativity Calculator", 
            font = "Ariel 30", command = self.relative)
        self.relativeity.grid(row = 0, column = 2)
        
        self.romeClock = Button(self.frameBottom, text = "Roman Numeral Clock and Calendar", 
            font = "Ariel 30", command = self.romeCalClock)
        self.romeClock.grid(row = 1, column = 0)

        self.refLiveButton = Button(self.frameBottom, text = "Reformed Calendar Live Edition", 
            font = "Ariel 30", command = self.refCalLive)
        self.refLiveButton.grid(row = 1, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def refCalCalc(self):                       #DONE              
        import reformedCalendarCalcGUI
        reformedCalendarCalcGUI.main()

    def romanNum(self):                         #DONE
        import romeNumConv
        romeNumConv.main()

    def relative(self):                         #DONE
        import relativityCalculator
        relativityCalculator.main()
        
    def romeCalClock(self):                     #DONE
        import romanNumeralClock
        romanNumeralClock.main()

    def refCalLive(self):                       #HERE
        import reformedCalendarLive
        reformedCalendarLive.main()

def main():
    root = Tk()
    root.title("Programs Starting With R")
    om = R(root)
    root.mainloop()

if __name__ == "__main__":
    main()