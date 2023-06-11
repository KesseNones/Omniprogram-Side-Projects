#Jesse A. Jones
#Version: 2023-06-11.20

from tkinter import *

#Contains programs that start with the letter T.
class T(object):
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

        self.tempButton = Button(self.frameBottom, text = "Temp Converter", 
            font = "Ariel 30", command = self.tempConv)
        self.tempButton.grid(row = 0, column = 0)

        self.moonButton = Button(self.frameBottom, text = "Time Displayer Ultima", 
            font = "Ariel 30", command = self.timeUltima)
        self.moonButton.grid(row = 0, column = 1)

        self.TOSButton = Button(self.frameBottom, text = "TOS Stardate", 
            font = "Ariel 30", command = self.stardateTOS)
        self.TOSButton.grid(row = 0, column = 2)

        self.TOSButton = Button(self.frameBottom, text = "TOS Stardate Calc", 
            font = "Ariel 30", command = self.stardateTOSCalc)
        self.TOSButton.grid(row = 1, column = 0)

        self.trueTNG = Button(self.frameBottom, text = "TNG True Stardate",
            font = "Ariel 30", command = self.TNGLiveSDate)
        self.trueTNG.grid(row = 1, column = 1)

        self.trueTNGCalc = Button(self.frameBottom, text = "TNG True Stardate Calculator",
            font = "Ariel 30", command = self.TNGSDateCalc)
        self.trueTNGCalc.grid(row = 1, column = 2)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    def tempConv(self):                 #DONE
        import tempConverterGUI
        tempConverterGUI.main()

    def timeUltima(self):               #DONE
        import timeDisplayUltima
        timeDisplayUltima.main()

    def stardateTOS(self):              #DONE
        import stardateTOS
        stardateTOS.main()

    def stardateTOSCalc(self):          #DONE
        import stardateTOSCalc
        stardateTOSCalc.main()

    def TNGLiveSDate(self):             #DONE
        import trueStardate
        trueStardate.main()

    def TNGSDateCalc(self):             #HERE
        import trueStardateCalc
        trueStardateCalc.main()

def main():
    root = Tk()
    root.title("T Programs")
    om = T(root)
    root.mainloop()

if __name__ == "__main__":
    main()