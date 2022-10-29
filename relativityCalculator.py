from tkinter import *
import math
import metricTimeToStandard

class RelCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageTime = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.messageTime.grid(row = 5, column = 0)

        self.messageTimeSeg = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.messageTimeSeg.grid(row = 6, column = 0)

        self.messageTimeSegOther = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.messageTimeSegOther.grid(row = 7, column = 0)

        self.messageI = Label(self.frameBottom, text = "Enter Velocity (m/s)", font = "Ariel 55")
        self.messageI.grid(row = 0, column = 0)

        self.speen = Entry(self.frameBottom, font = "Times 45")
        self.speen.grid(row = 1, column = 0)

        self.messageII = Label(self.frameBottom, text = "Enter Distance (m) ", font = "Ariel 55")
        self.messageII.grid(row = 2, column = 0)

        self.dist = Entry(self.frameBottom, font = "Times 45")
        self.dist.grid(row = 3, column = 0)
    
        self.convButton = Button(self.frameBottom, text = "Find Time", 
            font = "Ariel 50", command = self.timeFind)
        self.convButton.grid(row = 4, column = 0)

        self.C = 299792458

    def quitButtonAction(self):
        self.window.destroy()

    def timeFind(self):
        time = self.calcRelative()
        convToStand = metricTimeToStandard.MetricToStandard()
        self.messageTime["text"] = time
        self.messageTimeSeg["text"] = "Seconds"
        if (time == math.inf):
            self.messageTimeSegOther["text"] = "Inf yr"
            return
        self.messageTimeSegOther["text"] = convToStand.metricToStandard((time / 86400), True)
        return

    def distAndSpeedGet(self):
        self.vel = self.speen.get()
        if self.vel == "":
            self.vel = "0"
        if "%" in self.vel:
            self.vel = self.vel.replace("%", "")
            self.vel = float(self.vel) / 100
            self.vel = self.vel * self.C
        else:
            self.vel = float(self.vel)
        self.distance = self.dist.get()
        if self.distance == "":
            self.distance = "0"
        if "ly" in self.distance:
            self.distance = self.distance.replace("ly", "")
            self.distance = float(self.distance) * 9.461e+15
        else:
            self.distance = float(self.distance)
        return

    def calcTime(self):
        self.distAndSpeedGet()
        if self.vel >= self.C:
            return math.inf
        else:
            time = (1 / math.sqrt(1 - ((self.vel) ** 2) / ((self.C) ** 2)))
        return time

    def calcRelative(self):
        timeDistort = self.calcTime()
        if (self.vel == 0):
            return math.inf
        newtonTime = self.distance / abs(self.vel)
        relTime = newtonTime / timeDistort
        return relTime

def main():
    root = Tk()
    root.title("Relativity Calculator (Assuming Constant Velocity)")
    dateAndTime = RelCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
