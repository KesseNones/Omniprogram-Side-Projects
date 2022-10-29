import random
from time import sleep
import time
from tkinter import *
import math

class MetricDate(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "test", font = "Ariel 75", anchor = "w")
        self.message.pack(side = TOP)
    
        self.metricUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def metricUpdate(self):
        date = self.metric_time()
        date = format(date, ".9f")
        self.message["text"] = date
        self.message.after(1, self.metricUpdate)

    def metric_time(self):
        t = time.time()
        metric_time = ((t * 1.1574074074074074074074074074074) / 100000000) + 4371.952
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
