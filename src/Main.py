#!/usr/bin/env python3
import tcod
import Globals as Globals
from utilities import ScreenPrintHelper as sph
from utilities import InputHandler as InputHandler
from utilities import Logger as Logger

# import UnitTest as UnitTest

def quit() -> None:
    Logger.debug("User entered exit command... exiting...")
    raise SystemExit()

def runTitleSequence(context, SCALE) -> None:
    ''' print title screen and wait for [return] character input '''
    while True:
        title_window = sph.printTitle(context, Globals.TITLE, Globals.SCREEN_HANDLER.RENDER_X, Globals.SCREEN_HANDLER.RENDER_Y, SCALE)
        context.present(title_window, integer_scaling=False)
        for event in tcod.event.wait():
            if isinstance(event, tcod.event.Quit):
                raise SystemExit()
            elif isinstance(event, tcod.event.KeyDown):
                op = InputHandler.handleKeyboardInput(event, Globals.CONSOLE, False)
                # handle title sequence exit
                if (op == 50000):
                    return

def handleWindowScale(SCALE, event) -> None:
    ''' Use the mouse wheel to change the rendered tile size '''
    MAX_SCALE = 3
    MIN_SCALE = 0.5
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
            window = context.new_console(min_columns=Globals.SCREEN_HANDLER.RENDER_X, min_rows=Globals.SCREEN_HANDLER.RENDER_Y, order="C", magnification=SCALE)
            Globals.SCREEN_HANDLER.printScreen(window)
            context.present(window, integer_scaling=False)

            # handle events
            for event in tcod.event.wait():
                context.convert_event(event)  # Sets tile coordinates for mouse events.
                Logger.debug(event)  # Print event names and attributes.
                if isinstance(event, tcod.event.Quit): # Handle exit event (on window close)
                    quit()
                elif isinstance(event, tcod.event.KeyDown):
                    InputHandler.handleKeyboardInput(event, Globals.CONSOLE)
                elif isinstance(event, tcod.event.MouseWheel):
                    SCALE = handleWindowScale(SCALE, event) # Handle user scroll wheel input to change tileset scale
                elif isinstance(event, tcod.event.WindowResized) and event.type == "WINDOWRESIZED":
                    pass # Ignore resize events, we handle these explicitly on frame update


if __name__ == "__main__":
    # if (Globals.RUN_TESTS) :
        # UnitTest.main()
    main()