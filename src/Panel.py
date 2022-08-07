import tcod
import numpy as np
from utilities import InputHandler as InputHandler
from utilities import ScreenPrintHelper as sph
from utilities import Colors

class Panel(object):

    def initPanel(self):
        ''' fill panel with blank characters / print border on panel '''
        ret = np.full((self.PANEL_X, self.PANEL_Y), ord(" "))
        for i in range(self.PANEL_X):
            for j in range(self.PANEL_Y):
                sph.printBoxBorder(ret, i, j, self.PANEL_X, self.PANEL_Y)
        return ret

    def printColoredLine(self, message, r, g, b, window):
        ''' print message to panel at panel pointer with rgb colors '''
        colored_message = Colors.colored(r, g, b, message)
        self.printLine(colored_message, window)

    def printLine(self, message, window):
        ''' print message to panel at panel pointer with default color '''
        window.print(self.PANEL_POINTER[0] + self.PANEL_OFFSET_X, self.PANEL_POINTER[1] + self.PANEL_OFFSET_Y, message)
        self.PANEL_POINTER[0] = 2
        self.PANEL_POINTER[1] += 1

    def __init__(self):
        super(Panel, self).__init__()
        self.PANEL_X, self.PANEL_Y = 20, 55
        self.PANEL_OFFSET_X, self.PANEL_OFFSET_Y = 60, 0

        self.PANEL_MAX_X, self.PANEL_MAX_Y = 18, 58
        self.PANEL_OBJECT = self.initPanel()
        self.PANEL_POINTER = [2, 2]
