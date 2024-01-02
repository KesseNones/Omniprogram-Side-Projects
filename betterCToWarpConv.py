#Jesse A. Jones
#Version: 2024-01-02.10

from tkinter import *
from math import inf, log10
from math import ceil
import dateHandling

import decimal
from decimal import Decimal

decimal.getcontext().prec = 360

#Has the methods and members necessary to convert a multiple 
#   of the speed of light to a warp factor in the Star Trek TNG scale.
#Essentially, from 1 to about 1516 it's a simple polynomial conversion, 
#   but past 1516 C, 
#   it becomes an asymptotic growth reaching warp 10 at infinity C.
#This program is called betterCToWarpConv.py because there was 
#   a previous version that performed this same task that was a lot worse.
class CToWConv(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds C multiple entry, conversion button, and warp factor output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #C multiple input.
        self.message = Label(self.frameBottom, text = "Enter C Multiple:", font = "Times 30", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.cSpeed = Entry(self.frameBottom, font = "Times 30")
        self.cSpeed.grid(row = 1, column = 0)

        #Conversion button.
        self.convButton = Button(self.frameBottom, text = "Convert to Warp Factor", 
            font = "Times 30", command = self.antiWarpy)
        self.convButton.grid(row = 2, column = 0)

        #Warp factor output.
        self.wOutput = Entry(self.frameBottom, font = "Times 30", justify = LEFT)
        self.wOutput.grid(row = 3, column = 0)

        self.parse = dateHandling.GetDate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Displays the derived warp factor to the user.
    def antiWarpy(self):
        #Displays initial loading message to user.
        self.wOutput.delete(0, "end")
        self.wOutput.insert(0, "Loading...")
        self.wOutput.update()

        #Parses c multiple input.
        speed = self.parse.getGeneral(self.cSpeed.get())

        #Converts C multiple to Warp Factor and displays it to user.
        warpFac = self.cToWarp(speed)
        self.wOutput.delete(0, "end")
        self.wOutput.insert(0, f"Warp Factor: {warpFac}")

    #Converts warp factor to speed of light multiple.
    def warpToC(self, warp: Decimal) -> Decimal:
        if (warp <= 9):
            C = warp ** Decimal(10/3)
        else:
            C = ((warp ** Decimal(10/3))/(warp - Decimal(10))) * Decimal(-1)
        return C
    
    #Converts light speed multiple to warp factor.
    def cToWarp(self, speed: float) -> Decimal:
        #If speed is infinite, warp factor is 10.
        if (speed == inf):
            return 10

        div = 1

        #Calculates warp factor with constant time mathematics 
        #   if the speed of light multiple is less than 1516.4 or so.
        if (speed <= 1516.3811070048380994924114249569):
            warp = Decimal(speed) ** Decimal(3/10)
            return warp

        #Calculates necessary logarithims for converting 
        #   to a warp factor for a speed larger than 1516.4.
        warp = Decimal(9)
        expectedSpeed = round(log10(speed), 4)
        currentSpeed = round(log10(float(self.warpToC(warp))), 4)

        #Loop runs until sufficiently precise warp factor has been found.
        while (True):
            #Place represents the value of a particular decimal place, 
            #   ranging from 0 to 9. 
            #   Div represents what decimal place is being interfaced with.
            #For example, 9.52 would have div of 100 and place of 2.
            place = 0
            div *= 10

            #Calculates warp factor decimal place value. 
            while (place < 9):
                #Increases warp factor by 1/div.
                warp += Decimal(1 / div)

                #Rounds to desired place to avoid floating point messyness.
                warp = round(warp, int(ceil(log10(div))))

                #Calculates current speed from current warp factor.
                currentSpeed = round(log10(float(self.warpToC(warp))), 4)

                #If the exactly correct warp factor is found, 
                #   return the warp factor.
                if (currentSpeed == expectedSpeed):
                    return warp
                
                #If the warp factor becomes too great, 
                #   decrease by 1/div and quit this sub loop.
                if (currentSpeed > expectedSpeed):
                    warp -= Decimal(1 / div)
                    warp = round(warp, int(ceil(log10(div))))
                    break

                place += 1

def main():
    root = Tk()
    root.title("C Multiple to Warp Factor Converter")
    coin = CToWConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
