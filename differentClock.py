import time
from tkinter import *
from tkinter import messagebox
import datetime

class DiffTime(object):
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
        messagebox.showinfo("Clock Description", 
            "A dumb alternate clock I saw on a Youtube video that I decided to implement in code. One day is twenty hours, one hour is twenty minutes and one minute is two hundred and sixteen seconds. Have fun!")

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        timeString = self.timeConv(self.localUnix())
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def timeConv(self, unix):
        daySecTotal = unix % 86400
        hourCount = (daySecTotal // 4320) + 1
        daySecTotal %= 4320
        minCount = daySecTotal // 216
        secCount = daySecTotal % 216
        
        hourLabel = str(hourCount).zfill(2)
        minuteLabel = str(minCount).zfill(2)
        secLabel = str(secCount).zfill(3)

        return f"{hourLabel}:{minuteLabel}:{secLabel}"  


    def localUnix(self):
        t = time.time()
        t = int(t)
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = ((t % 86400) // 3600)
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        t = (t - (3600 * timeZoneDiff))
        return t

def main():
    root = Tk()
    root.title("Different Clock (Not Mine)")
    metric = DiffTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
