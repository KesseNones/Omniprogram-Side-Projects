#Jesse A. Jones
#Version: 2023-05-13.18

from tkinter import *

class D(object):
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

        self.dstButton = Button(self.frameBottom, text = "DST Calendar Converter", 
            font = "Ariel 30", command = self.dstCal)
        self.dstButton.grid(row = 0, column = 0)
        
        self.dayButton = Button(self.frameBottom, text = "Day Difference Date Calc", 
            font = "Ariel 30", command = self.dateDiff)
        self.dayButton.grid(row = 0, column = 1)

        self.dayButton2 = Button(self.frameBottom, text = "DST Rough Nightmare Cycle Calculator", 
            font = "Ariel 30", command = self.nightCalc)
        self.dayButton2.grid(row = 0, column = 2)

        self.dayButton3 = Button(self.frameBottom, text = "Different Countdown Clock", 
            font = "Ariel 30", command = self.differentCountdown)
        self.dayButton3.grid(row = 1, column = 0)

        self.newCountButton = Button(self.frameBottom, text = "Different Countdown Clock MK II", 
            font = "Ariel 30", command = self.differentCountdownII)
        self.newCountButton.grid(row = 1, column = 1)

        self.diffClockButton = Button(self.frameBottom, text = "Different Clock (Not Mine)", 
            font = "Ariel 30", command = self.diffClk)
        self.diffClockButton.grid(row = 1, column = 2)

        self.degreesClockButton = Button(self.frameBottom, text = "360 Degree Clock", 
            font = "Ariel 30", command = self.degClock)
        self.degreesClockButton.grid(row = 2, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def dstCal(self):                       #DONE (Needs some serious refactoring to look less gross)
        import dstCalendarCalcGUI
        dstCalendarCalcGUI.main()   

    def dateDiff(self):                     #DONE
        import dateDaysFromOrAgo
        dateDaysFromOrAgo.main()

    def nightCalc(self):                    #DONE
        import dstNightmareCycleCalc
        dstNightmareCycleCalc.main()
    
    def differentCountdown(self):           #DONE
        import nonMetricCountDown
        nonMetricCountDown.main()

    def differentCountdownII(self):         #DONE
        import nonMetricCountDown_MKII
        nonMetricCountDown_MKII.main()

    def diffClk(self):                      #DONE
        import differentClock
        differentClock.main()

    def degClock(self):                     #HERE
        import degreesClock
        degreesClock.main()

def main():
    root = Tk()
    root.title("Programs That Start With D")
    om = D(root)
    root.mainloop()

if __name__ == "__main__":
    main()