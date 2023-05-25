#Jesse A. Jones
#Version: 2023-05-25.83

import time
from tkinter import *
import math

#This class displays the live metric date 
#   that is currently occuring in kilocycles.
#   One kilocycle is 1000 cycles each of which
#   equates to one Earth day.
class MetricDate(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds time display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays metric time.
        self.message = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.message.pack(side = TOP)
    
        #Starts recursive loop to keep updating the metric time.
        self.metricUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates metric date and displays it in the proper format.
    def metricUpdate(self):
        self.message["text"] = format(self.metric_time(), ".9f")
        self.message.after(1, self.metricUpdate)

    #Calculates the current metric date based on the current unix time stamp.
    def metric_time(self):
        #Fetches current unix time.
        t = time.time()

        #Converts to current metric time stamp raw number.
        metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
        
        #Truncates number to display 9 decimal places without rounding.
        rounderI = metric_time * 1000000000
        rounderII = math.trunc(rounderI)
        rounderIII = rounderII / 1000000000
        return rounderIII

def main():
    root = Tk()
    root.title("Metric Date Live!")
    metric = MetricDate(root)
    root.mainloop()

if __name__ == "__main__":
    main()
