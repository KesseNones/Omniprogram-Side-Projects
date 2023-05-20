#Jesse A. Jones
#Version: 2023-05-20.08

from tkinter import *
import math
from tkinter import messagebox
import dateHandling

#This class displays a converter that takes in wattage 
#   and gives a Kardaschev Scale Type or vice versa.
class KarCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds power consumption input field, to kardaschev conversion button, 
        #   kardashev type input field, and to power consumption button. 
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
    
        #Power consumption input field.
        self.messageI = Label(self.frameBottom, text = "Enter Power Consumption (W):", font = "Ariel 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.watt = Entry(self.frameBottom, font = "Ariel 20")
        self.watt.grid(row = 0, column = 1)

        #Kardashev conversion button.
        self.karButton = Button(self.frameBottom, text = "Convert to Kardeshev", 
            font = "Ariel 20", command = self.wToKar)
        self.karButton.grid(row = 1, column = 0)

        #Classic Kardashev scale output.
        self.clkOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", wraplength = 666)
        self.clkOutput.grid(row = 2, column = 1)

        #Contemporary kardashev scale output.
        self.kOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.kOutput.grid(row = 3, column = 1)

        #Kardaschev Scale input field.
        self.messageII = Label(self.frameBottom, text = "Enter Kardeshev Type: ", font = "Ariel 20", anchor = "w")
        self.messageII.grid(row = 4, column = 0)
        self.kar = Entry(self.frameBottom, font = "Ariel 20")
        self.kar.grid(row = 4, column = 1)

        #Converts Kardaschev scale to power consumption when pressed.
        self.wButton = Button(self.frameBottom, text = "Convert to Power Consumption (W)", 
            font = "Ariel 20", command = self.karToW)
        self.wButton.grid(row = 5, column = 0)

        #Displays classical Kardaschev scale output.
        self.clkOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 20", wraplength = 666)
        self.clkOutputII.grid(row = 5, column = 1)

        #Power consumption output.
        self.wOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.wOutput.grid(row = 6, column = 1)

        self.inputParse = dateHandling.GetDate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls function to convert power consumption 
    #   to Kardaschev scale and then displays the result.
    def wToKar(self):
        retArr = self.karCalc(True)
        self.clkOutput["text"] = retArr[0]
        self.kOutput["text"] = retArr[1]

    #Calls function to convert Kardaschev scale value 
    #   to power consumption and displays it.
    def karToW(self):
        retArr = self.karCalc(False)
        self.clkOutputII["text"] = retArr[0]
        self.wOutput["text"] = retArr[1]

    #Given a power input it calculates the classical Kardashev scale value.
    def karClassStrFind(self, power):
        clsStr = None
        if power < 1e+6:
            clsStr = "Too Primitive for Classical Scale"
        elif 1e+16 > power >= 1e+6:
            clsStr = "Type: Zero"
        elif 1e+26 > power >= 1e+16:
            clsStr = "Type: I"
        elif 1e+36 > power >= 1e+26:
            clsStr = "Type: II"
        elif 1e+46 > power >= 1e+36:
            clsStr = "Type: III"
        else:
            clsStr = "Too Advanced for Classical Scale"
        return clsStr

    #Converts kardashev to power consumption or vice versa.
    def karCalc(self, isFindingKardashev):
        if isFindingKardashev:
            #Fetches input power consumption.
            p = self.inputParse.getGeneral(self.watt.get())
            if p <= 0:
                p = 1e-66

            #Calculates Kardashev scale from power.
            k = (math.log10(p) - 6)/10
            k = round(k, 3)
            return [self.karClassStrFind(p), f"Type: {k}"]
        else:
            #Fetches Kardashev scale input.
            k = self.inputParse.getGeneral(self.kar.get())

            #Edge case for when power's too much.
            if k > 30.221:
                return ["UNLIMITED POWER!!!", "∞"]
            else:
                #Finds power from Kardaschev scale and returns it.
                p = 10 ** (((k) * 10) + 6)
                return [self.karClassStrFind(p), f"{p} Watts"]

def main():
    root = Tk()
    root.title("Kardeshev Calculator")
    star = KarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
