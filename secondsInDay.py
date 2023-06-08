#Jesse A. Jones
#Version: 2023-06-07.26

import time
from tkinter import *
import datetime

#This class displays the number of seconds elapsed 
#   in the day based on the local time zone.
class SecTime(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays seconds elapsed in day.
        self.message = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.message.pack(side = TOP)
    
        #Starts recursive loop that displays the time.
        self.timeUpdate()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calculates seconds in day and displays it.
    def timeUpdate(self):
        t = time.time()

        #Finds time zone based on local time difference from UTC.
        local = datetime.datetime.now()
        localHr = local.hour
        utcHour = (t % 86400) // 3600
        if utcHour < localHr:
            utcHour += 24
        timeZoneDiff = abs(utcHour - localHr)
        
        #Total seconds calculated based on time zone difference and displayed.
        secTotal = (t - (3600 * timeZoneDiff)) % 86400
        self.message["text"] = str(round(secTotal, 1)).zfill(7)
        self.message.after(1, self.timeUpdate)

def main():
    root = Tk()
    root.title("Second Clock")
    metric = SecTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
