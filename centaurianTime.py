import time
from tkinter import *
from tkinter import messagebox

class CenTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.descButton = Button(self.frameTop, text = "Description",
            font = "Ariel 20", command = self.showDescription)
        self.descButton.grid(row = 0, column = 1)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "test", font = "Times 100", anchor = "w")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def showDescription(self):
        messagebox.showinfo("Centaurian Time Description", 
        "A time system introduced and imposed by the alien twins Bweryang and Bob at MiB headquarters. It's a 37 hour day; one either adapts to it or has a phsychotic episode.")

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        t = time.time()
        t = int(t)
        timeString = self.cenConv(t)
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

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
