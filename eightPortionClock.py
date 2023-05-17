#Jesse A. Jones
#Version: 2023-05-17.13

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
        self.messageTime = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w")
        self.messageTime.grid(row = 0, column = 0)

        #3 hour time label.
        self.messageTimeSeg = Label(self.frameBottom, text = "", font = "Ariel 50", anchor = "w", bg = "#373737")
        self.messageTimeSeg.grid(row = 1, column = 0)

        #Starts recursive time display loop.
        self.timeUpdate()

    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Fetches current 3 hour time and displays it.
    def timeUpdate(self):
        timeArr = self.convEightTime()
        #Displays converted time.
        self.messageTime["text"] = timeArr[0]
        self.messageTimeSeg["text"] = timeArr[1]
        self.messageTimeSeg["fg"] = timeArr[2]

        #Recursively loops time.
        self.window.after(1, self.timeUpdate)

    #Given current time, conversion to 3 hour time happens.
    def convEightTime(self):
        #Fetches current time.
        local = datetime.datetime.now()
        hour = local.hour
        minute = local.minute
        second = local.second

        #Sets up important lists for time display.
        poritonArr = ["Late Night", "Pre Morning", "Morning", "Late Morning", 
                    "Afternoon", "Late Afternoon", "Evening", "Night"]
        colorArr = ["black", "#00857d", "#ffff3f", "#00ff9b",
                    "#93ffd5", "#b6ff54", "#0e5efe", "#03006a"]
        
        #Calculates index for lists and new hour.
        index = hour // 3
        eightHour = (hour - (3 * index)) + 1

        #Time and portion info set.
        timeString = str(eightHour) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)
        portionText = poritonArr[index]
        portionColor = colorArr[index]
        
        return [timeString, portionText, portionColor]

def main():
    root = Tk()
    root.title("Clock With Eight Day Portions")
    dateAndTime = EightClock(root)
    root.mainloop()

if __name__ == "__main__":
    main()
