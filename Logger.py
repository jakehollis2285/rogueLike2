import Globals as Globals

def debug(message):
	if (Globals.DEBUG_FLAG):
		print("[DEBUG]" + str(message))