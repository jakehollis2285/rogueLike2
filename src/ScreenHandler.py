import numpy as np
import tcod
import math
import Globals as Globals
from utilities import InputHandler as InputHandler
from utilities import ScreenPrintHelper as sph
from bresenham import bresenham

class ScreenHandler(object):
    ''' ScreenHandler is a container object for objects that must be printed to the screen '''
    def __init__(self, CONSOLE, GRID, PANEL):
        super(ScreenHandler, self).__init__()
        self.CONSOLE = CONSOLE
        self.GRID = GRID
        self.PANEL = PANEL
        self.RENDER_X, self.RENDER_Y = GRID.GRID_X + PANEL.PANEL_X, GRID.GRID_Y + CONSOLE.CONSOLE_Y

    def printConsole(self, window) -> None:
        ''' print contents of console obj '''
        for i in range(self.CONSOLE.CONSOLE_X):
            for j in range(self.CONSOLE.CONSOLE_Y):
                # print char or space
                if (self.CONSOLE.CONSOLE_OBJECT[i, j] != ''):
                   window.put_char(i + self.CONSOLE.CONSOLE_OFFSET_X, j + self.CONSOLE.CONSOLE_OFFSET_Y, self.CONSOLE.CONSOLE_OBJECT[i, j])
                else:
                    window.put_char(i + self.CONSOLE.CONSOLE_OFFSET_X, j + self.CONSOLE.CONSOLE_OFFSET_Y, 0)
                # print cursor
                if [i, j] == self.CONSOLE.CONSOLE_POINTER:
                    window.put_char(i + self.CONSOLE.CONSOLE_OFFSET_X, j + self.CONSOLE.CONSOLE_OFFSET_Y, InputHandler.STRING_TO_TILESET["_"])

    def printGridNode(self, window, i, j) -> None:
        ''' function for printing a single grid node, call function in loop to print all grid nodes '''
        self.GRID.GRID_OBJECT[i, j] = self.GRID.GRID_DEFAULT[i, j]
        window.put_char(j + self.GRID.GRID_OFFSET_X, i + self.GRID.GRID_OFFSET_Y, ord(self.GRID.GRID_DEFAULT[i, j]))

    def printGrid(self, window) -> None:
        for i in range(self.GRID.GRID_Y):
            for j in range(self.GRID.GRID_X):
                if(self.GRID.GRID_DEFAULT[i, j] == "{" or self.GRID.GRID_DEFAULT[i, j] == "}"):
                    tcod.console_set_default_foreground(window, tcod.orange)
                else:
                    tcod.console_set_default_foreground(window, tcod.white)
                self.printGridNode(window, i, j)

    def printGridFOV(self, window) -> None:
        # draw grid (upper left quadrant)
        lines = []
        for i in range(self.GRID.GRID_Y):
            for j in range(self.GRID.GRID_X):
                # calculate lines to edges
                if(sph.isEdge(i, j, self.GRID.GRID_X, self.GRID.GRID_Y)):
                    # draw line between player and wall
                    lines.append(bresenham(self.GRID.PLAYER.POSITION[1], self.GRID.PLAYER.POSITION[2], j, i))
                # print explored set and non-explored set
                self.GRID.VISIBLE[i, j] = False
                if(self.GRID.EXPLORED_SET[i, j] == True):
                    tcod.console_set_default_foreground(window, tcod.grey)
                    self.printGridNode(window, i, j)
                else:
                    tcod.console_set_default_foreground(window, tcod.black)
                    self.printGridNode(window, i, j)

        # print vision radius around player
        for line in lines:
            for point in line:
                j = point[0]
                i = point[1]
                if(math.dist([j, i], [self.GRID.PLAYER.POSITION[1], self.GRID.PLAYER.POSITION[2]]) < Globals.PLAYER_FOV_RADIUS):
                    if(self.GRID.GRID_DEFAULT[i, j] == "{" or self.GRID.GRID_DEFAULT[i, j] == "}"):
                        tcod.console_set_default_foreground(window, tcod.orange)
                    else:
                        tcod.console_set_default_foreground(window, tcod.white)    
                    self.GRID.EXPLORED_SET[i, j] = True
                    self.GRID.VISIBLE[i, j] = True
                    self.printGridNode(window, i, j)
                    if(sph.isVisionBlocker(self.GRID.GRID_OBJECT[i, j])):
                        break;
        tcod.console_set_default_foreground(window, tcod.white)          

    def printPanel(self, window) -> None:
        # print border from panel obj
        for i in range(self.PANEL.PANEL_X):
            for j in range(self.PANEL.PANEL_Y):
                if (self.PANEL.PANEL_OBJECT[i, j] != ''):
                    window.put_char(i + self.PANEL.PANEL_OFFSET_X, j + self.PANEL.PANEL_OFFSET_Y, self.PANEL.PANEL_OBJECT[i, j])
        
        self.PANEL.PANEL_POINTER = [2 + self.PANEL.PANEL_OFFSET_X, 2 + self.PANEL.PANEL_OFFSET_Y]
        self.PANEL.printColoredLine("lvl:", 0, 255, 0, window)
        self.PANEL.printColoredLine("{0}".format(self.GRID.LEVELNAME), 0, 255, 0, window)
        self.PANEL.PANEL_POINTER[1] += 1
        self.PANEL.printColoredLine("PlayerPos: {0},{1}".format(self.GRID.PLAYER.POSITION[1] + 1, self.GRID.PLAYER.POSITION[2] + 1), 0, 255, 0, window)
        self.PANEL.PANEL_POINTER[1] += 1

    def printEntities(self, window) -> None:
        if self.GRID.WORLD:
            entities_list = self.GRID.WORLD.ENTITIES
        else:
            entities_list = [self.GRID.PLAYER]
        for i in entities_list:
            if self.GRID.WORLD == False or i.POSITION[0] == self.GRID.WORLD.LEVEL_INDEX:
                tcod.console_set_default_foreground(window, i.color)
                self.GRID.GRID_OBJECT[i.POSITION[2], i.POSITION[1]] = ord(i.symbol)
                window.put_char(i.POSITION[1], i.POSITION[2], ord(i.symbol))
            else:
                tcod.console_set_default_foreground(window, tcod.white)
                window.put_char(i.POSITION[1], i.POSITION[2], ord(self.GRID.GRID_DEFAULT[i.POSITION[2], i.POSITION[1]]))

    def printEntitiesFOV(self, window) -> None:
        if self.GRID.WORLD:
            entities_list = self.GRID.WORLD.ENTITIES
        else:
            entities_list = [self.GRID.PLAYER]
        for i in entities_list:
            if([i.POSITION[1], i.POSITION[2]] == [self.GRID.PLAYER.POSITION[1], self.GRID.PLAYER.POSITION[2]] # if the entity is the player
            or self.GRID.VISIBLE[i.POSITION[2], i.POSITION[1]]): # or the entity is within player sight range
                if self.GRID.WORLD == False or i.POSITION[0] == self.GRID.WORLD.LEVEL_INDEX:
                    tcod.console_set_default_foreground(window, i.color)
                    self.GRID.GRID_OBJECT[i.POSITION[2], i.POSITION[1]] = ord(i.symbol)
                    window.put_char(i.POSITION[1], i.POSITION[2], ord(i.symbol))
                else:
                    tcod.console_set_default_foreground(window, tcod.white)
                    window.put_char(i.POSITION[1], i.POSITION[2], ord(self.GRID.GRID_DEFAULT[i.POSITION[2], i.POSITION[1]]))
            elif(self.GRID.EXPLORED_SET[i.POSITION[2], i.POSITION[1]] == True):
                tcod.console_set_default_foreground(window, tcod.grey)
                window.put_char(i.POSITION[1], i.POSITION[2], ord(self.GRID.GRID_DEFAULT[i.POSITION[2], i.POSITION[1]]))
            else:
                window.put_char(i.POSITION[1], i.POSITION[2], ord(' '))
        tcod.console_set_default_foreground(window, tcod.white)

    def printScreen(self, window) -> None:
        self.printConsole(window)
        self.printPanel(window)
        if(Globals.FOV_ENABLED):
            self.printGridFOV(window)
            self.printEntitiesFOV(window)
        else:
            self.printGrid(window)
            self.printEntities(window)
