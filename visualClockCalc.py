#Jesse A. Jones
#Version: 2023-06-12.18

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
        self.hour = Entry(self.frameBottom, font = FONT)
        self.hour.grid(row = 0, column = 1)

        #Minute input field.
        self.messageII = Label(self.frameBottom, text = "Enter Minute:", font = FONT)
        self.messageII.grid(row = 2, column = 0)
        self.min = Entry(self.frameBottom, font = FONT)
        self.min.grid(row = 2, column = 1)

        #Second input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Second:", font = FONT)
        self.messageIII.grid(row = 3, column = 0)
        self.sec = Entry(self.frameBottom, font = FONT)
        self.sec.grid(row = 3, column = 1)
        
        #Converts input time to visual clock when pressed.
        self.convButton = Button(self.frameBottom, text = "Convert to Visual Clock", 
            font = FONT, command = self.clockConv)
        self.convButton.grid(row = 4, column = 0)

        #Displays output visual clock text.
        self.messageTime = Label(self.frameBottom, text = "", font = FONT, anchor = "w", bg = "#373737")
        self.messageTime.grid(row = 5, column = 1)

        #Used in time parsing.
        self.parse = dateHandling.GetDate()
    
    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates visual time and displays result.
    def clockConv(self):
        #Fetches input time.
        hour = self.parse.getHour(self.hour.get())
        minute = self.parse.getMinOrSec(self.min.get())
        second = self.parse.getMinOrSec(self.sec.get())

        timeStuff = self.visConv(hour, minute, second)
        self.messageTime["text"] = timeStuff[0]
        self.messageTime["fg"] = timeStuff[1]

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
    root.title("Visual Clock Calculator")
    dateAndTime = VisCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
