#Jesse A. Jones
#Version: 2023-08-01.32

from tkinter import *
import dateHandling

#This class takes in an input temperature 
#   and converts between fahrenheit, celsius, or Kelvin.
class TempConverter(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds temperature input field, 
        #   conversion buttons, and temperature output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Temperature input field.
        self.message = Label(self.frameBottom, text = "Enter Temperature:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.temp = Entry(self.frameBottom, font = "Ariel 20")
        self.temp.grid(row = 0, column = 1)

        #Converts fahrenheit to celsius when pressed.
        self.convButtonI = Button(self.frameBottom, text = "Fahrenheit to Celsius", 
            font = "Ariel 20", command = self.FtoC)
        self.convButtonI.grid(row = 1, column = 0)

        #Converts celsius to fahrenheit when pressed.
        self.convButtonII = Button(self.frameBottom, text = "Celsius to Fahrenheit", 
            font = "Ariel 20", command = self.CtoF)
        self.convButtonII.grid(row = 1, column = 1)

        #Converts fahrenheit to kelvin when pressed.
        self.convButtonIII = Button(self.frameBottom, text = "Fahrenheit to Kelvin", 
            font = "Ariel 20", command = self.FtoK)
        self.convButtonIII.grid(row = 2, column = 0)

        #Converts celsius to kelvin when pressed.
        self.convButtonIV = Button(self.frameBottom, text = "Celsius to Kelvin", 
            font = "Ariel 20", command = self.CtoK)
        self.convButtonIV.grid(row = 2, column = 1)

        #Converts from kelvin to fahrenheit when pressed.
        self.convButtonV = Button(self.frameBottom, text = "Kelvin to Fahrenheit", 
            font = "Ariel 20", command = self.KtoF)
        self.convButtonV.grid(row = 3, column = 0)

        #Converts from kelvin to celsius when pressed.
        self.convButtonVI = Button(self.frameBottom, text = "Kelvin to Celsius", 
            font = "Ariel 20", command = self.KtoC)
        self.convButtonVI.grid(row = 3, column = 1)

        #Displays converted temperatrue.
        self.message = Label(self.frameBottom, text = "Converted Temperature:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 4, column = 0)
        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 20", justify = LEFT, wraplength = 600 )
        self.tOutput.grid(row = 4, column = 1)

        #Used to indicate when a temperature is impossible.
        self.impossible = Label(self.frameBottom, text = "", 
            font = "Ariel 20")
        self.impossible.grid(row = 5, column = 1)

        self.parse = dateHandling.GetDate()

    #Converts fahrenheit to celsius when called and displays the result.
    def FtoC(self):
        conv = self.convert(1)
        if conv < -273.15:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " °C"

    #Converts celsius to fahrenheit when called and displays the result.
    def CtoF(self):
        conv = self.convert(2)
        if conv < -459.67:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " °F"

    #Converts fahrenheit to kelvin when called and displays the result.
    def FtoK(self):
        conv = self.convert(3)
        if conv < 0:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " Kelvin"

    #Converts celsius to kelvin when called and displays the result.
    def CtoK(self):
        conv = self.convert(4)
        if conv < 0:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " Kelvin"

    #Converts kelvin to fahrenheit when called and displays the result.
    def KtoF(self):
        conv = self.convert(5)
        if self.parse.getGeneral(self.temp.get()) < 0:
            self.impossible["text"] = "Impossible Temperature"
        else:
            self.impossible["text"] = ""
        self.tOutput["text"] = str(conv) + " °F"
    
    #Converts kelvin to celsius when called and displays the result.
    def KtoC(self):
        conv = self.convert(6)
        if self.parse.getGeneral(self.temp.get()) < 0:
            self.impossible["text"] = "Impossible Temperature"
        self.tOutput["text"] = str(conv) + " °C"

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Converts input temperature to any of the three systems given the T input.
    def convert(self, T):
        #F to C case.
        if T == 1:
            F = self.parse.getGeneral(self.temp.get())
            C = (F - 32) / 1.8
            C = round(C, 3)
            return C

        #C to F case
        elif T == 2:
            C = self.parse.getGeneral(self.temp.get())
            F = (C * 1.8) + 32
            F = round(F, 3)
            return F

        #F to K case
        elif T == 3:
            F = self.parse.getGeneral(self.temp.get())
            K = ((F - 32) / 1.8) + 273.15
            K = round(K, 3)
            return K

        #C to K case.
        elif T == 4:
            C = self.parse.getGeneral(self.temp.get())
            K = C + 273.15
            K = round(K, 3)
            return K

        #K to F case.
        elif T == 5:
            K = self.parse.getGeneral(self.temp.get())
            F = ((K - 273.15) * 1.8) + 32
            F = round(F, 3)
            return F

        #K to C case.
        else:
            K = self.parse.getGeneral(self.temp.get())
            C = K - 273.15
            C = round(C, 3)
            return C

def main():
    root = Tk()
    root.title("Temperature Converter")
    temp = TempConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
