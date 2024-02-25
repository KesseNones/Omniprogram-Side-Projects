#Jesse A. Jones
#Version: 2024-02-25.36

from tkinter import *
import ageCalcGUI
import affCalculator
import luniSolarCalAttempt
import alienNameGenerator
import analogClock
import zodiacClock
import asimovEarthMetricTime
import asimovEarthMetTimeCalc

#This class holds all programs that start with "A"
class A(object):
    #Creates all buttons of aPrograms
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

        self.ageButton = Button(self.frameBottom, text = "Age Calculator", 
            font = FONT, command = self.ageCalculator)
        self.ageButton.grid(row = 0, column = 0)

        self.affButton = Button(self.frameBottom, text = "Actillion FTL Calculator", 
            font = FONT, command = self.actillionCalc)
        self.affButton.grid(row = 0, column = 1)

        self.affButton = Button(self.frameBottom, text = "A Lunisolar Calendar", 
            font = FONT, command = self.lunisolarCalc)
        self.affButton.grid(row = 0, column = 2)

        self.affButton = Button(self.frameBottom, text = "Alien Name Generator", 
            font = FONT, command = self.alienName)
        self.affButton.grid(row = 1, column = 0)

        self.affButton = Button(self.frameBottom, text = "Analog Clock", 
            font = FONT, command = self.analogClock)
        self.affButton.grid(row = 1, column = 1)

        self.affButton = Button(self.frameBottom, text = "Astrology Zodiac Clock", 
            font = FONT, command = self.astrologyClock)
        self.affButton.grid(row = 1, column = 2)

        Button(self.frameBottom, text = "Asimov Metric Date and Time",
            font = FONT, command = self.asimovTime).grid(row = 2, column = 0)

        Button(self.frameBottom, text = "Asimov Metric Time Calculator",
            font = FONT, command = self.asimovTimeCalc).grid(row = 2, column = 1)

    #Quits the program chunk.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates the age based on a birth date and "current" date.
    def ageCalculator(self): 
        ageCalcGUI.main()

    #Calculates velocity based on the Actillion FTL Factor scale.
    def actillionCalc(self): 
        affCalculator.main()

    #Converts Gregorian Calendar Date to home-made lunisolar calendar date.
    def lunisolarCalc(self): 
        luniSolarCalAttempt.main()

    #Generates a random alien name based 
    #   on steriotypical alien name components.
    def alienName(self):
        alienNameGenerator.main()

    #Displays an analog clock with some extra information attached.
    def analogClock(self): 
        analogClock.main()

    #Displays the current position 
    #   in the western astrological zodiac.
    def astrologyClock(self):
        zodiacClock.main()

    def asimovTime(self):
        asimovEarthMetricTime.main()

    def asimovTimeCalc(self):
        asimovEarthMetTimeCalc.main()

#Creates and sustains GUI window.
def main():
    root = Tk()
    root.title("Programs That Start With A")
    om = A(root)
    root.mainloop()

if __name__ == "__main__":
    main()