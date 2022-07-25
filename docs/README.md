To run the game run the following shell executable:

	`./run.sh`

To run the map generator run the following shell executable:

	`./map_generator {number_of_floors} {generation_type} [filename]`

	number_of_floors --> number of maps to create
	generation_type --> "cave" / "building" / "simple" 
		cave --> generate cave style maps
		building --> generate building style maps using src/assets/map_generator/src/generator.py
		simple --> generate building style maps using src/assets/map_generator/src/generator2.py
	filename (optional) --> filename to load map generation config from (located in src/assets/map_generator/config)

	Created maps will be located in src/assets/map_generator/out/

Check `requirements.txt` to verify that you have the proper python packages installed

This project is loosely based on the RogueLikeDev community Tutorial written in 2019. Seeing as it is now 2022, and the old tutorial is a bit outdated, I figured I would construct my own example project using the same tools.

for more information on this project and my Dev-Log check out: https://www.jacobhollis.link/jrogue.html

for the reference tutorial check out the rogueliketutorials page here: https://rogueliketutorials.com/tutorials/tcod/2019/

I am utilizing the old tutorial (despite the fact that a 2022 version exists) as I am implementing custom event handling and building a framework for roguelike games in general.
	
	For Clarity: I am using the community tutorial as a reference because I am utilizing a similar toolset, design descisions are not dictated by the tutorial under any circumstances

This is a 2D top-down roguelike game built using `Python3` with `numpy` and `tcod` as major plugins

Community contributions are welcomed! Feel free to pull request!
	I am active on reddit u/EmuInteresting8880
