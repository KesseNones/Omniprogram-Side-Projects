#Jesse A. Jones
#Version: 2023-08-14.91

from tkinter import *
import tempConverterGUI
import timeDisplayUltima
import stardateTOS
import stardateTOSCalc
import trueStardate
import trueStardateCalc

#Contains programs that start with the letter T.
class T(object):
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

        self.tempButton = Button(self.frameBottom, text = "Temp Converter", 
            font = FONT, command = self.tempConv)
        self.tempButton.grid(row = 0, column = 0)

        self.moonButton = Button(self.frameBottom, text = "Time Displayer Ultima", 
            font = FONT, command = self.timeUltima)
        self.moonButton.grid(row = 0, column = 1)

        self.TOSButton = Button(self.frameBottom, text = "TOS Stardate", 
            font = FONT, command = self.stardateTOS)
        self.TOSButton.grid(row = 0, column = 2)

        self.TOSButton = Button(self.frameBottom, text = "TOS Stardate Calc", 
            font = FONT, command = self.stardateTOSCalc)
        self.TOSButton.grid(row = 1, column = 0)

        self.trueTNG = Button(self.frameBottom, text = "TNG True Stardate",
            font = FONT, command = self.TNGLiveSDate)
        self.trueTNG.grid(row = 1, column = 1)

        self.trueTNGCalc = Button(self.frameBottom, text = "TNG True Stardate Calculator",
            font = FONT, command = self.TNGSDateCalc)
        self.trueTNGCalc.grid(row = 1, column = 2)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    def tempConv(self):                 
        tempConverterGUI.main()

    def timeUltima(self):               
        timeDisplayUltima.main()

    def stardateTOS(self):              
        stardateTOS.main()

    def stardateTOSCalc(self):          
        stardateTOSCalc.main()

    def TNGLiveSDate(self):             
        trueStardate.main()

    def TNGSDateCalc(self):             
        trueStardateCalc.main()

def main():
    root = Tk()
    root.title("T Programs")
    om = T(root)
    root.mainloop()

if __name__ == "__main__":
    main()