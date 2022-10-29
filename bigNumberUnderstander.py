from tkinter import *
from tkinter import messagebox
import math
from math import log
from time import sleep

class BigNumbUnderstander(object):
    def __init__(self, window = None):
        self.window = window

        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack(side = RIGHT)

        self.clearButton = Button(self.frameTop, text = "Clear Entry",
            font = "Ariel 20", command = self.clear)
        self.clearButton.pack(side = LEFT)

        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        self.message = Label(self.frameBottom, text = "Enter an Integer:", font = "Ariel 75", anchor = "w")
        self.message.grid(row = 0, column = 0)

        self.numE = Entry(self.frameBottom, font = "Times 69")
        self.numE.grid(row = 1, column = 0)

        self.convButtonI = Button(self.frameBottom, text = "Convert to Understandibleness", 
            font = "Ariel 60", command = self.numbConverter)
        self.convButtonI.grid(row = 2, column = 0)

        self.tOutput = Label(self.frameBottom, text = "", 
            font = "Ariel 69", justify = LEFT)
        self.tOutput.grid(row = 3, column = 0)

        self.tOutputII = Label(self.frameBottom, text = "", 
            font = "Ariel 69", justify = LEFT)
        self.tOutputII.grid(row = 4, column = 0)

        self.tOutputIII = Label(self.frameBottom, text = "", 
            font = "Ariel 69", justify = LEFT)
        self.tOutputIII.grid(row = 5, column = 0)
    
    def quitButtonAction(self):
        self.window.destroy()

    def clear(self):
        self.numE.delete(0, "end")

    def numbConverter(self):
        self.stringNumber = ""
        self.tOutputIII["text"] = ""
        self.numbConv()
        self.scienceNotifier()
        self.tOutput["text"] = self.numbAlt
        self.tOutputII["text"] = self.stringNumber
        self.tOutputIII["text"] = str(self.scienceNotePI) + "x10" + " to the " + str(int(self.scienceNotePII)) + self.scienceNotePIII
        self.frameBottom.update()

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

    def scienceNotifier(self):
        numbOrig = float(self.numE.get())
        logo = self.logGet(numbOrig)
        numbAlt = numbOrig / (10 ** logo)
        numbAlt = round(numbAlt, 3)
        ORD = logo % 10
        if ORD == 0:
            ORDII = 'th'
        if ORD == 1:
            ORDII = "st"
            if ORD == 1 and 20 > logo > 10:
                ORDII = 'th'
        if ORD == 2:
            ORDII = "nd"
            if ORD == 2 and 20 > logo > 10:
                ORDII = 'th'
        if ORD == 3:
            ORDII = "rd"
            if ORD == 3 and 20 > logo > 10:
                ORDII = 'th'
        if ORD == 4:
            ORDII = "th"
        if ORD == 5:
            ORDII = "th"
        if ORD == 6:
            ORDII = "th"
        if ORD == 7:
            ORDII = "th"
        if ORD == 8:
            ORDII = "th"
        if ORD == 9:
            ORDII = "th"
        self.scienceNotePI = numbAlt
        self.scienceNotePII = logo
        self.scienceNotePIII = ORDII        

    def numbConv(self):
        if self.numE.get() == "":
            messagebox.showerror("Empty Input Error", "Input an integer!")
            return
        numbOrig = float(self.numE.get())
        logo = self.logGet(numbOrig)
        logo = logo - (logo % 3)
        numbAlt = numbOrig / (10 ** logo)
        numbAlt = round(numbAlt, 3)
        if numbAlt >= 1.797693e+308:
            messagebox.showerror("Out of Bounds Error", "Number is too big!")
            return
        self.numbAlt = numbAlt
        if 0 < logo < 3:
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
        return

