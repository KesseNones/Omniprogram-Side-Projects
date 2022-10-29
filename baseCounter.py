import time
from tkinter import *
import math
import baseConvertClass

class BaseStopwatch(object):
    def __init__(self, window = None):
        self.window = window

        self.pauseFlag = True

        self.timeDelta = 0
        self.clickedFlag = 0

        self.frameTop = Frame(self.window)
        self.frameTop.grid(row = 0, column = 0)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 3)

        self.resetButton = Button(self.frameTop, text = "Reset",
            font = "Ariel 20", command = self.resetButtonAction)
        self.resetButton.grid(row = 0, column = 2)

        self.startButton = Button(self.frameTop, text = "Pause",
            font = "Ariel 20", command = self.pauseButtonAction)
        self.startButton.grid(row = 0, column = 1)

        self.startButton = Button(self.frameTop, text = "Start",
            font = "Ariel 20", command = self.startButtonAction)
        self.startButton.grid(row = 0, column = 0)

        self.frameMiddle = Frame(self.window)
        self.frameMiddle.grid(row = 1, column = 0)

        self.baseScalar = Scale(self.frameMiddle, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 400, 
            label = "Base:", font = "Times 30", command = self.sliderNumber)
        self.baseScalar.grid(row = 0, column = 0)

        self.speedScalar = Scale(self.frameMiddle, orient = HORIZONTAL, 
            from_ = 0, to = 4, length = 400, 
            label = "Speed Factor", font = "Times 30", command = self.decimalNumber)
        self.speedScalar.grid(row = 1, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.grid(row = 2, column = 0)

        self.message = Label(self.frameBottom, text = "0", font = "Roboto 85", anchor = "w")
        self.message.pack(side = TOP)

        self.base = 2
        self.decCount = 0

    def sliderNumber(self, base):
        self.base = int(base)

    def decimalNumber(self, num):
        self.decCount = int(num)

    def convToOtherBase(self, time):
        baseConv = baseConvertClass.BaseConvert()
        base = self.base
        convTime = baseConv.tenToOtherBase(time, base)
        return convTime

    def pauseButtonAction(self):
        self.pauseFlag = True
        time = self.stopWatch()
        self.timeDelta = time

    def quitButtonAction(self):
        self.window.destroy()

    def startButtonAction(self):
        if self.pauseFlag:
            self.pauseFlag = False
            self.baseTime = (time.time())
            self.timeChange()

    def resetButtonAction(self):
        self.timeDelta = 0
        self.message["text"] = "0"

    def timeChange(self):
        if self.pauseFlag == False:
            time = self.stopWatch()
            time = int(time * (self.base ** (self.decCount)))
            convertedTime = self.convToOtherBase(time)
            self.message["text"] = convertedTime
            self.message.after(1, self.timeChange)

    def stopWatch(self):
        currentTime = (time.time())
        timeChange = currentTime - self.baseTime
        return timeChange + self.timeDelta

def main():
    root = Tk()
    root.title("Different Base Counting Stopwatch")
    metric = BaseStopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
