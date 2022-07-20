import tcod
import numpy as np
from utilities import Logger as Logger
from utilities import InputHandler as InputHandler
import Entities as Entities

GRID_X, GRID_Y = 60, 40
GRID_OFFSET_X, GRID_OFFSET_Y = 0, 0

class Grid(object):

    def initGrid(self):
        ret = np.full((GRID_Y, GRID_X), InputHandler.STRING_TO_TILESET["."])
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
        elif (pos_x > GRID_X - 1):
            return True
        elif (pos_y < 0):
            return True
        elif (pos_y > GRID_Y - 1):
            return True
        # check allowed tiles
        elif (self.GRID_OBJECT[pos_y, pos_x] == InputHandler.STRING_TO_TILESET['.']):
            return False
        elif (self.GRID_OBJECT[pos_y, pos_x] == InputHandler.STRING_TO_TILESET['{']):
            self.WORLD.decrementLevelIndex()
            self.rerenderGrid()
            return False
        elif (self.GRID_OBJECT[pos_y, pos_x] == InputHandler.STRING_TO_TILESET['}']):
            self.WORLD.incrementLevelIndex()
            self.rerenderGrid()
            return False
        elif (self.GRID_OBJECT[pos_y, pos_x] == InputHandler.STRING_TO_TILESET['%']):
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
        if (WORLD == None):
            self.GRID_DEFAULT = self.initGrid()
            self.GRID_OBJECT = self.initGrid()
            self.LEVELNAME = "default"
            self.ENTITIES = Entities.initDefaultEntities(GRID_X, GRID_Y)
        else:
            self.GRID_DEFAULT = self.initGridFromWorld(WORLD)
            self.GRID_OBJECT = self.initGridFromWorld(WORLD)
            self.WORLD = WORLD
            self.LEVELNAME = WORLD.NAME + " : " + str(WORLD.LEVEL_INDEX)
            self.ENTITIES = Entities.initDefaultEntities(GRID_X, GRID_Y)
        self.PLAYER = self.ENTITIES[-1]

    def draw(self, window) -> None:
        ''' Top level function to call rendering functions '''
        self.drawGrid(window)
        self.drawEntities(window)

    def drawGrid(self, window) -> None:
        ''' draw tiles in GRID '''
        tcod.console_set_default_foreground(window, tcod.white)
        for i in range(GRID_Y):
            for j in range(GRID_X):
                self.GRID_OBJECT[i, j] = self.GRID_DEFAULT[i, j]
                # draw stairs orange
                if(self.GRID_DEFAULT[i, j] == InputHandler.STRING_TO_TILESET["{"] or self.GRID_DEFAULT[i, j] == InputHandler.STRING_TO_TILESET["}"]):
                    tcod.console_set_default_foreground(window, tcod.orange)
                    window.put_char(j + GRID_OFFSET_X, i + GRID_OFFSET_Y, self.GRID_DEFAULT[i, j])
                    tcod.console_set_default_foreground(window, tcod.white)
                # draw all other chars white
                else:
                    window.put_char(j + GRID_OFFSET_X, i + GRID_OFFSET_Y, self.GRID_DEFAULT[i, j])

    def drawEntities(self, window) -> None:
        ''' draw entitties with specific entity color '''
        for i in self.ENTITIES:
            tcod.console_set_default_foreground(window, i.color)
            self.GRID_OBJECT[i.POSITION[1], i.POSITION[0]] = InputHandler.STRING_TO_TILESET[i.symbol]
            window.put_char(i.POSITION[0], i.POSITION[1], InputHandler.STRING_TO_TILESET[i.symbol])
        tcod.console_set_default_foreground(window, tcod.white)

    def move(self, entity, op) -> None:
        # NORTH -- 1
        # EAST -- 2
        # SOUTH -- 3
        # WEST -- 4
        # move player
        if (op == 1):
            if (self.isOccupied(entity.POSITION[0], entity.POSITION[1] - 1)):
                return
            entity.POSITION[1] -= 1
        elif (op == 2):
            if (self.isOccupied(entity.POSITION[0] + 1, entity.POSITION[1])):
                return
            entity.POSITION[0] += 1
        elif (op == 3):
            if (self.isOccupied(entity.POSITION[0], entity.POSITION[1] + 1)):
                return
            entity.POSITION[1] += 1
        elif (op == 4):
            if (self.isOccupied(entity.POSITION[0] - 1, entity.POSITION[1])):
                return
            entity.POSITION[0] -= 1
