#Jesse A. Jones
#Version: 2023-08-14.90

#All alphabet category programs imported as well as tkinter.
from tkinter import *
import aPrograms
import bPrograms
import cPrograms
import dPrograms
import ePrograms
import hPrograms
import kPrograms
import mPrograms
import rPrograms
import sPrograms
import tPrograms
import wPrograms
import yPrograms
import vPrograms

"""
This program is a compilation of various side projects 
    I have written over the course of two years or so. 
    These projects are generally time nerd related stuff, 
    nothing too serious. These projects were made for fun.
"""
class Omni(object):
    
    #Creates all necessary buttons to call the appropriate functions.
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

        self.aButton = Button(self.frameBottom, text = "A Programs",
            font = FONT, command = self.aFunc)
        self.aButton.grid(row = 0, column = 0)

        self.bButton = Button(self.frameBottom, text = "B Programs",
            font = FONT, command = self.bFunc)
        self.bButton.grid(row = 0, column = 1)

        self.cButton = Button(self.frameBottom, text = "C Programs",
            font = FONT, command = self.cFunc)
        self.cButton.grid(row = 0, column = 2)

        self.dButton = Button(self.frameBottom, text = "D Programs",
            font = FONT, command = self.dFunc)
        self.dButton.grid(row = 1, column = 0)

        self.eButton = Button(self.frameBottom, text = "E Programs",
            font = FONT, command = self.eFunc)
        self.eButton.grid(row = 1, column = 1)

        self.hButton = Button(self.frameBottom, text = "H Programs",
            font = FONT, command = self.hFunc)
        self.hButton.grid(row = 1, column = 2)

        self.kButton = Button(self.frameBottom, text = "K Programs", 
            font = FONT, command = self.kFunc)
        self.kButton.grid(row = 2, column = 0)

        self.mButton = Button(self.frameBottom, text = "M Programs", 
            font = FONT, command = self.mFunc)
        self.mButton.grid(row = 2, column = 1)

        self.rButton = Button(self.frameBottom, text = "R Programs", 
            font = FONT, command = self.rFunc)
        self.rButton.grid(row = 2, column = 2)

        self.sButton = Button(self.frameBottom, text = "S Programs", 
            font = FONT, command = self.sFunc)
        self.sButton.grid(row = 3, column = 0)

        self.tButton = Button(self.frameBottom, text = "T Programs", 
            font = FONT, command = self.tFunc)
        self.tButton.grid(row = 3, column = 1)

        self.vButton = Button(self.frameBottom, text = "V Programs", 
            font = FONT, command = self.vFunc)
        self.vButton.grid(row = 3, column = 2)

        self.wButton = Button(self.frameBottom, text = "W Programs", 
            font = FONT, command = self.wFunc)
        self.wButton.grid(row = 4, column = 0)

        self.yButton = Button(self.frameBottom, text = "Y Programs", 
            font = FONT, command = self.yFunc)
        self.yButton.grid(row = 4, column = 1)

    #This method quits the main window.
    def quitButtonAction(self):
        self.window.destroy()

    #All methods listed below call the alphabetized category programs.
    def aFunc(self):
        aPrograms.main()

    def bFunc(self): 
        bPrograms.main()

    def cFunc(self): 
        cPrograms.main()

    def dFunc(self):
        dPrograms.main()

    def eFunc(self):
        ePrograms.main()

    def hFunc(self):
        hPrograms.main()

    def kFunc(self):
        kPrograms.main()

    def mFunc(self):
        mPrograms.main()

    def rFunc(self):
        rPrograms.main()

    def sFunc(self):
        sPrograms.main()

    def tFunc(self):
        tPrograms.main()

    def vFunc(self):
        vPrograms.main()

    def wFunc(self):
        wPrograms.main()

    def yFunc(self):
        yPrograms.main()

def main():

    #Sets up initial omniprogram menu.
    root = Tk()
    root.title("Omniprogram Mark II")
    om = Omni(root)
    root.mainloop()

if __name__ == "__main__":
    main()