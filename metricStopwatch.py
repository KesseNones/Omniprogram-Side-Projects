#Jesse A. Jones
#Version: 2023-05-25.90

import time
from tkinter import *
import math

#This class displays a metric stopwatch.
#This watch uses milicycles as the time unit or 1000ths of a day.
class MetricStopwatch(object):
    def __init__(self, window = None):
        self.window = window

        self.pauseFlag = True

        self.timeDelta = 0
        self.clickedPause = False
        self.baseTime = 0

        #Holds quit, reset, pause, and start buttons.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 3)

        #Resets stopwatch when pressed.
        self.resetButton = Button(self.frameTop, text = "Reset",
            font = "Ariel 20", command = self.resetButtonAction)
        self.resetButton.grid(row = 0, column = 2)

        #Pauses stopwatch when pressed.
        self.startButton = Button(self.frameTop, text = "Pause",
            font = "Ariel 20", command = self.pauseButtonAction)
        self.startButton.grid(row = 0, column = 1)

        #Starts stopwatch when pressed.
        self.startButton = Button(self.frameTop, text = "Start",
            font = "Ariel 20", command = self.startButtonAction)
        self.startButton.grid(row = 0, column = 0)

        #Holds time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays time output.
        self.message = Label(self.frameBottom, text = "0.000000", font = "Ariel 50", anchor = "w")
        self.message.pack(side = TOP)

    #Pauses stopwatch.
    def pauseButtonAction(self):
        #If not paused, pauses stopwatch and saves time delta.
        if self.clickedPause == False:
            self.pauseFlag = True
            time = self.stopWatch()
            self.timeDelta = time
            self.clickedPause = True

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Starts stopwatch when called.
    def startButtonAction(self):
        #If the stopwatch is paused, it unpauses and sets 
        #   a new base time based on the unix time stamp.
        if self.pauseFlag:
            self.pauseFlag = False
            self.clickedPause = False
            self.baseTime = (time.time())
            self.timeChange()

    #Resets time delta and displays all zeroes on the stopwatch.
    def resetButtonAction(self):
        self.timeDelta = 0
        self.message["text"] = "0.000000"

    #If the stopwatch isn't paused this function loops 
    #   and displays the updated time.
    def timeChange(self):
        if self.pauseFlag == False:
            time = self.stopWatch()
            time = format(time, ".6f")
            self.message["text"] = time
            self.message.after(1, self.timeChange)

    #Fetches current time stamp, subtracts from base time and returns 
    #   the result with time delta added 
    #   from previous paused iterations of stopwatch.
    def stopWatch(self):
        currentTime = (time.time())
        timeChange = currentTime - self.baseTime
        tim = self.metric_time(timeChange)
        return tim + self.timeDelta

    #Calculates metric time based on input unix time stamp.
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
