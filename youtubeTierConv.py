#Jesse A. Jones
#Version: 2023-06-13.11

from tkinter import *
import math
from tkinter import messagebox

#This class converts a subscriber count to a youtube tier and vice versa.
class YoutubeTierConv(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds sub and tier input fields, conversion buttons, 
        #   and converted outputs.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)
    
        FONT = "Ariel 20"

        #Subscriber count input field.
        self.messageI = Label(self.frameBottom, text = "Enter Sub Count:", font = FONT, anchor = "w")
        self.messageI.grid(row = 0, column = 0)
        self.sI = Entry(self.frameBottom, font = FONT)
        self.sI.grid(row = 0, column = 1)

        #Converts subscriber count to tier when pressed.
        self.tierButton = Button(self.frameBottom, text = "Convert to Tier", 
            font = FONT, command = self.subToTier)
        self.tierButton.grid(row = 1, column = 0)

        #Youtube tier output.
        self.tOutput = Label(self.frameBottom, text = "", 
            font = FONT)
        self.tOutput.grid(row = 2, column = 1)

        #Displays classic tier.
        self.tOutputII = Label(self.frameBottom, text = "", 
            font = FONT)
        self.tOutputII.grid(row = 3, column = 1)

        #Tier input field.
        self.messageII = Label(self.frameBottom, text = "Enter Tier:", font = FONT, anchor = "w")
        self.messageII.grid(row = 4, column = 0)
        self.tier = Entry(self.frameBottom, font = FONT)
        self.tier.grid(row = 4, column = 1)

        #Converts tier to subscriber count.
        self.cButton = Button(self.frameBottom, text = "Convert to Sub Count", 
            font = FONT, command = self.tierToSub)
        self.cButton.grid(row = 5, column = 0)

        #Displays subscriber count based on tier.
        self.sOutput = Label(self.frameBottom, text = "", 
            font = FONT)
        self.sOutput.grid(row = 6, column = 1)
        
        #Holds named number of subscribers.
        self.sOutputII = Label(self.frameBottom, text = "", 
            font = FONT)
        self.sOutputII.grid(row = 7, column = 1)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Error checks subscriber count input.
    def subCount(self):
        if self.sI.get() == "":
            messagebox.showerror("Empty Entry Errror", "Enter a subscriber count!")
        if float(self.sI.get()) >= 1.797693e+308:
            messagebox.showerror("Out of Bounds Error", "Subscriber count is too big! Enter a lower one.")
            return
        else:
            subNum = float(self.sI.get())
        return subNum

    #Error checks tier.
    def tierGet(self):
        if self.tier.get() == "":
            messagebox.showerror("Empty Entry Error", "Enter a tier number!")
        else:
            tierNum = float(self.tier.get())
        return tierNum

    #Converts subscriber count to tier.
    def subToTier(self):
        tier = self.youtubeConv(1)
        self.tOutput["text"] = "Tier: " + str(tier)
        self.tOutputII["text"] = "Classic Tier: " + self.rome_conv(tier)

    #Converts tier number to subscriber count.
    def tierToSub(self):
        subs = self.youtubeConv(2)
        bigNum = self.numbConvArgTaking(subs)
        self.sOutput["text"] = str(subs) + " Subscribers"
        self.sOutputII["text"] = bigNum

    #Gets logarithim of number to find name of it. THIS CODE IS DATED AND YUCKY
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

    #BAD! OLD STOLEN ROMEN NUMERAL CONVERSION CODE!
    def rome_conv(self, decInt):
        numinit = int(decInt)
        if numinit == 0:
            return "Zero"
        if numinit > 0:
            numbs = (1000000000000000000000000000000000, 900000000000000000000000000000000, 500000000000000000000000000000000, 400000000000000000000000000000000,
                    100000000000000000000000000000000, 90000000000000000000000000000000, 50000000000000000000000000000000, 40000000000000000000000000000000,
                    10000000000000000000000000000000, 9000000000000000000000000000000, 5000000000000000000000000000000, 4000000000000000000000000000000,
                    1000000000000000000000000000000, 900000000000000000000000000000, 500000000000000000000000000000, 400000000000000000000000000000,
                    100000000000000000000000000000, 90000000000000000000000000000, 50000000000000000000000000000, 40000000000000000000000000000,
                    10000000000000000000000000000, 9000000000000000000000000000, 5000000000000000000000000000, 4000000000000000000000000000,
                    1000000000000000000000000000, 900000000000000000000000000, 500000000000000000000000000, 400000000000000000000000000,
                    100000000000000000000000000, 90000000000000000000000000, 50000000000000000000000000, 40000000000000000000000000,
                    10000000000000000000000000, 9000000000000000000000000, 5000000000000000000000000, 4000000000000000000000000,
                    1000000000000000000000000, 900000000000000000000000, 500000000000000000000000, 400000000000000000000000, 100000000000000000000000,
                    90000000000000000000000, 50000000000000000000000, 40000000000000000000000, 10000000000000000000000,
                    9000000000000000000000, 5000000000000000000000, 4000000000000000000000,
                    1000000000000000000000, 900000000000000000000, 500000000000000000000, 400000000000000000000,
                    100000000000000000000, 90000000000000000000, 50000000000000000000, 40000000000000000000,
                    10000000000000000000, 9000000000000000000, 5000000000000000000, 4000000000000000000,
                    1000000000000000000, 900000000000000000, 500000000000000000, 400000000000000000,
                    100000000000000000, 90000000000000000, 50000000000000000, 40000000000000000,
                    10000000000000000, 9000000000000000, 5000000000000000, 4000000000000000,
                    1000000000000000, 900000000000000, 500000000000000, 400000000000000, 100000000000000,
                    90000000000000, 50000000000000, 40000000000000, 10000000000000, 9000000000000, 5000000000000, 4000000000000,
                    1000000000000, 900000000000, 500000000000, 400000000000, 100000000000,
                    90000000000, 50000000000, 40000000000, 10000000000, 9000000000, 5000000000, 4000000000,
                    1000000000, 900000000, 500000000, 400000000, 100000000, 90000000, 50000000, 40000000, 10000000, 9000000, 5000000, 4000000,
                    1000000, 900000,  500000, 400000, 100000,  90000, 50000,  40000, 10000,
                    9000, 5000, 4000, 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
            romes = ('==M==','==CM==', '==D==', '==CD==','==C==', '==XC==','==L==','==XL==','==X==','==IX==','==V==','==IV==',
                    '|==M|==','|==CM|==', '|==D|==', '|==CD|==','|==C|==', '|==XC|==','|==L|==','|==XL|==','|==X|==','|==IX|==','|==V|==','|==IV|==',
                    '>|||M>|||','>|||CM>|||', '>|||D>|||', '>|||CD>|||','>|||C>|||', '>|||XC>|||','>|||L>|||','>|||XL>|||','>|||X>|||','>|||IX>|||',
                    '>|||V>|||','>|||IV>|||',
                    '>||M>||','>||CM>||', '>||D>||', '>||CD>||','>||C>||', '>||XC>||','>||L>||','>||XL>||','>||X>||','>||IX>||','>||V>||','>||IV>||',
                    '>|M>|','>|CM>|', '>|D>|', '>|CD>|','>|C>|', '>|XC>|','>|L>|','>|XL>|','>|X>|','>|IX>|','>|V>|','>|IV>|',
                    '>M>','>CM>', '>D>', '>CD>','>C>', '>XC>','>L>','>XL>','>X>','>IX>','>V>','>IV>',
                    '|>M|>','|>CM|>', '|>D|>', '|>CD|>','|>C|>', '|>XC|>','|>L|>','|>XL|>','|>X|>','|>IX|>','|>V|>','|>IV|>',
                    '|||M|||','|||CM|||', '|||D|||', '|||CD|||','|||C|||', '|||XC|||','|||L|||','|||XL|||','|||X|||','|||IX|||','|||V|||','|||IV|||',
                    '||M||','||CM||', '||D||', '||CD||','||C||', '||XC||','||L||','||XL||','||X||','||IX||','||V||','||IV||',
                    '|M|', '|CM|', '|D|', '|CD|','|C|', '|XC|','|L|','|XL|','|X|','|IX|','|V|',
                    '|IV|', 'M','CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
            romenum = []
            for i in range(len(numbs)):
                count = int(numinit / int(numbs[i]))
                romenum.append(romes[i] * count)
                numinit -= int(numbs[i]) * count
            
            return str(''.join(romenum))

    #I HATE THIS
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
        stringNumber = ""
        if 0 < logo < 3:
            stringNumber = ""
        if 6 > logo >= 3:
            stringNumber = "thousand"
        if 9 > logo >= 6:
            stringNumber = "million"
        if 12 > logo >= 9:
            stringNumber = "billion"
        if 15 > logo >= 12:
            stringNumber = "trillion"
        if 18 > logo >= 15:
            stringNumber = "quadrillion"
        if 21 > logo >= 18:
            stringNumber = "quintillion"
        if 24 > logo >= 21:
            stringNumber = "sextillion"
        if 27 > logo >= 24:
            stringNumber = "septillion"
        if 30 > logo >= 27:
            stringNumber = "octillion"
        if 33 > logo >= 30:
            stringNumber = "nonillion"
        if 36 > logo >= 33:
            stringNumber = "decillion"
        if 39 > logo >= 36:
            stringNumber = "undecillion"
        if 42 > logo >= 39:
            stringNumber = "duodecillion"
        if 45 > logo >= 42:
            stringNumber = "tredecillion"
        if 48 > logo >= 45:
            stringNumber = "quattuordecillion"
        if 51 > logo >= 48:
            stringNumber = "quindecillion"
        if 54 > logo >= 51:
            stringNumber = "sexdecillion"
        if 57 > logo >= 54:
            stringNumber = "septendecillion"
        if 60 > logo >= 57:
            stringNumber = "octodecillion"
        if 63 > logo >= 60:
            stringNumber = "novemdecillion"
        if 66 > logo >= 63:
            stringNumber = "vigintillion"
        if 69 > logo >= 66:
            stringNumber = "unvigintillion"
        if 72 > logo >= 69:
            stringNumber = "duovigintillion"
        if 75 > logo >= 72:
            stringNumber = "tresvigintillion"
        if 78 > logo >= 75:
            stringNumber = "quattuorvigintillion"
        if 81 > logo >= 78:
            stringNumber = "quinvigintillion"
        if 84 > logo >= 81:
            stringNumber = "sesvigintillion"
        if 87 > logo >= 84:
            stringNumber = "septemvigintillion"
        if 90 > logo >= 87:
            stringNumber = "octovigintillion"
        if 93 > logo >= 90:
            stringNumber = "novemvigintillion"
        if 96 > logo >= 93:
            stringNumber = "trigintillion"
        if 99 > logo >= 96:
            stringNumber = "untrigintillion"
        if 102 > logo >= 99:
            stringNumber = "duotrigintillion"
        if 105 > logo >= 102:
            stringNumber = "trestrigintillion"
        if 108 > logo >= 105:
            stringNumber = "quattuortrigintillion"
        if 111 > logo >= 118:
            stringNumber = "quintrigintillion"
        if 114 > logo >= 111:
            stringNumber = "sestrigintillion"
        if 117 > logo >= 114:
            stringNumber = "septentrigintillion"
        if 120 > logo >= 117:
            stringNumber = "octotrigintillion"
        if 123 > logo >= 120:
            stringNumber = "noventrigintillion"
        if 126 > logo >= 123:
            stringNumber = "quadragintillion"
        if 129 > logo >= 126:
            stringNumber = "unquadragintillion"
        if 132 > logo >= 129:
            stringNumber = "duoquadragintillion"
        if 135 > logo >= 132:
            stringNumber = "tresquadragintillion"
        if 138 > logo >= 135:
            stringNumber = "quattuorquadragintillion"
        if 141 > logo >= 138:
            stringNumber = "quinquequadragintillion"
        if 144 > logo >= 141:
            stringNumber = "sesquadragintillion"
        if 147 > logo >= 144:
            stringNumber = "septenquadragintillion"
        if 150 > logo >= 147:
            stringNumber = "octoquadragintillion"
        if 153 > logo >= 150:
            stringNumber = "novemquadragintillion"
        if 156 > logo >= 153:
            stringNumber = "quinquagintillion"
        if 159 > logo >= 156:
            stringNumber = "unquinquagintillion"
        if 162 > logo >= 159:
            stringNumber = "duoquinquagintillion"
        if 165 > logo >= 162:
            stringNumber = "trequinquagintillion"
        if 168 > logo >= 165:
            stringNumber = "quattuorquinquagintillion"
        if 171 > logo >= 168:
            stringNumber = "quinquenquinquagintillion"
        if 174 > logo >= 171:
            stringNumber = "sesquinquagintillion"
        if 177 > logo >= 174:
            stringNumber = "septenquinquagintillion"
        if 180 > logo >= 177:
            stringNumber = "octoquinquagintillion"
        if 183 > logo >= 180:
            stringNumber = "novemquinquagintillion"
        if 186 > logo >= 183:
            stringNumber = "sexagintillion"
        if 189 > logo >= 186:
            stringNumber = "unsexagintillion"
        if 192 > logo >= 189:
            stringNumber = "duosexagintillion"
        if 195 > logo >= 192:
            stringNumber = "tresexagintillion"
        if 198 > logo >= 195:
            stringNumber = "quattuorsexagintillion"
        if 201 > logo >= 198:
            stringNumber = "quinquesexagintillion"
        if 204 > logo >= 201:
            stringNumber = "sessexagintillion"
        if 207 > logo >= 204:
            stringNumber = "septensexagintillion"
        if 210 > logo >= 207:
            stringNumber = "octosexagintillion"
        if 213 > logo >= 210:
            stringNumber = "novemsexagintillion"
        if 216 > logo >= 213:
            stringNumber = "septuagintillion"
        if 219 > logo >= 216:
            stringNumber = "unseptuagintillion"
        if 222 > logo >= 219:
            stringNumber = "duoseptuagintillion"
        if 225 > logo >= 222:
            stringNumber = "treseptuagintillion"
        if 228 > logo >= 225:
            stringNumber = "quattuorseptuagintillion"
        if 231 > logo >= 228:
            stringNumber = "quinqueseptuagintillion"
        if 234 > logo >= 231:
            stringNumber = "sesseptuagintillion"
        if 237 > logo >= 234:
            stringNumber = "septenseptuagintillion"
        if 240 > logo >= 237:
            stringNumber = "octoseptuagintillion"
        if 243 > logo >= 240:
            stringNumber = "novemseptuagintillion"
        if 246 > logo >= 243:
            stringNumber = "octogintillion"
        if 249 > logo >= 246:
            stringNumber = "unoctogintillion"
        if 252 > logo >= 249:
            stringNumber = "duooctogintillion"
        if 255 > logo >= 252:
            stringNumber = "tresoctogintillion"
        if 258 > logo >= 255:
            stringNumber = "quattuoroctogintillion"
        if 261 > logo >= 258:
            stringNumber = "quinqueoctogintillion"
        if 264 > logo >= 261:
            stringNumber = "sesoctogintillion"
        if 267 > logo >= 264:
            stringNumber = "septenoctogintillion"
        if 270 > logo >= 267:
            stringNumber = "octumoctogintillion"
        if 273 > logo >= 270:
            stringNumber = "novemoctogintillion"
        if 276 > logo >= 273:
            stringNumber = "nonagintillion"
        if 279 > logo >= 276:
            stringNumber = "unonagintillion"
        if 282 > logo >= 279:
            stringNumber = "duononagintillion"
        if 285 > logo >= 282:
            stringNumber = "tresnonagintillion"
        if 288 > logo >= 285:
            stringNumber = "quattuornonagintillion"
        if 291 > logo >= 288:
            stringNumber = "quinquenonagintillion"
        if 294 > logo >= 291:
            stringNumber = "sesnonagintillion"
        if 297 > logo >= 294:
            stringNumber = "septennonagintillion"
        if 300 > logo >= 297:
            stringNumber = "octononagintillion"
        if 303 > logo >= 300:
            stringNumber = "novemnonagintillion"
        if 306 > logo >= 303:
            stringNumber = "centillion"
        if 309 > logo >= 306:
            stringNumber = "uncentillion"
        retVar = str(returnNumber) + " " + stringNumber 
        return retVar

    #Calculates sub count or tier number based on input.
    #THIS FUNCTION SHOULD BE SPLIT INTO TWO FFS!
    def youtubeConv(self, sw):
        #Sub count to tier conversion case.
        if sw == 1:
            subs = self.subCount()
            if subs < 0:
                messagebox.showerror("Invalid Sub Count Error", "Can't have negative subscribers!")
                return
            if 0 <= subs < 1000:
                return subs / 1000
            else:
                nonRounded = math.log(subs, 100) - 0.5
                rounded = round(nonRounded, 9)
                return rounded

        #Tier to subscriber count conversion case.
        if sw == 2:
            tier = self.tierGet()
            if tier < 0:
                messagebox.showerror("Invalid Tier Error", "Can't have a negative tier!")
                return
            if tier > 153.562:
                messagebox.showerror("Out of Bounds Error", "Tier number is too large!")
                return
            if 0 <= tier < 1:
                return tier * 1000
            else:
                return (100 ** tier) * 10

def main():
    root = Tk()
    root.title("Youtube Tier Converter")
    star = YoutubeTierConv(root)
    root.mainloop()

if __name__ == "__main__":
    main()
