import numpy as np
from random import randrange, seed
from datetime import datetime
from utilities import InputHandler as InputHandler
import MapGenerator as map_generator

class World(object):
	''' container class for holding world structures '''
	
	def generate_world(self):
		''' generate 3D numpy array containing 4 underground levels and one above ground '''
		underground_floors = 4
		cave_config = None
		building_config = None
		floors = map_generator.bottomUpGeneration(underground_floors, cave_config, building_config)
		obj = np.full((len(floors), len(floors[0]), len(floors[0][0])), InputHandler.STRING_TO_TILESET['.'])
		for k in range(len(floors)):
			for i in range(len(floors[0])):
				for j in range(len(floors[0][0])):
					obj[k, i, j] = InputHandler.STRING_TO_TILESET[floors[k][i][j]]
		for k in range(len(floors) - 1, 0, -1):
			# find location for stairs down
			while (True):
				seed(datetime.now())
				y = randrange(0, len(floors[0]) - 2) # minus 2 for both of these since we want to avoid the edges of the map
				x = randrange(0, len(floors[0][0]) - 2)
				if (obj[k, y, x] == InputHandler.STRING_TO_TILESET["."]):
					if (obj[k - 1, y + 1, x] == InputHandler.STRING_TO_TILESET["."]
					or obj[k - 1, y, x + 1] == InputHandler.STRING_TO_TILESET["."]
					or obj[k - 1, y - 1, x] == InputHandler.STRING_TO_TILESET["."]
					or obj[k - 1, y, x - 1] == InputHandler.STRING_TO_TILESET["."]):
						obj[k, y, x] = InputHandler.STRING_TO_TILESET["{"]
						obj[k - 1, y, x] = InputHandler.STRING_TO_TILESET["}"]
						break;
		return obj

	def incrementLevelIndex(self):
		if (self.LEVEL_INDEX == len(self.WORLD_OBJECT) - 1):
			return
		else:
			self.LEVEL_INDEX += 1

	def decrementLevelIndex(self):
		if (self.LEVEL_INDEX == 0):
			return
		else:
			self.LEVEL_INDEX -= 1

	def __init__(self, NAME):
		super(World, self).__init__()
		self.WORLD_OBJECT = self.generate_world()
		self.NAME = NAME
		self.LEVEL_INDEX = len(self.WORLD_OBJECT) - 1
