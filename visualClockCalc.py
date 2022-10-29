import time
from tkinter import *
import math
import datetime
import dateHandling

class VisCalc(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.messageTime = Label(self.frameBottom, text = "", font = "Times 50", anchor = "w", bg = "#373737")
        self.messageTime.grid(row = 5, column = 1)

        self.messageI = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 55")
        self.messageI.grid(row = 0, column = 0)

        self.hourE = Entry(self.frameBottom, font = "Times 45")
        self.hourE.grid(row = 0, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter Minute:", font = "Ariel 55")
        self.messageII.grid(row = 2, column = 0)

        self.minE = Entry(self.frameBottom, font = "Times 45")
        self.minE.grid(row = 2, column = 1)

        self.messageIII = Label(self.frameBottom, text = "Enter Second:", font = "Ariel 55")
        self.messageIII.grid(row = 3, column = 0)

        self.secE = Entry(self.frameBottom, font = "Times 45")
        self.secE.grid(row = 3, column = 1)
    
        self.convButton = Button(self.frameBottom, text = "Convert to Visual Clock", 
            font = "Ariel 50", command = self.clockConv)
        self.convButton.grid(row = 4, column = 0)

    def quitButtonAction(self):
        self.window.destroy()

    def clockConv(self):
        time = self.convVisTime()
        self.messageTime["text"] = time

    def timeGet(self):
        timeVerif = dateHandling.GetDate()

        self.hour = timeVerif.getHour(self.hourE.get())
        self.minute = timeVerif.getMinOrSec(self.minE.get())
        self.second = timeVerif.getMinOrSec(self.secE.get())

    def convVisTime(self):
        self.timeGet()
        hr = self.hour
        m = self.minute
        sec = self.second
        timeString = ""
        colorList = ["black", "#00857d", "#ffff3f", "#00ff9b", "#93ffd5", "#b6ff54", "#0e5efe", "#03006a"]
        colorIndex = hr // 3
        hourIconList = ["🌌", "⭐", "🌄", "☼", "☼", "☼", "🌅", "🌙"]
        self.messageTime["fg"] = colorList[colorIndex]
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
    root.title("Visual Clock Calculator")
    dateAndTime = VisCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
