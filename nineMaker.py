#Jesse A. Jones
#Version: 2023-05-31.12

from time import sleep
from tkinter import *
from math import log10

#This class hosts a crappy bootleg of cookie clicker 
#   that involves making nines. You can click the nine 
#   and also buy some upgrades using nines. It's kinda ass.
class NineMake(object):
    def __init__(self, window = None):
        self.window = window

        #Top frame holds quit button, save button, and load button.
        self.frameTop = Frame(self.window)
        self.frameTop.grid(row = 0, column = 0)

        #Quits game when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 0)
        
        #Saves game when pressed.
        self.saveButton = Button(self.frameTop, text = "Save",
            font = "Ariel 20", command = self.saveGame)
        self.saveButton.grid(row = 0, column = 1)

        #Loads game when pressed.
        self.loadButton = Button(self.frameTop, text = "Load",
            font = "Ariel 20", command = self.loadGame)
        self.loadButton.grid(row = 0, column = 2)

        #Holds clickable nine and nine amount.
        self.frameBottom = Frame(self.window)
        self.frameBottom.grid(row = 1, column = 0)

        #Clickable nine drawing made.
        self.draw = Canvas(self.frameBottom, width = 400, height = 400, 
            bg = "white", highlightbackground = "black", highlightthickness = 1)
        self.mouseInput = self.draw.bind("<Button-1>", self.mouse)
        self.draw.grid(row = 0, column = 0)
        self.nine = self.draw.create_text(200, 250, text = "9", font = "Times 320")

        #Displays how many nines exist.
        self.nineCount = self.draw.create_text(200, 50, text = "0.0", font = "Times 30", width = 300, anchor = CENTER)

        #Holds upgrade buttons, counts, and prices.
        self.sideFrame = Frame(self.window)
        self.sideFrame.grid(row = 1, column = 1)
        self.milisecondCount = 0

        #Tracks how many nines exist.
        self.nineAmount = 0.0

        #Auto replication, manual conversion, 
        #   and replication efficiency upgrade buttons.
        self.autoRep = UpgradeButton(self.sideFrame, "Auto Replication", 0, 9, 0, 0, 0, self.increaseRepRate, "AutoRep")
        self.manualConvert = UpgradeButton(self.sideFrame, "Manual Conversion Upgrade", 1, 9, 0, 1, 0, self.increaseManualDestruct, "ManualConvert")
        self.replicationEfficiencyUpgrade = UpgradeButton(self.sideFrame, "Replication Efficiency", 1, 9999, 0, 2, 0, self.increaseEfficiency, "RepEfficiency")

        #Holds information about nine upgrades for saving and loading.
        self.nineInfoArr = [self.nineAmount, self.autoRep, self.manualConvert, self.replicationEfficiencyUpgrade]
        #Creates some initial game displays for viewing.
        self.updateEff()
        self.updateManualDestructDisplay()
        self.updateRepCountAndPrice()

        #Starts auto increasing loop if auto replication exists.
        self.autoIncrease()

    #Saves game to a txt called nineSave.
    def saveGame(self):
        isFirst = True
        with open("nineSave.txt", "w") as save:
            for el in self.nineInfoArr:
                #Writes nine amount to save.
                if isFirst:
                    save.write(str(self.nineAmount) + "\n")
                    isFirst = False
                else:
                    #Writes upgrade info to save.
                    save.write(str(el.effect) + " ")
                    save.write(str(el.price) + " ")
                    save.write(str(el.count) + "\n")

    #Loads data from nine save into memory for game to work.
    def loadGame(self):
        isFirst = True
        index = 0
        with open("nineSave.txt", "r") as load:
            for line in load:
                #Reads nine amount in from save.
                if isFirst:
                    self.nineAmount = float(line.split()[0])
                    isFirst = False
                else:
                    #Reads upgrade into from save.
                    parse = line.split()
                    self.nineInfoArr[index].effect = float(parse[0])
                    self.nineInfoArr[index].price = float(parse[1])
                    self.nineInfoArr[index].count = float(parse[2])

                index += 1

        #Updates result of loading.
        self.updateNineDisp()
        self.updateRepCountAndPrice()
        self.updateManualDestructDisplay()
        self.updateEff()

    #Loops and automatically increases nine amount 
    #   by any automatic effects while also updating the nine display.
    def autoIncrease(self):
        self.milisecondCount += 1

        #Resets milisecond count if it gets too chunky.
        if self.milisecondCount % 4000000000 == 0:
            self.milisecondCount = 1

        #Increases nine amount and updates display every half second.
        if self.milisecondCount % 500 == 0:
            self.nineAmount += int(self.autoRep.effect * self.replicationEfficiencyUpgrade.effect)
            self.updateNineDisp()

        #Auto save mechanic. Auto saves every two minutes.
        if self.milisecondCount % 120000 == 0:
            self.saveGame()

        #Recursively loops to auto update again.
        self.frameBottom.after(1, self.autoIncrease)

    #Increases replication efficiency when called 
    #   if the player can affort the upgrade.
    def increaseEfficiency(self):
        if self.nineAmount - self.replicationEfficiencyUpgrade.price >= 0:
            #Increases replication efficiency and makes it an int for some reason???
            self.replicationEfficiencyUpgrade.effect *= 1.9

            #Subtracts price of upgrade from nine amount and updates display.
            self.nineAmount -= int(self.replicationEfficiencyUpgrade.price)
            self.updateNineDisp()

            #Increases price and count and updates to display new numbers.
            self.replicationEfficiencyUpgrade.price *= 99
            self.replicationEfficiencyUpgrade.count += 1
            self.updateEff()

    #Updates the price and multiplyer for the replication efficiency.
    def updateEff(self):
        self.replicationEfficiencyUpgrade.priceLabel["text"] = "Price " + self.numbConv(self.replicationEfficiencyUpgrade.price)
        self.replicationEfficiencyUpgrade.countLabel["text"] = "AutoRep * " + self.numbConv(self.replicationEfficiencyUpgrade.count)
        self.window.update()

    #Increases the manual destruct abilities of the user if they can afford it.
    def increaseManualDestruct(self):
        if self.nineAmount - self.manualConvert.price >= 0:
            #Increases manual destruction abilities.
            self.manualConvert.effect *= 1.5

            #Updates nine amount.
            self.nineAmount -= int(self.manualConvert.price)
            self.updateNineDisp()
            
            #Increases price, and updates result.
            self.manualConvert.price *= 1.8
            self.manualConvert.count += 1
            self.updateManualDestructDisplay()
    
    #Updates price and mult of manual destruction.
    def updateManualDestructDisplay(self):
        self.manualConvert.priceLabel["text"] = "Price " + self.numbConv(self.manualConvert.price)
        self.manualConvert.countLabel["text"] = "ManualConvert * " + self.numbConv(self.manualConvert.count)
        self.window.update()

    #Increases auto replication rate of nines for user if they can afford it.
    def increaseRepRate(self):
        if self.nineAmount - self.autoRep.price >= 0:
            #Updates auto replication effect.
            self.autoRep.effect = (self.autoRep.effect * 1.5) + (self.autoRep.effect == 0)

            #Decreases nine amount based on price and updates display.
            self.nineAmount -= int(self.autoRep.price)
            self.updateNineDisp()

            #Updates upgrade price and count, displaying the result.
            self.autoRep.price *= 1.6
            self.autoRep.count += 1
            self.updateRepCountAndPrice()

    #Updates price and multiplier of auto replication.
    def updateRepCountAndPrice(self):
        self.autoRep.priceLabel["text"] = "Price " + self.numbConv(self.autoRep.price)
        self.autoRep.countLabel["text"] = "AutoRep * " + self.numbConv(self.autoRep.count)
        self.window.update()

    #Updates count of nines existing.
    def updateNineDisp(self):
        sciNotArr = self.numToSciNot(self.nineAmount)
        num = sciNotArr[0] * (10 ** (sciNotArr[1] % 3))
        num = round(num, 3)
        name = self.expToName(sciNotArr[1])
        self.draw.itemconfig(self.nineCount, text = f"{num} {name}")
        self.draw.update()

    #Takes in a number and returns the number 
    #   and the name of its thousand multiple in a string together.
    def numbConv(self, num):
        sciNotArr = self.numToSciNot(num)
        num = sciNotArr[0] * (10 ** (sciNotArr[1] % 3))
        num = round(num, 3)
        name = self.expToName(sciNotArr[1])
        return f"{num} {name}"

    #Increases number of nines.
    def increaseNine(self):
        self.nineAmount += 1 * int(self.manualConvert.effect)
        self.updateNineDisp()

    #Detects when the nine is clicked and acts accordingly.
    def mouse(self, event):
        x = event.x
        y = event.y
        if (300 >= x >= 100) and (413 >= y >= 92):
            self.increaseNine()
            self.animateNine()

    #Animates the nine being clicked.
    def animateNine(self):
        self.draw.itemconfig(self.nine, font = "Times 270")
        self.draw.update()
        sleep(0.09)
        self.draw.itemconfig(self.nine, font = "Times 320")
        self.draw.update()

    #Quits program when clicked.
    def quitButtonAction(self):
        self.window.destroy()

    #Takes an input number and breaks it down 
    #   into its decimal compoenent and exponent.
    def numToSciNot(self, num):
        #Parses input number to see if it's 0.
        if num == 0:
            return [0.0, 0]
        
        logNum = log10(num)

        exp = int(logNum)
        decNum = round((10 ** (logNum - exp)), 3)

        return [decNum, exp]     

    #Takes in an exponent and returns the name of the thousand power it's in.
    def expToName(self, exp):
        #Holds all exponent thousand multiple names.
        nameList = ["", "thousand", "million", "billion", 
                    "trillion", "quadrillion", "quintillion", 
                    "sextillion", "septillion", "octillion", 
                    "nonillion", "decillion", "undecillion", 
                    "duodecillion", "tredecillion", "quattuordecillion", 
                    "quindecillion", "sexdecillion", "septendecillion",
                    "octodecillion", "novemdecillion", "vigintillion",
                    "unvigintillion", "duovigintillion", "tresvigintillion",
                    "quattuorvigintillion", "quinvigintillion", "sesvigintillion"
                    "septemvigintillion", "octovigintillion", "novemvigintillion",
                    "trigintillion", "untrigintillion", "duotrigintillion",
                    "trestrigintillion", "quattuortrigintillion", "quintrigintillion",
                    "sestrigintillion", "septentrigintillion", "octotrigintillion", 
                    "noventrigintillion", "quadragintillion", "unquadragintillion", 
                    "duoquadragintillion", "tresquadragintillion", "quattuorquadragintillion", 
                    "quinquequadragintillion", "sesquadragintillion", "septenquadragintillion",
                    "octoquadragintillion", "novemquadragintillion", "quinquagintillion",
                    "unquinquagintillion", "duoquinquagintillion", "trequinquagintillion",
                    "quattuorquinquagintillion", "quinquenquinquagintillion", "sesquinquagintillion",
                    "septenquinquagintillion", "octoquinquagintillion", "novemquinquagintillion",
                    "sexagintillion", "unsexagintillion", "duosexagintillion",
                    "tresexagintillion", "quattuorsexagintillion", "quinquesexagintillion",
                    "sessexagintillion", "septensexagintillion", "octosexagintillion",
                    "novemsexagintillion", "septuagintillion", "unseptuagintillion",
                    "duoseptuagintillion", "treseptuagintillion", "quattuorseptuagintillion", 
                    "quinqueseptuagintillion", "sesseptuagintillion", "septenseptuagintillion", 
                    "octoseptuagintillion", "novemseptuagintillion", "octogintillion", 
                    "unoctogintillion", "duooctogintillion", "tresoctogintillion", 
                    "quattuoroctogintillion", "quinqueoctogintillion", "sesoctogintillion", 
                    "septenoctogintillion", "octumoctogintillion", "novemoctogintillion", 
                    "nonagintillion", "unonagintillion", "duononagintillion", 
                    "tresnonagintillion", "quattuornonagintillion", "quinquenonagintillion", 
                    "sesnonagintillion", "septennonagintillion", "octononagintillion", 
                    "novemnonagintillion", "centillion", "uncentillion", "duocentillion"]

        index = abs(exp) // 3

        return nameList[index]

#This class holds all info and sets up 
#   a particular upgrade button for the nine maker.
class UpgradeButton():
    def __init__(self, frame, name, baseEffect, price, count, row, col, cmd, nameOfCount = "num"):
        self.effect = baseEffect
        self.price = price
        self.count = count

        #Actual button with the name.
        self.autoReplicationUpgrade = Button(frame, text = name,
            font = "Ariel 30", command = cmd)
        self.autoReplicationUpgrade.grid(row = row * 3, column = col)

        #Displays price of upgrade.
        self.priceLabel = Label(frame, text = "Price " + str(self.price), font = "Times 25", anchor = "e")
        self.priceLabel.grid(row = row * 3 + 1, column = col)
        
        #Displays multiplier of upgrade.
        self.countLabel = Label(frame, text = nameOfCount + " * " + str(self.count), font = "Times 25", anchor = "w")
        self.countLabel.grid(row = row * 3 + 2, column = col)

def main():
    root = Tk()
    root.title("Nine Maker (Cookie Clicker Bootleg)")
    metric = NineMake(root)
    root.mainloop()

if __name__ == "__main__":
    main()
