#Jesse A. Jones
#Version: 2023-05-26.17

from tkinter import *
from tkinter import messagebox
import dateHandling

#Class contains a calculator that calculates the date 
#   in the made up minecraft calendar based on the input day number. 
#   It's a calendar of 12 months of 8 days each, making a 96 day year. 
#   The months start on the full moon.
class MinecraftCalCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds day input field and minecraft 
        #   calendar conversion and converted calendar output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Day input field.
        self.message = Label(self.frameBottom, text = "Enter Day Number:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.day = Entry(self.frameBottom, font = "Ariel 20")
        self.day.grid(row = 1, column = 0)

        #Converts to minecraft calendar.
        self.convButtonI = Button(self.frameBottom, text = "Convert to Minecraft Calendar", 
            font = "Ariel 20", command = self.dayToCal)
        self.convButtonI.grid(row = 2, column = 0)

        #Minecraft calendar output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)

        self.dayParse = dateHandling.GetDate()
    
    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Fetches user input day and converts it 
    #   to minecraft calendar, displaying result.
    def dayToCal(self):
        day = self.dayParse.getYear(self.day.get())
        self.tOutput["text"] = self.mcCal(day)

    #Takes in input day and finds resulting minecraft calendar date.
    def mcCal(self, day):
        #Calculates minecraft date.
        year = (day // 96) + 1
        dayOfYear = day % 96
        month = dayOfYear // 8 + 1
        dayOfMonth = dayOfYear % 8 + 1

        #Finds month name.
        monthNames = ["Silverfish", "Cow", "Ocelot",\
                    "Rabbit", "Ender", "Skeleton", \
                    "Horse", "Sheep", "Steve",\
                    "Chicken", "Wolf", "Pig"]
        monthString = f"{monthNames[month - 1]} ({month})"
        
        #Calculates ordinal day suffix.
        ordSuffixes = ["st", "nd", "rd", "th", "th", "th", "th", "th"]
        ordSuffix = ordSuffixes[dayOfMonth - 1]

        #Returns date string.
        return f"{dayOfMonth}{ordSuffix} {monthString}, Year {year}\n New Redland Reckoning"

def main():
    root = Tk()
    root.title("Minecraft Calendar Calclator")
    temp = MinecraftCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
