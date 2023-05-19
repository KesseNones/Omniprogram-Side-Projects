#Jesse A. Jones
#Version: 2023-05-19.97

import time
from tkinter import *
from tkinter import messagebox
import baseConvertClass

#This class displays the current Eridian time used by the species in Project Hail Mary.
class EriTime(object):
    def __init__(self, window = None):
        self.window = window

        #Fixes window width to prevent text shifting the window size.
        self.window.geometry("400x200")

        #Holds quit button and description button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Displays info about clock when pressed.
        self.descButton = Button(self.frameTop, text = "Description",
            font = "Ariel 20", command = self.showDescription)
        self.descButton.grid(row = 0, column = 1)

        #Holds Eridian time output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Time output.
        self.message = Label(self.frameBottom, text = "", font = "Times 75", anchor = "w")
        self.message.pack(side = TOP)
    
        self.base = baseConvertClass.BaseConvert()

        #Starts recursive loop that keeps the time updated.
        self.timeUpdate()

    #When called uses messagebox to display clock info.
    def showDescription(self):
        messagebox.showinfo("Eridian Time Description", 
        "Based on the base six clock that the Eridian known as 'Rocky' displayed in the Xenonite hall to Grace.")

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Calls functions to calculate eridian time 
    #   and displays the result before recursively looping.
    def timeUpdate(self):
        self.message["text"] = self.eriConv(int(time.time() / 2.663))
        self.message.after(1, self.timeUpdate)

    #Converts a base six number to a number that is made of Eridian symbols.
    def toEriSymbols(self, num):
        #Useful dictionary and string and index for swapping symbols.
        eriNumDict = {"0":"ℓ", "1":"I", "2":"V", "3":"λ", "4":"+", "5":"∀"}
        numStr = []

        #Builds new list that uses the dictionary 
        #   to swap out numbers 0 - 5 with eridian 0 to 5.
        for el in num:
            numStr.append(eriNumDict[el])

        return numStr

    #Converts an input unix time in eridian seconds to an eridian time stamp.
    def eriConv(self, unix):
        eriSecTotal = unix % 7776
        timestringI = self.base.baseConv(eriSecTotal, 6).zfill(5)
        return self.toEriSymbols(timestringI)

def main():
    root = Tk()
    root.title("Eridian Time")
    metric = EriTime(root)
    root.mainloop()

if __name__ == "__main__":
    main()
