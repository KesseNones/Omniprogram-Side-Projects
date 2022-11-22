#Jesse A. Jones
#Version: 2022-11-22.3

from tkinter import *
import coinFlipGUI
import betterCToWarpConv
import connecFour
import chineseCalCalc
import gradeCalc
import calMonthDisplayGUI
import caesarCipher
import centaurianTime
import gradeCalcGUI

#Contains programs that start with the letter C in their Omniprogram titles.
class C(object):
    #Sets up all of the program buttons.
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

        self.flipButton = Button(self.frameBottom, text = "Coin Flipper",
            font = "Ariel 30", command = self.coinFlipper)
        self.flipButton.grid(row = 0, column = 0)

        self.CButton = Button(self.frameBottom, text = "C to Warp Converter", 
            font = "Ariel 30", command = self.CToWarp)
        self.CButton.grid(row = 0, column = 1)

        self.connecButton = Button(self.frameBottom, text = "Connect Four", 
            font = "Ariel 30", command = self.connecFour)
        self.connecButton.grid(row = 0, column = 2)

        self.chiButton = Button(self.frameBottom, text = "Chinese Year Calculator", 
            font = "Ariel 30", command = self.chineseCalc)
        self.chiButton.grid(row = 1, column = 0)

        self.grdButton = Button(self.frameBottom, text = "Calculate Weighted Grade Not GUI", 
            font = "Ariel 30", command = self.grdCalc)
        self.grdButton.grid(row = 1, column = 1)

        self.calButton = Button(self.frameBottom, text = "Calendar Month Displayer", 
            font = "Ariel 30", command = self.mnthCalc)
        self.calButton.grid(row = 1, column = 2)

        self.caeButton = Button(self.frameBottom, text = "Caesar Cipher", 
            font = "Ariel 30", command = self.caesarCode)
        self.caeButton.grid(row = 2, column = 0)

        self.cenButton = Button(self.frameBottom, text = "Centaurian Time", 
            font = "Ariel 30", command = self.centaurian)
        self.cenButton.grid(row = 2, column = 1)

        self.gradeMarkII = Button(self.frameBottom, text = "Calculate Weighted Grade GUI Edition", 
            font = "Ariel 30", command = self.guiGrade)
        self.gradeMarkII.grid(row = 2, column = 2)

    def quitButtonAction(self):
        self.window.destroy()
    
    def coinFlipper(self):
        coinFlipGUI.main()

    def CToWarp(self):
        betterCToWarpConv.main()

    def connecFour(self):
        connecFour.main()

    def chineseCalc(self):
        chineseCalCalc.main()

    def grdCalc(self):
        gradeCalc.main()

    def mnthCalc(self):
        calMonthDisplayGUI.main()

    def caesarCode(self):
        caesarCipher.main()

    def centaurian(self):
        centaurianTime.main()

    def guiGrade(self):
        gradeCalcGUI.main()

def main():
    root = Tk()
    root.title("Programs That Start With C")
    om = C(root)
    root.mainloop()

if __name__ == "__main__":
    main()