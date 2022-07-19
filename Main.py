#!/usr/bin/env python3
import tcod
import numpy as np
import Console as Console
import Grid as Grid
import Panel as Panel
import InputHandler as InputHandler

SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720  # Window pixel resolution (when not maximized.)
FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED

GRID = Grid.Grid()
CONSOLE = Console.Console()
PANEL = Panel.Panel()

tileset = tcod.tileset.load_tilesheet(
    "Terminus.png", 16, 16, tcod.tileset.CHARMAP_CP437,
)

RENDERER_WIDTH, RENDERER_HEIGHT = Grid.GRID_X + Panel.PANEL_X, Grid.GRID_Y + Console.CONSOLE_Y

MAX_SCALE = 1.3
MIN_SCALE = 0.8

def printScreen(window) -> None:
    GRID.printGrid(window)
    CONSOLE.printConsole(window)
    PANEL.printPanel(window)

def main() -> None:
    """Script entry point."""
    SCALE = 1.2
    with tcod.context.new(  # New window with pixel resolution of width×height, alllow window resizeable, and set the default tileset
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, sdl_window_flags=FLAGS, tileset=tileset
    ) as context:
        while True: # Main Loop (frame update)
            # rerender screen (dynamic resolution)
            window = context.new_console(min_columns=RENDERER_WIDTH, min_rows=RENDERER_HEIGHT, order="C", magnification=SCALE)
            printScreen(window)
            context.present(window, integer_scaling=False)

            # handle events
            for event in tcod.event.wait():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                print(event)  # Print event names and attributes.
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.KeyDown):
                    if(not InputHandler.handleInput(event.sym, CONSOLE)):
                        raise SystemExit()
                elif isinstance(event, tcod.event.MouseWheel):
                    # Use the mouse wheel to change the rendered tile size.
                    sign = 1
                    if (event.y < 0):
                        sign = -1
                    SCALE += sign * 0.1
                    if (SCALE <= MIN_SCALE):
                        SCALE = MIN_SCALE
                    elif (SCALE >= MAX_SCALE):
                        SCALE = MAX_SCALE
                elif isinstance(event, tcod.event.WindowResized) and event.type == "WINDOWRESIZED":
                    pass  # Ignore resize events, we handle these explicitly on frame update


if __name__ == "__main__":
    main()