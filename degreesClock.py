import time
from tkinter import *
import datetime

class DegTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        # self.descButton = Button(self.frameTop, text = "Description",
        #     font = "Ariel 20", command = self.showDescription)
        # self.descButton.grid(row = 0, column = 1)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "test", font = "Times 100", anchor = "w")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        t = time.time()
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (t % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        secTotal = (t - (3600 * timeZoneDiff)) % 86400
        self.message["text"] = self.convToDeg(secTotal)
        self.message.after(1, self.timeUpdate)


    def convToDeg(self, secNet):
        degCount = secNet // 240
        secNet %= 240
        arcMinCount = secNet // 4
        secNet %= 4
        arcSecondCount = int((secNet / (4 / 60)))

        degString = str(int(degCount)).zfill(3)
        arcMinString = str(int(arcMinCount)).zfill(2)
        arcSecString = str(arcSecondCount).zfill(2)

        return f"{degString}\u00B0{arcMinString}\'{arcSecString}\""

def main():
    root = Tk()
    root.title("Degree Clock")
    metric = DegTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
