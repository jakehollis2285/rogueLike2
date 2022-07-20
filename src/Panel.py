import tcod
import numpy as np
from utilities import InputHandler as InputHandler
from utilities import ScreenPrintHelper as sph

PANEL_X, PANEL_Y = 20, 50
PANEL_OFFSET_X, PANEL_OFFSET_Y = 60, 0

PANEL_MAX_X, PANEL_MAX_Y = 18, 58

class Panel(object):

    def colored(self, r, g, b, text):
        ''' color formated tcod string '''
        return f"{tcod.COLCTRL_FORE_RGB:c}{r:c}{g:c}{b:c}{text}"

    def initPanel(self):
        ''' fill panel with blank characters / print border on panel '''
        ret = np.full((PANEL_X, PANEL_Y), InputHandler.STRING_TO_TILESET[" "])
        for i in range(PANEL_X):
            for j in range(PANEL_Y):
                sph.printBoxBorder(ret, i, j, PANEL_X, PANEL_Y)
        return ret

    def printColoredLine(self, message, r, g, b, window):
        ''' print message to panel at panel pointer with rgb colors '''
        colored_message = self.colored(r, g, b, message)
        self.printLine(colored_message, window)

    def printLine(self, message, window):
        ''' print message to panel at panel pointer with default color '''
        window.print(self.PANEL_POINTER[0] + PANEL_OFFSET_X, self.PANEL_POINTER[1] + PANEL_OFFSET_Y, message)
        self.PANEL_POINTER[0] = 2
        self.PANEL_POINTER[1] += 1


    def printLevelName(self, GRID, window):
        '''
            lvl:
            levelname
        '''
        self.printColoredLine("lvl:", 0, 255, 0, window)
        self.printColoredLine("{0}".format(GRID.LEVELNAME), 0, 255, 0, window)
        self.PANEL_POINTER[1] += 1

    def printPlayerPosition(self, GRID, window):
        '''
            PlayerPos: x,y
        '''
        self.printColoredLine("PlayerPos: {0},{1}".format(GRID.PLAYER.POSITION[0] + 1, GRID.PLAYER.POSITION[1] + 1), 0, 255, 0, window)
        self.PANEL_POINTER[1] += 1

    def __init__(self):
        super(Panel, self).__init__()
        self.PANEL_OBJECT = self.initPanel()
        self.PANEL_POINTER = [2, 2]

    def printPanel(self, GRID, window) -> None:
        # print border from panel obj
        for i in range(PANEL_X):
            for j in range(PANEL_Y):
                if (self.PANEL_OBJECT[i, j] != ''):
                    window.put_char(i + PANEL_OFFSET_X, j + PANEL_OFFSET_Y, self.PANEL_OBJECT[i, j])

        # set pointer / print contents
        self.PANEL_POINTER = [2, 2]
        self.printLevelName(GRID, window)
        self.printPlayerPosition(GRID, window)