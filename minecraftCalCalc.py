#Jesse A. Jones
#Version: 2023-05-26.16

from tkinter import *
from tkinter import messagebox

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
        self.dayE = Entry(self.frameBottom, font = "Ariel 20")
        self.dayE.grid(row = 1, column = 0)

        #Converts to minecraft calendar.
        self.convButtonI = Button(self.frameBottom, text = "Convert to Minecraft Calendar", 
            font = "Ariel 20", command = self.dayToCal)
        self.convButtonI.grid(row = 2, column = 0)

        #Minecraft calendar output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)
    
    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Converts input date to calendar and displays result.
    def dayToCal(self):
        self.mcCal()
        self.tOutput["text"] = self.dateString

    #Takes in input day and finds resulting minecraft calendar date.
    def mcCal(self):
        #Fetches day input.
        day = self.dayE.get()
        if day == "":
            messagebox.showerror("Empty Entry Error", "Enter something into the day box!")
            return
        day = int(day)

        #Calculates minecraft date.
        year = (day // 96) + 1
        dayOfYear = day % 96
        month = dayOfYear // 8 + 1
        dayOfMonth = dayOfYear % 8 + 1
        
        #Calculates ordinal day suffix.
        ORD = dayOfMonth % 10
        if month == 1:
            monthString = "Silverfish (1)"
        if month == 2:
            monthString = "Cow (2)"
        if month == 3:
            monthString = "Ocelot (3)"
        if month == 4:
            monthString = "Rabbit (4)"
        if month == 5:
            monthString = "Ender (5)"
        if month == 6:
            monthString = "Skeleton (6)"
        if month == 7:
            monthString = "Horse (7)"
        if month == 8:
            monthString = "Sheep (8)"
        if month == 9:
            monthString = "Steve (9)"
        if month == 10:
            monthString = "Chicken (10)"
        if month == 11:
            monthString = "Wolf (11)"
        if month == 12:
            monthString = "Pig (12)"
        if ORD == 0:
            ORDII = 'th'
        if ORD == 1:
            ORDII = "st"
            if ORD == 1 and 20 > dayOfMonth > 10:
                ORDII = 'th'
        if ORD == 2:
            ORDII = "nd"
            if ORD == 2 and 20 > dayOfMonth > 10:
                ORDII = 'th'
        if ORD == 3:
            ORDII = "rd"
            if ORD == 3 and 20 > dayOfMonth > 10:
                ORDII = 'th'
        if ORD == 4:
            ORDII = "th"
        if ORD == 5:
            ORDII = "th"
        if ORD == 6:
            ORDII = "th"
        if ORD == 7:
            ORDII = "th"
        if ORD == 8:
            ORDII = "th"
        if ORD == 9:
            ORDII = "th"

        #Builds date string and sets class variable as such.
        self.dateString = str(dayOfMonth) + ORDII + " of " + monthString + ", " + "Year " + str(year)

def main():
    root = Tk()
    root.title("Minecraft Calendar Calclator")
    temp = MinecraftCalCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
