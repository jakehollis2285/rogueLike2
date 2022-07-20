import sys

import assets.map_generator.src.generator as generator
import assets.map_generator.src.generator2 as simple
import assets.map_generator.src.cavegen as cavegen

def bottomUpGeneration(underground_floors, cave_config, building_config):
	'''
		generate x `underground_floors` using cave generation

		genrate 1 aboveground floor using building generation

		return list containing:
			lists of string rows in each map
		[[map1_row1, map1_row2, ...], ..., [mapN_row1, ...]]
	'''
	floors = []

	for i in range(int(underground_floors)):
		if (cave_config == None):
			f = cavegen.entrypoint("assets/map_generator/" + "config/cave/default.json", "out_" + str(i) + ".txt")
		else:
			f = cavegen.entrypoint("assets/map_generator/" + cave_config, "out_" + str(i) + ".txt")

		floors.append(f)

	if (building_config == None):
		f = simple.entrypoint("assets/map_generator/" + "config/building/default.json", "out_" + str(int(underground_floors)) + ".txt")
		floors.append(f)
	else:
		f = simple.entrypoint("assets/map_generator/" + building_config, "out_" + str(i) + ".txt")
		floors.append(f)

	return floors

def standard(number_of_floors, generation_type, filename):
	'''
		generate x 'floors' using generation type and config from filename

		return list containing:
			lists of string rows in each map
		[[map1_row1, map1_row2, ...], ..., [mapN_row1, ...]]
	'''

	floors = []
	for i in range(int(number_of_floors)):
		if (generation_type == "cave"):
			if (filename == None):
				f = cavegen.entrypoint("assets/map_generator/" + "config/cave/default.json", "out_" + str(i) + ".txt")
			else:
				f = cavegen.entrypoint("assets/map_generator/" + filename, "out_" + str(i) + ".txt")
		elif (generation_type == "complex"):
			if (filename == None):
				f = generator.entrypoint("assets/map_generator/" + "config/building/default.json", "out_" + str(i) + ".txt")
			else:
				f = generator.entrypoint("assets/map_generator/" + filename, "out_" + str(i) + ".txt")
		elif (generation_type == "simple"):
			if (filename == None):
				f = simple.entrypoint("assets/map_generator/" + "config/building/default.json", "out_" + str(i) + ".txt")
			else:
				f = simple.entrypoint("assets/map_generator/" + filename, "out_" + str(i) + ".txt")
		floors.append(f)
	return floors


def main(args):
	print(args)
	if(args[1] == 'bottomUp'):
		# required arguments
		if (len(args) > 2):
			number_of_floors = args[2]
		cave_config = None
		if (len(args) > 3):
			cave_config = args[3]
		building_config = None
		if (len(args) > 4):
			building_config = args[4]
		bottomUpGeneration(number_of_floors, cave_config, building_config)
	elif(args[1] == 'standard'):
		# required arguments
		if (len(args) > 3):
			number_of_floors = args[2]
			generation_type = args[3]
		# optional arguments
		filename = None
		if (len(args) > 4):
			filename = args[4]
		standard(number_of_floors, generation_type, filename)
	

if __name__ == '__main__':
	main(sys.argv)
