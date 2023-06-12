#Jesse A. Jones
#Version: 2023-06-12.18

from tkinter import *

#Runs programs that start with the letter V.
class V(object):
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

        self.vikingButton = Button(self.frameBottom, text = "Viking Calendar (WIP)", 
            font = "Ariel 30", command = self.viking)
        self.vikingButton.grid(row = 0, column = 0)

        self.visualButton = Button(self.frameBottom, text = "Visual Clock", 
            font = "Ariel 30", command = self.visClock)
        self.visualButton.grid(row = 0, column = 1)

        self.visualCalcButton = Button(self.frameBottom, text = "Visual Clock Calculator", 
            font = "Ariel 30", command = self.visClockCalc)
        self.visualCalcButton.grid(row = 0, column = 2)

    def quitButtonAction(self):
        self.window.destroy()

    def viking(self):                           #DONE
        import vikingCalendarCalc
        vikingCalendarCalc.main()

    def visClock(self):                         #DONE
        import visualClock
        visualClock.main()
    
    def visClockCalc(self):                     #DONE
        import visualClockCalc
        visualClockCalc.main()

def main():
    root = Tk()
    root.title("V Programs")
    om = V(root)
    root.mainloop()

if __name__ == "__main__":
    main()