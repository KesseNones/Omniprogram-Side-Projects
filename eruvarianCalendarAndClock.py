import random
from time import sleep
import time
from tkinter import *
import math
from tkinter import messagebox
import baseConvertClass

class EruCal(object):
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

        self.message = Label(self.frameBottom, text = "", font = "Times 100", anchor = "w")
        self.message.grid(row = 0, column = 0)
        
        self.messageII = Label(self.frameBottom, text = "", font = "Times 100", anchor = "w")
        self.messageII.grid(row = 1, column = 0)

        self.messageIII = Label(self.frameBottom, text = "Sub-Age: 281171", font = "Times 100", anchor = "w")
        self.messageIII.grid(row = 2, column = 0)
    
        self.cOutputIII = Label(self.frameBottom, text = "Age of Balance", 
            font = "Times 100")
        self.cOutputIII.grid(row = 3, column = 0)

        self.timeUpdate()

    # def showDescription(self):
    #     messagebox.showinfo("Centaurian Time Description", 
    #     "A time system introduced and imposed by the alien twins Bweryang and Bob at MiB headquarters. It's a 37 hour day; one either adapts to it or has a phsychotic episode.")

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        #88400
        t = time.time()
        timeString = self.eruConv(t)
        self.message["text"] = timeString
        self.messageII["text"] = self.otherTimeString
        self.message.after(1, self.timeUpdate)

    def eruConv(self, unix):
        eruYearsElapsed = unix // 31824000
        eruYear = 5376 + eruYearsElapsed
        secondsOfCurrentYear = unix % 31824000
        lunarCycle = secondsOfCurrentYear // 2652000
        secondsOfCurrentLunarCycle = secondsOfCurrentYear % 2652000
        eruDay = secondsOfCurrentLunarCycle // 88400
        eruWeekdayNum = int(eruDay) % 6
        weekArr = ["Torfung", "Solfung", "Varfung", "Melfung", "Orivfung", "T'rarfung"]
        eruWeekday =  weekArr[eruWeekdayNum]

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

        trueEruYear = base.baseConv(int(eruYear), 12)
        trueEruLunarCycle = base.baseConv(int(lunarCycle), 12)
        trueEruDay = base.baseConv(int(eruDay), 12)

        self.otherTimeString = trueEruYear + "-" + trueEruLunarCycle + "-" + trueEruDay.zfill(2) + ", " + eruWeekday
        timeString = firstPlace + "." + secondPlace + thirdPlace + fourthPlace + fifthPlace
        return timeString
        # eruDec = eruSecTotal / 88400
        # return format(round(eruDec * 1000, 3), ".3f")

def main():
    root = Tk()
    root.title("Eru'varian Clock and Calendar")
    metric = EruCal(root)
    root.mainloop()

if __name__ == "__main__":
    main()
