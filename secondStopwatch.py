import random
from time import sleep
import time
from tkinter import *
import math

class SecStopwatch(object):
    def __init__(self, window = None):
        self.window = window

        self.pauseFlag = True

        self.timeDelta = 0
        self.clickedFlag = 0

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

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

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "0.000", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)

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
        self.message["text"] = "0.000"

    def timeChange(self):
        if self.pauseFlag == False:
            time = self.stopWatch()
            time = round(time, 3)
            time = format(time, ".3f")
            self.message["text"] = time
            self.message.after(1, self.timeChange)

    def stopWatch(self):
        currentTime = (time.time())
        timeChange = currentTime - self.baseTime
        return timeChange + self.timeDelta

def main():
    root = Tk()
    root.title("Second Stopwatch")
    metric = SecStopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
