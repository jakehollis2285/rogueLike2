import numpy as np
import InputHandler as InputHandler

GRID_X, GRID_Y = 100, 40
GRID_OFFSET_X, GRID_OFFSET_Y = 0, 0

class Grid(object):

	def initGrid(self):
	    ret = np.full((GRID_X, GRID_Y), InputHandler.STRING_TO_TILESET["."])
	    return ret

	def __init__(self):
		super(Grid, self).__init__()
		self.GRID_OBJECT = self.initGrid()

	def printGrid(self, window) -> None:
	    for i in range(GRID_X):
	        for j in range(GRID_Y):
	            window.put_char(i + GRID_OFFSET_X, j + GRID_OFFSET_Y, self.GRID_OBJECT[i, j])
			