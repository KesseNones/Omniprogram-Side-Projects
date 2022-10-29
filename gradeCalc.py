class GradeCalc(object):

    def __init__(self):
        self.catScoreList = []
        self.catValList = []
        self.calcList = []
        self.isHundred = False

    def process(self):
        while self.isHundred == False:
            self.inp()
            self.checkHundred()
            if self.isHundred:
                self.isHundred = True
                grade = self.grdCalc()
                grade = round(grade, 3)
                print("Grade is: " + str(grade) + "% (" + self.letterGradeCalc(float(grade)) + ")")
                self.reset()

    def reset(self):
        resetOrNo = input("Calculate Another Grade (Y/N)? ").upper()
        print("------------------------------------------------------------")
        if resetOrNo == "Y":
            self.catScoreList = []
            self.catValList = []
            self.calcList = []
            self.isHundred = False
            self.process()
        else:
            exit()

    def inp(self):
        isFinished = input("Finished (Y/N)? ").upper()
        if isFinished == "N":
            score = float(input("Enter Category Score (0 to 100): ")) / 100
            val = float(input("Enter Category Value (0 to 100): ")) / 100
            if score > 1:
                score = 1
            if score < 0:
                score = 0
            if val > 1:
                val = 1
            if val < 0:
                val = 0
            self.catScoreList.append(score)
            self.catValList.append(val)
            # print(self.catScoreList)
            # print(self.catValList)
            return
        else:
            if len(self.catScoreList) == 0:
                self.isHundred = True
                return
            else:
                self.equilizer()
                self.isHundred = True
        # print(self.catScoreList)
        # print(self.catValList)

    def equilizer(self):
        sumat = 0
        for el in self.catValList:
            sumat += el
        diff = 1 - sumat
        diff = diff / len(self.catValList)
        # print(diff)
        # print(self.catValList)
        pos = 0
        while pos < len(self.catValList):
            self.catValList[pos] += diff
            pos += 1
        #print(self.catValList)

    def checkHundred(self):
        sumat = 0
        for el in self.catValList:
            sumat += el
            if sumat >= 1.0:
                self.isHundred = True
                return True
        return False

    def grdCalc(self):
        pos = 0
        grdSum = 0
        while pos < len(self.catScoreList):
            #print(self.calcList)
            self.calcList.append(self.catScoreList[pos] * self.catValList[pos])
            pos += 1
        pos = 0
        while pos < len(self.catValList):
            grdSum += self.calcList[pos]
            pos += 1
        grdSum *= 100
        return grdSum

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

def main():
    grd = GradeCalc()
    grd.process()

if __name__ == "__main__":
    main()