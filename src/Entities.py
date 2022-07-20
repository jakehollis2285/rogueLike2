import tcod

def initDefaultEntities(GRID_X, GRID_Y):
    ''' entities are static for each level in the world change this '''
    player = Entity('@', int(GRID_X / 2), int(GRID_Y / 2), tcod.white)
    npc = Entity('@', int(GRID_X / 2), int(GRID_Y / 2) - 5, tcod.yellow)
    return [npc, player]

class Entity(object):
    ''' default class representing a grid object '''
    def __init__(self, symbol, pos_x, pos_y, color):
        super(Entity, self).__init__()
        self.symbol = symbol
        self.POSITION = [pos_x, pos_y]
        self.color = color
        