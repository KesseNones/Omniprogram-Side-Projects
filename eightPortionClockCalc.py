#Jesse A. Jones
#Version: 2023-05-17.14

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
        self.hour = Entry(self.frameBottom, font = "Ariel 20")
        self.hour.grid(row = 0, column = 1)

        #Minute input field.
        self.messageII = Label(self.frameBottom, text = "Enter Minute:", font = "Ariel 20")
        self.messageII.grid(row = 2, column = 0)
        self.min = Entry(self.frameBottom, font = "Ariel 20")
        self.min.grid(row = 2, column = 1)

        #Second input field.
        self.messageIII = Label(self.frameBottom, text = "Enter Second:", font = "Ariel 20")
        self.messageIII.grid(row = 3, column = 0)
        self.sec = Entry(self.frameBottom, font = "Ariel 20")
        self.sec.grid(row = 3, column = 1)
    
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

        #Used for input date parsing.
        self.dateFind = dateHandling.GetDate()
    
    #Quits program.
    def quitButtonAction(self):
        self.window.destroy()

    #Converts input time to eight day portion time.
    def clockConv(self):
        timeArr = self.convEightTime()
        self.messageTime["text"] = timeArr[0]
        self.messageTimeSeg["text"] = timeArr[1]
        self.messageTimeSeg["fg"] = timeArr[2]

    #Given current time, conversion to 3 hour time happens.
    def convEightTime(self):
        #Fetches input dates.
        hour = self.dateFind.getHour(self.hour.get())
        minute = self.dateFind.getMinOrSec(self.min.get())
        second = self.dateFind.getMinOrSec(self.sec.get())

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
    dateAndTime = EightClockCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
