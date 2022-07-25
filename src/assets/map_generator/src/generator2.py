# coding: utf-8

# generator-1.py, a simple python dungeon generator by
# James Spencer <jamessp [at] gmail.com>.

# You should have received a copy of the CC0 legalcode along with this
# work. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.

import random
from datetime import datetime
import sys
import json

CHARACTER_TILES = {'stone': '.',
                   'floor': '.',
                   'wall': '#',
                   'wall_y': '═',
                   'wall_x': '║',
                   'wall_yu': '╩',
                   'wall_yd': '╦',
                   'wall_xr': '╠',
                   'wall_xl': '╣',
                   'wall_corner_ld': '╗',
                   'wall_corner_rd': '╔',
                   'wall_corner_lu': '╝',
                   'wall_corner_ru': '╚',
                   'door': '%',
                   'door_y': '_',
                   'door_x': '|'}


class Generator2():

    def __init__(self, config):
        self.width = config['width']
        self.height = config['height']
        self.max_rooms = config['max_rooms']
        self.min_room_xy = config['min_room_xy']
        self.max_room_xy = config['max_room_xy']
        self.tiles = CHARACTER_TILES
        self.level = []
        self.room_list = []
        self.corridor_list = []
        self.tiles_level = []

    def isWall(self, char):
        if(char == 'wall'):
            return True
        elif(char == 'wall_y'):
            return True
        elif(char == 'wall_x'):
            return True
        elif(char == 'wall_yu'):
            return True
        elif(char == 'wall_yd'):
            return True
        elif(char == 'wall_xr'):
            return True
        elif(char == 'wall_xl'):
            return True
        elif(char == 'wall_corner_ld'):
            return True
        elif(char == 'wall_corner_rd'):
            return True
        elif(char == 'wall_corner_lu'):
            return True
        elif(char == 'wall_corner_ru'):
            return True
        else:
            return False

    def gen_door_location(self, w, h, x, y):
        d_x, d_y = 0, 0

        if (random.randint(0, 1)):
            if (random.randint(0, 1)):
                door_x = x - 1
            else:
                door_x = x + w
            rand_y = random.randint(y, y + h - 2)
            while(True):
                rand_y = random.randint(y, y + h - 2)
                if(not rand_y <= y and not rand_y >= y + h - 2):
                    break;
            d_x = door_x
            d_y = rand_y
        else:
            if (random.randint(0, 1)):
                door_y = y - 1
            else:
                door_y = y + h
            rand_x = random.randint(x, x + w - 2)
            while(True):
                rand_x = random.randint(x, x + w - 2)
                if(not rand_x <= x and not rand_x >= x + w - 2):
                    break;
            d_x = rand_x
            d_y = door_y

        return d_x, d_y

    def gen_room(self):
        x, y, w, h, d_x, d_y = 0, 0, 0, 0, 0, 0

        random.seed(datetime.now())
        # random.seed(datetime.now())

        w = random.randint(self.min_room_xy, self.max_room_xy)
        h = random.randint(self.min_room_xy, self.max_room_xy)
        x = random.randint(2, (self.width - w - 2))
        y = random.randint(2, (self.height - h - 2))

        d_x, d_y = self.gen_door_location(w, h, x, y)

        return [x, y, w, h, d_x, d_y]

    def room_overlapping(self, room, room_list):
        x = room[0]
        y = room[1]
        w = room[2]
        h = room[3]
        d_x = room[4]
        d_y = room[5]

        for current_room in room_list:

            # The rectangles overlap if either
            # the x coordinate or the y coordinate
            # of either door is the same
            if(d_x == current_room[4]):
                return True
            if(d_y == current_room[5]):
                return True
            # The rectangles don't overlap if
            # one rectangle's minimum in some dimension
            # is greater than the other's maximum in
            # that dimension.
            if (x < (current_room[0] + current_room[2]) and
                current_room[0] < (x + w) and
                y < (current_room[1] + current_room[3]) and
                current_room[1] < (y + h)):

                return True

        return False

    def gen_level(self):

        # build an empty dungeon, blank the room and corridor lists
        for i in range(self.height):
            self.level.append(['stone'] * self.width)
        self.room_list = []
        self.corridor_list = []

        max_iters = self.max_rooms * 10

        for a in range(max_iters):
            tmp_room = self.gen_room()

            if not self.room_list:
                self.room_list.append(tmp_room)
            else:
                tmp_room = self.gen_room()
                tmp_room_list = self.room_list[:]

                if self.room_overlapping(tmp_room, tmp_room_list) is False:
                    self.room_list.append(tmp_room)

            if len(self.room_list) >= self.max_rooms:
                break

        # make sure 2 rooms do not have adjacent doors
        for room_num1, room1 in enumerate(self.room_list):
            for room_num2, room2 in enumerate(self.room_list):
                if(room1[5] == room2[5] - 1):
                    room1[4], room1[5] = self.gen_door_location(room1[2], room1[3], room1[0], room1[1])
                elif(room1[5] == room2[5] + 1):
                    room1[4], room1[5] = self.gen_door_location(room1[2], room1[3], room1[0], room1[1])
                elif(room1[4] == room2[4] - 1):
                    room1[4], room1[5] = self.gen_door_location(room1[2], room1[3], room1[0], room1[1])
                elif(room1[4] == room2[4] + 1):
                    room1[4], room1[5] = self.gen_door_location(room1[2], room1[3], room1[0], room1[1])

        # paint rooms
        for room_num, room in enumerate(self.room_list):
            for b in range(room[2]):
                for c in range(room[3]):
                    self.level[room[1] + c][room[0] + b] = 'floor'
            # draw doors
            self.level[room[5]][room[4]] = 'door'


        # paint the walls
        for row in range(1, self.height - 1):
            for col in range(1, self.width - 1):
                if self.level[row][col] == 'floor':
                    if self.level[row - 1][col] == 'stone':
                        self.level[row - 1][col] = 'wall_y'
                    if self.level[row][col - 1] == 'stone':
                        self.level[row][col - 1] = 'wall_x'
                    if self.level[row][col + 1] == 'stone':
                        self.level[row][col + 1] = 'wall_x'
                    if self.level[row + 1][col] == 'stone':
                        self.level[row + 1][col] = 'wall_y'

        # repaint walls fixing disconnections
        # paint the walls
        for row in range(1, self.height - 1):
            for col in range(1, self.width - 1):
                if self.level[row][col] == 'wall_y':
                    if self.level[row + 1][col] == 'wall_x':
                        self.level[row][col] = 'wall_yd'
                    elif self.level[row - 1][col] == 'wall_x':
                        self.level[row][col] = 'wall_yu'

                if self.level[row][col] == 'wall_x':
                    if self.level[row][col + 1] == 'wall_y':
                        self.level[row][col] = 'wall_xr'
                    elif self.level[row][col - 1] == 'wall_y':
                        self.level[row][col] = 'wall_xl'


        # paint corners
        for row in range(1, self.height - 1):
            for col in range(1, self.width - 1):
                if self.level[row][col] == 'stone':
                    if self.level[row][col - 1] == 'wall_y' and (self.level[row + 1][col] == 'wall_x' or self.level[row + 1][col] == 'wall_xl' or self.level[row + 1][col] == 'wall_xr'):
                        self.level[row][col] = 'wall_corner_ld'
                    if self.level[row][col + 1] == 'wall_y' and (self.level[row + 1][col] == 'wall_x' or self.level[row + 1][col] == 'wall_xl' or self.level[row + 1][col] == 'wall_xr'):
                        self.level[row][col] = 'wall_corner_rd'

                    if self.level[row][col - 1] == 'wall_y' and (self.level[row - 1][col] == 'wall_x' or self.level[row + 1][col] == 'wall_yd' or self.level[row + 1][col] == 'wall_yu'):
                        self.level[row][col] = 'wall_corner_lu'
                    if self.level[row][col + 1] == 'wall_y' and (self.level[row - 1][col] == 'wall_x' or self.level[row + 1][col] == 'wall_yd' or self.level[row + 1][col] == 'wall_yu'):
                        self.level[row][col] = 'wall_corner_ru'

                    if self.level[row][col + 1] == 'wall_y' and self.level[row][col - 1] == 'wall_y' and self.level[row + 1][col] == 'wall_x':
                        self.level[row][col] = 'wall_yd'
                    if self.level[row][col + 1] == 'wall_y' and self.level[row][col - 1] == 'wall_y' and self.level[row - 1][col] == 'wall_x':
                        self.level[row][col] = 'wall_yu'

                    if self.level[row + 1][col] == 'wall_x' and self.level[row - 1][col] == 'wall_x' and self.level[row][col + 1] == 'wall_y':
                        self.level[row][col] = 'wall_xr'
                    if self.level[row + 1][col] == 'wall_x' and self.level[row - 1][col] == 'wall_x' and self.level[row][col - 1] == 'wall_y':
                        self.level[row][col] = 'wall_xl'


        # remove floating doors
        for room_num, room in enumerate(self.room_list):
            # remove doors that have floor on 3 sides
            floor_count = 0
            if(self.level[room[5] + 1][room[4]] == 'floor'):
                floor_count += 1
            if(self.level[room[5] - 1][room[4]] == 'floor'):
                floor_count += 1
            if(self.level[room[5]][room[4] + 1] == 'floor'):
                floor_count += 1
            if(self.level[room[5]][room[4] - 1] == 'floor'):
                floor_count += 1
            if(floor_count > 2):
                self.level[room[5]][room[4]] = 'floor'

            wall_count = 0
            if(self.isWall(self.level[room[5] + 1][room[4]])):
                wall_count += 1
            if(self.isWall(self.level[room[5] - 1][room[4]])):
                wall_count += 1
            if(self.isWall(self.level[room[5]][room[4] + 1])):
                wall_count += 1
            if(self.isWall(self.level[room[5]][room[4] - 1])):
                wall_count += 1
            if(wall_count > 2):
                self.level[room[5]][room[4]] = 'floor'

    def gen_tiles_level(self):

        for row_num, row in enumerate(self.level):
            tmp_tiles = []

            for col_num, col in enumerate(row):
                if col == 'stone':
                    tmp_tiles.append(self.tiles['stone'])
                if col == 'floor':
                    tmp_tiles.append(self.tiles['floor'])
                if col == 'wall':
                    tmp_tiles.append(self.tiles['wall'])
                if col == 'wall_x':
                    tmp_tiles.append(self.tiles['wall_x'])
                if col == 'wall_y':
                    tmp_tiles.append(self.tiles['wall_y'])
                if col == 'wall_yd':
                    tmp_tiles.append(self.tiles['wall_yd'])
                if col == 'wall_yu':
                    tmp_tiles.append(self.tiles['wall_yu'])
                if col == 'wall_xr':
                    tmp_tiles.append(self.tiles['wall_xr'])
                if col == 'wall_xl':
                    tmp_tiles.append(self.tiles['wall_xl'])
                if col == 'wall_corner_rd':
                    tmp_tiles.append(self.tiles['wall_corner_rd'])
                if col == 'wall_corner_ru':
                    tmp_tiles.append(self.tiles['wall_corner_ru'])
                if col == 'wall_corner_ld':
                    tmp_tiles.append(self.tiles['wall_corner_ld'])
                if col == 'wall_corner_lu':
                    tmp_tiles.append(self.tiles['wall_corner_lu'])
                if col == 'door':
                    tmp_tiles.append(self.tiles['door'])

            self.tiles_level.append(''.join(tmp_tiles))

        print('Room List: ', self.room_list)
        print('\nCorridor List: ', self.corridor_list)

def show(gen):
    for row in gen.tiles_level:
        print (row)

def printToFile(gen, out_file):
    with open('assets/map_generator/out/' + out_file, 'w') as f:
        for row in gen.tiles_level:
            print (row, file=f)

def entrypoint(filename, out_file):
    config = {}

    if(len(filename) != None):
        print("loading config from file: " + str(filename))
        file = open(filename)
        config = json.loads(file.read())
        

    if('width'and 'height'and 'max_rooms'and 'min_room_xy'and'max_room_xy'and 'rooms_overlap'and 'random_connections'and'random_spurs' and 'connected') not in config:
        print("failed to load config from file, check command line arguments")
        quit()

    # config = {
    #     'width':180, 
    #     'height':50, 
    #     'max_rooms':8, 
    #     'min_room_xy':5,
    #     'max_room_xy':25, 
    #     'rooms_overlap':False, 
    #     'random_connections':2,
    #     'random_spurs':0
    # }

    gen = Generator2(config)
    gen.gen_level()
    gen.gen_tiles_level()
    show(gen)
    printToFile(gen, out_file)

    return gen.tiles_level

if __name__ == '__main__':
    entrypoint(sys.argv[1])
