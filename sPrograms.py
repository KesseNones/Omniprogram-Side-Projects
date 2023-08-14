#Jesse A. Jones
#Version: 2023-08-14.91

from tkinter import *
import stardateGUILIVE
import stardateCalculatorGUI
import seasonalCalCalc
import shireCalConv
import secondStopwatch
import stringReverser
import secondsInDay
import seasonClock
import starfield
import seasonalSyncCalendar

#Runs programs that start with the letter S when selected.
class S(object):
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

        self.starButtonII = Button(self.frameBottom, text = "Stardate",
            font = FONT, command = self.stardateLive)
        self.starButtonII.grid(row = 0, column = 0)

        self.stardateButton = Button(self.frameBottom, text = "Stardate Calculator", 
            font = FONT, command = self.stardateCalc)
        self.stardateButton.grid(row = 0, column = 1)

        self.seasonButton = Button(self.frameBottom, text = "Season Calendar Calculator", 
            font = FONT, command = self.seasonCalc)
        self.seasonButton.grid(row = 0, column = 2)

        self.shireButton = Button(self.frameBottom, text = "Shire Calendar Calculator", 
            font = FONT, command = self.shireCalc)
        self.shireButton.grid(row = 1, column = 0)

        self.secButton = Button(self.frameBottom, text = "Second Counting Stopwatch", 
            font = FONT, command = self.secStopwatch)
        self.secButton.grid(row = 1, column = 1)

        self.revButton = Button(self.frameBottom, text = "String Reverser", 
            font = FONT, command = self.revString)
        self.revButton.grid(row = 1, column = 2)

        self.daysecButton = Button(self.frameBottom, text = "Seconds in Day", 
            font = FONT, command = self.secCountOfDay)
        self.daysecButton.grid(row = 2, column = 0)

        self.seasonclkButton = Button(self.frameBottom, text = "Season Clock", 
            font = FONT, command = self.seasonClock)
        self.seasonclkButton.grid(row = 2, column = 1)

        self.seasonclkButton = Button(self.frameBottom, text = "Starfield", 
            font = FONT, command = self.starfield)
        self.seasonclkButton.grid(row = 2, column = 2)

        self.sesSynButton = Button(self.frameBottom, text = "Seasonaly Synced Calendar", 
            font = FONT, command = self.sesSynCalc)
        self.sesSynButton.grid(row = 3, column = 0)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    def stardateLive(self):                     
        stardateGUILIVE.main()

    def stardateCalc(self):                     
        stardateCalculatorGUI.main()

    def seasonCalc(self):                       
        seasonalCalCalc.main()

    def shireCalc(self):                        
        shireCalConv.main()

    def secStopwatch(self):                     
        secondStopwatch.main()

    def revString(self):                        
        stringReverser.main()

    def secCountOfDay(self):                    
        secondsInDay.main()

    def seasonClock(self):                      
        seasonClock.main()

    def starfield(self):                        #DONE (could use some optimization)
        starfield.main()

    def sesSynCalc(self):                       
        seasonalSyncCalendar.main()

def main():
    root = Tk()
    root.title("S Starting Programs")
    om = S(root)
    root.mainloop()

if __name__ == "__main__":
    main()