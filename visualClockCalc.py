#Jesse A. Jones
#Version: 2023-06-12.17

from tkinter import *
import dateHandling

#This class is same as the visual clock but it takes 
#   in time input and displays the resulting string.
class VisCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds time input fields and output visual clock.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        FONT = "Ariel 20"

        #Hour input field.
        self.messageI = Label(self.frameBottom, text = "Enter Hour:", font = FONT)
        self.messageI.grid(row = 0, column = 0)
        self.hourE = Entry(self.frameBottom, font = FONT)
        self.hourE.grid(row = 0, column = 1)

        #Minute input field.
        self.messageII = Label(self.frameBottom, text = "Enter Minute:", font = FONT)
        self.messageII.grid(row = 2, column = 0)
        self.minE = Entry(self.frameBottom, font = FONT)
        self.minE.grid(row = 2, column = 1)

        #Second input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Second:", font = FONT)
        self.messageIII.grid(row = 3, column = 0)
        self.secE = Entry(self.frameBottom, font = FONT)
        self.secE.grid(row = 3, column = 1)
        
        #Converts input time to visual clock when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Visual Clock", 
            font = FONT, command = self.clockConv)
        self.convButton.grid(row = 4, column = 0)

        #Displays output visual clock text.
        self.messageTime = Label(self.frameBottom, text = "", font = FONT, anchor = "w", bg = "#373737")
        self.messageTime.grid(row = 5, column = 1)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates visual time and displays result.
    def clockConv(self):
        time = self.convVisTime()
        self.messageTime["text"] = time

    #Fetches input time and sets some class variables because yes.
    #   THIS DISGUSTS ME AND SHOULD BE FIXED.
    def timeGet(self):
        timeVerif = dateHandling.GetDate()

        self.hour = timeVerif.getHour(self.hourE.get())
        self.minute = timeVerif.getMinOrSec(self.minE.get())
        self.second = timeVerif.getMinOrSec(self.secE.get())

    #calculates current visual clock time and returns the time string necessary.
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
