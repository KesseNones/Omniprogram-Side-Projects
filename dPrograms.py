#Jesse A. Jones
#Version: 2023-08-14.91

from tkinter import *
import dstCalendarCalcGUI
import dateDaysFromOrAgo
import dstNightmareCycleCalc
import nonMetricCountDown
import nonMetricCountDown_MKII
import differentClock
import degreesClock

#This class contains all programs that start with the letter D.
class D(object):
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        FONT = "Ariel 20"

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = FONT, command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds all other program buttons.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.dstButton = Button(self.frameBottom, text = "DST Calendar Converter", 
            font = FONT, command = self.dstCal)
        self.dstButton.grid(row = 0, column = 0)
        
        self.dayButton = Button(self.frameBottom, text = "Day Difference Date Calc", 
            font = FONT, command = self.dateDiff)
        self.dayButton.grid(row = 0, column = 1)

        self.dayButton2 = Button(self.frameBottom, text = "DST Rough Nightmare Cycle Calculator", 
            font = FONT, command = self.nightCalc)
        self.dayButton2.grid(row = 0, column = 2)

        self.dayButton3 = Button(self.frameBottom, text = "Different Countdown Clock", 
            font = FONT, command = self.differentCountdown)
        self.dayButton3.grid(row = 1, column = 0)

        self.newCountButton = Button(self.frameBottom, text = "Different Countdown Clock MK II", 
            font = FONT, command = self.differentCountdownII)
        self.newCountButton.grid(row = 1, column = 1)

        self.diffClockButton = Button(self.frameBottom, text = "Different Clock (Not Mine)", 
            font = FONT, command = self.diffClk)
        self.diffClockButton.grid(row = 1, column = 2)

        self.degreesClockButton = Button(self.frameBottom, text = "360 Degree Clock", 
            font = FONT, command = self.degClock)
        self.degreesClockButton.grid(row = 2, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def dstCal(self):                       #DONE (Needs some serious refactoring to look less gross)
        dstCalendarCalcGUI.main()   

    def dateDiff(self):                     
        dateDaysFromOrAgo.main()

    def nightCalc(self):                    
        dstNightmareCycleCalc.main()
    
    def differentCountdown(self):           
        nonMetricCountDown.main()

    def differentCountdownII(self):         
        nonMetricCountDown_MKII.main()

    def diffClk(self):                      
        differentClock.main()

    def degClock(self):                     
        degreesClock.main()

def main():
    root = Tk()
    root.title("Programs That Start With D")
    om = D(root)
    root.mainloop()

if __name__ == "__main__":
    main()