from tkinter import *
import math
from math import log

class tempConverter(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter Temperature Units:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.temp = Entry(self.frameBottom, font = "Times 50")
        self.temp.grid(row = 0, column = 1)

        print(self.temp)

        self.convButtonI = Button(self.frameBottom, text = "Fahrenheit to Celcius", 
            font = "Ariel 45", command = self.FtoC)
        self.convButtonI.grid(row = 1, column = 0)

        self.convButtonII = Button(self.frameBottom, text = "Celcius to Fahrenheit", 
            font = "Ariel 45", command = self.CtoF)
        self.convButtonII.grid(row = 1, column = 1)

        self.convButtonIII = Button(self.frameBottom, text = "Fahrenheit to Kelvin", 
            font = "Ariel 45", command = self.FtoK)
        self.convButtonIII.grid(row = 2, column = 0)

        self.convButtonIV = Button(self.frameBottom, text = "Celcius to Kelvin", 
            font = "Ariel 45", command = self.CtoK)
        self.convButtonIV.grid(row = 2, column = 1)

        self.convButtonV = Button(self.frameBottom, text = "Kelvin to Fahrenheit", 
            font = "Ariel 45", command = self.KtoF)
        self.convButtonV.grid(row = 3, column = 0)

        self.convButtonVI = Button(self.frameBottom, text = "Kelvin to Celcius", 
            font = "Ariel 45", command = self.KtoC)
        self.convButtonVI.grid(row = 3, column = 1)

        self.message = Label(self.frameBottom, text = "Converted Temperature:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 4, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 50", justify = LEFT, wraplength = 600 )
        self.tOutput.grid(row = 4, column = 1)

        self.impossible = Label(self.frameBottom, text = "", 
            font = "Ariel 50")
        self.impossible.grid(row = 5, column = 1)

    def FtoC(self):
        conv = self.convert(1)
        if conv < -273.15:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " °C"

    def CtoF(self):
        conv = self.convert(2)
        if conv < -459.66999999999996:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " °F"

    def FtoK(self):
        conv = self.convert(3)
        if conv < 0:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " Kelvin"

    def CtoK(self):
        conv = self.convert(4)
        if conv < 0:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " Kelvin"

    def KtoF(self):
        conv = self.convert(5)
        if float(self.temp.get()) < 0:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " °F"
    
    def KtoC(self):
        conv = self.convert(6)
        if float(self.temp.get()) < 0:
            self.impossible["text"] = "Impossible Temperature"
        self.tOutput["text"] = str(conv) + " °C"

    def quitButtonAction(self):
        self.window.destroy()

    def convert(self, T):
        if T == 1:
            F = float(self.temp.get())
            C = (F - 32) / 1.8
            C = round(C, 3)
            return C
        if T == 2:
            C = float(self.temp.get())
            F = (C * 1.8) + 32
            F = round(F, 3)
            return F
        if T == 3:
            F = float(self.temp.get())
            K = ((F - 32) / 1.8) + 273.15
            K = round(K, 3)
            return K
        if T == 4:
            C = float(self.temp.get())
            K = C + 273.15
            K = round(K, 3)
            return K
        if T == 5:
            K = float(self.temp.get())
            F = ((K - 273.15) * 1.8) + 32
            F = round(F, 3)
            return F
        if T == 6:
            K = float(self.temp.get())
            C = K - 273.15
            C = round(C, 3)
            return C

def main():
    root = Tk()
    root.title("Temperature Converter")
    temp = tempConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
