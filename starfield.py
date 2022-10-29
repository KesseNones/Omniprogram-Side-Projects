import random
from time import sleep
import time
import datetime
from tkinter import *
import math
from tkinter import messagebox
import tkinter as tk

class Starfield(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "black", highlightbackground = "black", highlightthickness = 2)
        self.mouseInput = self.draw.bind("<Button-1>", self.mouse)
        self.draw.grid(row = 0, column = 0)

        self.isNotFirstTime = False
        self.createBackgroundStars()
        self.starFlag = 0
        self.starArr = []
        self.createStars(600)

        self.starfieldUpdate()

    def mouse(self, event):
        print(event.x, event.y)

    def createBackgroundStars(self, hype = 600):
        self.backGroundStars = []
        while hype > 0:
            starSize = random.choice(range(1, 4))
            starPos = random.choice(range(0, 360))
            self.backGroundStars.append(Star(starPos, hype, starSize, "white", self.draw))
            hype -= 2
        self.window.update()

    def createStars(self, hype = 450):
        localStar = []
        hypeInit = hype
        while hype > 0:
            starSize = random.choice(range(1, 4))
            starPos = random.choice(range(0, 360))
            self.starArr.append(Star(starPos, hype, starSize, "white", self.draw))
            hype -= 2
        #localStar.append(self.starArr)
        #print(len(self.starArr))
        #self.megaStarArr.append(self.starArr)
        #self.megaColorArr.append(self.colorArr)
        if self.isNotFirstTime:
            self.starFadeIn(self.starArr, hypeInit)
        self.window.update()
        #time.sleep(1)
            
    def starFadeIn(self, starArray, hype):
        #65793
        #16777215
        colorNum = 0
        #print(self.megaStarArr, len(self.megaStarArr))
        #subColorArr = self.megaColorArr[-2]
        #print(subColorArr, len(self.megaColorArr))
        #print(starArray)
        #print(hype)
        start = ((hype // 2) * - 1)
        # print(starArray[-1])
        # print(increm)
        step = 65793
        while colorNum <= 16777215:
            for index in range(start, -1):
                hexNum = self.tenToOtherBase(colorNum, 16)
                hashtagHex = "#" + hexNum.zfill(6)
                starArray[index].colorChange(hashtagHex)
            self.updateStars()
            colorNum += step * 32
            #self.updateStars()
            self.window.update()
            #colorNum += 65793


    def baseAlg(self, num, base):
        digitArr = []
        if num == 0:
            return ["0"]
        while num > 0:
            digitArr.append(str(num % base))
            num = num // base
        return digitArr

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

    def updateStars(self, altersBackground = False):
        if altersBackground:
            arr = self.backGroundStars
        else:
            arr = self.starArr
        for el in arr:
            el.speedUp(0.25)
            #el.sizeIncrease(0.01)
            el.move()
            self.window.update()

    def quitButtonAction(self):
        self.window.destroy()

    def starfieldUpdate(self):
        if len(self.starArr) >= 1600:
            self.delStars()
            self.starArr = []
            self.updateStars(True)
        if self.starFlag % 300 == 0:
            if self.isNotFirstTime:
                self.createStars(400)
                self.updateStars(True)
        self.updateStars()
        self.starFlag += 1
        self.isNotFirstTime = True
        self.window.after(1, self.starfieldUpdate)

    def delStars(self):
        for star in self.starArr:
            star.delete()

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

    def move(self):
        self.canvas.move(self.starDraw, self.hyp * math.cos(math.radians(self.deg - 90)) / self.slowFactor, self.hyp * math.sin(math.radians(self.deg - 90)) / self.slowFactor)

    def colorChange(self, newColor):
        self.canvas.itemconfig(self.starDraw, fill = newColor)

    def delete(self):
        self.canvas.delete(self.starDraw)

    def speedUp(self, amount):
        if self.slowFactor - amount <= 0:
            self.slowFactor = 1
            return
        self.slowFactor -= amount

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
