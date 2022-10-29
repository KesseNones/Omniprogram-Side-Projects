import time
import datetime
from tkinter import *
import math

class VisTime(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "test", font = "Times 50", anchor = "w", bg = "#373737")
        self.message.pack(side = TOP)
    
        self.timeUpdate()

    def quitButtonAction(self):
        self.window.destroy()

    def timeUpdate(self):
        timeString = self.visConv()
        self.message["text"] = timeString
        self.message.after(1, self.timeUpdate)

    def visConv(self):
        self.local = datetime.datetime.now()
        hr = int(self.local.hour)
        m = int(self.local.minute)
        sec = int(self.local.second)
        timeString = ""
        colorList = ["black", "#00857d", "#ffff3f", "#00ff9b", "#93ffd5", "#b6ff54", "#0e5efe", "#03006a"]
        colorIndex = hr // 3
        hourIconList = ["🌌", "⭐", "🌄", "☼", "☼", "☼", "🌅", "🌙"]
        self.message["fg"] = colorList[colorIndex]
        flag = 0

        if hr >= 12:
            timeString += "🎇\n"
        else:
            timeString += "🎆\n"
        for i in range(0, hr % 12 + 1):
            if (flag > 4):
                timeString += " "
                flag = 0
            timeString += hourIconList[colorIndex]
            flag += 1
        timeString += "\n"
        
        flag = 0
        for j in range(0, m // 5):
            if (flag > 4):
                timeString += " "
                flag = 0
            timeString += "⏱️"
            flag += 1
        timeString += "\n"
        
        flag = 0
        for k in range (0, m % 5):
            if (flag > 4):
                timeString += " "
                flag = 0
            timeString += "⌛"
            flag += 1
        timeString += "\n"

        flag = 0
        for el in range(0, sec // 5):
            if (flag > 4):
                timeString += " "
                flag = 0
            timeString += "🖐"
            flag += 1
        timeString += "\n"

        flag = 0
        for s in range(0, sec % 5):
            if (flag > 4):
                timeString += " "
                flag = 0
            timeString += "💚"
            flag += 1
        return timeString

def main():
    root = Tk()
    root.title("Visual Time")
    metric = VisTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
