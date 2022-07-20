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

            #=========#
            |         |
            |         |
            |         |
            #=========#

        for best results call this function in a for loop iterating over the object array indecies

    '''
    if (i == 0  or i == max_x - 1) :
        obj[i, j] = InputHandler.STRING_TO_TILESET["|"]
    if (j == 0  or j == max_y - 1) :
        obj[i, j] = InputHandler.STRING_TO_TILESET["="]
    if (i == 0 and j == 0) or (i == max_x - 1 and j == max_y - 1) or (i == 0 and j == max_y - 1) or (i == max_x - 1 and j == 0) :
        obj[i, j] = InputHandler.STRING_TO_TILESET["#"]