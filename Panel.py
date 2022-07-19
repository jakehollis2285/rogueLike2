import numpy as np

PANEL_WIDTH, PANEL_HEIGHT = 20, 40
PANEL_OFFSET_X, PANEL_OFFSET_Y = 120, 0

class Panel(object):

    def initPanel(self) -> np.full((PANEL_WIDTH, PANEL_HEIGHT), 23):
        ret = np.full((PANEL_WIDTH, PANEL_HEIGHT), 23)
        for i in range(PANEL_WIDTH):
            for j in range(PANEL_HEIGHT):
                if (i == 0  or i == PANEL_WIDTH - 1) :
                    ret[i, j] = 124
                if (j == 0  or j == PANEL_HEIGHT - 1) :
                    ret[i, j] = 61
                if (i == 0 and j == 0) or (i == PANEL_WIDTH - 1 and j == PANEL_HEIGHT - 1) or (i == 0 and j == PANEL_HEIGHT - 1) or (i == PANEL_WIDTH - 1 and j == 0) :
                    ret[i, j] = 35
        return ret

    def __init__(self):
        super(Panel, self).__init__()
        self.PANEL_OBJECT = self.initPanel()

    def printPanel(self, window) -> None:
        for i in range(PANEL_WIDTH):
            for j in range(PANEL_HEIGHT):
                if (self.PANEL_OBJECT[i, j] != ''):
                    window.put_char(i + PANEL_OFFSET_X, j + PANEL_OFFSET_Y, self.PANEL_OBJECT[i, j])