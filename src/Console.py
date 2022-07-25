import tcod
import numpy as np
import CommandHandler as CommandHandler
from utilities import InputHandler as InputHandler
from utilities import ScreenPrintHelper as sph
from utilities import Logger as Logger

class Console(object):

    def initConsole(self):
        ret = np.full((self.CONSOLE_X, self.CONSOLE_Y), ord(" "))
        for i in range(self.CONSOLE_X):
            for j in range(self.CONSOLE_Y):
                # draw prompt
                if (i == 1 and j == 1) :
                    ret[i, j] = ord("$")
                # draw bounding box
                sph.printBoxBorder(ret, i, j, self.CONSOLE_X, self.CONSOLE_Y)
        return ret

    def __init__(self):
        super(Console, self).__init__()
        self.CONSOLE_X, self.CONSOLE_Y = 60, 10
        self.CONSOLE_OFFSET_X, self.CONSOLE_OFFSET_Y = 0, 40
        self.HISTORY_MAX_LENGTH = 100
        self.CONSOLE_OBJECT = self.initConsole()
        self.CONSOLE_POINTER = [2, 1]
        self.HISTORY = []

    # def printConsole(self, window) -> None:
        ''' print contents of console obj '''
        # for i in range(CONSOLE_X):
        #     for j in range(CONSOLE_Y):
                

    def printLine(self, message, saveToHistory=False) -> None:
        ''' print a string {message} in the console at console pointer '''
        self.CONSOLE_POINTER = [2, self.CONSOLE_POINTER[1] + 1]
        for i in range(len(message)):
            self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0] + i, self.CONSOLE_POINTER[1]] = ord(message[i])
        if (saveToHistory):
            self.saveLineToHistory()
        self.CONSOLE_POINTER[1] += 1

    def printLines(self, messages) -> None:
        for line in messages:
            self.printLine(line)

    def saveLineToHistory(self) -> None:
        ''' append line to history list '''
        self.HISTORY.append(self.CONSOLE_OBJECT[2:,self.CONSOLE_POINTER[1]])
        if(len(self.HISTORY) > self.HISTORY_MAX_LENGTH):
            self.HISTORY.pop(0)

    def set(self, val) -> None:
        ''' 
            set value of CONSOLE_OBJECT at CONSOLE_POINTER, and increment CONSOLE_POINTER
             - handles incrementing to new line with no prompt with line saving to history
             - handles clearing the console when the console object buffer is full
        '''
        if (self.CONSOLE_POINTER[0] < self.CONSOLE_X - 1 and self.CONSOLE_POINTER[1] < self.CONSOLE_Y - 1):
            # increment pointer same line
            self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = val
            self.CONSOLE_POINTER[0] += 1
        elif (self.CONSOLE_POINTER[0] >= self.CONSOLE_X - 1):
            # increment pointer new line
            self.saveLineToHistory()
            self.CONSOLE_POINTER[0] = 2
            self.CONSOLE_POINTER[1] += 1
        elif (self.CONSOLE_POINTER[1] >= self.CONSOLE_Y - 1):
            # clear screen / reset pointer
            self.CONSOLE_OBJECT = self.initConsole()
            self.CONSOLE_POINTER = [2, 1]

    def newLine(self) -> None:
        '''
            return character input in the console
             - get command
             - save line to history
             - increment pointer to new line and add prompt
        '''
        command_array = self.CONSOLE_OBJECT[2:,self.CONSOLE_POINTER[1]]
        command = CommandHandler.parseCommand(command_array)
        Logger.debug("user entered command: {0}".format(command))
        self.saveLineToHistory()
        self.set(ord(" "))
        command_response = CommandHandler.handleCommand(command)
        if (command_response != None):
            self.printLines(command_response)
        self.CONSOLE_POINTER = [1, self.CONSOLE_POINTER[1] + 1]
        self.set(ord("$"))
        self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = ord("_")

    def backspace(self) -> None:
        ''' handle backspace input in console, delete current char move cursor back '''
        self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = ord(" ")
        self.CONSOLE_POINTER[0] -= 1
        if (self.CONSOLE_POINTER[0] <= 2) :
            self.CONSOLE_POINTER[0] = 2
        self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = ord("_")
