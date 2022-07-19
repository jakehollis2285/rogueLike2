#!/usr/bin/env python3
import tcod
import numpy as np
import Console as Console
import Grid as Grid
import Panel as Panel
import InputHandler as InputHandler
import Globals as Globals
import Logger as Logger

RESOLUTION_X, RESOLUTION_Y = 1920, 1080  # Window pixel resolution (when not maximized.)
FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED # allow window resizing

# screen objects
GRID = Grid.Grid()
CONSOLE = Console.Console()
PANEL = Panel.Panel()

# load tileset
tileset = tcod.tileset.load_tilesheet(
    "Terminus.png", 16, 16, tcod.tileset.CHARMAP_CP437,
)

# set max number of chars in console (computed from dimensions of screen objects)
RENDER_X, RENDER_Y = Grid.GRID_X + Panel.PANEL_X, Grid.GRID_Y + Console.CONSOLE_Y

MAX_SCALE = 2
MIN_SCALE = 1

def printScreen(window) -> None:
    ''' print screen objects '''
    CONSOLE.printConsole(window)
    GRID.printGrid(window)
    PANEL.printPanel(window, GRID)

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
                if(op == 500):
                    return;

def handleWindowScale(SCALE, event) -> None:
    ''' Use the mouse wheel to change the rendered tile size '''
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
        width=RESOLUTION_X, height=RESOLUTION_Y, sdl_window_flags=FLAGS, tileset=tileset
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
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.KeyDown):
                    op = InputHandler.handleKeyboardInput(event.sym, CONSOLE)
                    # handle exit
                    if(op < 0):
                        raise SystemExit()
                    else:
                        # player movement operators
                        if(op > 0 and op < 5):
                            GRID.movePlayer(op)
                elif isinstance(event, tcod.event.MouseWheel):
                    SCALE = handleWindowScale(SCALE, event)
                elif isinstance(event, tcod.event.WindowResized) and event.type == "WINDOWRESIZED":
                    pass  # Ignore resize events, we handle these explicitly on frame update


if __name__ == "__main__":
    main()