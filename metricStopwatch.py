import random
from time import sleep
import time
from tkinter import *
import math

class MetricStopwatch(object):
    def __init__(self, window = None):
        self.window = window

        self.pauseFlag = True

        self.timeDelta = 0
        self.clickedPause = False
        self.baseTime = 0

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

        self.message = Label(self.frameBottom, text = "0.000000", font = "Times 75", anchor = "w")
        self.message.pack(side = TOP)

    def pauseButtonAction(self):
        if self.clickedPause == False:
            self.pauseFlag = True
            time = self.stopWatch()
            self.timeDelta = time
            self.clickedPause = True

    def quitButtonAction(self):
        self.window.destroy()

    def startButtonAction(self):
        if self.pauseFlag:
            self.pauseFlag = False
            self.clickedPause = False
            self.baseTime = (time.time())
            self.timeChange()

    def resetButtonAction(self):
        self.timeDelta = 0
        self.message["text"] = "0.000000"

    def timeChange(self):
        if self.pauseFlag == False:
            time = self.stopWatch()
            time = format(time, ".6f")
            self.message["text"] = time
            self.message.after(1, self.timeChange)

    def stopWatch(self):
        currentTime = (time.time())
        timeChange = currentTime - self.baseTime
        tim = self.metric_time(timeChange)
        return tim + self.timeDelta

    def metric_time(self, t):
        metric_time = ((t * 1.1574074074074074074074074074074) / 100)
        rounderI = metric_time * 1000000
        rounderII = math.trunc(rounderI)
        rounderIII = rounderII / 1000000
        return rounderIII

def main():
    root = Tk()
    root.title("Metric Stopwatch")
    metric = MetricStopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
