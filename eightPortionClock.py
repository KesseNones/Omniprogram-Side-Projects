#Jesse A. Jones
#Version: 2023-05-13.20

from tkinter import *
import datetime

#This class displays a version of time where the day is split 
#   up into eight named portions instead of just 2 like in the 12 hour system.
class EightClock(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quit button.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds time output and time label.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #3 hour time
        self.messageTime = Label(self.frameBottom, text = "", font = "Ariel 75", anchor = "w")
        self.messageTime.grid(row = 0, column = 0)

        #3 hour time label.
        self.messageTimeSeg = Label(self.frameBottom, text = "", font = "Ariel 75", anchor = "w", bg = "#373737")
        self.messageTimeSeg.grid(row = 1, column = 0)

        #Starts recursive time display loop.
        self.timeUpdate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Fetches current 3 hour time and displays it.
    def timeUpdate(self):
        time = self.convFunTime()
        self.messageTime["text"] = time
        self.messageTimeSeg["text"] = self.portion
        self.window.after(1, self.dateUpdate)

    #Gets the current time.
    def currentTime(self):
        self.local = datetime.datetime.now()
        self.hourUnalt = self.local.hour
        self.min = self.local.minute
        self.sec = self.local.second

    #Given current time, conversion to 3 hour time happens.
    def convFunTime(self):
        #Fetches current time.
        self.currentTime()

        #Late night case.
        if 0 <= self.hourUnalt < 3:
            portion = "Late Night"
            hour = self.hourUnalt + 1
            self.messageTimeSeg["fg"] = "black"
        
        #Pre-morning case.
        if 3 <= self.hourUnalt < 6:
            portion = "Pre-Morning"
            hour = (self.hourUnalt - 3) + 1
            self.messageTimeSeg["fg"] = "#00857d"

        #Morning case
        if 6 <= self.hourUnalt < 9:
            portion = "Morning"
            hour = (self.hourUnalt - 6) + 1
            self.messageTimeSeg["fg"] = "#ffff3f"
        
        #Late morning case.
        if 9 <= self.hourUnalt < 12:
            portion = "Late Morning"
            hour = (self.hourUnalt - 9) + 1
            self.messageTimeSeg["fg"] = "#00ff9b"
        
        #Afternoon case.
        if 12 <= self.hourUnalt < 15:
            portion = "Afternoon"
            hour = (self.hourUnalt - 12) + 1
            self.messageTimeSeg["fg"] = "#93ffd5"
        
        #Late afternoon case.
        if 15 <= self.hourUnalt < 18:
            portion = "Late Afternoon"
            hour = (self.hourUnalt - 15) + 1
            self.messageTimeSeg["fg"] = "#b6ff54"
    
        #Evening case.
        if 18 <= self.hourUnalt < 21:
            portion = "Evening"
            hour = (self.hourUnalt - 18) + 1
            self.messageTimeSeg["fg"] = "#0e5efe"
        
        #Night case.
        if 21 <= self.hourUnalt < 24:
            portion = "Night"
            hour = (self.hourUnalt - 21) + 1
            self.messageTimeSeg["fg"] = "#03006a"
            
        #Sets appropriate portion and generates time string.
        self.portion = portion
        timeString = str(hour) + ":" + str(self.min).zfill(2) + ":" + str(self.sec).zfill(2)
        return timeString

def main():
    root = Tk()
    root.title("Clock With Eight Day Portions")
    dateAndTime = EightClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
