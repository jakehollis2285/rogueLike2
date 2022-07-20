import tcod
import numpy as np

import InputHandler as InputHandler
import ScreenPrintHelper as sph
import Logger as Logger

CONSOLE_X, CONSOLE_Y = 80, 20
CONSOLE_OFFSET_X, CONSOLE_OFFSET_Y = 0, 40
HISTORY_MAX_LENGTH = 100

class Console(object):

    def initConsole(self):
        ret = np.full((CONSOLE_X, CONSOLE_Y), InputHandler.STRING_TO_TILESET[" "])
        for i in range(CONSOLE_X):
            for j in range(CONSOLE_Y):
                # draw prompt
                if (i == 1 and j == 1) :
                    ret[i, j] = InputHandler.STRING_TO_TILESET["$"]
                # draw bounding box
                sph.printBoxBorder(ret, i, j, CONSOLE_X, CONSOLE_Y)
        return ret

    def __init__(self):
        super(Console, self).__init__()
        self.CONSOLE_OBJECT = self.initConsole()
        self.CONSOLE_POINTER = [2, 1]
        self.HISTORY = []

    def printConsole(self, window) -> None:
        ''' print contents of console obj '''
        for i in range(CONSOLE_X):
            for j in range(CONSOLE_Y):
                # print char or space
                if (self.CONSOLE_OBJECT[i, j] != ''):
                   window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, self.CONSOLE_OBJECT[i, j])
                else:
                    window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, 0)
                # print cursor
                if [i, j] == self.CONSOLE_POINTER:
                    window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, InputHandler.STRING_TO_TILESET["_"])

    def printLine(self, message, saveToHistory=False) -> None:
        ''' print a string {message} in the console at console pointer '''
        self.CONSOLE_POINTER = [2, self.CONSOLE_POINTER[1] + 1]
        for i in range(len(message)):
            self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0] + i, self.CONSOLE_POINTER[1]] = InputHandler.STRING_TO_TILESET[message[i]]
        if (saveToHistory):
            self.saveLineToHistory()
        self.CONSOLE_POINTER[1] += 1

    def saveLineToHistory(self) -> None:
        ''' append line to history list '''
        self.HISTORY.append(self.CONSOLE_OBJECT[2:,self.CONSOLE_POINTER[1]])
        if(len(self.HISTORY) > HISTORY_MAX_LENGTH):
            self.HISTORY.pop(0)

    def set(self, val) -> None:
        ''' 
            set value of CONSOLE_OBJECT at CONSOLE_POINTER, and increment CONSOLE_POINTER
             - handles incrementing to new line with no prompt with line saving to history
             - handles clearing the console when the console object buffer is full
        '''
        if (self.CONSOLE_POINTER[0] < CONSOLE_X - 1 and self.CONSOLE_POINTER[1] < CONSOLE_Y - 1):
            # increment pointer same line
            self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = val
            self.CONSOLE_POINTER[0] += 1
        elif (self.CONSOLE_POINTER[0] >= CONSOLE_X - 1):
            # increment pointer new line
            self.saveLineToHistory()
            self.CONSOLE_POINTER[0] = 2
            self.CONSOLE_POINTER[1] += 1
        elif (self.CONSOLE_POINTER[1] >= CONSOLE_Y - 1):
            # clear screen / reset pointer
            self.CONSOLE_OBJECT = self.initConsole()
            self.CONSOLE_POINTER = [2, 1]

    def printHelp(self):
        ''' print help command '''
        lines = ["[commands]",
        "    help    print this message"]
        for line in lines:
            self.printLine(line)

    def handleCommand(self, command) -> None:
        ''' command interfaces (given string command call relevant function) '''
        if (command == "help"):
            self.printHelp()

    def parseCommand(self, command_array) -> None:
        ''' 
            given an array of character return a string command 
            strings returned are in the form "arg1 arg2 arg3 ... argN"
            where arguments are allowed 1 space in between

            '|' and '_' characters are ignored
            2 spaces terminates the string
        '''
        command = ""
        for i in range(len(command_array)):
            if (InputHandler.TILESET_TO_STRING[command_array[i]] == " ") and (InputHandler.TILESET_TO_STRING[command_array[i + 1]] == " "):
                break;
            if (InputHandler.TILESET_TO_STRING[command_array[i]] != "|" and InputHandler.TILESET_TO_STRING[command_array[i]] != "_"):
                command += InputHandler.TILESET_TO_STRING[command_array[i]]
        return command

    def newLine(self) -> None:
        '''
            return character input in the console
             - get command
             - save line to history
             - increment pointer to new line and add prompt
        '''
        command_array = self.CONSOLE_OBJECT[2:,self.CONSOLE_POINTER[1]]
        command = self.parseCommand(command_array)
        Logger.debug("user entered command: {0}".format(command))
        self.saveLineToHistory()
        self.set(InputHandler.STRING_TO_TILESET[" "])
        self.CONSOLE_POINTER[0] = 1
        self.CONSOLE_POINTER[1] += 1
        self.handleCommand(command)
        self.set(InputHandler.STRING_TO_TILESET["$"])

    def backspace(self) -> None:
        ''' handle backspace input in console, delete current char move cursor back '''
        self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = InputHandler.STRING_TO_TILESET[" "]
        self.CONSOLE_POINTER[0] -= 1
        if (self.CONSOLE_POINTER[0] <= 2) :
            self.CONSOLE_POINTER[0] = 2
        self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = InputHandler.STRING_TO_TILESET["_"]
