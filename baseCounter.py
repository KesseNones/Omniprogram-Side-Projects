#Jesse A. Jones
#Version: 2022-12-22.9

import time
from tkinter import *
import baseConvertClass

#This class contains members and methods necessary 
#   for a base stopwatch to exist.
#The base stopwatch counts the number 
#   of seconds since the arbitrary start point in base 2 to 36. 
class BaseStopwatch(object):
    def __init__(self, window = None):
        self.window = window

        #Tracks wheather stopwatch is paused or not.
        self.pauseFlag = True

        #Tracks time delta.
        self.timeDelta = 0

        #Top frame contains quit button, reset button, 
        #   start button, and pause button.
        self.frameTop = Frame(self.window)
        self.frameTop.grid(row = 0, column = 0)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 3)

        #Reset button.
        self.resetButton = Button(self.frameTop, text = "Reset",
            font = "Ariel 20", command = self.resetButtonAction)
        self.resetButton.grid(row = 0, column = 2)

        #Pause button.
        self.startButton = Button(self.frameTop, text = "Pause",
            font = "Ariel 20", command = self.pauseButtonAction)
        self.startButton.grid(row = 0, column = 1)

        #Start button.
        self.startButton = Button(self.frameTop, text = "Start",
            font = "Ariel 20", command = self.startButtonAction)
        self.startButton.grid(row = 0, column = 0)

        #Middle frame contains base selector and time distortion factor.
        self.frameMiddle = Frame(self.window)
        self.frameMiddle.grid(row = 1, column = 0)

        #Base selector.
        self.baseScalar = Scale(self.frameMiddle, orient = HORIZONTAL, 
            from_ = 2, to = 36, length = 400, 
            label = "Base:", font = "Times 30", command = self.sliderNumber)
        self.baseScalar.grid(row = 0, column = 0)

        #Precision slider.
        self.precScalar = Scale(self.frameMiddle, orient = HORIZONTAL, 
            from_ = 0, to = 5, length = 400, 
            label = "Precision:", font = "Times 30", command = self.decimalNumber)
        self.precScalar.grid(row = 1, column = 0)

        #Bottom frame contains time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.grid(row = 2, column = 0)

        #Time output.
        self.message = Entry(self.frameBottom, font = "Times 50")
        self.message.pack(side = TOP)
        self.message.insert(0, "0")

        #Tracks current base and precision.
        self.base = 2
        self.decCount = 0

        self.baseConv = baseConvertClass.BaseConvert()

    #Sets instance variable of base from user slider input.
    def sliderNumber(self, base):
        self.base = int(base)

    #Sets time distortion instance variable.
    def decimalNumber(self, num):
        self.decCount = int(num)

    #Converts seconds elapsed to desired base.
    def convToOtherBase(self, time):
        base = self.base
        convTime = self.baseConv.tenToOtherBase(time, base)
        return convTime

    #Performs the function of pausing the stopwatch.
    def pauseButtonAction(self):
        if self.pauseFlag == False:
            self.pauseFlag = True
            time = self.stopWatch()
            self.timeDelta = time

    #Quits the program.
    def quitButtonAction(self):
        self.window.destroy()

    #Starts the stopwatch.
    def startButtonAction(self):
        if self.pauseFlag:
            self.pauseFlag = False
            self.baseTime = (time.time())
            self.timeChange()

    #Resets the stopwatch time.
    def resetButtonAction(self):
        self.timeDelta = 0
        self.baseTime = time.time()
        self.message.delete(0, "end")
        self.message.insert(0, "0" + ('.' * (self.decCount > 0)) + ('0' * self.decCount))

    #Live updates the time while the stopwatch is not paused.
    def timeChange(self):
        if self.pauseFlag == False:
            #Fetches current time delta and shifts scale by input precision.
            time = self.stopWatch()
            time = int(time * (self.base ** (self.decCount)))

            #Converts time delta to base in range 2 to 36.
            convertedTime = self.convToOtherBase(time)

            #Uses python string magic to place a decimal in 
            #   the appropriate place of the count, indicating precision.
            if (self.decCount > 0):
                integer = convertedTime[0:(len(convertedTime) - (self.decCount))]
                decimal = convertedTime[(len(convertedTime) - (self.decCount)):len(convertedTime)]
                convertedTime = integer.zfill(1) + '.' + decimal.zfill(self.decCount)

            #Displays time to user.
            self.message.delete(0, "end")
            self.message.insert(0, convertedTime)

            #Uses recursive call.
            self.message.after(1, self.timeChange)

    #Fetches current timestamp and calculates present time delta.
    def stopWatch(self):
        currentTime = (time.time())
        timeChange = currentTime - self.baseTime
        return timeChange + self.timeDelta

def main():
    root = Tk()
    root.title("Base Counting Stopwatch")
    metric = BaseStopwatch(root)
    root.mainloop()

if __name__ == "__main__":
    main()
