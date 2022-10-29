import random
from time import sleep
from tkinter import *
import winsound
class Connect4(object):

    def __init__(self, width, height, window=None):
        self.clickFlag = 0
        self.width = width
        self.height = height
        self.data = []
        self.ox = "x"

        self.soundsAllowed = False

        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]

        self.replayMoveList = []
        self.victoryList = []

        self.linePadding = 60
        
        self.drawFlag = 0
        
        self.window = window
        self.winHeight = self.height * 100
        self.winWidth = self.width * 100
        self.padding = 5
        self.xSize = self.width
        self.ySize = self.height
        self.diameterX = (self.winHeight / self.ySize) - self.padding
        self.diameterY = (self.winWidth / self.xSize) - self.padding

        self.frame = Frame(self.window)
        self.frame.grid(row = 0, column = 0)

        self.quitButton = Button(self.frame, text = "Quit Game",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 2)

        self.newGameButton = Button(self.frame, text = "New Game",font = "Ariel 20", 
            command = self.newGame)
        self.newGameButton.grid(row = 0, column = 0)

        self.scalar = Scale(self.frame, orient = HORIZONTAL, 
            from_ = 0, to = 7, length = 200, 
            label = "AI Difficulty:", font = "Ariel 20", command = self.sliderNumber)
        self.scalar.grid(row = 0, column = 1)

        self.draw = Canvas(self.window, width = self.winWidth + 
            self.padding, height = self.winHeight + self.padding, 
            bg = "yellow", highlightbackground = "black", highlightthickness = 2)
        self.mouseInput = self.draw.bind("<Button-1>", self.mouse)
        self.draw.grid(row = 1, column = 0)

        self.circles = []

        y = self.padding
        for row in range(self.ySize):
            circleRow = []
            x = self.padding
            for col in range(self.xSize):
                circleRow += [self.draw.create_oval(x, y, x + self.diameterX, 
                y + self.diameterY, fill = "white" )]
                x += self.diameterX + self.padding
            self.circles.append(circleRow) 
            y += self.diameterY + self.padding

        self.frameII = Frame(self.window)
        self.frameII.grid(row = 2, column = 0)

        self.message = Label(self.frameII, text = "Choose a move location", font = "Ariel 25", anchor = "w")
        self.message.pack(side = TOP)

        self.frameIII = Frame(self.window)
        self.frameIII.grid(row = 3, column = 0)

        self.replayButton = Button(self.frameIII, text = "Replay Game", font = "Ariel 25", command = self.replayFunc)
        self.replayButton.grid(row = 0, column = 0)

        self.onSoundButton = Button(self.frameIII, text = "Sound On", font = "Ariel 25", command = self.soundOn)
        self.onSoundButton.grid(row = 0, column = 1)

        self.offSoundButton = Button(self.frameIII, text = "Sound Off", font = "Ariel 25", command = self.soundOff)
        self.offSoundButton.grid(row = 0, column = 2)

    def chipSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/chipDrop.wav", winsound.SND_ASYNC)

    def winningSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/playerWin.wav", winsound.SND_ASYNC)

    def loosingSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/aiWin.wav", winsound.SND_ASYNC)

    def stalemateSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/stalemate.wav", winsound.SND_ASYNC)

    def clickSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("C:/Users/creep/Desktop/programmingStuff/Python_Programs/random_ass_programs/click.wav", winsound.SND_ASYNC)

    def soundOn(self):
        self.soundsAllowed = True
        self.clickSound()
    
    def soundOff(self):
        self.soundsAllowed = False

    def sliderNumber(self, num):
        self.AI.ply = int(self.scalar.get())

    def playGUI(self, AI):
        self.AI = AI

    def AIMove(self):
        ox = "o"
        move = self.AI.nextMove(self)
        self.col = move
        self.replayMoveList.append(move)
        self.animate(move, ox)
        self.addMove(move, ox)
        self.colorFiller()
        self.chipSound()

    def mouse(self, event):
        ox = "x"
        self.draw.unbind("<Button-1>")
        if self.winFullMessageMaker():
            return
        col = int(event.x/self.diameterX)
        row = int(event.y/self.diameterY)
        if row > self.ySize - 1:
            row = self.ySize - 1
        if col > self.xSize - 1:
            col = self.xSize - 1 
        if self.allowsMove(col):
            self.animate(col, ox)
            self.addMove(col, ox)
            self.replayMoveList.append(col)
            self.colorFiller()
            self.chipSound()
            self.window.update()
            self.loadingMessage()
            self.window.update()
            if self.winFullMessageMaker() == False:
                self.AIMove()
                self.AIMoveMessage()
                self.window.update() 
            if self.winFullMessageMaker():
                return
        else:
            self.message["text"] = "Full Col!"
            self.window.update()
        self.draw.bind("<Button-1>", self.mouse)

    def lineDraw(self):
        if self.drawFlag == 0:
            self.winLine = self.draw.create_line(
            self.victoryList[-3] * self.diameterX + self.linePadding, 
            self.victoryList[-4] * self.diameterY + self.linePadding, 
            self.victoryList[-1] * self.diameterX + self.linePadding, 
            self.victoryList[-2] * self.diameterY + self.linePadding, 
                width = 15, fill = "blue")
        self.drawFlag += 1

    def winFullChecker(self, ox):
        if self.winsFor(ox):
            return True
        if self.isFull():
            return True

    def winFullMessageMaker(self):
        if self.winFullChecker("x") or self.winFullChecker("o"):
            if self.winFullChecker("x"):
                player = "You "
                sEnd = ""
                self.winningSound()
            else:
                player = "AI "
                sEnd = "s" 
                self.loosingSound()
            if self.isFull():
                self.message["text"] = "Stalemate! Board is full!"
                self.stalemateSound()
                return True
            self.lineDraw()
            self.message["text"] = player + "win" + sEnd + "!"
            self.window.update()
            return True 
        return False

    def animate(self, col, ox):
        row = 0
        while self.data[row][col] == " " and row < self.ySize - 1:
            self.data[row][col] = ox
            self.colorFiller()
            self.window.update()
            sleep(0.05)
            self.data[row][col] = " "
            self.colorFiller()
            self.window.update()
            row += 1 

    def defaultMessage(self):
        self.message["text"] = "Choose a move location"

    def AIMoveMessage(self):
        self.message["text"] = "The AI moved in col: " + str(self.col)            

    def loadingMessage(self):
        self.message["text"] = "Loading..."

    def colorFiller(self):
        rowAccum = -1
        for row in self.data:
            rowAccum += 1
            colAccum = 0
            for element in row:
                if element == "x":
                    self.draw.itemconfig(self.circles[rowAccum][colAccum], fill = "red")
                if element == "o":
                    self.draw.itemconfig(self.circles[rowAccum][colAccum], fill = "black")
                if element == " ":
                    self.draw.itemconfig(self.circles[rowAccum][colAccum], fill = "white")
                colAccum += 1
    
    def quitButtonAction(self):
        self.window.destroy()
        self.clickSound()

    def replayFunc(self):
        self.clickSound()
        sleep(0.3)
        self.clear()
        self.colorFiller()
        if self.drawFlag > 0:
            self.winLine = self.draw.delete(self.winLine)
        self.message["text"] = "Replaying..."
        self.drawFlag = 0
        self.window.update()
        turn = "x"
        for element in self.replayMoveList:
            self.animate(element, turn)
            self.addMove(element, turn)
            self.colorFiller()
            self.chipSound()
            self.window.update()
            if turn == "x":
                turn = "o"
            else:
                turn = "x"
            sleep(0.5)
        if self.winFullMessageMaker():
            self.winFullMessageMaker()
            self.window.update()
        else:
            self.defaultMessage()
            self.window.update()
        
    def newGame(self):
        self.clickSound()
        self.draw.bind("<Button-1>", self.mouse)
        self.replayMoveList = []
        self.victoryList = []
        self.defaultMessage()
        if self.drawFlag > 0:
            self.winLine = self.draw.delete(self.winLine)
        self.drawFlag = 0
        self.clear()
        self.colorFiller()

    def __repr__(self):
        boardData = self.data
        board = ''
        for row in range(self.height):
            board += '|'
            for col in range(self.width):
                board += boardData[row][col] + '|'
            board += "\n"
        board += "--" * self.width + "-\n"
        for col in range(self.width):
            board += ' ' + str(col % 10)
        board += "\n"
        return board

    def addMove(self, col, ox):
        if self.allowsMove(col):
            for row in range(self.height):
                if self.data[row][col] != " ":
                    self.data[row-1][col] = ox
                    return
            self.data[self.height-1][col] = ox

    def delMove(self, col):
        if self.allowsMove(col):
            for row in range(self.height):
                if self.data[row][col] != " ":
                    self.data[row][col] = " "
                    return
        elif self.allowsMove(col) == False:
            self.data[0][col] = " "

    def allowsMove(self, col):
        boardData = self.data
        if col < 0 or col > self.width - 1:
            return False
        if boardData[0][col] != " ":
            return False
        else:
            return True
        
    def clear(self):
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = " "
    
    def isFull(self):
        condit = None
        total = 0
        for col in range(self.width):
            if self.allowsMove(col) == False:
                condit = True
                total += condit
            else:
                condit = False
                total += condit
        if total == self.width:
            return True
        else:
            return False 

    def winsFor(self, ox):
        for row in range(0, self.height):
            for col in range(0, self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row][col+1] == ox and \
                    self.data[row][col+2] == ox and \
                    self.data[row][col + 3] == ox:
                    self.victoryList.append(row)
                    self.victoryList.append(col)
                    self.victoryList.append(row)
                    self.victoryList.append(col + 3)
                    return True
        for row in range(0, self.height - 3):
            for col in range(0, self.width):
                if self.data[row][col] == ox and \
                   self.data[row + 1][col] == ox and \
                    self.data[row + 2][col] == ox and \
                    self.data[row + 3][col] == ox:
                    self.victoryList.append(row)
                    self.victoryList.append(col)
                    self.victoryList.append(row + 3)
                    self.victoryList.append(col)
                    return True
        for row in range(0, self.height - 3):
            for col in range(0, self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row + 1][col + 1] == ox and \
                    self.data[row + 2][col + 2] == ox and \
                    self.data[row + 3][col + 3] == ox:
                    self.victoryList.append(row)
                    self.victoryList.append(col)
                    self.victoryList.append(row + 3)
                    self.victoryList.append(col + 3)
                    return True
        for row in range(3, self.height):
            for col in range(0, self.width - 3):
                if self.data[row][col] == ox and \
                   self.data[row - 1][col + 1] == ox and \
                    self.data[row - 2][col + 2] == ox and \
                    self.data[row - 3][col + 3] == ox:
                    self.victoryList.append(row)
                    self.victoryList.append(col)
                    self.victoryList.append(row - 3)
                    self.victoryList.append(col + 3)
                    return True
        return False

    def playGameWith(self):
        diff = int(input("Please Input Difficulty of AI (0 - 7): "))
        player = "x"
        AI = Player("o", "Random", diff)
        while True:
            sleep(0.05)
            flag = 0
            if self.winsFor(player):
                print(self)
                print(player + " is the Winner!")
                break
            if self.isFull():
                print(self)
                print("Nobody Wins; Board is full!")
                break
            print(self)
            if player == "x":
                moveColP = int(input("Choose Column to Place Your "  + player + " Piece: "))
                validMove = self.allowsMove(moveColP)
                if validMove == False:
                    print("Error! Move out of Board Range! Try Again!")
                    flag = 1
                elif validMove:
                    self.addMove(moveColP, player)
            if player == "o":
                moveColAI = AI.nextMove(self)
                self.addMove(moveColAI, player)
            if flag == 0 and player == "x" and self.winsFor("x") == False:
                player = "o"
            elif flag == 0 and player == "o" and self.winsFor("o") == False:
                player = "x"
            elif (flag != 0 or self.winsFor("x")) and player == "x":
                player = "x"
            elif (flag != 0 or self.winsFor("o")) and player == "o":
                player = "o"

    def hostGame(self):
        player = input("Choose Between x or o ")
        while True:
            flag = 0
            if self.winsFor(player):
                print(self)
                print(player + " is the Winner!")
                break
            if self.isFull():
                print(self)
                print("Nobody Wins; Board is full!")
                break
            print(self)
            moveCol = int(input("Choose Column to Place Your "  + player + " Piece: "))
            validMove = self.allowsMove(moveCol)
            if validMove == False:
                print("Error! Move out of Board Range! Try Again!")
                flag = 1
            elif validMove:
                self.addMove(moveCol, player)
            if flag == 0 and player == "x" and self.winsFor("x") == False:
                player = "o"
            elif flag == 0 and player == "o" and self.winsFor("o") == False:
                player = "x"
            elif (flag != 0 or self.winsFor("x")) and player == "x":
                player = "x"
            elif (flag != 0 or self.winsFor("o")) and player == "o":
                player = "o"

