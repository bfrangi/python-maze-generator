import random
from lib import bcolors

MAZE_MAP_DIMENSIONS = (6, 4)
INITIAL_POSITION = (0, 0)
FINAL_POSITION = (0, 1)

maze_map = [# (E, S)
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
    (1, ''), (1, ''), (1, ''), (1, ''), (1, ''), ('', '')
]

position_buffer = [INITIAL_POSITION]

def check_initial_parameters():
    if INITIAL_POSITION[0] >= MAZE_MAP_DIMENSIONS[0] or INITIAL_POSITION[1] >= MAZE_MAP_DIMENSIONS[1]:
        print('Initial position is outside the dimensions of the maze map.')
        exit()
    elif FINAL_POSITION[0] >= MAZE_MAP_DIMENSIONS[0] or FINAL_POSITION[1] >= MAZE_MAP_DIMENSIONS[1]:
        print('Initial position is outside the dimensions of the maze map.')
        exit()
    elif INITIAL_POSITION == FINAL_POSITION:
        print('Final position has to be different from the initial position.')
        exit()
    return True

def maze_map_index_from_coordinates(x, y):
    return MAZE_MAP_DIMENSIONS[0]*y + x

def random_directons():
    return random.shuffle([0, 1, 2, 3])

def advance(curr_x, curr_y):
    directions = random_directons()
    for direction in directions:
        pass

def generate_maze():
    pass

l = bcolors.WARNING+'██'+bcolors.ENDC
def print_maze(maze, wall='██', space='  '):
    width = MAZE_MAP_DIMENSIONS[0]*2 + 1
    height = MAZE_MAP_DIMENSIONS[1]*2 + 1
    for i in range(height):
        if i == 0 or i == height - 1:
            print(wall*width)
        elif i%2 == 0:
            for j in range(width):
                if j%2 == 0:
                    print(wall, end='')
                else:
                    x_idx = j//2
                    y_idx = i//2-1
                    box = maze_map[maze_map_index_from_coordinates(x_idx, y_idx)]
                    if box[1]: ch = wall
                    else: ch = space
                    print(ch, end='')
            print()
        else:
            for j in range(width):
                if j%2 != 0:
                    print(space, end='')
                elif j == 0 or j == width-1:
                    print(wall, end='')
                else:
                    box = maze_map[maze_map_index_from_coordinates(j//2 - 1, i//2)]
                    ch = wall if box[0] else space
                    print(ch, end='')
            print()

def main():
    check_initial_parameters()
    maze = generate_maze()
    print_maze(maze)



if __name__=='__main__':
    main()

EX2 = '''
@@@@@@@@@@@@@
@ @ @ @ @ @ @
@@@@@@@@@@@@@
@ @ @ @ @ @ @
@@@@@@@@@@@@@
@ @ @ @ @ @ @
@@@@@@@@@@@@@
@ @ @ @ @ @ @
@@@@@@@@@@@@@
'''

EX = '''
Γ‾|‾|‾|‾|‾|‾Ꞁ
-------------
| | | | | | |
-------------
| | | | | | |
-------------
L_|_|_|_|_|_⅃
'''
    


