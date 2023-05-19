#Jesse A. Jones
#Version: 2023-05-19.08

from tkinter import *

#Contains all programs that start with the letter E
class E(object):
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

        self.eightButton = Button(self.frameBottom, text = "Eight Day Portion Clock", 
            font = "Ariel 30", command = self.eightClock)
        self.eightButton.grid(row = 0, column = 0)

        self.eightCalcButton = Button(self.frameBottom, text = "Eight Day Portion Clock Calculator", 
            font = "Ariel 30", command = self.eightClockCalc)
        self.eightCalcButton.grid(row = 0, column = 1)

        self.easterCalcButton = Button(self.frameBottom, text = "Easter Calculator", 
            font = "Ariel 30", command = self.easterCalc)
        self.easterCalcButton.grid(row = 0, column = 2)

        self.eruClockButton = Button(self.frameBottom, text = "Eru'varian Clock", 
            font = "Ariel 30", command = self.eruClock)
        self.eruClockButton.grid(row = 1, column = 0)

        self.eruCalButton = Button(self.frameBottom, text = "Eru'varian Calendar and Clock", 
            font = "Ariel 30", command = self.eruCal)
        self.eruCalButton.grid(row = 1, column = 1)

        self.eruCalcButton = Button(self.frameBottom, text = "Eru'varian Reckoning Calculator", 
            font = "Ariel 30", command = self.eruCalc)
        self.eruCalcButton.grid(row = 1, column = 2)

        self.elfCalcButton = Button(self.frameBottom, text = "Elven Calendar Calculator", 
            font = "Ariel 30", command = self.elfCalc)
        self.elfCalcButton.grid(row = 2, column = 0)

        self.elfCalcButton = Button(self.frameBottom, text = "Eridanian Clock", 
            font = "Ariel 30", command = self.eriClock)
        self.elfCalcButton.grid(row = 2, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def eightClock(self):                           #DONE
        import eightPortionClock
        eightPortionClock.main()

    def eightClockCalc(self):                       #DONE
        import eightPortionClockCalc
        eightPortionClockCalc.main()

    def easterCalc(self):                           #DONE
        import easterCalc
        easterCalc.main()

    def eruClock(self):                             #DONE
        import eruvarianClock
        eruvarianClock.main()

    def eruCal(self):                               #DONE (Could use some refactoring)
        import eruvarianCalendarAndClock
        eruvarianCalendarAndClock.main()

    def eruCalc(self):                              #HERE
        import eruvarianReckoningCalculator
        eruvarianReckoningCalculator.main()

    def elfCalc(self):
        import rivendellCalendarCalc
        rivendellCalendarCalc.main()

    def eriClock(self):
        import eridanianClock
        eridanianClock.main()

def main():
    root = Tk()
    root.title("Programs that Start with E")
    om = E(root)
    root.mainloop()

if __name__ == "__main__":
    main()