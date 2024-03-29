#Jesse A. Jones
#Version: 2024-01-14.93

from tkinter import *
import math
import metricTimeToStandard
import dateHandling

import decimal
from decimal import Decimal

decimal.getcontext().prec = 1000

#Takes in a distance and velocity 
#   (optionally in light years and light speed percentage) 
#   and calculates the time it takes relative to the traveler to get there.
class RelCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds velocity and distance input fields, 
        #   calculation button, and time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
        
        #Distance input field.
        self.messageII = Label(self.frameBottom, text = "Enter Distance (m) ", font = "Ariel 20")
        self.messageII.grid(row = 0, column = 0)
        self.distance = Entry(self.frameBottom, font = "Ariel 20")
        self.distance.grid(row = 1, column = 0)

        #Velocity input field.
        self.messageI = Label(self.frameBottom, text = "Enter Velocity (m/s)", font = "Ariel 20")
        self.messageI.grid(row = 2, column = 0)
        self.velocity = Entry(self.frameBottom, font = "Ariel 20")
        self.velocity.grid(row = 3, column = 0)

        #Holds second count.
        self.messageTime = Label(self.frameBottom, text = "", font = "Ariel 20", anchor = "w")
        self.messageTime.grid(row = 5, column = 0)

        #Displays second unit.
        self.messageTimeSeg = Label(self.frameBottom, text = "", font = "Ariel 20", anchor = "w")
        self.messageTimeSeg.grid(row = 6, column = 0)

        #Displays seconds converted to a more standard time duration.
        self.messageTimeSegOther = Label(self.frameBottom, text = "", font = "Ariel 20", anchor = "w")
        self.messageTimeSegOther.grid(row = 7, column = 0)

        #Calculates time to travel distance and velocity when pressed.
        self.convButton = Button(self.frameBottom, text = "Find Time", 
            font = "Ariel 20", command = self.timeFind)
        self.convButton.grid(row = 4, column = 0)

        self.convToStand = metricTimeToStandard.MetricToStandard()
        
        self.C: Decimal = Decimal(299792458)

        self.parse = dateHandling.GetDate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Determines time taken and displays result in seconds and standard time.
    def timeFind(self):
        #Calculates time in seconds and displays result.
        time = self.calcRelative()
        self.messageTime["text"] = float(time)
        self.messageTimeSeg["text"] = "Seconds"

        #Displays time as infinite or a finite amount of converted time.
        if (time == math.inf):
            self.messageTimeSegOther["text"] = "Inf yr"
        else:
            self.messageTimeSegOther["text"] = self.convToStand.metricToStandard((time / 86400), True)
        

    #Fetches speed and distance from inputs 
    #   and sets class variables unnescesarily.
    def distAndSpeedGet(self) -> list[Decimal]:
        #Parses the input velocity.
        vel = self.velocity.get()

        try:
            #Accounts for if light speed percentage is given.
            #Otherwise just converts to regular decimal.
            if "%" in vel:
                vel = vel.replace("%", "")
                vel = Decimal(vel) / Decimal("100")
                vel = vel * self.C
            else:
                vel = Decimal(vel)
        except decimal.InvalidOperation:
            vel = Decimal(0)

        #Parses input distance.
        dist = self.distance.get()
        
        try:
            #Accounts for if light year is given as distance unit.
            #If not given, meters are assumed.
            if "ly" in dist:
                dist = dist.replace("ly", "")
                dist = Decimal(dist) * Decimal(9.461e+15)
            else:
                dist = Decimal(dist)
        except decimal.InvalidOperation:
            dist = Decimal(0)

        return [dist, vel]

    #Calculates time distortion based on velocity and speed.
    def calcTime(self) -> list[Decimal]:
        retLs = self.distAndSpeedGet()
        d: Decimal = retLs[0]
        v: Decimal = retLs[1]

        #If velocity is equal to or larger than C, distortion is infinite.
        if v >= self.C:
            return [math.inf, d, v]
        else:
            #This calculation is based on Einstein's relativisitic equations.
            distortion = (Decimal(1) / Decimal(math.sqrt(Decimal(1) - ((v) ** Decimal(2)) / ((self.C) ** Decimal(2)))))
        return [distortion, d, v]

    #Calculates time with reletavistic distortion.
    def calcRelative(self) -> Decimal:
        retLs = self.calcTime()
        distort = retLs[0]
        d = retLs[1]
        v = retLs[2]

        #Time is infinity if movement never occurs. 
        if (v == 0):
            return math.inf

        #Calculates time with distortion and returns it.
        newtonTime = d / abs(v) 
        return newtonTime / distort 

def main():
    root = Tk()
    root.title("Relativity Calculator (Assuming Constant Velocity)")
    dateAndTime = RelCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
