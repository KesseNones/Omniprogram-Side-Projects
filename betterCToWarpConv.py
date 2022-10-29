from tkinter import *
from math import inf, log10
from math import ceil

class CToWConv(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter C Multiple:", font = "Ariel 75", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.cSpeed = Entry(self.frameBottom, font = "Times 69")
        self.cSpeed.grid(row = 1, column = 0)

        self.convButton = Button(self.frameBottom, text = "Convert to Warp Factor", 
            font = "Ariel 60", command = self.antiWarpy)
        self.convButton.grid(row = 2, column = 0)

        self.wOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 69", justify = LEFT, wraplength = 700 )
        self.wOutput.grid(row = 3, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def antiWarpy(self):
        self.wOutput["text"] = "Loading..."
        self.window.update()
        if (self.cSpeed.get() == ""):
            speed = 0
        else:
            speed = float(self.cSpeed.get())
        warpFac = self.cToWarp(speed)
        self.wOutput["text"] = "The Factor is: " + str(warpFac)

    def warpToC(self, warp):
        try:
            C = 0
            if (warp <= 9):
                C = warp ** (10/3)
            else:
                C = ((warp ** (10/3))/(warp - 10)) * -1
            return C
        except:
            ZeroDivisionError
            return inf
    
    def cToWarp(self, speed):
        if (speed == inf):
            return 10
        div = 1
        if (speed <= 1516.3811070048380994924114249569):
            warp = speed ** (3/10)
            return warp
        warp = 9
        expectedSpeed = round(log10(speed), 4)
        currentSpeed = round(log10(self.warpToC(warp)), 4)
        maxSpeed = round(log10(1.2128389084027075e+18), 4)
        if (expectedSpeed > maxSpeed):
            return "> 9.999999999999999 and < 10"
        while (True):
            place = 0
            div *= 10
            print(log10(div))
            while (place < 9):
                warp += (1 / div)
                warp = round(warp, int(ceil(log10(div))))
                currentSpeed = round(log10(self.warpToC(warp)), 4)
                if (currentSpeed == expectedSpeed):
                    return warp
                elif (currentSpeed > expectedSpeed):
                    warp -= (1 / div)
                    warp = round(warp, int(ceil(log10(div))))
                    break
                place += 1
            if (log10(div) > 15):
                return warp
            
            
            
        

def main():
    root = Tk()
    root.title("C Multiple to Warp Factor Converter")
    coin = CToWConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
