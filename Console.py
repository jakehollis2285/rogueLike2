import numpy as np

CONSOLE_WIDTH, CONSOLE_HEIGHT = 140, 10
CONSOLE_OFFSET_X, CONSOLE_OFFSET_Y = 0, 40

class Console(object):

    def initConsole(self) -> np.full((CONSOLE_WIDTH, CONSOLE_HEIGHT), 32):
        ret = np.full((CONSOLE_WIDTH, CONSOLE_HEIGHT), 32)
        for i in range(CONSOLE_WIDTH):
            for j in range(CONSOLE_HEIGHT):
                if (i == 1 and j == 1) :
                    ret[i, j] = 36
                if (i == 0  or i == CONSOLE_WIDTH - 1) :
                    ret[i, j] = 124
                if (j == 0  or j == CONSOLE_HEIGHT - 1) :
                    ret[i, j] = 61
                if (i == 0 and j == 0) or (i == CONSOLE_WIDTH - 1 and j == CONSOLE_HEIGHT - 1) or (i == 0 and j == CONSOLE_HEIGHT - 1) or (i == CONSOLE_WIDTH - 1 and j == 0) :
                    ret[i, j] = 35
        return ret

    def __init__(self):
        super(Console, self).__init__()
        self.CONSOLE_OBJECT = self.initConsole()
        self.CONSOLE_POINTER = [2, 1]
        self.HISTORY = []

    def printConsole(self, window) -> None:
        for i in range(CONSOLE_WIDTH):
            for j in range(CONSOLE_HEIGHT):
                if (self.CONSOLE_OBJECT[i, j] != ''):
                   window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, self.CONSOLE_OBJECT[i, j])
                else:
                    window.put_char(i + CONSOLE_OFFSET_X, j + CONSOLE_OFFSET_Y, 0)

    def set(self, val) -> None:
        if (self.CONSOLE_POINTER[0] < CONSOLE_WIDTH - 1 and self.CONSOLE_POINTER[1] < CONSOLE_HEIGHT - 1):
            self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0], self.CONSOLE_POINTER[1]] = val
            self.CONSOLE_POINTER[0] += 1
        elif (self.CONSOLE_POINTER[0] >= CONSOLE_WIDTH - 1):
            self.saveLineToHistory()
            self.CONSOLE_POINTER[0] = 2
            self.CONSOLE_POINTER[1] += 1
        elif (self.CONSOLE_POINTER[1] >= CONSOLE_HEIGHT - 1):
            self.CONSOLE_OBJECT = self.initConsole()
            self.CONSOLE_POINTER = [2, 1]

    def saveLineToHistory(self) -> None:
        self.HISTORY.append(self.CONSOLE_OBJECT[self.CONSOLE_POINTER[0]])

    def newLine(self) -> None:
        self.saveLineToHistory()
        self.CONSOLE_POINTER[0] = 1
        self.CONSOLE_POINTER[1] += 1
        self.set(36)
