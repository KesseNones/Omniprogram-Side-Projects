#Jesse A. Jones
#Version: 2023-06-09.14

from tkinter import *

#Runs programs that start with the letter S when selected.
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

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    def stardateLive(self):                     #DONE
        import stardateGUILIVE
        stardateGUILIVE.main()

    def stardateCalc(self):                     #DONE
        import stardateCalculatorGUI
        stardateCalculatorGUI.main()

    def seasonCalc(self):                       #DONE
        import seasonalCalCalc
        seasonalCalCalc.main()

    def shireCalc(self):                        #DONE
        import shireCalConv
        shireCalConv.main()

    def secStopwatch(self):                     #DONE
        import secondStopwatch
        secondStopwatch.main()

    def revString(self):                        #DONE
        import stringReverser
        stringReverser.main()

    def secCountOfDay(self):                    #DONE
        import secondsInDay
        secondsInDay.main()

    def seasonClock(self):                      #DONE
        import seasonClock
        seasonClock.main()

    def starfield(self):                        #DONE (could use some optimization)
        import starfield
        starfield.main()

    def sesSynCalc(self):                       #HERE
        import seasonalSyncCalendar
        seasonalSyncCalendar.main()

def main():
    root = Tk()
    root.title("S Starting Programs")
    om = S(root)
    root.mainloop()

if __name__ == "__main__":
    main()