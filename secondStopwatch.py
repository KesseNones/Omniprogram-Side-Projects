#Jesse A. Jones
#Version: 2023-06-07.24

import time
from tkinter import *

#This class is a program that runs a second counting stopwatch.
class SecStopwatch(object):
    def __init__(self, window = None):
        self.window = window

        self.pauseFlag = True
        self.timeDelta = 0
        self.clickedFlag = 0

        #Holds time control buttons and quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 3)

        #Resets stopwatch.
        self.resetButton = Button(self.frameTop, text = "Reset",
            font = "Ariel 20", command = self.resetButtonAction)
        self.resetButton.grid(row = 0, column = 2)

        #Pauses stopwatch.
        self.startButton = Button(self.frameTop, text = "Pause",
            font = "Ariel 20", command = self.pauseButtonAction)
        self.startButton.grid(row = 0, column = 1)

        #Starts stopwatch.
        self.startButton = Button(self.frameTop, text = "Start",
            font = "Ariel 20", command = self.startButtonAction)
        self.startButton.grid(row = 0, column = 0)

        #Holds time display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays time.
        self.message = Label(self.frameBottom, text = "0.000", font = "Ariel 50", anchor = "w")
        self.message.pack(side = TOP)

    #Pauses stopwatch.
    def pauseButtonAction(self):
        self.pauseFlag = True

        #Saves current time to time delta.
        time = self.stopWatch()
        self.timeDelta = time

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Starts stopwatch.
    def startButtonAction(self):
        if self.pauseFlag:
            self.pauseFlag = False
            self.baseTime = (time.time())
            self.timeChange()

    #Resets stopwatch.
    def resetButtonAction(self):
        self.timeDelta = 0
        self.message["text"] = "0.000"

    #Automatically updates and displays the changed stopwatch time.
    def timeChange(self):
        if self.pauseFlag == False:
            time = self.stopWatch()
            time = round(time, 3)
            time = format(time, ".3f")
            self.message["text"] = time
            self.message.after(1, self.timeChange)

    #Calculates current time elapsed on stopwatch.
    def stopWatch(self):
        currentTime = time.time()
        timeChange = currentTime - self.baseTime
        return timeChange + self.timeDelta

def main():
    root = Tk()
    root.title("Second Stopwatch")
    metric = SecStopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
