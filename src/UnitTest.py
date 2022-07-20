import tcod
from utilities import Logger as Logger
from utilities import InputHandler as InputHandler
import Console as Console
import World as World
import Grid as Grid
import Panel as Panel

import Globals as Globals

# set max number of chars in console (computed from dimensions of screen objects)
RENDER_X, RENDER_Y = Grid.GRID_X + Panel.PANEL_X, Grid.GRID_Y + Console.CONSOLE_Y

WORLD = World.World("Test_World")
EMPTY_GRID = Grid.Grid()
GRID = Grid.Grid(WORLD)
CONSOLE = Console.Console()
PANEL = Panel.Panel()

####################
# LOGGER
####################
def testLogger():
	Globals.LOGGER_FLAGS.info = False
	Globals.LOGGER_FLAGS.debug = False
	Globals.LOGGER_FLAGS.warn = False
	Globals.LOGGER_FLAGS.error = False
	Logger.info("info test")
	Logger.debug("debug test")
	Logger.warn("warn test")
	Logger.error("error test")
	Globals.LOGGER_FLAGS.info = True
	Globals.LOGGER_FLAGS.debug = True
	Globals.LOGGER_FLAGS.warn = True
	Globals.LOGGER_FLAGS.error = True
	Logger.info("Logger Unit Tests Complete")

####################
# GRID
####################
def testGrid():
	RESOLUTION_X, RESOLUTION_Y = 1920, 1080  # Window pixel resolution (when not maximized.)
	FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED # allow window resizing
	SCALE = 1.5
	with tcod.context.new(  # New window with pixel resolution of width×height, alllow window resizeable, and set the default tileset
		width=RESOLUTION_X, height=RESOLUTION_Y, sdl_window_flags=FLAGS, tileset=Globals.tileset
	) as context:
		window = context.new_console(min_columns=RENDER_X, min_rows=RENDER_Y, order="C", magnification=SCALE)
		EMPTY_GRID.draw(window)
		position = list(EMPTY_GRID.PLAYER.POSITION)
		EMPTY_GRID.move(EMPTY_GRID.PLAYER, 1)
		EMPTY_GRID.draw(window)
		if (EMPTY_GRID.PLAYER.POSITION != [position[0], position[1] - 1]):
			Logger.error("case1 failed in UnitTest.testGrid()")
			raise SystemExit()
		EMPTY_GRID.move(EMPTY_GRID.PLAYER, 3)
		EMPTY_GRID.draw(window)
		if (EMPTY_GRID.PLAYER.POSITION != position):
			Logger.error("case2 failed in UnitTest.testGrid()")
			raise SystemExit()
		EMPTY_GRID.move(EMPTY_GRID.PLAYER, 2)
		EMPTY_GRID.draw(window)
		if (EMPTY_GRID.PLAYER.POSITION != [position[0] + 1, position[1]]):
			Logger.error("case3 failed in UnitTest.testGrid()")
			raise SystemExit()
		EMPTY_GRID.move(EMPTY_GRID.PLAYER, 4)
		EMPTY_GRID.draw(window)
		if (EMPTY_GRID.PLAYER.POSITION != position):
			Logger.error("case4 failed in UnitTest.testGrid()")
			raise SystemExit()

		GRID.WORLD.incrementLevelIndex()
		GRID.rerenderGrid()
		GRID.WORLD.decrementLevelIndex()
		GRID.rerenderGrid()
	Logger.info("Grid Unit Tests Complete")

####################
# PANEL
####################
def testPanel():
	RESOLUTION_X, RESOLUTION_Y = 1920, 1080  # Window pixel resolution (when not maximized.)
	FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED # allow window resizing
	SCALE = 1.5
	with tcod.context.new(  # New window with pixel resolution of width×height, alllow window resizeable, and set the default tileset
		width=RESOLUTION_X, height=RESOLUTION_Y, sdl_window_flags=FLAGS, tileset=Globals.tileset
	) as context:
		window = context.new_console(min_columns=RENDER_X, min_rows=RENDER_Y, order="C", magnification=SCALE)
		PANEL.printLine("string", window)
		PANEL.printColoredLine("string", 255, 255, 255, window)
		PANEL.printLevelName(GRID, window)
		PANEL.printPlayerPosition(GRID, window)
		PANEL.printPanel(GRID, window)
	Logger.info("Panel Unit Tests Complete")

####################
# CONSOLE
####################
def testConsole():
	RESOLUTION_X, RESOLUTION_Y = 1920, 1080  # Window pixel resolution (when not maximized.)
	FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED # allow window resizing
	SCALE = 1.5
	with tcod.context.new(  # New window with pixel resolution of width×height, alllow window resizeable, and set the default tileset
		width=RESOLUTION_X, height=RESOLUTION_Y, sdl_window_flags=FLAGS, tileset=Globals.tileset
	) as context:
		window = context.new_console(min_columns=RENDER_X, min_rows=RENDER_Y, order="C", magnification=SCALE)
		# test Console I/O
		CONSOLE.printConsole(window)
		CONSOLE.printLine("this is the line to print", saveToHistory=True)
		CONSOLE.set(InputHandler.STRING_TO_TILESET["q"])
		CONSOLE.newLine()
		CONSOLE.backspace()
		CONSOLE.set(InputHandler.STRING_TO_TILESET["q"])
		CONSOLE.backspace()
		CONSOLE.saveLineToHistory()
		# test Console Commands
		CONSOLE.printHelp()
		CONSOLE.newLine()
		CONSOLE.handleCommand("help")
		# test cases (console has a history, so we can validate the console by checking its history)
		# newLine function saves line to history and increments pointer
		# saveLineToHistory function saves the current line to history
		case1 = CONSOLE.parseCommand(CONSOLE.HISTORY[0])
		case1_expected = "this is the line to print"
		if (case1 != case1_expected):
			Logger.error("case1 failed in UnitTest.testConsole()")
			Logger.error("Input: " + case1)
			Logger.error("Expected: " + case1_expected)
			raise SystemExit()
		case2 = CONSOLE.parseCommand(CONSOLE.HISTORY[1])
		case2_expected = "q"
		if (case2 != "q"):
			Logger.error("case2 failed in UnitTest.testConsole()")
			Logger.error("Input: " + case2)
			Logger.error("Expected: " + case2_expected)
			raise SystemExit()
		case3 = CONSOLE.parseCommand(CONSOLE.HISTORY[2])
		case3_expected = ""
		if (case3 != ""):
			Logger.error("case3 failed in UnitTest.testConsole()")
			Logger.error("Input: " + case3)
			Logger.error("Expected: " + case3_expected)
			raise SystemExit()
		Logger.info("Console Unit Tests Complete")

####################
# MAIN
####################
def main():
	testLogger()
	Globals.LOGGER_FLAGS.debug = False
	testGrid()
	testConsole()
	testPanel()
	Globals.LOGGER_FLAGS.debug = True