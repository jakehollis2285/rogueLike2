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

RENDERER_WIDTH, RENDERER_HEIGHT = Grid.GRID_WIDTH + Panel.PANEL_WIDTH, Grid.GRID_HEIGHT + Console.CONSOLE_HEIGHT

def printScreen(window) -> None:
    GRID.printGrid(window)
    CONSOLE.printConsole(window)
    PANEL.printPanel(window)

def main() -> None:
    """Script entry point."""
    with tcod.context.new(  # New window with pixel resolution of width×height.
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, sdl_window_flags=FLAGS, tileset=tileset
    ) as context:
        while True:
            window = context.new_console(min_columns=RENDERER_WIDTH, min_rows=RENDERER_HEIGHT, order="C")  # Console size based on window resolution and tile size.
            printScreen(window)
            context.present(window, integer_scaling=True)

            for event in tcod.event.wait():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                print(event)  # Print event names and attributes.
                if isinstance(event, tcod.event.Quit):
                    raise SystemExit()
                elif isinstance(event, tcod.event.KeyDown):
                    InputHandler.handleInput(event.sym, window, CONSOLE)
                elif isinstance(event, tcod.event.WindowResized) and event.type == "WINDOWRESIZED":
                    pass  # The next call to context.new_console may return a different size.


if __name__ == "__main__":
    main()