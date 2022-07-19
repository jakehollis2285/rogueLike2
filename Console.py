import numpy as np

import InputHandler as InputHandler

CONSOLE_X, CONSOLE_Y = 100, 20
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
                # draw border
                if (i == 0  or i == CONSOLE_X - 1) :
                    ret[i, j] = InputHandler.STRING_TO_TILESET["|"]
                if (j == 0  or j == CONSOLE_Y - 1) :
                    ret[i, j] = InputHandler.STRING_TO_TILESET["="]
                if (i == 0 and j == 0) or (i == CONSOLE_X - 1 and j == CONSOLE_Y - 1) or (i == 0 and j == CONSOLE_Y - 1) or (i == CONSOLE_X - 1 and j == 0) :
                    ret[i, j] = InputHandler.STRING_TO_TILESET["#"]
        return ret

    def __init__(self):
        super(Console, self).__init__()
        self.CONSOLE_OBJECT = self.initConsole()
        self.CONSOLE_POINTER = [2, 1]
        self.HISTORY = []

    def printConsole(self, window) -> None:
        for i in range(CONSOLE_X):
            for j in range(CONSOLE_Y):
                if (self.CONSOLE_OBJECT[i, j] != ''):
                   window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, self.CONSOLE_OBJECT[i, j])
                else:
                    window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, 0)
                if [i, j] == self.CONSOLE_POINTER:
                    window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, InputHandler.STRING_TO_TILESET["_"])

    def saveLineToHistory(self) -> None:
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
            self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = val
            self.CONSOLE_POINTER[0] += 1
        elif (self.CONSOLE_POINTER[0] >= CONSOLE_X - 1):
            self.saveLineToHistory()
            self.CONSOLE_POINTER[0] = 2
            self.CONSOLE_POINTER[1] += 1
        elif (self.CONSOLE_POINTER[1] >= CONSOLE_Y - 1):
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
        command = ""
        for i in range(len(command_array)):
            if (InputHandler.TILESET_TO_STRING[command_array[i]] == " ") and (InputHandler.TILESET_TO_STRING[command_array[i + 1]] == " "):
                break;
            if (InputHandler.TILESET_TO_STRING[command_array[i]] != "|"):
                command += InputHandler.TILESET_TO_STRING[command_array[i]]
        print("[DEBUG] user entered command: {command}", command)
        self.saveLineToHistory()
        self.set(InputHandler.STRING_TO_TILESET[" "])
        self.CONSOLE_POINTER[0] = 1
        self.CONSOLE_POINTER[1] += 1
        self.set(InputHandler.STRING_TO_TILESET["$"])

    def backspace(self) -> None:
        self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = InputHandler.STRING_TO_TILESET[" "]
        self.CONSOLE_POINTER[0] -= 1
        if (self.CONSOLE_POINTER[0] <= 2) :
            self.CONSOLE_POINTER[0] = 2
        self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = InputHandler.STRING_TO_TILESET["_"]
