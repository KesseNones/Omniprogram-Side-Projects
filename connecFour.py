#Jesse A. Jones
#Version: 2025-06-20.1

import random
from time import sleep
from tkinter import *
from playsound3 import playsound

#This class works with the player class and manages 
#   tkinter stuff to run a GUI game of Connect Four.
#   This version of the game features animations, 
#   sound effects, as well as a rewind after a game is finished.

class Connect4(object):

    #Sets up the GUI.
    def __init__(self, width, height, window=None):

        #Sets up board dimensions, data, and current player.
        self.width = width
        self.height = height
        self.data = []
        self.ox = "x"

        #Used to toggle sound effects.
        self.soundsAllowed = False

        #Creates an empty connect 4 board matrix.
        for row in range(self.height):
            boardRow = []
            for col in range(self.width):
                boardRow += [' ']
            self.data += [boardRow]

        #Used in the replay feature.
        self.replayMoveList = []
        self.victoryList = []

        self.linePadding = 60
        
        self.victoryLineIsDrawn = False
        
        #Translates board data dimensions into GUI dimensions.
        self.window = window
        self.winHeight = self.height * 100
        self.winWidth = self.width * 100
        self.padding = 5
        self.xSize = self.width
        self.ySize = self.height
        self.diameterX = (self.winHeight / self.ySize) - self.padding
        self.diameterY = (self.winWidth / self.xSize) - self.padding

        #Top frame made to contain AI difficulty slider 
        #   and "New Game" and "Quit Game" buttons.
        self.frame = Frame(self.window)
        self.frame.grid(row = 0, column = 0)

        #Quit game button created.
        self.quitButton = Button(self.frame, text = "Quit Game",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.grid(row = 0, column = 2)

        #New game button created.
        self.newGameButton = Button(self.frame, text = "New Game",font = "Ariel 20", 
            command = self.newGame)
        self.newGameButton.grid(row = 0, column = 0)

        #Slider used to determine layers of recursion AI uses 
        #   which determines how difficult the AI is.
        self.scalar = Scale(self.frame, orient = HORIZONTAL, 
            from_ = 0, to = 7, length = 200, 
            label = "AI Difficulty:", font = "Ariel 20", command = self.sliderNumber)
        self.scalar.grid(row = 0, column = 1)

        #Creates canvas that contains the graphical representation of the board data.
        self.draw = Canvas(self.window, width = self.winWidth + 
            self.padding, height = self.winHeight + self.padding, 
            bg = "yellow", highlightbackground = "black", highlightthickness = 2)

        #Binds left mouse input.
        self.mouseInput = self.draw.bind("<Button-1>", self.mouse)
        self.draw.grid(row = 1, column = 0)

        self.circles = []

        #Creates circles that represent the spots in the board data.
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

        #Bottom frame created that holds game text.
        self.frameII = Frame(self.window)
        self.frameII.grid(row = 2, column = 0)

        #This text displays various game information that is useful for the player.
        self.message = Label(self.frameII, text = "Choose a move location", 
            font = "Ariel 25", anchor = "w")
        self.message.pack(side = TOP)

        #This frame holds more game option buttons 
        #   for replaying the game, and turning the sound on or off.
        self.frameIII = Frame(self.window)
        self.frameIII.grid(row = 3, column = 0)

        #Button used to trigger game replay.
        self.replayButton = Button(self.frameIII, 
            text = "Replay Game", font = "Ariel 25", command = self.replayFunc)
        self.replayButton.grid(row = 0, column = 0)

        #Button used to turn sound on.
        self.onSoundButton = Button(self.frameIII, 
            text = "Sound On", font = "Ariel 25", command = self.soundOn)
        self.onSoundButton.grid(row = 0, column = 1)

        #Button used to turn sound off.
        self.offSoundButton = Button(self.frameIII, 
            text = "Sound Off", font = "Ariel 25", command = self.soundOff)
        self.offSoundButton.grid(row = 0, column = 2)

    #Plays sound of chip hitting falling into place.
    def chipSound(self):
        if self.soundsAllowed:
            playsound("connectFourSoundEffects/chipDrop.wav", False)

    #Plays sound of player winning game.
    def winningSound(self):
        if self.soundsAllowed:
            playsound("connectFourSoundEffects/playerWin.wav", False)

    #Plays sound of AI winning game.
    def loosingSound(self):
        if self.soundsAllowed:
            playsound("connectFourSoundEffects/aiWin.wav", False)

    #Plays if stalemate occurs.
    def stalemateSound(self):
        if self.soundsAllowed:
            playsound("connectFourSoundEffects/stalemate.wav", False)

    #Plays a clip of my dumb voice saying "Click" which is pretty 
    #   much used to confirm if the sound is enabled or not.
    def clickSound(self):
        if self.soundsAllowed:
            playsound("connectFourSoundEffects/click.wav", block=False)

    #This is called if the sound on button is pressed.
    #   Enables sound and plays the confirmation sound.
    def soundOn(self):
        self.soundsAllowed = True
        self.clickSound()
    
    #Called if sound off button is pressed.
    #   Disables sound.
    def soundOff(self):
        self.soundsAllowed = False

    #Called to fetch the AI difficulty slider number.
    def sliderNumber(self, num):
        self.AI.ply = int(self.scalar.get())

    #Sets the class variable self.AI to a passed in player class instance.
    def playGUI(self, AI):
        self.AI = AI

    #Causes the AI to perform a move.
    def AIMove(self):
        ox = "o"
        move = self.AI.nextMove(self)
        self.col = move
        self.replayMoveList.append(move)
        self.animate(move, ox)
        self.addMove(move, ox)
        self.colorFiller()
        self.chipSound()

    #Called when mouse is clicked.
    #This effectively performs the player move and follows it with an AI move.
    def mouse(self, event):
        ox = "x"
        #Unbinds mouse so game can process move.
        self.draw.unbind("<Button-1>")

        #If there's a win or the board is full, no move is made.
        if self.winFullMessageMaker():
            return
        #Determines which row and column was clicked 
        #   on based on calculations made from mouse input.
        col = int(event.x/self.diameterX)
        row = int(event.y/self.diameterY)
        
        #Accounts for edge case of desired move being beyond valid parameters.
        if row > self.ySize - 1:
            row = self.ySize - 1
        if col > self.xSize - 1:
            col = self.xSize - 1 
        
        #If the move can be made (the column isn't full) then the player move 
        #   is made and is followed by the AI move if no win occurs for player.
        if self.allowsMove(col):
            #Displays chip falling animation.
            self.animate(col, ox)

            #Adds move to board data and replay list. 
            self.addMove(col, ox)
            self.replayMoveList.append(col)

            #Fills in colors and plays sound of chip hitting its place.
            self.colorFiller()
            self.chipSound()
            
            #Displays loading message for AI's move.
            self.window.update()
            self.loadingMessage()
            self.window.update()
            
            #If no win has been detected, the AI will make its move.
            if self.winFullMessageMaker() == False:
                self.AIMove()
                self.AIMoveMessage()
                self.window.update() 

            #Function returns if win was detected for AI.
            if self.winFullMessageMaker():
                return
        else:
            #Displays error message if player tries 
            #   to move in column that's full.
            self.message["text"] = "Full Col!"
            self.window.update()

        #Rebinds mouse after moves made and processed.
        self.draw.bind("<Button-1>", self.mouse)

    #Creates a blue line that highlights a player 
    #   or AI victory configuration.
    def lineDraw(self):
        if not(self.victoryLineIsDrawn):
            self.winLine = self.draw.create_line(
            self.victoryList[-3] * self.diameterX + self.linePadding, 
            self.victoryList[-4] * self.diameterY + self.linePadding, 
            self.victoryList[-1] * self.diameterX + self.linePadding, 
            self.victoryList[-2] * self.diameterY + self.linePadding, 
                width = 15, fill = "blue")
        self.victoryLineIsDrawn = True
        self.window.update()

    #Returns a list that has info on if x wins, o wins, or the board is full.
    def winFullChecker(self):
        retArr = [None, None, None]
        retArr[0] = self.isFull()
        retArr[1] = self.winsFor("x")
        retArr[2] = self.winsFor("o")

        return retArr

    #Returns true if board is full or a player 
    #   has won and updates the text appropriately.
    def winFullMessageMaker(self):
        resArr = self.winFullChecker()
        
        #If board is full, true is returned. 
        #   Otherwise, further evaluation happens.
        if resArr[0]:
            self.message["text"] = "Stalemate! Board is full!"
            self.stalemateSound()
            return True

        if resArr[1]:
            self.message["text"] = "You win!"
            self.lineDraw()
            self.winningSound()
            return True

        if resArr[2]:
            self.message["text"] = "AI wins!"
            self.lineDraw()
            self.loosingSound()
            return True

        return False

    #Animates a chip falling into a given column if it can.
    def animate(self, col, ox):
        row = 0

        #Inserts a chip into a spot, updates the GUI to display it 
        #   and then repeats until the "chip" falls into where it needs to be.
        while self.data[row][col] == " " and row < self.ySize - 1:
            self.data[row][col] = ox
            self.colorFiller()
            self.window.update()
            sleep(0.05)
            self.data[row][col] = " "
            self.colorFiller()
            self.window.update()
            row += 1 

    #Sets game text to default message.
    def defaultMessage(self):
        self.message["text"] = "Choose a move location"
        self.window.update()

    #Notifies the player where the AI moves.
    def AIMoveMessage(self):
        self.message["text"] = "The AI moved in col: " + str(self.col)
        self.window.update()            

    #Sets the text to the loading text when an AI is moving.
    def loadingMessage(self):
        self.message["text"] = "Loading..."
        self.window.update()

    #Fills in all the circles their appropriate colors based on the board data.
    def colorFiller(self):
        rowAccum = 0
        colAccum = 0
        
        #Dictionary used in filling of circles.
        fillDict = {}
        fillDict["x"] = "red"
        fillDict["o"] = "black"
        fillDict[" "] = "white"

        #Iterates through board and fills circles appropriately.
        for row in self.data:
            for element in row:
                self.draw.itemconfig(self.circles[rowAccum][colAccum], fill = fillDict[element])
                colAccum += 1

            rowAccum += 1
            colAccum = 0
    
    #Called when quit button is pressed. Quits game.
    def quitButtonAction(self):
        self.window.destroy()
        self.clickSound()

    #Removes victory line if it exists.
    def removeVictoryLine(self):
        if self.victoryLineIsDrawn:
            self.winLine = self.draw.delete(self.winLine)
            self.victoryLineIsDrawn = False

    #Initiates game replay when called due to player clicking replay button.
    def replayFunc(self):
        #Clears board in preperation for replay.
        self.clickSound()
        sleep(0.3)
        self.clear()
        self.colorFiller()

        self.removeVictoryLine()
        
        #Updates game text to notify player a replay is occuring.
        self.message["text"] = "Replaying..."
        self.window.update()

        turn = "x"
        
        #Recreates the game to be replayed move 
        #   by move based on what's in the replay list.
        for element in self.replayMoveList:

            #Makes move and displays it.
            self.animate(element, turn)
            self.addMove(element, turn)
            self.colorFiller()
            self.chipSound()
            self.window.update()
            
            #Changes turn based on condition.
            if turn == "x":
                turn = "o"
            else:
                turn = "x"
            sleep(0.5)

        #If the player won or the board was full,
        #   the window is updated, otherwise default message is set.
        self.winFullMessageMaker()
       
    #Creates a new game when called. 
    def newGame(self):
        #Plays click sound and rebinds mouse.
        self.clickSound()
        self.draw.bind("<Button-1>", self.mouse)

        #Clears replay and victory lists, and sets message to default.
        self.replayMoveList = []
        self.victoryList = []
        self.defaultMessage()
        
        self.removeVictoryLine()

        #Clears board data and updates GUI to show it. 
        self.clear()
        self.colorFiller()

    #This is used to tell print how to represent 
    #   the board data if printed directly.
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

    #Adds move to board data.
    def addMove(self, col, ox):
        #Adds move if allowed.
        if self.allowsMove(col):
            for row in range(self.height):
                if self.data[row][col] != " ":
                    self.data[row-1][col] = ox
                    return
            self.data[self.height-1][col] = ox

    #Removes a move from the board data.
    def delMove(self, col):
        if self.allowsMove(col):
            for row in range(self.height):
                if self.data[row][col] != " ":
                    self.data[row][col] = " "
                    return
        else:
            self.data[0][col] = " "

    #Determines if a move can be made in the desired column.
    def allowsMove(self, col):
        boardData = self.data
        if (col < 0 or col > self.width - 1) or boardData[0][col] != " ":
            return False
        else:
            return True
        
    #Empties out board data.
    def clear(self):
        for row in range(self.height):
            for col in range(self.width):
                self.data[row][col] = " "
    
    #Checks to see if the board is full.
    def isFull(self):
        total = 0
        #Checks to see if can't move in reach column.
        for col in range(self.width):
            total += not(self.allowsMove(col))

        return total == self.width

    #Checks if a win occured for the player or the AI.
    def winsFor(self, ox):
        #Checks for horizontal victory.
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

        #Checks for vertical victory.
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

        #Checks for down right diagonal victory.
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
        
        #Checks for down left diagonal victory.
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

    #This is a leftover from the text based version of the game.
    #This was the old game loop that ran the game.
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

    #This is a two player version of the game.
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

#This class contains the code that runs the AI for the game.
class Player(object):

    #Sets up recursion depth, starting player, and tie breaker method.
    def __init__(self, ox, tbt, ply):
        self.ox = ox
        self.tbt = tbt
        self.ply = ply
    
    #This uses recursion to generate all score values 
    #   based on what moves are potentially made.
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
    
    #Picks the best positions to move to based on generated score values.
    def pickBestSpots(self, scores):
        bestScore = max(scores)
        bestPositions = []
        for i in range(len(scores)):
            if bestScore == scores[i]:
                bestPositions.append(i)
        return bestPositions

    #This breaks the tie if there's multiple valid spots either 
    #   by picking the leftmost spot, rightmost spot, or randomly picking.
    def tieBreaker(self, tbt, scores):
        goodList = self.pickBestSpots(scores)
        if tbt == "Random":
            return random.choice(goodList)
        if tbt == "Left":
            return goodList[0]
        if tbt == "Right":
            return goodList[-1]

    #Determines what the actual next move the AI should make is.
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
