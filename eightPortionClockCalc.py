#Jesse A. Jones
#Version: 2023-05-17.12

from tkinter import *
import dateHandling

#This class displays the resulting 
#   eight poriton clock time based on user input time.
class EightClockCalc(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button that calls function to quit program.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Bottom frame holds input fields and converted time.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Hour input field.
        self.messageI = Label(self.frameBottom, text = "Enter Hour:", font = "Ariel 20")
        self.messageI.grid(row = 0, column = 0)
        self.hourE = Entry(self.frameBottom, font = "Ariel 20")
        self.hourE.grid(row = 0, column = 1)

        #Minute input field.
        self.messageII = Label(self.frameBottom, text = "Enter Minute:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.minE = Entry(self.frameBottom, font = "Ariel 20")
        self.minE.grid(row = 2, column = 1)

        #Second input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Second:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)
        self.secE = Entry(self.frameBottom, font = "Ariel 20")
        self.secE.grid(row = 3, column = 1)
    
        #Button that calls function to convert input time to 3 hour time.
        self.convButton = Button(self.frameBottom, text = "Convert to Eight Portion Clock", 
            font = "Ariel 20", command = self.clockConv)
        self.convButton.grid(row = 4, column = 0)

        #Clock time.        
        self.messageTime = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.messageTime.grid(row = 5, column = 0)

        #Day portion name display.
        self.messageTimeSeg = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w", bg = "#373737")
        self.messageTimeSeg.grid(row = 6, column = 0)

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Converts input time to eight day portion time.
    def clockConv(self):
        time = self.convFunTime()
        self.messageTime["text"] = time
        self.messageTimeSeg["text"] = self.portion

    #Fetches time input fields.
    def timeGet(self):
        dateFind = dateHandling.GetDate()
        self.hourUnalt = dateFind.getHour(self.hourE.get())
        self.minute = dateFind.getMinOrSec(self.minE.get())
        self.second = dateFind.getMinOrSec(self.secE.get())

    #Converts input time to eight day portion time 
    #   and sets the display accordingly.
    def convFunTime(self):
        self.timeGet()
        if 0 <= self.hourUnalt < 3:
            portion = "Late Night"
            hour = self.hourUnalt + 1
            self.messageTimeSeg["fg"] = "black"
        if 3 <= self.hourUnalt < 6:
            portion = "Pre-Morning"
            hour = (self.hourUnalt - 3) + 1
            self.messageTimeSeg["fg"] = "#00857d"
        if 6 <= self.hourUnalt < 9:
            portion = "Morning"
            hour = (self.hourUnalt - 6) + 1
            self.messageTimeSeg["fg"] = "#ffff3f"
        if 9 <= self.hourUnalt < 12:
            portion = "Late Morning"
            hour = (self.hourUnalt - 9) + 1
            self.messageTimeSeg["fg"] = "#00ff9b"
        if 12 <= self.hourUnalt < 15:
            portion = "Afternoon"
            hour = (self.hourUnalt - 12) + 1
            self.messageTimeSeg["fg"] = "#93ffd5"
        if 15 <= self.hourUnalt < 18:
            portion = "Late Afternoon"
            hour = (self.hourUnalt - 15) + 1
            self.messageTimeSeg["fg"] = "#b6ff54"
        if 18 <= self.hourUnalt < 21:
            portion = "Evening"
            hour = (self.hourUnalt - 18) + 1
            self.messageTimeSeg["fg"] = "#0e5efe"
        if 21 <= self.hourUnalt < 24:
            portion = "Night"
            hour = (self.hourUnalt - 21) + 1
            self.messageTimeSeg["fg"] = "#03006a"
        self.portion = portion
        timeString = str(hour) + ":" + str(self.minute).zfill(2) + ":" + str(self.second).zfill(2)
        return timeString

def main():
    root = Tk()
    root.title("Clock With Eight Day Portions")
    dateAndTime = EightClockCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
