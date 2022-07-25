import tcod
from utilities import InputHandler as InputHandler

class ScreenHandler(object):
    ''' ScreenHandler is a container object for objects that must be printed to the screen '''
    def __init__(self, CONSOLE, GRID, PANEL):
        super(ScreenHandler, self).__init__()
        self.CONSOLE = CONSOLE
        self.GRID = GRID
        self.PANEL = PANEL
        self.RENDER_X, self.RENDER_Y = GRID.GRID_X + PANEL.PANEL_X, GRID.GRID_Y + CONSOLE.CONSOLE_Y

    def printScreen(self, window) -> None:
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

        # print border from panel obj
        for i in range(self.PANEL.PANEL_X):
            for j in range(self.PANEL.PANEL_Y):
                if (self.PANEL.PANEL_OBJECT[i, j] != ''):
                    window.put_char(i + self.PANEL.PANEL_OFFSET_X, j + self.PANEL.PANEL_OFFSET_Y, self.PANEL.PANEL_OBJECT[i, j])

        # draw grid
        for i in range(self.GRID.GRID_Y):
            for j in range(self.GRID.GRID_X):
                self.GRID.GRID_OBJECT[i, j] = self.GRID.GRID_DEFAULT[i, j]
                # draw stairs orange
                if(self.GRID.GRID_DEFAULT[i, j] == "{" or self.GRID.GRID_DEFAULT[i, j] == "}"):
                    tcod.console_set_default_foreground(window, tcod.orange)
                    window.put_char(j + self.GRID.GRID_OFFSET_X, i + self.GRID.GRID_OFFSET_Y, ord(self.GRID.GRID_DEFAULT[i, j]))
                # draw all other chars white
                else:
                    tcod.console_set_default_foreground(window, tcod.white)
                    window.put_char(j + self.GRID.GRID_OFFSET_X, i + self.GRID.GRID_OFFSET_Y, ord(self.GRID.GRID_DEFAULT[i, j]))
                tcod.console_set_default_foreground(window, tcod.white)

        self.PANEL.PANEL_POINTER = [2 + self.PANEL.PANEL_OFFSET_X, 2 + self.PANEL.PANEL_OFFSET_Y]
        self.PANEL.printColoredLine("lvl:", 0, 255, 0, window)
        self.PANEL.printColoredLine("{0}".format(self.GRID.LEVELNAME), 0, 255, 0, window)
        self.PANEL.PANEL_POINTER[1] += 1
        self.PANEL.printColoredLine("PlayerPos: {0},{1}".format(self.GRID.PLAYER.POSITION[1] + 1, self.GRID.PLAYER.POSITION[2] + 1), 0, 255, 0, window)
        self.PANEL.PANEL_POINTER[1] += 1

        if self.GRID.WORLD:
            entities_list = self.GRID.WORLD.ENTITIES
        else:
            entities_list = [self.GRID.PLAYER]
        for i in entities_list:
            if self.GRID.WORLD == False or i.POSITION[0] == self.GRID.WORLD.LEVEL_INDEX:
                tcod.console_set_default_foreground(window, i.color)
                self.GRID.GRID_OBJECT[i.POSITION[2], i.POSITION[1]] = ord(i.symbol)
                window.put_char(i.POSITION[1], i.POSITION[2], ord(i.symbol))
        tcod.console_set_default_foreground(window, tcod.white)
