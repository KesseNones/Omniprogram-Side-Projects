#Jesse A. Jones
#Version: 2023-08-14.91

from tkinter import *
import eightPortionClock
import eightPortionClockCalc
import easterCalc
import eruvarianClock
import eruvarianCalendarAndClock
import eruvarianReckoningCalculator
import rivendellCalendarCalc
import eridanianClock

#Contains all programs that start with the letter E
class E(object):
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

        self.eightButton = Button(self.frameBottom, text = "Eight Day Portion Clock", 
            font = FONT, command = self.eightClock)
        self.eightButton.grid(row = 0, column = 0)

        self.eightCalcButton = Button(self.frameBottom, text = "Eight Day Portion Clock Calculator", 
            font = FONT, command = self.eightClockCalc)
        self.eightCalcButton.grid(row = 0, column = 1)

        self.easterCalcButton = Button(self.frameBottom, text = "Easter Calculator", 
            font = FONT, command = self.easterCalc)
        self.easterCalcButton.grid(row = 0, column = 2)

        self.eruClockButton = Button(self.frameBottom, text = "Eru'varian Clock", 
            font = FONT, command = self.eruClock)
        self.eruClockButton.grid(row = 1, column = 0)

        self.eruCalButton = Button(self.frameBottom, text = "Eru'varian Calendar and Clock", 
            font = FONT, command = self.eruCal)
        self.eruCalButton.grid(row = 1, column = 1)

        self.eruCalcButton = Button(self.frameBottom, text = "Eru'varian Reckoning Calculator", 
            font = FONT, command = self.eruCalc)
        self.eruCalcButton.grid(row = 1, column = 2)

        self.elfCalcButton = Button(self.frameBottom, text = "Elven Calendar Calculator", 
            font = FONT, command = self.elfCalc)
        self.elfCalcButton.grid(row = 2, column = 0)

        self.elfCalcButton = Button(self.frameBottom, text = "Eridian Clock", 
            font = FONT, command = self.eriClock)
        self.elfCalcButton.grid(row = 2, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def eightClock(self):                           
        eightPortionClock.main()

    def eightClockCalc(self):                       
        eightPortionClockCalc.main()

    def easterCalc(self):                           
        easterCalc.main()

    def eruClock(self):                             
        eruvarianClock.main()

    def eruCal(self):                               
        eruvarianCalendarAndClock.main()

    def eruCalc(self):                              
        eruvarianReckoningCalculator.main()

    def elfCalc(self):                              
        rivendellCalendarCalc.main()

    def eriClock(self):                             
        eridanianClock.main()

def main():
    root = Tk()
    root.title("Programs that Start with E")
    om = E(root)
    root.mainloop()

if __name__ == "__main__":
    main()