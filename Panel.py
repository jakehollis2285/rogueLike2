import numpy as np
import InputHandler as InputHandler

PANEL_X, PANEL_Y = 20, 60
PANEL_OFFSET_X, PANEL_OFFSET_Y = 100, 0

class Panel(object):

    def initPanel(self):
        ret = np.full((PANEL_X, PANEL_Y), InputHandler.STRING_TO_TILESET[" "])
        for i in range(PANEL_X):
            for j in range(PANEL_Y):
                if (i == 0  or i == PANEL_X - 1) :
                    ret[i, j] = InputHandler.STRING_TO_TILESET["|"]
                if (j == 0  or j == PANEL_Y - 1) :
                    ret[i, j] = InputHandler.STRING_TO_TILESET["="]
                if (i == 0 and j == 0) or (i == PANEL_X - 1 and j == PANEL_Y - 1) or (i == 0 and j == PANEL_Y - 1) or (i == PANEL_X - 1 and j == 0) :
                    ret[i, j] = InputHandler.STRING_TO_TILESET["#"]
        return ret

    def __init__(self):
        super(Panel, self).__init__()
        self.PANEL_OBJECT = self.initPanel()

    def printPanel(self, window) -> None:
        for i in range(PANEL_X):
            for j in range(PANEL_Y):
                if (self.PANEL_OBJECT[i, j] != ''):
                    window.put_char(i + PANEL_OFFSET_X, j + PANEL_OFFSET_Y, self.PANEL_OBJECT[i, j])