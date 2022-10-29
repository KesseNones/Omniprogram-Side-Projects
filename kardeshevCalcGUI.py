from tkinter import *
import math
from tkinter import messagebox

class KarCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
    
        self.messageI = Label(self.frameBottom, text = "Enter Power Consumption (W):", font = "Ariel 45", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.watt = Entry(self.frameBottom, font = "Times 55")
        self.watt.grid(row = 0, column = 1)

        self.karButton = Button(self.frameBottom, text = "Convert to Kardeshev", 
            font = "Ariel 45", command = self.wToKar)
        self.karButton.grid(row = 1, column = 0)

        self.clkOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 45", wraplength = 666)
        self.clkOutput.grid(row = 2, column = 1)

        self.kOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 45")
        self.kOutput.grid(row = 3, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Kardeshev Type: ", font = "Ariel 45", anchor = "w")
        self.messageII.grid(row = 4, column = 0)

        self.kar = Entry(self.frameBottom, font = "Times 55")
        self.kar.grid(row = 4, column = 1)

        self.wButton = Button(self.frameBottom, text = "Convert to Power Consumption (W)", 
            font = "Ariel 45", command = self.karToW)
        self.wButton.grid(row = 5, column = 0)

        self.clkOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 45", wraplength = 666)
        self.clkOutputII.grid(row = 5, column = 1)

        self.wOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 45")
        self.wOutput.grid(row = 6, column = 1)

    def quitButtonAction(self):
        self.window.destroy()

    def wToKar(self):
        self.karCalc(1)
        self.clkOutput["text"] = self.karClassic
        self.kOutput["text"] = self.karDec

    def karToW(self):
        self.karCalc(2)
        self.clkOutputII["text"] = self.karClassic
        self.wOutput["text"] = self.pow

    def karCalc(self, ch):
        if ch == 1:
            p = self.watt.get()
            if p == "":
                messagebox.showerror("Empty Entry Error", "You have to enter something for the calculation to work!")
                return
            p = float(p)
            if p <= 0:
                messagebox.showerror("Out of Bounds Error", "Watts must be larger than zero!")
                return
            k = (math.log10(p) - 6)/10
            k = round(k, 3)
            if p < 1e+6:
                Cl = "Too Primitive for Classical Scale"
            if 1e+16 > p >= 1e+6:
                Cl = "Type: Zero"
            if 1e+26 > p >= 1e+16:
                Cl = "Type: I"
            if 1e+36 > p >= 1e+26:
                Cl = "Type: II"
            if 1e+46 > p >= 1e+36:
                Cl = "Type: III"
            if p >= 1e+46:
                Cl = "Too Advanced for Classical Scale"
            self.karClassic = Cl
            self.karDec = "Type: " + str(k)
            return
        if ch == 2:
            k = self.kar.get()
            if k == "":
                messagebox.showerror("Empty Entry Error", "Something must be in the entry for the calculation to work!")
            k = float(k)
            if k > 30.221:
                self.karClassic = "UNLIMITED POWER!!!"
                self.pow = "∞"
                return
            p = 10 ** (((k) * 10) + 6)
            if p < 1e+6:
                Cl = "Too Primitive for Classical Scale"
            if 1e+16 > p >= 1e+6:
                Cl = "Type: Zero"
            if 1e+26 > p >= 1e+16:
                Cl = "Type: I"
            if 1e+36 > p >= 1e+26:
                Cl = "Type: II"
            if 1e+46 > p >= 1e+36:
                Cl = "Type: III"
            if p >= 1e+46:
                Cl = "Too Advanced for Classical Scale"
            self.karClassic = Cl
            self.pow = p, "Watts"
            return

def main():
    root = Tk()
    root.title("Kardeshev Calculator")
    star = KarCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
