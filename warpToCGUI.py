#Jesse A. Jones
#Version: 2024-01-02.07

from tkinter import *
import dateHandling

import decimal
from decimal import Decimal

decimal.getcontext().prec = 1000

#This class takes in an input Warp Factor 
#   and returns the multiple of light speed it correlates to.
class WarpToCConv(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds warp factor input, conversion button, and C multiple output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        FONT = "Ariel 20"

        #Warp Factor input field.
        self.message = Label(self.frameBottom, text = "Enter Warp Factor:", font = FONT, anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.warp = Entry(self.frameBottom, font = FONT)
        self.warp.grid(row = 1, column = 0)

        #Converts Warp Factor to C multiple when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to C Multiple", 
            font = FONT, command = self.warpy)
        self.convButton.grid(row = 2, column = 0)

        #Displays converted to C multiple.
        self.cOutput = Label(self.frameBottom, text = "", font = FONT)
        self.cOutput.grid(row = 3, column = 0)

        self.parse = dateHandling.GetDate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Caclulates C multiple and displays result.
    def warpy(self) -> None:
        #Parses input warp factor.
        warpFac: Decimal = None
        try: 
            warpFac = Decimal(self.warp.get())
        except decimal.InvalidOperation:
            warpFac = Decimal(0)

        #Calculates C and shows it.
        speed = self.warpToC(warpFac)
        self.cOutput["text"] = "The speed is: " + str(speed) + " C"

    #Calculates C multiple based on warp factor and returns it.
    def warpToC(self, warpFac: Decimal):
        #Invalid warp factor case.
        if warpFac > Decimal(10) or warpFac < Decimal(0):
            return "[INVALID WARP FACTOR]"
        
        #Caclulates C from warp factors in normal range.
        if Decimal(0) <= warpFac <= Decimal(9):
            C = warpFac ** Decimal(10/3)
            C = float(round(C, 3))

        #Calculates C for warp factors of threshold case.
        elif Decimal(10) > warpFac > Decimal(9):
            C = (warpFac ** Decimal(10/3)) / (warpFac - Decimal(10)) * Decimal(-1)
            C = float(round(C, 3))
        else:
            C = "INFINITY"
        
        return C

def main():
    root = Tk()
    root.title("Warp Factor to C Multiple Converter")
    coin = WarpToCConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
