#Jesse A. Jones
#Version: 2022-12-28.1

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
    def __init__(self, window = None):
        self.window = window

        self.soundsAllowed = False

        #Top frame contains quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 30", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame contains all buttons 
        #   for programs that start with the letter C.
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

        self.grdButton = Button(self.frameBottom, text = "Calculate Weighted Grade", 
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

    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()
    
    #Displays the result of a coin flip.
    def coinFlipper(self):                      #DONE (maybe add head and tails counter later)
        coinFlipGUI.main()

    #Converts a multiple of the speed of light 
    #   to the Star Trek TNG Warp Drive Scale.
    def CToWarp(self):                          #HERE
        betterCToWarpConv.main()

    #Runs a GUI connect four game with several bells and wistles. 
    #   The sound is currently a bit broken and needs to be fixed.
    def connecFour(self):
        connecFour.main()

    #Converts a year to the equivalent year in the Chinese Calendar.
    def chineseCalc(self):
        chineseCalCalc.main()

    #Calculates a grade from weighted grade portions. This is not a GUI.
    def grdCalc(self):
        gradeCalc.main()

    #Displays a calendar month page for a given year and month.
    #   Is kind of garbage and could use improving.
    def mnthCalc(self):
        calMonthDisplayGUI.main()

    #Performs the classic Caeser Cipher encrption or decryption on a string.
    def caesarCode(self):
        caesarCipher.main()

    #Displays the present Centaurian time that m.i.b Headquarters uses.
    def centaurian(self):
        centaurianTime.main()

    #Calculates a grade from weighted grade portions.
    def guiGrade(self):
        gradeCalcGUI.main()

def main():
    root = Tk()
    root.title("Programs That Start With C")
    om = C(root)
    root.mainloop()

if __name__ == "__main__":
    main()