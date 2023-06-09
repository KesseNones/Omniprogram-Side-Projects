#Jesse A. Jones
#Version: 2023-06-09.08

import random
from tkinter import *
import math

#This class generates a starfield displayed in a GUI window.
class Starfield(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        #Holds starfield output.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #Displays starfield.
        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "black", highlightbackground = "black", highlightthickness = 2)
        self.draw.grid(row = 0, column = 0)

        #Creates background stars and sets up data.
        self.isNotFirstTime = False
        self.createBackgroundStars()
        self.starFlag = 0
        self.starArr = []
        self.createStars(600)

        #Starts recursive loop that updates starfield.
        self.starfieldUpdate()

    #Creates the background stars featured when this is called.
    def createBackgroundStars(self, hype = 600):
        self.backGroundStars = []
        #Randomly draws a star in a position 
        #   of a circle that is shrinking as the drawing continues.
        while hype > 0:
            #Random size and degree picked.
            starSize = random.choice(range(1, 4))
            starPos = random.choice(range(0, 360))
            
            #Star created with parameters.
            self.backGroundStars.append(Star(starPos, hype, starSize, "white", self.draw))
            hype -= 2

        self.window.update()

    #Creates stars that are newer and keep being made.
    def createStars(self, hype = 450):
        localStar = []
        hypeInit = hype
        #Creates stars.
        while hype > 0:
            starSize = random.choice(range(1, 4))
            starPos = random.choice(range(0, 360))
            self.starArr.append(Star(starPos, hype, starSize, "white", self.draw))
            hype -= 2

        #Has stars fade in if it's a new batch 
        #   of stars that hasn't been drawn in for the first time.
        if self.isNotFirstTime:
            self.starFadeIn(self.starArr, hypeInit)
        
        self.window.update()
         
    #Causes the effect to phase stars in.   
    def starFadeIn(self, starArray, hype):
        #Numbers used in hex code math for the star color.
        #65793
        #16777215

        colorNum = 0
        start = ((hype // 2) * - 1)
        step = 65793
        
        #While the color is less than pure white, 
        #   increment the color of the stars to be brighter.
        while colorNum <= 16777215:
            #Iterates through and changes every star to a lighter color.
            for index in range(start, -1):
                hexNum = self.tenToOtherBase(colorNum, 16)
                hashtagHex = "#" + hexNum.zfill(6)
                starArray[index].colorChange(hashtagHex)
            
            self.updateStars()
            colorNum += step * 32
            self.window.update()

    #Converts a number to a given base as a list of digits in that base.
    def baseAlg(self, num, base):
        digitArr = []
        if num == 0:
            return ["0"]
        while num > 0:
            digitArr.append(str(num % base))
            num = num // base
        return digitArr

    #Converts an input number in base 10 to another base.
    def tenToOtherBase(self, num, base):
        convNum = str()
        if base < 11:
            digits = self.baseAlg(num, base)
            digits.reverse()
            for el in digits:
                convNum = convNum + el
        if base >= 11:
            digits = self.baseAlg(num, base)
            digits.reverse()
            letterDigits = self.toLetters(digits, base)
            for el in letterDigits:
                convNum = convNum + el
        return convNum

    #Turns digits in a digit array that are 10 or higher 
    #   to letters in higher bases, for example 10 turning into A in base 16.
    def toLetters(self, digitArr, base):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        loc = 0
        for el in digitArr:
            if int(el) > 9:
                index = int(el) - 10
                el = letters[index]
                digitArr[loc] = el
            loc += 1
        return digitArr

    #Updates the stars by speeding them up and moving them.
    def updateStars(self, altersBackground = False):
        #Determines if background or foreground stars need to be updated.
        if altersBackground:
            arr = self.backGroundStars
        else:
            arr = self.starArr

        #Increases star velocity and moves every star in the list.
        for el in arr:
            el.speedUp(0.25)
            el.moveStar()
            self.window.update()

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Updates the starfield based on the new information.
    def starfieldUpdate(self):
        #Deletes excess stars if too many show up.
        if len(self.starArr) >= 1600:
            self.delStars()
            self.starArr = []
            self.updateStars(True)

        #Spawns new stars at regular intervals.
        if self.starFlag % 300 == 0:
            if self.isNotFirstTime:
                self.createStars(400)
                self.updateStars(True)

        #Updates stars and increments.
        self.updateStars()
        self.starFlag += 1
        self.isNotFirstTime = True
        self.window.after(1, self.starfieldUpdate)

    #Deletes every star in the star array.
    def delStars(self):
        for star in self.starArr:
            star.delete()

#This class is used to represent every star in the starfield.
class Star():
    def __init__(self, starDeg, hype, starSize, color, canvas, slow = 82):
        self.deg = starDeg
        self.hyp = hype
        self.size = starSize
        self.color = color
        self.canvas = canvas
        self.slowFactor = slow
        x = 400 + hype * math.cos(math.radians(starDeg - 90))
        y = 400 + hype * math.sin(math.radians(starDeg - 90))
        self.x = x
        self.y = y
        self.size = starSize
        self.starDraw = self.canvas.create_oval(x, y, x + starSize, y + starSize, width = 0, fill = color)

    #Moves star based on its current position and velocity.
    def moveStar(self):
        if self.starDraw != None:
            self.canvas.move(self.starDraw, self.hyp * math.cos(math.radians(self.deg - 90)) / self.slowFactor, self.hyp * math.sin(math.radians(self.deg - 90)) / self.slowFactor)

    #Changes color of star to new color.
    def colorChange(self, newColor):
        self.canvas.itemconfig(self.starDraw, fill = newColor)

    #Destroys star when called.
    def delete(self):
        self.canvas.delete(self.starDraw)
        self.starDraw = None

    #Speeds up star by a certain amount.
    def speedUp(self, amount):
        if self.slowFactor - amount <= 0:
            self.slowFactor = 1
            return
        self.slowFactor -= amount

    #Increases size of a star by a certain number of pixels.
    def sizeIncrease(self, pixNum):
        self.delete()
        self.starDraw = self.canvas.create_oval(self.x, self.y, self.x + self.size + pixNum, self.y + self.size + pixNum, width = 0, fill = self.color)
        self.size += pixNum

def main():
    root = Tk()
    root.title("Starfield")
    metric = Starfield(root)
    root.mainloop()

if __name__ == "__main__":
    main()
