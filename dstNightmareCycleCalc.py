from tkinter import *
import math
from math import log
from tkinter import messagebox

class NightmareCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter Day Number:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.dayE = Entry(self.frameBottom, font = "Times 55")
        self.dayE.grid(row = 1, column = 0)

        self.message = Label(self.frameBottom, text = "Enter Sliver Number:", font = "Ariel 55", anchor = "w")
        self.message.grid(row = 2, column = 0)

        self.slv = Entry(self.frameBottom, font = "Times 55")
        self.slv.grid(row = 3, column = 0)

        self.convButtonI = Button(self.frameBottom, text = "Find Approximate Nightmare Phase", 
            font = "Ariel 55", command = self.timeToCy)
        self.convButtonI.grid(row = 4, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 55", justify = LEFT)
        self.tOutput.grid(row = 5, column = 0)

        self.tOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 55")
        self.tOutputII.grid(row = 6, column = 0)
    
    def quitButtonAction(self):
        self.window.destroy()

    def dayGet(self):
        if self.dayE.get() == "":
            return 0
        return int(self.dayE.get())

    def sliverGet(self):
        if self.slv.get() == "":
            return 0
        if int(self.slv.get()) > 15 or int(self.slv.get()) < 0:
            messagebox.showerror("Out of range error!", "Sliver must be in range 0 to 15!")
            return
        return int(self.slv.get())

    def timeToCy(self):
        daysElapsed = self.dayGet() - 1
        sliversElapsed = self.sliverGet()
        secondsTotal = (daysElapsed * 480) + (sliversElapsed * 30)

        nightmareSeconds = secondsTotal % 600
        nightmarePhase = ""

        if 0 <= nightmareSeconds < 286:
            nightmarePhase = "Calm Phase"
            self.tOutput["fg"] = "#4b5c74"
        if 286 <= nightmareSeconds < 346:
            nightmarePhase = "Warning Phase"
            self.tOutput["fg"] = "#3e3833"
        if 346 <= nightmareSeconds < 556:
            nightmarePhase = "Nightmare Phase"
            self.tOutput["fg"] = "#d34541"
        if 556 <= nightmareSeconds < 600:
            nightmarePhase = "Dawn Phase"
            self.tOutput["fg"] = "#544e49"

        self.tOutput["text"] = nightmarePhase
        self.tOutputII["text"] = "Seconds in Cycle: " + str(nightmareSeconds)
        return nightmarePhase

def main():
    root = Tk()
    root.title("DST Approximate Nightmare Cycle Calculator")
    temp = NightmareCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
