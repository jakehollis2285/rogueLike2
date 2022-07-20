#!/usr/bin/env python3
import tcod
import numpy as np
import World as World
import Console as Console
import Grid as Grid
import Panel as Panel
from utilities import InputHandler as InputHandler
from utilities import Logger as Logger
import Globals as Globals

import UnitTest as UnitTest

# world object
WORLD = World.World("WORLD_1")
# screen objects
GRID = Grid.Grid(WORLD) # "world renderer"
CONSOLE = Console.Console() # console renderer
PANEL = Panel.Panel() # info panel renderer
# set max number of chars in console (computed from dimensions of screen objects)
RENDER_X, RENDER_Y = Grid.GRID_X + Panel.PANEL_X, Grid.GRID_Y + Console.CONSOLE_Y

def quit() -> None:
    Logger.debug("User entered exit command... exiting...")
    raise SystemExit()

def printScreen(window) -> None:
    ''' print screen objects '''
    CONSOLE.printConsole(window)
    GRID.draw(window)
    PANEL.printPanel(GRID, window)

def printTitle(context) -> None:
    ''' print title screen from globals '''
    window = context.new_console(min_columns=RENDER_X, min_rows=RENDER_Y, order="C", magnification=2)
    pointer = [0, 0]
    for char in list(Globals.TITLE):
        if (char == '\n'):
            pointer[0] = 0
            pointer[1] += 1
        elif (char == '\t'):
            pointer[0] += 4
        else:
            window.put_char(pointer[0], pointer[1], InputHandler.STRING_TO_TILESET[char])
            pointer[0] += 1
    return window


def runTitleSequence(context, SCALE) -> None:
    ''' print title screen and wait for [return] character input '''
    while True:
        title_window = printTitle(context)
        context.present(title_window, integer_scaling=False)
        for event in tcod.event.wait():
            if isinstance(event, tcod.event.Quit):
                raise SystemExit()
            elif isinstance(event, tcod.event.KeyDown):
                op = InputHandler.handleKeyboardInput(event.sym, CONSOLE, False)
                if(op < 0):
                    quit()
                elif(op == 500):
                    return;

def handleWindowScale(SCALE, event) -> None:
    ''' Use the mouse wheel to change the rendered tile size '''
    MAX_SCALE = 3
    MIN_SCALE = 0.05
    sign = 1
    if (event.y < 0):
        sign = -1
    SCALE += sign * 0.1
    if (SCALE <= MIN_SCALE):
        SCALE = MIN_SCALE
    elif (SCALE >= MAX_SCALE):
        SCALE = MAX_SCALE
    return SCALE

def main() -> None:
    ''' Script entry point '''
    SCALE = 1.5
    with tcod.context.new(  # New window with pixel resolution of width×height, alllow window resizeable, and set the default tileset
        width=Globals.RESOLUTION_X, height=Globals.RESOLUTION_Y, sdl_window_flags=Globals.FLAGS, tileset=Globals.tileset
    ) as context:

        # run title sequence and ignore all events other than the title sequence exit event
        runTitleSequence(context, SCALE)
        for event in tcod.event.wait():
            pass

        # Start Main Loop (frame update)
        while True:
            # rerender screen (dynamic resolution)
            window = context.new_console(min_columns=RENDER_X, min_rows=RENDER_Y, order="C", magnification=SCALE)
            printScreen(window)
            context.present(window, integer_scaling=False)

            # handle events
            for event in tcod.event.wait():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                Logger.debug(event)  # Print event names and attributes.
                if isinstance(event, tcod.event.Quit): # Handle exit event (on window close)
                    quit()
                elif isinstance(event, tcod.event.KeyDown):
                    op = InputHandler.handleKeyboardInput(event.sym, CONSOLE)
                    # handle exit (on user input)
                    if(op < 0):
                        quit()
                    else:
                        # player movement operators
                        if(op > 0 and op < 5):
                            GRID.move(GRID.PLAYER, op)
                elif isinstance(event, tcod.event.MouseWheel):
                    SCALE = handleWindowScale(SCALE, event) # Handle user scroll wheel input to change tileset scale
                elif isinstance(event, tcod.event.WindowResized) and event.type == "WINDOWRESIZED":
                    pass # Ignore resize events, we handle these explicitly on frame update


if __name__ == "__main__":
    if (Globals.RUN_TESTS) :
        UnitTest.main()
    main()