def numbConvArgTaking(self, num):
        numbOrig = num
        logo = self.logGet(numbOrig)
        logo = logo - (logo % 3)
        numbAlt = numbOrig / (10 ** logo)
        numbAlt = round(numbAlt, 3)
        if numbAlt >= 1.797693e+308:
            messagebox.showerror("Out of Bounds Error", "Number is too big!")
            return
        returnNumber = numbAlt
        if 0 < logo < 3:
            stringNumber = ""
        elif 6 > logo >= 3:
            stringNumber = "thousand"
        elif 9 > logo >= 6:
            stringNumber = "million"
        elif 12 > logo >= 9:
            stringNumber = "billion"
        elif 15 > logo >= 12:
            stringNumber = "trillion"
        elif 18 > logo >= 15:
            stringNumber = "quadrillion"
        elif 21 > logo >= 18:
            stringNumber = "quintillion"
        elif 24 > logo >= 21:
            stringNumber = "sextillion"
        elif 27 > logo >= 24:
            stringNumber = "septillion"
        elif 30 > logo >= 27:
            stringNumber = "octillion"
        elif 33 > logo >= 30:
            stringNumber = "nonillion"
        elif 36 > logo >= 33:
            stringNumber = "decillion"
        elif 39 > logo >= 36:
            stringNumber = "undecillion"
        elif 42 > logo >= 39:
            stringNumber = "duodecillion"
        elif 45 > logo >= 42:
            stringNumber = "tredecillion"
        elif 48 > logo >= 45:
            stringNumber = "quattuordecillion"
        elif 51 > logo >= 48:
            stringNumber = "quindecillion"
        elif 54 > logo >= 51:
            stringNumber = "sexdecillion"
        elif 57 > logo >= 54:
            stringNumber = "septendecillion"
        elif 60 > logo >= 57:
            stringNumber = "octodecillion"
        elif 63 > logo >= 60:
            stringNumber = "novemdecillion"
        elif 66 > logo >= 63:
            stringNumber = "vigintillion"
        elif 69 > logo >= 66:
            stringNumber = "unvigintillion"
        elif 72 > logo >= 69:
            stringNumber = "duovigintillion"
        elif 75 > logo >= 72:
            stringNumber = "tresvigintillion"
        elif 78 > logo >= 75:
            stringNumber = "quattuorvigintillion"
        elif 81 > logo >= 78:
            stringNumber = "quinvigintillion"
        elif 84 > logo >= 81:
            stringNumber = "sesvigintillion"
        elif 87 > logo >= 84:
            stringNumber = "septemvigintillion"
        elif 90 > logo >= 87:
            stringNumber = "octovigintillion"
        elif 93 > logo >= 90:
            stringNumber = "novemvigintillion"
        elif 96 > logo >= 93:
            stringNumber = "trigintillion"
        elif 99 > logo >= 96:
            stringNumber = "untrigintillion"
        elif 102 > logo >= 99:
            stringNumber = "duotrigintillion"
        elif 105 > logo >= 102:
            stringNumber = "trestrigintillion"
        elif 108 > logo >= 105:
            stringNumber = "quattuortrigintillion"
        elif 111 > logo >= 118:
            stringNumber = "quintrigintillion"
        elif 114 > logo >= 111:
            stringNumber = "sestrigintillion"
        elif 117 > logo >= 114:
            stringNumber = "septentrigintillion"
        elif 120 > logo >= 117:
            stringNumber = "octotrigintillion"
        elif 123 > logo >= 120:
            stringNumber = "noventrigintillion"
        elif 126 > logo >= 123:
            stringNumber = "quadragintillion"
        elif 129 > logo >= 126:
            stringNumber = "unquadragintillion"
        elif 132 > logo >= 129:
            stringNumber = "duoquadragintillion"
        elif 135 > logo >= 132:
            stringNumber = "tresquadragintillion"
        elif 138 > logo >= 135:
            stringNumber = "quattuorquadragintillion"
        elif 141 > logo >= 138:
            stringNumber = "quinquequadragintillion"
        elif 144 > logo >= 141:
            stringNumber = "sesquadragintillion"
        elif 147 > logo >= 144:
            stringNumber = "septenquadragintillion"
        elif 150 > logo >= 147:
            stringNumber = "octoquadragintillion"
        elif 153 > logo >= 150:
            stringNumber = "novemquadragintillion"
        elif 156 > logo >= 153:
            stringNumber = "quinquagintillion"
        elif 159 > logo >= 156:
            stringNumber = "unquinquagintillion"
        elif 162 > logo >= 159:
            stringNumber = "duoquinquagintillion"
        elif 165 > logo >= 162:
            stringNumber = "trequinquagintillion"
        elif 168 > logo >= 165:
            stringNumber = "quattuorquinquagintillion"
        elif 171 > logo >= 168:
            stringNumber = "quinquenquinquagintillion"
        elif 174 > logo >= 171:
            stringNumber = "sesquinquagintillion"
        elif 177 > logo >= 174:
            stringNumber = "septenquinquagintillion"
        elif 180 > logo >= 177:
            stringNumber = "octoquinquagintillion"
        elif 183 > logo >= 180:
            stringNumber = "novemquinquagintillion"
        elif 186 > logo >= 183:
            stringNumber = "sexagintillion"
        elif 189 > logo >= 186:
            stringNumber = "unsexagintillion"
        elif 192 > logo >= 189:
            stringNumber = "duosexagintillion"
        elif 195 > logo >= 192:
            stringNumber = "tresexagintillion"
        elif 198 > logo >= 195:
            stringNumber = "quattuorsexagintillion"
        elif 201 > logo >= 198:
            stringNumber = "quinquesexagintillion"
        elif 204 > logo >= 201:
            stringNumber = "sessexagintillion"
        elif 207 > logo >= 204:
            stringNumber = "septensexagintillion"
        elif 210 > logo >= 207:
            stringNumber = "octosexagintillion"
        elif 213 > logo >= 210:
            stringNumber = "novemsexagintillion"
        elif 216 > logo >= 213:
            stringNumber = "septuagintillion"
        elif 219 > logo >= 216:
            stringNumber = "unseptuagintillion"
        elif 222 > logo >= 219:
            stringNumber = "duoseptuagintillion"
        elif 225 > logo >= 222:
            stringNumber = "treseptuagintillion"
        elif 228 > logo >= 225:
            stringNumber = "quattuorseptuagintillion"
        elif 231 > logo >= 228:
            stringNumber = "quinqueseptuagintillion"
        elif 234 > logo >= 231:
            stringNumber = "sesseptuagintillion"
        elif 237 > logo >= 234:
            stringNumber = "septenseptuagintillion"
        elif 240 > logo >= 237:
            stringNumber = "octoseptuagintillion"
        elif 243 > logo >= 240:
            stringNumber = "novemseptuagintillion"
        elif 246 > logo >= 243:
            stringNumber = "octogintillion"
        elif 249 > logo >= 246:
            stringNumber = "unoctogintillion"
        elif 252 > logo >= 249:
            stringNumber = "duooctogintillion"
        elif 255 > logo >= 252:
            stringNumber = "tresoctogintillion"
        elif 258 > logo >= 255:
            stringNumber = "quattuoroctogintillion"
        elif 261 > logo >= 258:
            stringNumber = "quinqueoctogintillion"
        elif 264 > logo >= 261:
            stringNumber = "sesoctogintillion"
        elif 267 > logo >= 264:
            stringNumber = "septenoctogintillion"
        elif 270 > logo >= 267:
            stringNumber = "octumoctogintillion"
        elif 273 > logo >= 270:
            stringNumber = "novemoctogintillion"
        elif 276 > logo >= 273:
            stringNumber = "nonagintillion"
        elif 279 > logo >= 276:
            stringNumber = "unonagintillion"
        elif 282 > logo >= 279:
            stringNumber = "duononagintillion"
        elif 285 > logo >= 282:
            stringNumber = "tresnonagintillion"
        elif 288 > logo >= 285:
            stringNumber = "quattuornonagintillion"
        elif 291 > logo >= 288:
            stringNumber = "quinquenonagintillion"
        elif 294 > logo >= 291:
            stringNumber = "sesnonagintillion"
        elif 297 > logo >= 294:
            stringNumber = "septennonagintillion"
        elif 300 > logo >= 297:
            stringNumber = "octononagintillion"
        elif 303 > logo >= 300:
            stringNumber = "novemnonagintillion"
        elif 306 > logo >= 303:
            stringNumber = "centillion"
        else:
            stringNumber = "uncentillion"
        retVar = str(returnNumber) + stringNumber 
        return retVar

def main():
    root = Tk()
    root.title("Big Number Understander")
    numb = BigNumbUnderstander(root)
    root.mainloop()

if __name__ == "__main__":
    main()
