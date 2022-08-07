import tcod
import random
from datetime import datetime

def initDefaultEntities(WORLD_OBJECT, GRID_X, GRID_Y, GRID_Z):
    ''' entities are static for each level in the world change this '''
    
    # Place a player and an NPC on the first floor of the dungeon in a random position
    random.seed(datetime.now())
    p_x, p_y = random.randrange(GRID_X), random.randrange(GRID_Y)
    n_x, n_y = random.randrange(GRID_X), random.randrange(GRID_Y)
    # ensure player and npc are not in the same location
    while(True):
        if(p_x == n_x or p_y == n_y or WORLD_OBJECT[GRID_Z][p_y][p_x] != '.' or WORLD_OBJECT[GRID_Z][n_y][n_x] != '.'):
            p_x, p_y = random.randrange(GRID_X), random.randrange(GRID_Y)
            n_x, n_y = random.randrange(GRID_X), random.randrange(GRID_Y)
        else:
            break;

    player = Entity('@', GRID_Z, p_x, p_y, tcod.white)
    npc = Entity('@', GRID_Z, n_x, n_y, tcod.yellow)
    return [npc, player]

def initPlayerOnly(GRID_X, GRID_Y):
    player = Entity('@', 0, int(GRID_X / 2), int(GRID_Y / 2), tcod.white)
    return player

class Entity(object):
    ''' default class representing a grid object '''
    def __init__(self, symbol, pos_z, pos_x, pos_y, color):
        super(Entity, self).__init__()
        self.symbol = symbol
        self.POSITION = [pos_z, pos_x, pos_y]
        self.color = color
        