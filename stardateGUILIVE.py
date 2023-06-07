#Jesse A. Jones
#Version: 2023-06-07.11

import time
from tkinter import *

#This class calculates a TNG based stardate and displays it.
class Stardate(object):
    def __init__(self, window = None):
        self.window = window

        #Fixes window width to prevent text shifting the window size.
        self.window.geometry("400x160")

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Precision slider used to control stardate precision.
        self.prec = Scale(self.frameTop, orient = HORIZONTAL, 
            from_ = 1, to = 5, length = 300,
            label = "SD Precision", font = "Ariel 20", command = self.precGet)
        self.prec.grid(row = 0, column = 1)

        #Holds stardate display window.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays stardate output.
        self.message = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.message.pack(side = TOP)
    
        #Starts recursive updating loop.
        self.starUpdate()

    #Fetches precision from slider.
    def precGet(self, num):
        return int(self.prec.get())

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Gets stardate and precision setting, and displays resulting stardate.
    def starUpdate(self):
        self.message["text"] = format(self.stardate(), f".{self.precGet(1)}f")
        self.message.after(1, self.starUpdate)

    #Calculates and returns stardate.
    def stardate(self):
        #Calculates stardate based on unix time.
        t = time.time()
        s = (t / 31557.6) + (740583679.968 / 31557.6)

        #Truncates stardate to desired precision.
        RI = s * (10 ** self.precGet(1))
        RII = int(RI)
        RIII = RII / (10 ** self.precGet(1))

        return RIII

def main():
    root = Tk()
    root.title("Stardate")
    star = Stardate(root)
    root.mainloop()

if __name__ == "__main__":
    main()

