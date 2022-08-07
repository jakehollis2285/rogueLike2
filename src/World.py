import numpy as np
from random import randrange, seed
from datetime import datetime
from utilities import InputHandler as InputHandler
import MapGenerator as map_generator
import Entities as Entities

class World(object):
	''' container class for holding world structures '''

	def generate_world(self):
		''' generate 3D numpy array containing 4 underground levels and one above ground '''
		underground_floors = 4
		cave_config = None
		building_config = None
		floors = map_generator.bottomUpGeneration(underground_floors, cave_config, building_config)
		obj = np.full((len(floors), len(floors[0]), len(floors[0][0])), '.')
		for k in range(len(floors)):
			for i in range(len(floors[0])):
				for j in range(len(floors[0][0])):
					obj[k, i, j] = floors[k][i][j]
		# find location for stairs down
		for k in range(len(floors) - 1, 0, -1):
			while (True):
				seed(datetime.now())
				y = randrange(0, len(floors[0]) - 2) # minus 2 for both of these since we want to avoid the edges of the map
				x = randrange(0, len(floors[0][0]) - 2)
				if (obj[k, y, x] == "."):
					if (obj[k - 1, y + 1, x] == "."
					or obj[k - 1, y, x + 1] == "."
					or obj[k - 1, y - 1, x] == "."
					or obj[k - 1, y, x - 1] == "."):
						obj[k, y, x] = "{"
						obj[k - 1, y, x] = "}"
						break;
		return obj

	def generate_explored_set(self, shape):
		''' generate a 3D boolean array of the same size as the world '''
		return np.full(shape, False)

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
		self.EXPLORED_SET = self.generate_explored_set(np.shape(self.WORLD_OBJECT))
		self.ENTITIES = Entities.initDefaultEntities(self.WORLD_OBJECT, 60, 40, 4)
		self.NAME = NAME
		self.LEVEL_INDEX = len(self.WORLD_OBJECT) - 1
