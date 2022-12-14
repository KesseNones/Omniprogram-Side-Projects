from tkinter import *
#import winsound

class W(object):
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

        self.warpButton = Button(self.frameBottom, text = "Warp to C Converter", 
            font = "Ariel 30", command = self.warpToC)
        self.warpButton.grid(row = 0, column = 0)

        self.weekButton = Button(self.frameBottom, text = "Weekday Calculator", 
            font = "Ariel 30", command = self.weekFind)
        self.weekButton.grid(row = 0, column = 1)

        self.warButton = Button(self.frameBottom, text = "Warhammer 40K Calendar", 
            font = "Ariel 30", command = self.warhammerFind)
        self.warButton.grid(row = 0, column = 2)

        self.warCalcButton = Button(self.frameBottom, text = "Warhammer 40K Calendar Calculator", 
            font = "Ariel 30", command = self.warhammerCalc)
        self.warCalcButton.grid(row = 1, column = 0)

    # def clickSound(self):
    #     if self.soundsAllowed:
    #         winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def quitButtonAction(self):
        self.window.destroy()
    
    def warpToC(self):
        import warpToCGUI
        #self.clickSound()
        warpToCGUI.main()

    def weekFind(self):
        import dayOfWeekCalc
        dayOfWeekCalc.main()

    def warhammerFind(self):
        import W40KCalendar
        W40KCalendar.main()

    def warhammerCalc(self):
        import W40KCalendarCalc
        W40KCalendarCalc.main()

def main():
    root = Tk()
    root.title("W Starting Programs")
    om = W(root)
    root.mainloop()

if __name__ == "__main__":
    main()