class Player(object):
    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
    
    def scoresFor(self, board, ox, ply):
        scores = []
        for col in range(board.width):
                if board.allowsMove(col):
                    board.addMove(col, ox)
                    if board.winsFor(ox):
                        scores.append(100)
                    else:
                        if ply > 1:
                            if ox == "x":
                                otherOx = "o"
                            else:
                                otherOx = "x"
                            best = max(self.scoresFor(board, otherOx, ply - 1))
                            scores.append(100 - best)
                        else:
                            scores.append(50)
                    board.delMove(col) 
                else:
                    scores.append(-1)
        return scores
    
    def pickBestSpots(self, scores):
        bestScore = max(scores)
        bestPositions = []
        for i in range(len(scores)):
            if bestScore == scores[i]:
                bestPositions.append(i)
        return bestPositions

    def tieBreaker(self, tbt, scores):
        goodList = self.pickBestSpots(scores)
        if tbt == "Random":
            return random.choice(goodList)
        if tbt == "Left":
            return goodList[0]
        if tbt == "Right":
            return goodList[-1]

    def nextMove(self, board):
        scoreList = self.scoresFor(board, self.ox, self.ply)
        move = self.tieBreaker(self.tbt, scoreList)
        return move
                
def main():
    root = Tk()
    root.title("Connect Four, the Vertical Four in a Row Checkers Game")
    connec = Connect4(7,6,root)
    AI = Player("o", "Random", 0)
    connec.playGUI(AI)
    root.mainloop()

if __name__ == '__main__':
    main()
