#Jesse A. Jones
#Version: 2023-06-07.26

from tkinter import *

#This takes in a string and reverses it. Pretty boring, I know.
class StrRev(object):
    def __init__(self, window = None):
        self.window = window

        #Holds quit button.
        self.frameTop = Frame(self.window)
        self.frameTop.pack(side = TOP)

        #Quits program when pressed.
        self.quitButton = Button(self.frameTop, text = "Quit",
            font = "Ariel 20", command = self.quitButtonAction)
        self.quitButton.pack()

        #Holds string input field, reverse button, and reversed string.
        self.frameBottom = Frame(self.window)
        self.frameBottom.pack(side = BOTTOM)

        #String input field.
        self.message = Label(self.frameBottom, text = "Enter String:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 0, column = 0)
        self.msg = Entry(self.frameBottom, font = "Ariel 20")
        self.msg.grid(row = 0, column = 1)

        #Reverses string when pressed.
        self.convButtonI = Button(self.frameBottom, text = "Reverse", 
            font = "Ariel 20", command = self.reverse)
        self.convButtonI.grid(row = 1, column = 0)

        #Reversed string output.
        self.message = Label(self.frameBottom, text = "Output:", font = "Ariel 20", anchor = "w")
        self.message.grid(row = 3, column = 0)
        self.tOutput = Entry(self.frameBottom, font = "Ariel 20")
        self.tOutput.grid(row = 3, column = 1)

    #Quits program when called.
    def quitButtonAction(self):
        self.window.destroy()

    #Reverses string when called.
    def reverse(self):
        #Gets string and reverses it.
        entryString = self.msg.get()
        revString = entryString[::-1]

        #Displays resulting reversed string.
        self.tOutput.delete(0, "end")
        self.tOutput.insert(0, revString)

def main():
    root = Tk()
    root.title("String Reverser")
    temp = StrRev(root)
    root.mainloop()

if __name__ == "__main__":
    main()
