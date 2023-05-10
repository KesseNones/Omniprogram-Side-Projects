#Jesse A. Jones
#Version: 2023-05-10.12

import time
from tkinter import *
from tkinter import messagebox

#This class displays the current Centaurian time that m.i.b headquarters uses.
class CenTime(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button and description.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Description button.
        self.descButton = Button(self.frameTop, text = "Description",
            font = "Ariel 20", command = self.showDescription)
        self.descButton.grid(row = 0, column = 1)

        #Bottom frame holds time display.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time output.
        self.message = Label(self.frameBottom, text = "test", font = "Ariel 50", anchor = "w")
        self.message.pack(side = TOP)
    
        #Starts recursive time update loop.
        self.timeUpdate()

    #Shows the description when function is called.
    def showDescription(self):
        messagebox.showinfo("Centaurian Time Description", 
        "A time system introduced and imposed by the alien twins\
         Bweryang and Bob at MiB headquarters. It's a 37 hour day; \
         one either adapts to it or has a phsychotic episode.")

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Gets time, converts it to centaurian time, updates display, and loops.
    def timeUpdate(self):
        t = time.time()
        t = int(t)
        timeString = self.cenConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    #Converts passed in unix time stamp to Centaurian time. 
    #   Basically our time but the day is 37 hours instead of 24.
    def cenConv(self, unix):
        cenSecTotal = unix % 133200
        cenHour = cenSecTotal // 3600
        cenSecReducedI = cenSecTotal % 3600
        cenMin = cenSecReducedI // 60
        cenSecReducedII = cenSecTotal % 60
        cenSec = cenSecReducedII
        timeString = str(cenHour).zfill(2) + "." + str(cenMin).zfill(2) + "." + str(cenSec).zfill(2)
        return timeString

def main():
    root = Tk()
    root.title("Centaurian Time")
    metric = CenTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
