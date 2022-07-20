import tcod

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
	                                                                         
class LOGGER_FLAGS:
      info = True
      debug = True
      warn = True
      error = True

RESOLUTION_X, RESOLUTION_Y = 1920, 1080  # Window pixel resolution (when not maximized.)
FLAGS = tcod.context.SDL_WINDOW_RESIZABLE | tcod.context.SDL_WINDOW_MAXIMIZED # allow window resizing

# load tileset
tileset = tcod.tileset.load_tilesheet(
    "Terminus.png", 16, 16, tcod.tileset.CHARMAP_CP437,
)

MAX_SCALE = 2
MIN_SCALE = 1                                                                
