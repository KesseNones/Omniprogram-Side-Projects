from tkinter import *

class WarpToCConv(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter Warp Factor:", font = "Ariel 75", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.warp = Entry(self.frameBottom, font = "Times 69")
        self.warp.grid(row = 1, column = 0)

        self.convButton = Button(self.frameBottom, text = "Convert to C Multiple", 
            font = "Ariel 60", command = self.warpy)
        self.convButton.grid(row = 2, column = 0)

        self.cOutput = Label(self.frameBottom, text = "The Speed is: N/A C", font = "Ariel 69")
        self.cOutput.grid(row = 3, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def warpy(self):
        speed = self.warpToC()
        self.cOutput["text"] = "The speed is: " + str(speed) + " C"

    def warpToC(self):
        W = float(self.warp.get())
        if W > 10:
            C = 'invalid warp factor'
        if W < 0:
            C = 'invalid warp factor'
        if 0 <= W <= 9:
            C = W**(10/3)
            C = round(C, 3)
        if 10 > W > 9:
            C = (W**(10/3))/(W - 10) * -1
            C = round(C, 3)
        if W == 10:
            C = '∞'
        return C

def main():
    root = Tk()
    root.title("Warp Factor to C Multiple Converter")
    coin = WarpToCConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
