#Jesse A. Jones
#Version: 2023-08-01.26

from tkinter import *
import math
import dateHandling

#This class contains the inputs necessary to convert multiples of the speed 
#   of light to the Actillion FTL Factor, 
#   a faster than light metric used by a fictional alien race, and back. 
class ActillionFTLFactorCalc(object):

    #Sets up input components in tkinter window.
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
    
        self.messageI = Label(self.frameBottom, text = "Enter C Multiple:", font = "Times 20", anchor = "w")
        self.messageI.grid(row = 0, column = 0)

        self.cI = Entry(self.frameBottom, font = "Times 20")
        self.cI.grid(row = 0, column = 1)

        self.affButton = Button(self.frameBottom, text = "Convert to AFF", 
            font = "Times 20", command = self.CTOAff)
        self.affButton.grid(row = 1, column = 0)

        self.aOutput = Label(self.frameBottom, text = "", 
            font = "Times 20")
        self.aOutput.grid(row = 2, column = 1)

        self.messageII = Label(self.frameBottom, text = "Enter AFF:", font = "Times 20", anchor = "w")
        self.messageII.grid(row = 3, column = 0)

        self.aff = Entry(self.frameBottom, font = "Times 20")
        self.aff.grid(row = 3, column = 1)

        self.cButton = Button(self.frameBottom, text = "Convert to C Multiple", 
            font = "Times 20", command = self.affToC)
        self.cButton.grid(row = 4, column = 0)

        self.cOutput = Label(self.frameBottom, text = "", 
            font = "Times 20")
        self.cOutput.grid(row = 5, column = 1)

        self.parse = dateHandling.GetDate()

    def quitButtonAction(self):
        self.window.destroy()

    #Calls function that converts Actillion FTL Factor 
    #   to multiple of light speed. Displays result.
    def affToC(self):
        C = self.print_AFF_Calculation(1)
        self.cOutput["text"] = C

    #Calls function that converts multiple of light speed
    #   to Actillion FTL Factor. Displays result.
    def CTOAff(self):
        aff = self.print_AFF_Calculation(2)
        self.aOutput["text"] = aff

    #This method performs the conversion from Actillion 
    #   FTL Factor to light speed multiple and vice versa.
    def print_AFF_Calculation(self, S):
        #AFF to light speed case.
        if S == 1:
            W = self.parse.getGeneral(self.aff.get())
            C = 200 ** W
            return C

        #Light speed to AFF case.
        if S == 2:
            C = self.parse.getGeneral(self.cI.get())

            #Accounts for negative and 0 multiples of light speed.
            if C == 0:
                return "Infinitely Negative Factor!"
            if C < 0:
                return "Impossible!"
        
            #Converts to light speed.    
            W = math.log(C, 200)
            return W

def main():
    root = Tk()
    root.title("Actillion FTL Factor Calculator")
    star = ActillionFTLFactorCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()
