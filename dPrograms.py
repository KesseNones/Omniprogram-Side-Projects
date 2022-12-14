from tkinter import *
#import winsound

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

    # def clickSound(self):
    #     if self.soundsAllowed:
    #         winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def quitButtonAction(self):
        self.window.destroy()

    def dstCal(self):
        import dstCalendarCalcGUI
        #self.clickSound()
        dstCalendarCalcGUI.main()   

    def dateDiff(self):
        import dateDaysFromOrAgo
        dateDaysFromOrAgo.main()

    def nightCalc(self):
        import dstNightmareCycleCalc
        dstNightmareCycleCalc.main()
    
    def differentCountdown(self):
        import nonMetricCountDown
        nonMetricCountDown.main()

    def differentCountdownII(self):
        import nonMetricCountDown_MKII
        nonMetricCountDown_MKII.main()

    def diffClk(self):
        import differentClock
        differentClock.main()

    def degClock(self):
        import degreesClock
        degreesClock.main()

def main():
    root = Tk()
    root.title("Programs That Start With D")
    om = D(root)
    root.mainloop()

if __name__ == "__main__":
    main()