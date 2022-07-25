import tcod
import math
import numpy as np
from utilities import Logger as Logger
from utilities import InputHandler as InputHandler
import Globals as Globals
import Entities as Entities

class Grid(object):

    def initGrid(self):
        ret = np.full((GRID_Y, GRID_X), ".")
        return ret

    def initGridFromWorld(self, WORLD):
        ret = WORLD.WORLD_OBJECT[WORLD.LEVEL_INDEX].copy()
        return ret

    def rerenderGrid(self):
        '''
            this function should be called if the WORLD.LEVEL_INDEX is changed
            update levelname and grid objects

        '''
        self.LEVELNAME = self.WORLD.NAME + " : " + str(self.WORLD.LEVEL_INDEX)
        self.GRID_DEFAULT = self.initGridFromWorld(self.WORLD)
        self.GRID_OBJECT = self.initGridFromWorld(self.WORLD)

    def isOccupied(self, pos_x, pos_y):
        # check bounds
        if (pos_x < 0):
            return True
        elif (pos_x > self.GRID_X - 1):
            return True
        elif (pos_y < 0):
            return True
        elif (pos_y > self.GRID_Y - 1):
            return True
        # check allowed tiles
        elif (self.GRID_OBJECT[pos_y, pos_x] == '.'):
            return False
        elif (self.GRID_OBJECT[pos_y, pos_x] == '{'):
            self.WORLD.decrementLevelIndex()
            self.PLAYER.POSITION[0] -= 1
            self.rerenderGrid()
            return False
        elif (self.GRID_OBJECT[pos_y, pos_x] == '}'):
            self.WORLD.incrementLevelIndex()
            self.PLAYER.POSITION[0] += 1
            self.rerenderGrid()
            return False
        elif (self.GRID_OBJECT[pos_y, pos_x] == '%'):
            return False
        # prevent all others
        else:
            return True

    def __init__(self, WORLD=None):
        ''' 
            constructor for Grid
            WORLD object is optional, if no world is passed, the default blank level will be loaded
        '''
        super(Grid, self).__init__()
        # create 2 grid objects, one to update and one to store initial data locally
        # set levelname
        # place entities on screen
        self.GRID_X, self.GRID_Y = 60, 40
        self.GRID_OFFSET_X, self.GRID_OFFSET_Y = 0, 0
        if (WORLD == None):
            self.GRID_DEFAULT = self.initGrid()
            self.GRID_OBJECT = self.initGrid()
            self.LEVELNAME = "default"
            self.WORLD = False
            self.PLAYER = Entities.initPlayerOnly(self.GRID_X, self.GRID_Y)
        else:
            self.GRID_DEFAULT = self.initGridFromWorld(WORLD)
            self.GRID_OBJECT = self.initGridFromWorld(WORLD)
            self.WORLD = WORLD
            self.LEVELNAME = WORLD.NAME + " : " + str(WORLD.LEVEL_INDEX)
            self.PLAYER = self.WORLD.ENTITIES[-1]

    def set(self, y, x, char) :
        if(x >= 0 and x < self.GRID_X and y >= 0 and y < self.GRID_Y):
            self.GRID_DEFAULT[y, x] = char
            k = self.WORLD.LEVEL_INDEX
            self.WORLD.WORLD_OBJECT[k, y, x] = char

    def move(self, entity, op) -> None:
        # NORTH -- 1
        # EAST -- 2
        # SOUTH -- 3
        # WEST -- 4
        # move player
        if (op == 1):
            if (self.isOccupied(entity.POSITION[1], entity.POSITION[2] - 1)):
                return
            entity.POSITION[2] -= 1
        elif (op == 2):
            if (self.isOccupied(entity.POSITION[1] + 1, entity.POSITION[2])):
                return
            entity.POSITION[1] += 1
        elif (op == 3):
            if (self.isOccupied(entity.POSITION[1], entity.POSITION[2] + 1)):
                return
            entity.POSITION[2] += 1
        elif (op == 4):
            if (self.isOccupied(entity.POSITION[1] - 1, entity.POSITION[2])):
                return
            entity.POSITION[1] -= 1
