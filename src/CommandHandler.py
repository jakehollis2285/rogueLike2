from utilities import InputHandler as InputHandler
from utilities import Logger as Logger
import Globals as Globals

def parseCommand(chars):
    ''' 
        given an array of character return a string command 
        strings returned are in the form "arg1 arg2 arg3 ... argN"
        where arguments are allowed 1 space in between

        '|' and '_' characters are ignored
        2 spaces terminates the string
    '''
    command = ""
    for i in range(len(chars)):
        if (chars[i] == ord(" ")) and (chars[i + 1] == ord(" ")):
            break;
        if (chars[i] != ord("│") and chars[i] != ord("_")):
            command += InputHandler.TILESET_TO_STRING[chars[i]]
    if (command != ""):
        while True:
            if(len(command) > 0 and command[-1] == " "):
                command = command[:len(command) - 1]
            else:
                break;
    command = command.lower()
    return command

def handleCommand(command):
    ''' command interfaces 
        (given string command call relevant function) 

        commands are in the following form:
            `command arg1 arg2 ... argN`
    '''
    command_array = []
    if(' ' in command):
        command_array = command.split()
    else:
        command_array = [command]
    Logger.debug(command_array)
    if (command_array[0] == "help"):
        return helpCommand()
    elif (command_array[0] == "dig"):
        if(len(command_array) == 2):
            return digCommand(command_array[1])
        else: 
            return ["wrong number of args"]

def helpCommand():
    ''' return help command message to console'''
    return ["[commands]",
    "    help    print this message"]

def digCommand(direction):
    ''' return dig command message to console'''
    if (direction == "up"):
        pos_y = Globals.GRID.PLAYER.POSITION[2] - 1
        pos_x = Globals.GRID.PLAYER.POSITION[1]
        Globals.GRID.set(pos_y, pos_x, ".")
        return ["stone removed at x:{},y:{}".format(pos_x, pos_y)]
    elif (direction == "right"):
        pos_y = Globals.GRID.PLAYER.POSITION[2]
        pos_x = Globals.GRID.PLAYER.POSITION[1] + 1
        Globals.GRID.set(pos_y, pos_x, ".")
        return ["stone removed at x:{},y:{}".format(pos_x, pos_y)]
    elif (direction == "down"):
        pos_y = Globals.GRID.PLAYER.POSITION[2] + 1
        pos_x = Globals.GRID.PLAYER.POSITION[1]
        Globals.GRID.set(pos_y, pos_x, ".")
        return ["stone removed at x:{},y:{}".format(pos_x, pos_y)]
    elif (direction == "left"):
        pos_y = Globals.GRID.PLAYER.POSITION[2]
        pos_x = Globals.GRID.PLAYER.POSITION[1] - 1
        Globals.GRID.set(pos_y, pos_x, ".")
        return ["stone removed at x:{},y:{}".format(pos_x, pos_y)]
