#Jesse A. Jones
#Version: 2023-05-08.99

import random
from time import sleep
from tkinter import *
import winsound

#This class works with the player class and manages 
#   tkinter stuff to run a GUI game of Connect Four.
#   This version of the game features animations, 
#   sound effects, as well as a rewind after a game is finished.

class Connect4(object):

    #Sets up the GUI.
    def __init__(self, width, height, window=None):
        self.clickFlag = 0

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
        
        self.drawFlag = 0
        
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
            winsound.PlaySound("connectFourSoundEffects/chipDrop.wav", winsound.SND_ASYNC)

    #Plays sound of player winning game.
    def winningSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("connectFourSoundEffects/playerWin.wav", winsound.SND_ASYNC)

    #Plays sound of AI winning game.
    def loosingSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("connectFourSoundEffects/aiWin.wav", winsound.SND_ASYNC)

    #Plays if stalemate occurs.
    def stalemateSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("connectFourSoundEffects/stalemate.wav", winsound.SND_ASYNC)

    #Plays a clip of my dumb voice saying "Click" which is pretty 
    #   much used to confirm if the sound is enabled or not.
    def clickSound(self):
        if self.soundsAllowed:
            winsound.PlaySound("connectFourSoundEffects/click.wav", winsound.SND_ASYNC)

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
        if self.drawFlag == 0:
            self.winLine = self.draw.create_line(
            self.victoryList[-3] * self.diameterX + self.linePadding, 
            self.victoryList[-4] * self.diameterY + self.linePadding, 
            self.victoryList[-1] * self.diameterX + self.linePadding, 
            self.victoryList[-2] * self.diameterY + self.linePadding, 
                width = 15, fill = "blue")
        self.drawFlag += 1

    #Checks for a win for the passed in player                                                  THIS CODE IS TRASH, REFACTOR LATER!!
    #   and checks if the column is full.
    def winFullChecker(self, ox):
        if self.winsFor(ox):
            return True
        if self.isFull():
            return True

    #Returns true if board is full or a player 
    #   has won and updates the text appropriately.
    def winFullMessageMaker(self):                                                              # REFACTOR TRASH CODE!!!!!!!!!!!!!!
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

    #Notifies the player where the AI moves.
    def AIMoveMessage(self):
        self.message["text"] = "The AI moved in col: " + str(self.col)            

    #Sets the text to the loading text when an AI is moving.
    def loadingMessage(self):
        self.message["text"] = "Loading..."

    #Fills in all the circles their appropriate colors based on the board data.
    def colorFiller(self):
        rowAccum = -1
        for row in self.data:
            rowAccum += 1
            colAccum = 0
            for element in row:
                if element == "x":
                    self.draw.itemconfig(self.circles[rowAccum][colAccum], fill = "red")                                            #THIS IS BAD CODE THAT CAN BE REFACTORED TO ARRAY INDEXING. FIX LATER!
                if element == "o":
                    self.draw.itemconfig(self.circles[rowAccum][colAccum], fill = "black")
                if element == " ":
                    self.draw.itemconfig(self.circles[rowAccum][colAccum], fill = "white")
                colAccum += 1
    
    #Called when quit button is pressed. Quits game.
    def quitButtonAction(self):
        self.window.destroy()
        self.clickSound()

    #Initiates game replay when called due to player clicking replay button.
    def replayFunc(self):
        #Clears board in preperation for replay.
        self.clickSound()
        sleep(0.3)
        self.clear()
        self.colorFiller()

        #Deletes any victory lines.
        if self.drawFlag > 0:
            self.winLine = self.draw.delete(self.winLine)
        
        #Updates game text to notify player a replay is occuring.
        self.message["text"] = "Replaying..."
        self.drawFlag = 0
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

        #If the player won or the board was full,                                                                       THIS WHOLE BLOCK OF CODE IS INCREDIBLY JANK. FIX THIS PLZ
        #   the window is updated, otherwise default message is set.
        if self.winFullMessageMaker():
            self.winFullMessageMaker()                  #WHY TF IS THIS BEING CALLED TWICE???? UGLY! FIX THIS LATER!
            self.window.update()
        else:
            self.defaultMessage()
            self.window.update()
       
    #Creates a new game when called. 
    def newGame(self):
        #Plays click sound and rebinds mouse.
        self.clickSound()
        self.draw.bind("<Button-1>", self.mouse)

        #Clears replay and victory lists, and sets message to default.
        self.replayMoveList = []
        self.victoryList = []
        self.defaultMessage()
        
        #Deletes any win line that exists.
        if self.drawFlag > 0:                                                                                                           #DELETION OF WIN LINE SHOULD BE ITS OWN DISCRETE FUNCTION BECAUSE IT'S THE SAME CHECK EVERY TIME!
            self.winLine = self.draw.delete(self.winLine)
        self.drawFlag = 0

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
        elif self.allowsMove(col) == False:                                             #GET RID OF THIS GROSS ELIF SOMEHOW
            self.data[0][col] = " "

    #Determines if a move can be made in the desired column.
    def allowsMove(self, col):
        boardData = self.data
        if col < 0 or col > self.width - 1:
            return False
        if boardData[0][col] != " ":
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
        condit = None
        total = 0
        for col in range(self.width):                                                   #CAN BE REFACTORED TO BE A LOT LESS DISGUSTING
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
