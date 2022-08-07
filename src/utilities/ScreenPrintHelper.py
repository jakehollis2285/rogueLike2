import tcod
import numpy as np
from utilities import InputHandler as InputHandler

def printBoxBorder(obj, i, j, max_x, max_y):
    '''
        input:
            2d array {obj}
            indecies {i, j}
            and {max_x, max_y} values for the array
        
        output:
            if {i, j} on the edge of the array:
                draw a box edge character based on {i, j}
        
        box style:

            ┌─────────┐
            │         │
            │         │
            │         │
            └─────────┘

        for best results call this function in a for loop iterating over the object array indecies

    '''
    if (i == 0  or i == max_x - 1) :
        obj[i, j] = ord("│")
    if (j == 0  or j == max_y - 1) :
        obj[i, j] = ord("─")
    if (i == 0 and j == 0) :
        obj[i, j] =  ord("┌")
    if (i == max_x - 1 and j == max_y - 1) :
        obj[i, j] = ord("┘")
    if (i == 0 and j == max_y - 1) :
        obj[i, j] = ord("└")
    if (i == max_x - 1 and j == 0) :
        obj[i, j] = ord("┐")

def isEdge(i, j, max_x, max_y):
    if ((i == 0  or j == max_x - 1)
        or (j == 0  or i == max_y - 1)
        or (i == 0 and j == 0)
        or (j == max_x - 1 and i == max_y - 1)
        or (i == 0 and i == max_y - 1)
        or (j == max_x - 1 and j == 0)) :
     return True

def isVisionBlocker(symbol):
    if (symbol == '#'
        or symbol == '╣'
        or symbol == '║'
        or symbol == '╗'
        or symbol == '╝'
        or symbol == '╚'
        or symbol == '╔'
        or symbol == '╩'
        or symbol == '╦'
        or symbol == '╠'
        or symbol == '═'):
     return True

def printTitle(context, message, RENDER_X, RENDER_Y, SCALE) -> None:
    ''' print title screen from globals '''
    window = context.new_console(min_columns=RENDER_X, min_rows=RENDER_Y, order="C", magnification=SCALE)
    pointer = [0, 0]
    for char in list(message):
        if (char == '\n'):
            pointer[0] = 0
            pointer[1] += 1
        elif (char == '\t'):
            pointer[0] += 4
        else:
            window.put_char(pointer[0], pointer[1], ord(char))
            pointer[0] += 1
    return window