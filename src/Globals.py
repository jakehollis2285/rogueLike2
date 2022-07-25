import tcod
import World as World
import Console as Console
import Grid as Grid
import Panel as Panel
import ScreenHandler as ScreenHandler

TITLE = """

      ## ########   #######   ######   ##     ## ########  #######  
      ## ##     ## ##     ## ##    ##  ##     ## ##       ##     ## 
      ## ##     ## ##     ## ##        ##     ## ##              ## 
      ## ########  ##     ## ##   #### ##     ## ######    #######  
##    ## ##   ##   ##     ## ##    ##  ##     ## ##       ##        
##    ## ##    ##  ##     ## ##    ##  ##     ## ##       ##        
 ######  ##     ##  #######   ######    #######  ######## ######### 


welcome to the jrogue demo

press [enter/return] to start the game...

      or

press [esc] to exit the game...

"""                                                                         
	                                                                         
RUN_TESTS = True

class LOGGER_FLAGS:
      info = True
      debug = True
      warn = True
      error = True

RESOLUTION_X, RESOLUTION_Y = 1920, 1080  # Window pixel resolution (when not maximized.)
FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED # allow window resizing

# load tileset
# tileset = tcod.tileset.load_tilesheet(
#     "assets/tilesets/Hack_square_64x64.png", 16, 16, tcod.tileset.CHARMAP_CP437,
# ) 
tileset = tcod.tileset.load_tilesheet(
    "assets/tilesets/Bisasam_20x20.png", 16, 16, tcod.tileset.CHARMAP_CP437,
)
# tileset = tcod.tileset.load_tilesheet(
#     "assets/tilesets/Gold_plated_16x16_v2.png", 16, 16, tcod.tileset.CHARMAP_CP437,
# )
# tileset = tcod.tileset.load_tilesheet(
#     "assets/tilesets/Terminus.png", 16, 16, tcod.tileset.CHARMAP_CP437,
# )

tcod.tileset.set_default(tileset)                                                              

# world object
WORLD = World.World("WORLD_1")
# screen objects
# GRID = Grid.Grid() # screen renderer
CONSOLE = Console.Console() # console renderer
GRID = Grid.Grid(WORLD) # "world renderer"
PANEL = Panel.Panel() # info panel renderer
SCREEN_HANDLER =  ScreenHandler.ScreenHandler(CONSOLE, GRID, PANEL)
