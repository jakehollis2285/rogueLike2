This project is loosely based on the RogueLikeDev community Tutorial written in 2019. Seeing as it is now 2022, and the old tutorial is a bit outdated, I figured I would construct my own example project using the same tools.

reference tutorial here: https://rogueliketutorials.com/tutorials/tcod/2019/

I am utilizing the old tutorial (despite the fact that a 2022 version exists) as I am implementing custom event handling.
	
	For Clarity: I am using the community tutorial as a reference because I am utilizing a similar toolset, design descisions are not dictated by the tutorial under any circumstances

This is a 2D top-down roguelike game built using `Python3` with `numpy` and `tcod` as major plugins

Community contributions are welcomed! Feel free to pull request!
	I am active on reddit u/EmuInteresting8880


Features:

	Dynamic Resolution Scalable Window

	Scalable Tileset -- scroll wheel 
	 	(in window)
		[tileset is cusom currently `terminus.png`]
	
	Playable Area -- arrow keys
		(called `GRID` in code)
		2D map renderer, Player controller
	
	Terminal Input Window - latin chars, backspace, return
		(called `CONSOLE` in code)
		terminal input adapter (line feed, history, command line interface)

	Side Panel Display window
		(called `PANEL` in code)
		2D text render to display info

Map_Generator:
	
	Included are 2 python examples of map generators and some generated maps

	These are not implemented in the game in any way but may be in the future