#Jesse A. Jones
#Version: 2023-06-11.16

import time
from tkinter import *

#This class displays the current stardate in TOS format.
class StardateTOS(object):
    def __init__(self, window = None):
        self.window = window

        #Fixes window width to prevent text shifting the window size.
        self.window.geometry("550x200")

        #Holds quit button and stardate precision slider.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when called.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Used to set stardate precision from one decimal place to five.
        self.prec = Scale(self.frameTop, orient = HORIZONTAL, 
            from_ = 1, to = 5, length = 300,
            label = "SD Precision", font = "Ariel 20", command = self.precGet)
        self.prec.grid(row = 0, column = 1)

        #Holds stardate output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays stardate.
        self.message = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.message.pack(side = TOP)
        
        #Starts recursive updating loop.
        self.starUpdate()

    #Acquires the precision value from the slider.
    def precGet(self, num):
        return int(self.prec.get())

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Recursively calculates TOS stardate, displays it and loops.
    def starUpdate(self):
        #Fetches stardate and precision.
        date = self.stardateTOS()
        prec = self.precGet(1)
        date[0] = format(date[0], f".{prec}f")

        #Displays stardate before looping.
        self.message["text"] = f"{date[0]} ({int(date[1])})"
        self.message.after(1, self.starUpdate)

    #Calculates TOS stardate from unix time.
    def stardateTOS(self):
        #Unix time fetched.
        t = time.time()

        #Calculates number of stardates remaining in current issue.
        s = (6059232000 / 86400) - (t / 86400)
        s *= 5

        #Caclulates current stardate.
        subStar = abs((s % 10000) - 10000)
        
        #Truncates stardate based on precision setting.
        prec = self.precGet(1)
        subStar = subStar * (10 ** prec)
        subStar = int(subStar)
        subStar = subStar / (10 ** prec)
        
        #Finds issue number and returns list of stardate and issue number.
        superStar = s // 10000
        return [subStar, (superStar * -1) - 1]

def main():
    root = Tk()
    root.title("Stardate TOS Version")
    star = StardateTOS(root)
    root.mainloop()

if __name__ == "__main__":
    main()

