#Jesse A. Jones
#Version: 2023-08-01.29

from tkinter import *
import dateHandling

#This class contains a gui weighted grade calculator.
#   It is recommended to not put more than ten 
#   or so entries in because it goes off the screen!
class GuiGradeCalc(object):
    #Sets up initial values and tk members.
    def __init__(self, window = None):
        self.catScoreList = []
        self.catValList = []
        self.calcList = []
        self.entryList = []
        self.entryCount = 0
        self.isHundred = False

        self.window = window

        #Top frame with quit button created.
        self.frameTop = Frame(self.window)
        self.frameTop.grid(row = 0, column = 0)
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Times 25", command = self.quitButtonAction)
        self.quitButton.pack()

        #Frame middle used to grade entries.
        self.frameMiddle = Frame(self.window)
        self.frameMiddle.grid(row = 1, column = 0)

        self.frameBottom = Frame(self.window)
        self.frameBottom.grid(row = 2, column = 0)

        #Buttons in bottom frame used for manipulating 
        #   number of entries in list and calculating the grade.
        self.add = Button(self.frameBottom, text = "Add Entry", 
            font = "Times 25", command = self.addEntry)
        self.add.grid(row = 0, column = 0)

        self.removeEntry = Button(self.frameBottom, text = "Pop Last", 
            font = "Times 25", command = self.popEntry)
        self.removeEntry.grid(row = 0, column = 1)

        self.convButton = Button(self.frameBottom, text = "Calculate Grade", 
            font = "Times 25", command = self.gradeCalc)
        self.convButton.grid(row = 0, column = 2)

        self.frameBottomest = Frame(self.window)
        self.frameBottomest.grid(row = 3, column = 0)

        self.gradeOutput = Label(self.frameBottomest, 
            text = "", 
            font = "Times 25")
        self.gradeOutput.grid(row = 1, column = 1)

        self.parse = dateHandling.GetDate()

    #Adds grade entry to list.
    def addEntry(self):
        newEntry = GradeEntry(self.frameMiddle, self.entryCount * 2)
        self.entryCount += 1

        self.entryList.append(newEntry)
        return

    #Gets rid of last grade entry from list.
    def popEntry(self):
        if self.entryCount > 0:
            self.entryList[self.entryCount - 1].delete()
            self.entryList.pop()
            self.entryCount -= 1
    
    #Converts user input into something more usable for the calculations.
    def inputHandler(self, entry):
        grade = 0
        value = 0
        entryDataArr = []
        
        #Gets initial user data.
        usrGrd = entry.catGrd.get()
        usrVal = entry.weightVal.get()
        
        #Casts user data if the entries were not empty.
        if usrGrd != "":
            grade = (self.parse.getGeneral(usrGrd)) / 100
        if usrVal != "":
            value = (self.parse.getGeneral(usrVal)) / 100

        #Makes sure grades stay in range 0 to 1.
        if (grade > 1):
            grade = 1
        if (value > 1):
            value = 1
        if (grade < 0):
            grade = 0
        if (value < 0):
            value = 0

        entryDataArr.append(grade)
        entryDataArr.append(value)

        return entryDataArr

    def gradeCalc(self):
        #Calculates grade from inputs if there 
        #   is at least one entry to get data from.
        if self.entryCount > 0:
            self.zeroCalcArrays()
            gradeAndWeightArr = []
            finalGrade = 0.0
            letterGrade = "F"

            #Retrieves values from all input entry fields,
            #   determines if they are valid, 
            #   and adds them to the appropriate arrays,
            #   all while the total category value hasn't hit 100 percent.
            for item in self.entryList:
                gradeAndWeightArr = self.inputHandler(item)
                self.catScoreList.append(gradeAndWeightArr[0])
                self.catValList.append(gradeAndWeightArr[1])
                if self.checkHundred():
                    break

            #Takes remaining non taken percentage 
            #   and distributes it to all the grade categories involved.
            if not self.checkHundred():
                self.equilizer()

            #Calculates weighted grade.
            finalGrade = self.grdCalc()
            letterGrade = self.letterGradeCalc(finalGrade)

            self.gradeOutput["text"] = f"Grade: {round(finalGrade, 3)}% ({letterGrade})"

    #Sets all calculatory arrays to empty, 
    #   so each grade calculation is fresh. 
    def zeroCalcArrays(self):
        self.catScoreList = []
        self.catValList = []
        self.calcList = []

    #Quits program when quit button pressed.
    def quitButtonAction(self):
        self.window.destroy()

    #Distributes any remaining percentage chunks 
    #   to the remaining grade elements.
    def equilizer(self):
        sumat = 0
        for el in self.catValList:
            sumat += el
        diff = 1 - sumat
        diff = diff / len(self.catValList)
        pos = 0
        while pos < len(self.catValList):
            self.catValList[pos] += diff
            pos += 1

    #Checks to see if a value of 1 (100%) has been reached 
    #   for the categories to add to.
    def checkHundred(self):
        sumat = 0
        for el in self.catValList:
            sumat += el
            if sumat >= 1.0:
                self.isHundred = True
                return True
        return False

    #Calculates grade based on data in catScoreList and catValList.
    def grdCalc(self):
        pos = 0
        grdSum = 0
        while pos < len(self.catScoreList):
            self.calcList.append(self.catScoreList[pos] * self.catValList[pos])
            pos += 1
        pos = 0
        while pos < len(self.catValList):
            grdSum += self.calcList[pos]
            pos += 1
        grdSum *= 100
        return grdSum

    #Converts passed in percentage to a letter grade.
    #Based on Skyward grade percentages from my old school district.
    def letterGradeCalc(self, perc):
        t = perc
        if t >= 92.5:
            L = "A"
        if 89.5 <= t < 92.5:
            L = "A-"
        if 86.5 <= t < 89.5:
            L = "B+"
        if 82.5 <= t < 86.5:
            L = "B"
        if 79.5 <= t < 82.50:
            L = "B-"
        if 76.5 <= t < 79.50:
            L = "C+"
        if 72.5 <= t < 76.50:
            L = "C"
        if 69.5 <= t < 72.50:
            L = "C-"
        if 64.5 <= t < 69.50:
            L = "D+"
        if 59.5 <= t < 64.5:
            L = "D"
        if t < 59.5:
            L = "F"
        return L

#This class contains members for each grade entry.
class GradeEntry():
    #Creates all entry members.
    def __init__(self, frame, row, col = 0):
        self.enterCat = Label(frame, 
            text = "Enter Category Grade:", 
            font = "Times 25")
        self.enterCat.grid(row = row, column = col)

        self.catGrd = Entry(frame, font = "Times 25")
        self.catGrd.grid(row = row + 1, column = col)

        self.enterWeight = Label(frame, 
            text = "Enter Category Weight:", 
            font = "Times 25")
        self.enterWeight.grid(row = row, column = col + 1)

        self.weightVal = Entry(frame, font = "Times 25")
        self.weightVal.grid(row = row + 1, column = col + 1)

    #Destroys all entry members.
    def delete(self):
        self.enterCat.destroy()
        self.catGrd.destroy()
        self.enterWeight.destroy()
        self.weightVal.destroy()
        return

def main():
    root = Tk()
    root.title("Calculate Weighted Grade GUI Edition")
    dateAndTime = GuiGradeCalc(root)
    root.mainloop()

if __name__ == "__main__":
    main()