Features Overview:

	Dynamic Resolution Scalable Window

	Scalable Tileset -- scroll wheel 
	 	(in window)
		[additional custom tilesets are saved in assets/tilesets/]
	
	Playable Area -- arrow keys
		(called `GRID` in code)
		2D map renderer, Player controller
	
	Terminal Input Window - latin chars, backspace, return
		(called `CONSOLE` in code)
		terminal input adapter
			- line feed
			- history
			- command line interface

	Side Panel Display window
		(called `PANEL` in code)
		2D text render to display in-game info

	Level / World Generator
		(called `WORLD` in code)
		- generate 3 Dimensional world and populate with entities
		- maintain state dynamically across the entire World
			** this is gonna be complicated without major performance hit

	Field of View
		(Managed by `ScreenHandler.py`)
		- print level tiles with color only if they exist in the player vision radius
		- block player vision on walls and other `vision blocker` objects
		- render tiles player has already explored in a darker, generic color
		- only render entities within the player vision radius

Map_Generator:
	
Included are 2 python examples of map generators and some generated maps

These are wrapped using `MapGenerator.py` and are intended to be used to generate maps / levels / worlds for the player to explore.
