import random
from time import sleep
import time
import datetime
from tkinter import *
import math
from tkinter import messagebox
import tkinter as tk

class NineMake(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.grid(row = 0, column = 0)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)
        
        self.saveButton = Button(self.frameTop, text = "Save",
            font = "Ariel 20", command = self.saveGame)
        self.saveButton.grid(row = 0, column = 1)

        self.loadButton = Button(self.frameTop, text = "Load",
            font = "Ariel 20", command = self.loadGame)
        self.loadButton.grid(row = 0, column = 2)

        self.frameBottom = Frame(self.window)
        self.frameBottom.grid(row = 1, column = 0)

        self.draw = Canvas(self.frameBottom, width = 800, height = 800, 
            bg = "white", highlightbackground = "black", highlightthickness = 2)
        self.mouseInput = self.draw.bind("<Button-1>", self.mouse)
        self.draw.grid(row = 0, column = 0)
        self.nine = self.draw.create_text(400, 500, text = "9", font = "Times 640")

        self.nineCount = self.draw.create_text(400, 100, text = "0", font = "Times 60", width = 600, anchor = CENTER)

        self.sideFrame = Frame(self.window)
        self.sideFrame.grid(row = 1, column = 1)
        self.saveFlag = 0

        self.nineAmount = 0.0

        self.autoRep = UpgradeButton(self.sideFrame, "Auto Replication", 0, 9, 0, 0, 0, self.increaseRepRate, "AutoRep")
        self.manualConvert = UpgradeButton(self.sideFrame, "Manual Conversion Upgrade", 1, 9, 0, 1, 0, self.increaseManualDestruct, "ManualConvert")
        self.replicationEfficiencyUpgrade = UpgradeButton(self.sideFrame, "Replication Efficiency", 1, 9999, 0, 2, 0, self.increaseEfficiency, "RepEfficiency")

        # self.replicationRate = 0
        # self.autoRepPrice = 9
        # self.autoRepUpgradCount = 0
        # self.nineClickMult = 1
        # self.manualConvPrice = 9
        # self.manualConvQuant = 0

        # #////////////////////////////
        self.nineInfoArr = [self.autoRep, self.manualConvert, self.replicationEfficiencyUpgrade]
        self.updateEff()
        self.updateManualDestructDisplay()
        self.updateRepCountAndPrice()
        #self.nineInfoArr = [self.nineAmount, self.replicationRate, self.autoRepPrice, self.autoRepUpgradCount, self.nineClickMult, self.manualConvPrice, self.manualConvQuant]
        # #////////////////////////////

        # self.autoReplicationUpgradePrice = Label(self.sideFrame, text = "Price " + str(self.autoRepPrice), font = "Times 50", anchor = "e")
        # self.autoReplicationUpgradePrice.grid(row = 1, column = 0)
        
        # self.autoReplicationUpgradeCount = Label(self.sideFrame, text = "AutoRep * " + str(self.autoRepUpgradCount), font = "Times 50", anchor = "w")
        # self.autoReplicationUpgradeCount.grid(row = 2, column = 0)

        # self.autoReplicationUpgrade = Button(self.sideFrame, text = "Auto-Replication",
        #     font = "Ariel 30", command = self.increaseRepRate)
        # self.autoReplicationUpgrade.grid(row = 0, column = 0)

        # self.manDesPrice = Label(self.sideFrame, text = "Price " + str(self.manualConvPrice), font = "Times 50", anchor = "e")
        # self.manDesPrice.grid(row = 4, column = 0)
        
        # self.manDesCount = Label(self.sideFrame, text = "ManualConvert * " + str(self.manualConvQuant), font = "Times 50", anchor = "w")
        # self.manDesCount.grid(row = 5, column = 0)

        # self.manualDestructUpgrade = Button(self.sideFrame, text = "Manual Conversion Boost",
        #     font = "Ariel 30", command = self.increaseManualDestruct)
        # self.manualDestructUpgrade.grid(row = 3, column = 0)

        self.autoIncrease()

    def saveGame(self):
        with open("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/nineSave.txt", "w") as save:
            save.write(str(self.nineAmount) + "\n")
            for el in self.nineInfoArr:
                save.write(str(el.effect) + " ")
                save.write(str(el.price) + " ")
                save.write(str(el.count) + "\n")
            #save.close()

    def loadGame(self):
        nineIndex = 0
        with open("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/nineSave.txt", "r") as load:
            for line in load:
                if nineIndex == 0:
                    self.nineAmount = int(line[:-3].strip())
                    nineIndex += 1
                else:
                    lineArr = line.strip().split(" ")
                    #print(lineArr)
                    self.nineInfoArr[nineIndex - 1].effect = int(lineArr[0])
                    self.nineInfoArr[nineIndex - 1].price = int(lineArr[1])
                    self.nineInfoArr[nineIndex - 1].count = int(lineArr[2])
                    nineIndex += 1
        self.updateNineDisp()
        self.updateRepCountAndPrice()
        self.updateManualDestructDisplay()
        self.updateEff()

    def autoIncrease(self):
        self.saveFlag += 1
        self.nineAmount += (self.nineInfoArr[0].effect * self.nineInfoArr[2].effect)
        self.updateNineDisp()
        if self.saveFlag % 120 == 0:
            self.saveGame()
            print("saved")
        self.frameBottom.after(1000, self.autoIncrease)

    def increaseEfficiency(self):
        if self.nineAmount - self.nineInfoArr[2].price >= 0:
            if self.nineInfoArr[2].effect == 1:
                self.nineInfoArr[2].effect += 1
            self.nineInfoArr[2].effect *= 1.9
            self.nineInfoArr[2].effect = int(self.nineInfoArr[2].effect)
            self.nineAmount -= self.nineInfoArr[2].price
            self.updateNineDisp()
            self.nineInfoArr[2].price *= 99
            self.nineInfoArr[2].price = int(self.nineInfoArr[2].price)
            self.nineInfoArr[2].count += 1
            self.updateEff()

    def updateEff(self):
        self.replicationEfficiencyUpgrade.priceLabel["text"] = "Price " + self.numbConv(self.nineInfoArr[2].price)
        self.replicationEfficiencyUpgrade.countLabel["text"] = "AutoRep * " + self.numbConv(self.nineInfoArr[2].count)
        self.window.update()

    def increaseManualDestruct(self):
        if self.nineAmount - self.nineInfoArr[1].price >= 0:
            if self.nineInfoArr[1].effect == 1:
                self.nineInfoArr[1].effect += 1
            self.nineInfoArr[1].effect *= 1.5
            self.nineInfoArr[1].effect = int(self.nineInfoArr[1].effect)
            self.nineAmount -= self.nineInfoArr[1].price
            self.updateNineDisp()
            self.nineInfoArr[1].price *= 1.8
            self.nineInfoArr[1].price = int(self.nineInfoArr[1].price)
            self.nineInfoArr[1].count += 1
            self.updateManualDestructDisplay()

    def increaseRepRate(self):
        if self.nineAmount - self.nineInfoArr[0].price >= 0:
            if self.nineInfoArr[0].effect == 0:
                self.nineInfoArr[0].effect = 2
            else:
                self.nineInfoArr[0].effect *= 1.5
                self.nineInfoArr[0].effect = int(self.nineInfoArr[0].effect)
            self.nineAmount -= self.nineInfoArr[0].price
            self.updateNineDisp()
            self.nineInfoArr[0].price *= 1.6
            self.nineInfoArr[0].price = int(self.nineInfoArr[0].price)
            self.nineInfoArr[0].count += 1
            self.updateRepCountAndPrice()

    def updateRepCountAndPrice(self):
        self.autoRep.priceLabel["text"] = "Price " + self.numbConv(self.nineInfoArr[0].price)
        self.autoRep.countLabel["text"] = "AutoRep * " + self.numbConv(self.nineInfoArr[0].count)
        self.window.update()

    def updateManualDestructDisplay(self):
        self.manualConvert.priceLabel["text"] = "Price " + self.numbConv(self.nineInfoArr[1].price)
        self.manualConvert.countLabel["text"] = "ManualConvert * " + self.numbConv(self.nineInfoArr[1].count)
        self.window.update()

    def updateNineDisp(self):
        nineCount = self.numbConv(self.nineAmount)
        if self.nineAmount > 1000:
            nineCount = str(nineCount).zfill(6)
        self.draw.itemconfig(self.nineCount, text = (str(nineCount) + ""))
        self.draw.update()

    def increaseNine(self):
        self.nineAmount += 1 * self.nineInfoArr[1].effect
        self.updateNineDisp()

    def mouse(self, event):
        #print(event.x, event.y)
        x = event.x
        y = event.y
        if (600 >= x >= 200) and (825 >= y >= 183):
            self.increaseNine()
            self.animateNine()

    def animateNine(self):
        self.draw.itemconfig(self.nine, font = "Times 540")
        self.draw.update()
        sleep(0.09)
        self.draw.itemconfig(self.nine, font = "Times 640")
        self.draw.update()

    def quitButtonAction(self):
        self.window.destroy()

    def logGet(self, numb):
        iterator = 0
        numb = abs(numb)
        if numb >= 1.797693e+308:
            return 308
        while True:
            numb = numb / 10
            if numb >= 1:
                iterator += 1
            else:
                break
        return iterator

    def numbConv(self, number):
        numbOrig = float(number)
        logo = self.logGet(numbOrig)
        logo = logo - (logo % 3)
        numbAlt = numbOrig / (10 ** logo)
        numbAlt = round(numbAlt, 3)
        if 0 <= logo < 3:
            self.stringNumber = ""
        elif 6 > logo >= 3:
            self.stringNumber = "thousand"
        elif 9 > logo >= 6:
            self.stringNumber = "million"
        elif 12 > logo >= 9:
            self.stringNumber = "billion"
        elif 15 > logo >= 12:
            self.stringNumber = "trillion"
        elif 18 > logo >= 15:
            self.stringNumber = "quadrillion"
        elif 21 > logo >= 18:
            self.stringNumber = "quintillion"
        elif 24 > logo >= 21:
            self.stringNumber = "sextillion"
        elif 27 > logo >= 24:
            self.stringNumber = "septillion"
        elif 30 > logo >= 27:
            self.stringNumber = "octillion"
        elif 33 > logo >= 30:
            self.stringNumber = "nonillion"
        elif 36 > logo >= 33:
            self.stringNumber = "decillion"
        elif 39 > logo >= 36:
            self.stringNumber = "undecillion"
        elif 42 > logo >= 39:
            self.stringNumber = "duodecillion"
        elif 45 > logo >= 42:
            self.stringNumber = "tredecillion"
        elif 48 > logo >= 45:
            self.stringNumber = "quattuordecillion"
        elif 51 > logo >= 48:
            self.stringNumber = "quindecillion"
        elif 54 > logo >= 51:
            self.stringNumber = "sexdecillion"
        elif 57 > logo >= 54:
            self.stringNumber = "septendecillion"
        elif 60 > logo >= 57:
            self.stringNumber = "octodecillion"
        elif 63 > logo >= 60:
            self.stringNumber = "novemdecillion"
        elif 66 > logo >= 63:
            self.stringNumber = "vigintillion"
        elif 69 > logo >= 66:
            self.stringNumber = "unvigintillion"
        elif 72 > logo >= 69:
            self.stringNumber = "duovigintillion"
        elif 75 > logo >= 72:
            self.stringNumber = "tresvigintillion"
        elif 78 > logo >= 75:
            self.stringNumber = "quattuorvigintillion"
        elif 81 > logo >= 78:
            self.stringNumber = "quinvigintillion"
        elif 84 > logo >= 81:
            self.stringNumber = "sesvigintillion"
        elif 87 > logo >= 84:
            self.stringNumber = "septemvigintillion"
        elif 90 > logo >= 87:
            self.stringNumber = "octovigintillion"
        elif 93 > logo >= 90:
            self.stringNumber = "novemvigintillion"
        elif 96 > logo >= 93:
            self.stringNumber = "trigintillion"
        elif 99 > logo >= 96:
            self.stringNumber = "untrigintillion"
        elif 102 > logo >= 99:
            self.stringNumber = "duotrigintillion"
        elif 105 > logo >= 102:
            self.stringNumber = "trestrigintillion"
        elif 108 > logo >= 105:
            self.stringNumber = "quattuortrigintillion"
        elif 111 > logo >= 118:
            self.stringNumber = "quintrigintillion"
        elif 114 > logo >= 111:
            self.stringNumber = "sestrigintillion"
        elif 117 > logo >= 114:
            self.stringNumber = "septentrigintillion"
        elif 120 > logo >= 117:
            self.stringNumber = "octotrigintillion"
        elif 123 > logo >= 120:
            self.stringNumber = "noventrigintillion"
        elif 126 > logo >= 123:
            self.stringNumber = "quadragintillion"
        elif 129 > logo >= 126:
            self.stringNumber = "unquadragintillion"
        elif 132 > logo >= 129:
            self.stringNumber = "duoquadragintillion"
        elif 135 > logo >= 132:
            self.stringNumber = "tresquadragintillion"
        elif 138 > logo >= 135:
            self.stringNumber = "quattuorquadragintillion"
        elif 141 > logo >= 138:
            self.stringNumber = "quinquequadragintillion"
        elif 144 > logo >= 141:
            self.stringNumber = "sesquadragintillion"
        elif 147 > logo >= 144:
            self.stringNumber = "septenquadragintillion"
        elif 150 > logo >= 147:
            self.stringNumber = "octoquadragintillion"
        elif 153 > logo >= 150:
            self.stringNumber = "novemquadragintillion"
        elif 156 > logo >= 153:
            self.stringNumber = "quinquagintillion"
        elif 159 > logo >= 156:
            self.stringNumber = "unquinquagintillion"
        elif 162 > logo >= 159:
            self.stringNumber = "duoquinquagintillion"
        elif 165 > logo >= 162:
            self.stringNumber = "trequinquagintillion"
        elif 168 > logo >= 165:
            self.stringNumber = "quattuorquinquagintillion"
        elif 171 > logo >= 168:
            self.stringNumber = "quinquenquinquagintillion"
        elif 174 > logo >= 171:
            self.stringNumber = "sesquinquagintillion"
        elif 177 > logo >= 174:
            self.stringNumber = "septenquinquagintillion"
        elif 180 > logo >= 177:
            self.stringNumber = "octoquinquagintillion"
        elif 183 > logo >= 180:
            self.stringNumber = "novemquinquagintillion"
        elif 186 > logo >= 183:
            self.stringNumber = "sexagintillion"
        elif 189 > logo >= 186:
            self.stringNumber = "unsexagintillion"
        elif 192 > logo >= 189:
            self.stringNumber = "duosexagintillion"
        elif 195 > logo >= 192:
            self.stringNumber = "tresexagintillion"
        elif 198 > logo >= 195:
            self.stringNumber = "quattuorsexagintillion"
        elif 201 > logo >= 198:
            self.stringNumber = "quinquesexagintillion"
        elif 204 > logo >= 201:
            self.stringNumber = "sessexagintillion"
        elif 207 > logo >= 204:
            self.stringNumber = "septensexagintillion"
        elif 210 > logo >= 207:
            self.stringNumber = "octosexagintillion"
        elif 213 > logo >= 210:
            self.stringNumber = "novemsexagintillion"
        elif 216 > logo >= 213:
            self.stringNumber = "septuagintillion"
        elif 219 > logo >= 216:
            self.stringNumber = "unseptuagintillion"
        elif 222 > logo >= 219:
            self.stringNumber = "duoseptuagintillion"
        elif 225 > logo >= 222:
            self.stringNumber = "treseptuagintillion"
        elif 228 > logo >= 225:
            self.stringNumber = "quattuorseptuagintillion"
        elif 231 > logo >= 228:
            self.stringNumber = "quinqueseptuagintillion"
        elif 234 > logo >= 231:
            self.stringNumber = "sesseptuagintillion"
        elif 237 > logo >= 234:
            self.stringNumber = "septenseptuagintillion"
        elif 240 > logo >= 237:
            self.stringNumber = "octoseptuagintillion"
        elif 243 > logo >= 240:
            self.stringNumber = "novemseptuagintillion"
        elif 246 > logo >= 243:
            self.stringNumber = "octogintillion"
        elif 249 > logo >= 246:
            self.stringNumber = "unoctogintillion"
        elif 252 > logo >= 249:
            self.stringNumber = "duooctogintillion"
        elif 255 > logo >= 252:
            self.stringNumber = "tresoctogintillion"
        elif 258 > logo >= 255:
            self.stringNumber = "quattuoroctogintillion"
        elif 261 > logo >= 258:
            self.stringNumber = "quinqueoctogintillion"
        elif 264 > logo >= 261:
            self.stringNumber = "sesoctogintillion"
        elif 267 > logo >= 264:
            self.stringNumber = "septenoctogintillion"
        elif 270 > logo >= 267:
            self.stringNumber = "octumoctogintillion"
        elif 273 > logo >= 270:
            self.stringNumber = "novemoctogintillion"
        elif 276 > logo >= 273:
            self.stringNumber = "nonagintillion"
        elif 279 > logo >= 276:
            self.stringNumber = "unonagintillion"
        elif 282 > logo >= 279:
            self.stringNumber = "duononagintillion"
        elif 285 > logo >= 282:
            self.stringNumber = "tresnonagintillion"
        elif 288 > logo >= 285:
            self.stringNumber = "quattuornonagintillion"
        elif 291 > logo >= 288:
            self.stringNumber = "quinquenonagintillion"
        elif 294 > logo >= 291:
            self.stringNumber = "sesnonagintillion"
        elif 297 > logo >= 294:
            self.stringNumber = "septennonagintillion"
        elif 300 > logo >= 297:
            self.stringNumber = "octononagintillion"
        elif 303 > logo >= 300:
            self.stringNumber = "novemnonagintillion"
        elif 306 > logo >= 303:
            self.stringNumber = "centillion"
        else:
            self.stringNumber = "uncentillion"
        return str(numbAlt) + " " + self.stringNumber

class UpgradeButton():
    def __init__(self, frame, name, baseEffect, price, count, row, col, cmd, nameOfCount = "num"):
        self.effect = baseEffect
        self.price = price
        self.count = count

        self.autoReplicationUpgrade = Button(frame, text = name,
            font = "Ariel 30", command = cmd)
        self.autoReplicationUpgrade.grid(row = row * 3, column = col)

        self.priceLabel = Label(frame, text = "Price " + str(self.price), font = "Times 50", anchor = "e")
        self.priceLabel.grid(row = row * 3 + 1, column = col)
        
        self.countLabel = Label(frame, text = nameOfCount + " * " + str(self.count), font = "Times 50", anchor = "w")
        self.countLabel.grid(row = row * 3 + 2, column = col)

def main():
    root = Tk()
    root.title("Nine Maker (Cookie Clicker Bootleg)")
    metric = NineMake(root)
    root.mainloop()

if __name__ == "__main__":
    main()
