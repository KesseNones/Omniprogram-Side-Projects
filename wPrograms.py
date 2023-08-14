#Jesse A. Jones
#Version: 2023-08-14.92

from tkinter import *
import warpToCGUI
import dayOfWeekCalc
import W40KCalendar
import W40KCalendarCalc

#Holds all programs that start with W.
class W(object):
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

        self.warpButton = Button(self.frameBottom, text = "Warp to C Converter", 
            font = FONT, command = self.warpToC)
        self.warpButton.grid(row = 0, column = 0)

        self.weekButton = Button(self.frameBottom, text = "Weekday Calculator", 
            font = FONT, command = self.weekFind)
        self.weekButton.grid(row = 0, column = 1)

        self.warButton = Button(self.frameBottom, text = "Warhammer 40K Calendar", 
            font = FONT, command = self.warhammerFind)
        self.warButton.grid(row = 0, column = 2)

        self.warCalcButton = Button(self.frameBottom, text = "Warhammer 40K Calendar Calculator", 
            font = FONT, command = self.warhammerCalc)
        self.warCalcButton.grid(row = 1, column = 0)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()
    
    def warpToC(self):                  
        warpToCGUI.main()

    def weekFind(self):                 
        dayOfWeekCalc.main()

    def warhammerFind(self):            
        W40KCalendar.main()

    def warhammerCalc(self):            
        W40KCalendarCalc.main()

def main():
    root = Tk()
    root.title("W Starting Programs")
    om = W(root)
    root.mainloop()

if __name__ == "__main__":
    main()