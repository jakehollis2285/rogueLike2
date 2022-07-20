HOW-TO:
	use `./run.sh` to execute the map generator

`./run.sh` `cave / building` `[optional]config_filename`

argv[1] == `cave` or `building`  		# determines the generator to run
argv[2] == `[optional]config_filename`  # determines the generator config file to load

generated files are saved to out.txt

FILE-STRUCTURE:
	
	Main.py
		script entrypoint

	generator.py
		square room map generator

	cavegen.py
		cave map generator

	config/
		storage location for generator config files

	config/building/
		building config files

	config/cave/
		cave config files

	maps/
		storage location for map files