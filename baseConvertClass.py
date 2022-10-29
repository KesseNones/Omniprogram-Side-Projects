class BaseConvert():

    def baseConv(self, numX, base, ch = 1, numOther = None):
    # Base Ten to Different Base System (1)
    # Any Base to Base Ten (2) 
        if ch == 1:
            convertedNum = self.tenToOtherBase(numX, base)
            return convertedNum
            #self.out = convertedNum
        else:
            decnum = int(str(numX), base)
            return decnum

    def baseAlg(self, num, base):
        digitArr = []
        if num == 0:
            return ["0"]
        while num > 0:
            digitArr.append(str(num % base))
            num = num // base
        return digitArr

    def tenToOtherBase(self, num, base):
        neg = False
        if (num < 0):
            neg = True
            num *= -1
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
        if neg:
            convNum = "-" + convNum 
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