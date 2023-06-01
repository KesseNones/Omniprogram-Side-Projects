#Jesse A. Jones
#Version: 2023-06-01.22

from tkinter import *
import math
import metricTimeToStandard

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
        self.dist = Entry(self.frameBottom, font = "Ariel 20")
        self.dist.grid(row = 1, column = 0)

        #Velocity input field.
        self.messageI = Label(self.frameBottom, text = "Enter Velocity (m/s)", font = "Ariel 20")
        self.messageI.grid(row = 2, column = 0)
        self.speen = Entry(self.frameBottom, font = "Ariel 20")
        self.speen.grid(row = 3, column = 0)

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

        self.C = 299792458

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Determines time taken and displays result in seconds and standard time.
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

    #Fetches speed and distance from inputs 
    #   and sets class variables unnescesarily.
    def distAndSpeedGet(self):
        self.vel = self.speen.get()

        #Checks for empty velocity input.
        if self.vel == "":
            self.vel = "0"
        
        #Checks to see if user intended percentage of light speed for velocity.
        if "%" in self.vel:
            self.vel = self.vel.replace("%", "")
            self.vel = float(self.vel) / 100
            self.vel = self.vel * self.C
        else:
            self.vel = float(self.vel)

        self.distance = self.dist.get()
        
        #Checks for empty distance field.
        if self.distance == "":
            self.distance = "0"
        if "ly" in self.distance:
            self.distance = self.distance.replace("ly", "")
            self.distance = float(self.distance) * 9.461e+15
        else:
            self.distance = float(self.distance)
        return

    #Calculates time distortion based on velocity and speed.
    def calcTime(self):
        self.distAndSpeedGet()
        #If velocity is equal to or larger than C, distortion is infinite.
        if self.vel >= self.C:
            return math.inf
        else:
            #This calculation is based on Einstein's relativisitic equations.
            time = (1 / math.sqrt(1 - ((self.vel) ** 2) / ((self.C) ** 2)))
        return time

    #Calculates time with reletavistic distortion.
    def calcRelative(self):
        timeDistort = self.calcTime()

        #Time is infinity if movement never occurs. 
        if (self.vel == 0):
            return math.inf

        #Calculates time with distortion and returns it.
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
