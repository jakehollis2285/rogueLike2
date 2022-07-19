import numpy as np
import InputHandler as InputHandler

GRID_X, GRID_Y = 80, 40
GRID_OFFSET_X, GRID_OFFSET_Y = 0, 0

class Grid(object):

	def initGrid(self):
	    ret = np.full((GRID_X, GRID_Y), InputHandler.STRING_TO_TILESET["."])
	    return ret

	def __init__(self, LEVELNAME="default"):
		super(Grid, self).__init__()
		self.GRID_OBJECT = self.initGrid()
		self.PLAYER_POSITON = [int(GRID_X / 2), int(GRID_Y / 2)]
		self.LEVELNAME = LEVELNAME

	def printGrid(self, window) -> None:
		# print grid
	    for i in range(GRID_X):
	        for j in range(GRID_Y):
	            window.put_char(i + GRID_OFFSET_X, j + GRID_OFFSET_Y, self.GRID_OBJECT[i, j])
	    # print contents
	    window.put_char(self.PLAYER_POSITON[0], self.PLAYER_POSITON[1], InputHandler.STRING_TO_TILESET["@"])

	def movePlayer(self, op):
		# UP -- 1
	    # RIGHT -- 2
	    # DOWN -- 3
	    # LEFT -- 4
	    # move player
		if (op == 1):
			self.PLAYER_POSITON[1] -= 1
		elif (op == 2):
			self.PLAYER_POSITON[0] += 1
		elif (op == 3):
			self.PLAYER_POSITON[1] += 1
		elif (op == 4):
			self.PLAYER_POSITON[0] -= 1
		# check bounds
		if (self.PLAYER_POSITON[0] <= 0):
			self.PLAYER_POSITON[0] = 0
		if (self.PLAYER_POSITON[0] >= GRID_X - 1):
			self.PLAYER_POSITON[0] = GRID_X - 1
		if (self.PLAYER_POSITON[1] <= 0):
			self.PLAYER_POSITON[1] = 0
		if (self.PLAYER_POSITON[1] >= GRID_Y - 1):
			self.PLAYER_POSITON[1] = GRID_Y - 1
