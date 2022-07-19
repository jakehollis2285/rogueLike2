import numpy as np

GRID_WIDTH, GRID_HEIGHT = 120, 40
GRID_OFFSET_X, GRID_OFFSET_Y = 0, 0

class Grid(object):

	def initGrid(self) -> np.full((GRID_WIDTH, GRID_HEIGHT), 46):
	    ret = np.full((GRID_WIDTH, GRID_HEIGHT), 46)
	    return ret

	def __init__(self):
		super(Grid, self).__init__()
		self.GRID_OBJECT = self.initGrid()

	def printGrid(self, window) -> None:
	    for i in range(GRID_WIDTH):
	        for j in range(GRID_HEIGHT):
	            window.put_char(i + GRID_OFFSET_X, j + GRID_OFFSET_Y, self.GRID_OBJECT[i, j])
			