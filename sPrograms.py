from tkinter import *
#import winsound

class S(object):
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

        self.starButtonII = Button(self.frameBottom, text = "Stardate",
            font = "Ariel 30", command = self.stardateLive)
        self.starButtonII.grid(row = 0, column = 0)

        self.stardateButton = Button(self.frameBottom, text = "Stardate Calculator", 
            font = "Ariel 30", command = self.stardateCalc)
        self.stardateButton.grid(row = 0, column = 1)

        self.seasonButton = Button(self.frameBottom, text = "Season Calendar Calculator", 
            font = "Ariel 30", command = self.seasonCalc)
        self.seasonButton.grid(row = 0, column = 2)

        self.shireButton = Button(self.frameBottom, text = "Shire Calendar Calculator", 
            font = "Ariel 30", command = self.shireCalc)
        self.shireButton.grid(row = 1, column = 0)

        self.secButton = Button(self.frameBottom, text = "Second Counting Stopwatch", 
            font = "Ariel 30", command = self.secStopwatch)
        self.secButton.grid(row = 1, column = 1)

        self.revButton = Button(self.frameBottom, text = "String Reverser", 
            font = "Ariel 30", command = self.revString)
        self.revButton.grid(row = 1, column = 2)

        self.daysecButton = Button(self.frameBottom, text = "Seconds in Day", 
            font = "Ariel 30", command = self.secCountOfDay)
        self.daysecButton.grid(row = 2, column = 0)

        self.seasonclkButton = Button(self.frameBottom, text = "Season Clock", 
            font = "Ariel 30", command = self.seasonClock)
        self.seasonclkButton.grid(row = 2, column = 1)

        self.seasonclkButton = Button(self.frameBottom, text = "Starfield", 
            font = "Ariel 30", command = self.starfield)
        self.seasonclkButton.grid(row = 2, column = 2)

        self.sesSynButton = Button(self.frameBottom, text = "Seasonaly Synced Calendar", 
            font = "Ariel 30", command = self.sesSynCalc)
        self.sesSynButton.grid(row = 3, column = 0)

    # def clickSound(self):
    #     if self.soundsAllowed:
    #         winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def quitButtonAction(self):
        self.window.destroy()

    def stardateLive(self):
        import stardateGUILIVE
        #self.clickSound()
        stardateGUILIVE.main()

    def stardateCalc(self):
        import stardateCalculatorGUI
        #self.clickSound()
        stardateCalculatorGUI.main()

    def seasonCalc(self):
        import seasonalCalCalc
        seasonalCalCalc.main()

    def shireCalc(self):
        import shireCalConv
        shireCalConv.main()

    def secStopwatch(self):
        import secondStopwatch
        secondStopwatch.main()

    def revString(self):
        import stringReverser
        stringReverser.main()

    def secCountOfDay(self):
        import secondsInDay
        secondsInDay.main()

    def seasonClock(self):
        import seasonClock
        seasonClock.main()

    def starfield(self):
        import starfield
        starfield.main()

    def sesSynCalc(self):
        import seasonalSyncCalendar
        seasonalSyncCalendar.main()

def main():
    root = Tk()
    root.title("S Starting Programs")
    om = S(root)
    root.mainloop()

if __name__ == "__main__":
    main()