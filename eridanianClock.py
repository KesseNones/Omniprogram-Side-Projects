import random
from time import sleep
import time
from tkinter import *
import math
from tkinter import messagebox
import baseConvertClass

class EriTime(object):
    def __init__(self, window = None):
        self.window = window

        self.window.geometry("800x200")

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.descButton = Button(self.frameTop, text = "Description",
            font = "Ariel 20", command = self.showDescription)
        self.descButton.grid(row = 0, column = 1)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "", font = "Times 100", anchor = "w")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def showDescription(self):
        messagebox.showinfo("Eridanian Time Description", 
        "Based on the clock that the Eridanian known as 'Rocky' displayed in the Xenonite hall.")

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        t = time.time() / 2.663
        t = int(t)
        timeString = self.eriConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def toEriSymbols(self, num):
        eriNumArr = ["ℓ", "I", "V", "λ", "+", "∀"]
        numArr = []
        ind = 0
        for el in num:
            numArr.append(el)
        for numb in numArr:
            index = int(numb)
            symbol = eriNumArr[index]
            numArr[ind] = symbol
            ind += 1
        newNum = numArr
        return newNum

    def eriConv(self, unix):
        eriSecTotal = unix % 7776
        base = baseConvertClass.BaseConvert()
        timestringI = base.baseConv(eriSecTotal, 6).zfill(5)
        timestringII = self.toEriSymbols(timestringI)
        #timeString = str(cenHour).zfill(2) + "." + str(cenMin).zfill(2) + "." + str(cenSec).zfill(2)
        return timestringII

def main():
    root = Tk()
    root.title("Eridanian Time")
    metric = EriTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
