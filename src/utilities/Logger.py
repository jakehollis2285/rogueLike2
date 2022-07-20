from utilities.ANSIColors import Colors as ac

import Globals as Globals

def info(message):
	if (Globals.LOGGER_FLAGS.info):
		msg = "[INFO] " + str(message)
		print(ac.green.format(msg))

def debug(message):
	if (Globals.LOGGER_FLAGS.debug):
		msg = "[DEBUG] " + str(message)
		print(msg)

def warn(message):
	if (Globals.LOGGER_FLAGS.warn):
		msg = "[WARN] " + str(message)
		print(ac.orange.format(msg))

def error(message):
	if (Globals.LOGGER_FLAGS.error):
		msg = "[ERROR] " + str(message)
		print(ac.red.format(msg))