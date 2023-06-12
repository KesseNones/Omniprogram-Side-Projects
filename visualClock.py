#Jesse A. Jones
#Version: 2023-06-12.15

import datetime
from tkinter import *

#This class contains a visual version of the common clock. 
#   This clock uses emojis and different icons to indicate time 
#   in a visual way, with hearts being seconds, 
#   hands being groups of five seconds, hour glasses being minutes, 
#   clocks being five minutes, and lastly hours being themselves.
#   Hours are ordinal so seeing one hour chip indicates 
#   that it's the first hour of the twelve hour cycle, 
#   so 1 corellates to midnight or noon.  
class VisTime(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds visual clock output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays visual time.
        self.message = Label(self.frameBottom, text = "", font = "Ariel 20", anchor = "w", bg = "#373737")
        self.message.pack(side = TOP)
    
        #Starts recursive time loop.
        self.timeUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Creates visual clock time string and displays it before looping.
    def timeUpdate(self):
        #Current time fetched.
        local = datetime.datetime.now()
        hr = local.hour
        m = local.minute
        sec = local.second

        timeStuff = self.visConv(hr, m, sec)
        self.message["text"] = timeStuff[0]
        self.message["fg"] = timeStuff[1]
        self.message.after(1, self.timeUpdate)

    #Creates visual clock time string based on current time.
    def visConv(self, hour, minute, second):
        #Useful lists in further calculations 
        #   and determines what hours look like 
        #   and what color is displayed for the text foreground.
        timeString = ""
        colorList = ["black", "#00857d", "#ffff3f", "#00ff9b", "#93ffd5", "#b6ff54", "#0e5efe", "#03006a"]
        colorIndex = hour // 3
        hourIconList = ["🌌", "⭐", "🌄", "☼", "☼", "☼", "🌅", "🌙"]
        timeColor = colorList[hour // 3]

        #Determines which 12 hour indicator starts the time string.
        timeString += ["🔅\n", "🌕\n"][hour >= 12]
        
        #Creates all hour icons with the appropriate icon for each.
        for i in range(0, hour % 12 + 1):
            #Hour symbol added.
            timeString += hourIconList[colorIndex]
            timeString += (" " * ((i + 1) % 5 == 0))
        timeString += "\n"
        
        #Builds visual minutes and seconds.
        timeString += self.generateBaseSixtyChunks("⏱️", "⌛", minute)
        timeString += self.generateBaseSixtyChunks("🖐", "💚", second)

        return [timeString, timeColor]

    #Generates visual minutes or seconds depending on input.
    def generateBaseSixtyChunks(self, bigSymbol, littleSymbol, unitsElapsed):
        timeSubString = ""

        #Creates all five unit icons of the time.
        for i in range(0, unitsElapsed // 5):
            timeSubString += bigSymbol
            #Adds space when needed.
            timeSubString += (" " * ((i + 1) % 5 == 0))
        timeSubString += "\n"
        
        #Creates all unit icons.
        for i in range (0, unitsElapsed % 5):
            timeSubString += littleSymbol
        timeSubString += "\n"

        return timeSubString

def main():
    root = Tk()
    root.title("Visual Time")
    metric = VisTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
