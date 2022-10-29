import random
from time import sleep
import time
from tkinter import *
import math
from tkinter import messagebox
import baseConvertClass

class EruTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        # self.descButton = Button(self.frameTop, text = "Description",
        #     font = "Ariel 20", command = self.showDescription)
        # self.descButton.grid(row = 0, column = 1)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "test", font = "Times 100", anchor = "w")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def showDescription(self):
        messagebox.showinfo("Centaurian Time Description", 
        "A time system introduced and imposed by the alien twins Bweryang and Bob at MiB headquarters. It's a 37 hour day; one either adapts to it or has a phsychotic episode.")

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        #88400
        t = time.time()
        timeString = self.eruConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def eruConv(self, unix):
        eruSecTotal = unix % 88400
        twelfth = 88400 / 12
        onefortyfourth = 88400 / 144
        oneseventeentwentyeigth = 88400 / 1728
        onetwentyK = 88400 / 20736
        onetwofiftyK = 88400 / 248832

        twelfths = eruSecTotal // twelfth
        reducedEruSecI = eruSecTotal % twelfth
        onefortyfourths = reducedEruSecI // onefortyfourth
        reducedEruSecII = reducedEruSecI % onefortyfourth
        oneseventeentwentyeigths = reducedEruSecII // oneseventeentwentyeigth
        reducedEruSecIII = reducedEruSecII % oneseventeentwentyeigth
        onetwentyKs = reducedEruSecIII // onetwentyK
        reducedEruSecIV = reducedEruSecIII % onetwentyK
        onetwofiftyKs = reducedEruSecIV // onetwofiftyK

        base = baseConvertClass.BaseConvert()
        firstPlace = base.baseConv(int(twelfths), 12)
        secondPlace = base.baseConv(int(onefortyfourths), 12)
        thirdPlace = base.baseConv(int(oneseventeentwentyeigths), 12)
        fourthPlace = base.baseConv(int(onetwentyKs), 12)
        fifthPlace = base.baseConv(int(onetwofiftyKs), 12)

        timeString = firstPlace + "." + secondPlace + thirdPlace + fourthPlace + fifthPlace
        return timeString
        # eruDec = eruSecTotal / 88400
        # return format(round(eruDec * 1000, 3), ".3f")

def main():
    root = Tk()
    root.title("Eru'varian Clock")
    metric = EruTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
