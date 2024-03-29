#Jesse A. Jones
#Version: 2023-08-14.90

from tkinter import *
import bearimyConverterGUI
import baseConvGui
import binEncoder
import binaryClock
import baseCounter
import baseSixClock
import baseCalculator
import baseSixClock2

#This class contains all the buttons that yield 
#   the programs made that start with the letter B.
class B(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        FONT = "Ariel 20"

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = FONT, command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.berButton = Button(self.frameBottom, text = "Bearimy Converter", 
            font = FONT, command = self.berimyConv)
        self.berButton.grid(row = 0, column = 0)

        self.baseConvButton = Button(self.frameBottom, text = "Base Converter", 
            font = FONT, command = self.baseConvert)
        self.baseConvButton.grid(row = 0, column = 1)

        self.binConvButton = Button(self.frameBottom, text = "Binary Encoder and Decoder", 
            font = FONT, command = self.binConv)
        self.binConvButton.grid(row = 0, column = 2)

        self.binClockButton = Button(self.frameBottom, text = "Binary Clock", 
            font = FONT, command = self.binClock)
        self.binClockButton.grid(row = 1, column = 0)

        self.binClockButton = Button(self.frameBottom, text = "Base Stopwatch", 
            font = FONT, command = self.anyBaseStop)
        self.binClockButton.grid(row = 1, column = 1)
        
        self.baseSixClockButton = Button(self.frameBottom, text = "Base Six Clock", 
            font = FONT, command = self.baseSixClock)
        self.baseSixClockButton.grid(row = 1, column = 2)
        
        self.baseCalcButton = Button(self.frameBottom, text = "Base Calculator", 
            font = FONT, command = self.baseCalculator)
        self.baseCalcButton.grid(row = 2, column = 0)

        self.baseSixClockButtonII = Button(self.frameBottom, text = "Base Six Clock V. II", 
            font = FONT, command = self.baseSixClock2)
        self.baseSixClockButtonII.grid(row = 2, column = 1)

    #Quits the given window.
    def quitButtonAction(self):
        self.window.destroy()

    #Activates program that converts from regular time to Bearmies and back.
    def berimyConv(self):
        bearimyConverterGUI.main()

    #Calls main of program that converts between various bases.
    def baseConvert(self):
        baseConvGui.main()

    #Converts text to the ascii binary equivalents.
    def binConv(self):
        binEncoder.main()

    #Tells the time in a binary fashion.
    def binClock(self):
        binaryClock.main()

    #A stopwatch for bases 2 through 36.
    def anyBaseStop(self):
        baseCounter.main()
        
    #A clock that reckons time in base six.
    def baseSixClock(self):
        baseSixClock.main()
        
    #Performs math in different bases.
    def baseCalculator(self):
        baseCalculator.main()       #FLOATING POINT STUFF STILL NEEDS SOME WORK

    #Another base six clock.
    def baseSixClock2(self):
        baseSixClock2.main()

def main():
    root = Tk()
    root.title("Programs That Start With B")
    om = B(root)
    root.mainloop()

if __name__ == "__main__":
    main()