#Jesse A. Jones
#Version: 2022-11-16.2

from tkinter import *
import ageCalcGUI
import affCalculator
import luniSolarCalAttempt
import alienNameGenerator
import analogClock
import zodiacClock

#This class holds all programs that start with "A"
class A(object):
    #Creates all buttons of aPrograms
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

        self.ageButton = Button(self.frameBottom, text = "Age Calculator", 
            font = "Ariel 30", command = self.ageCalculator)
        self.ageButton.grid(row = 0, column = 0)

        self.affButton = Button(self.frameBottom, text = "Actillion FTL Calculator", 
            font = "Ariel 30", command = self.actillionCalc)
        self.affButton.grid(row = 0, column = 1)

        self.affButton = Button(self.frameBottom, text = "A Lunisolar Calendar", 
            font = "Ariel 30", command = self.lunisolarCalc)
        self.affButton.grid(row = 0, column = 2)

        self.affButton = Button(self.frameBottom, text = "Alien Name Generator", 
            font = "Ariel 30", command = self.alienName)
        self.affButton.grid(row = 1, column = 0)

        self.affButton = Button(self.frameBottom, text = "Analog Clock", 
            font = "Ariel 30", command = self.analogClock)
        self.affButton.grid(row = 1, column = 1)

        self.affButton = Button(self.frameBottom, text = "Astrology Zodiac Clock", 
            font = "Ariel 30", command = self.astrologyClock)
        self.affButton.grid(row = 1, column = 2)

    #Quits the program chunk.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates the age based on a birth date and "current" date.
    def ageCalculator(self): #DONE
        ageCalcGUI.main()

    #Calculates velocity based on the Actillion FTL Factor scale.
    def actillionCalc(self): #DONE
        affCalculator.main()

    #Converts Gregorian Calendar Date to home-made lunisolar calendar date.
    def lunisolarCalc(self): #DONE
        luniSolarCalAttempt.main()

    #Generates a random alien name based 
    #   on steriotypical alien name components.
    def alienName(self): #DONE
        alienNameGenerator.main()

    #Displays an analog clock with some extra information attached.
    def analogClock(self):  #COMMENTING RIGHT HERE
        analogClock.main()

    #Displays the current position 
    #   in the western astrological zodiac.
    def astrologyClock(self):
        zodiacClock.main()

#Creates and sustains GUI window.
def main():
    root = Tk()
    root.title("Programs That Start With A")
    om = A(root)
    root.mainloop()

if __name__ == "__main__":
    main()