#Jesse A. Jones
#Version: 2023-08-14.92

from tkinter import *
import vikingCalendarCalc
import visualClock
import visualClockCalc

#Runs programs that start with the letter V.
class V(object):
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

        self.vikingButton = Button(self.frameBottom, text = "Viking Calendar (WIP)", 
            font = FONT, command = self.viking)
        self.vikingButton.grid(row = 0, column = 0)

        self.visualButton = Button(self.frameBottom, text = "Visual Clock", 
            font = FONT, command = self.visClock)
        self.visualButton.grid(row = 0, column = 1)

        self.visualCalcButton = Button(self.frameBottom, text = "Visual Clock Calculator", 
            font = FONT, command = self.visClockCalc)
        self.visualCalcButton.grid(row = 0, column = 2)

    def quitButtonAction(self):
        self.window.destroy()

    def viking(self):                           
        vikingCalendarCalc.main()

    def visClock(self):                         
        visualClock.main()
    
    def visClockCalc(self):                     
        visualClockCalc.main()

def main():
    root = Tk()
    root.title("V Programs")
    om = V(root)
    root.mainloop()

if __name__ == "__main__":
    main()