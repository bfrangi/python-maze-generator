import random
from lib import bcolors

MAZE_MAP_DIMENSIONS = (6, 4)
INITIAL_POSITION = (0, 0)
FINAL_POSITION = (0, 1)

maze_map = [# (E, S)
    (1, 1), (1, 1), (1, 0), (1, 1), (1, 1), ('', 1), 
    (1, 0), (1, 1), (1, 0), (1, 1), (1, 1), ('', 1), 
    (1, 1), (1, 1), (1, 0), (1, 1), (1, 1), ('', 0), 
    (1, ''), (1, ''), (1, ''), (1, ''), (0, ''), ('', '')
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

def maze_to_string(maze, wall='██', space='  ', color_walls='', color_spaces='', highlighted_cells=[], highlight_color=bcolors.FAIL):
    
    # CONFIG
    # Set colors
    wall = color_walls + wall + bcolors.ENDC
    space = color_spaces + space + bcolors.ENDC
    # Get size of the printed maze
    width = MAZE_MAP_DIMENSIONS[0]*2 + 1
    height = MAZE_MAP_DIMENSIONS[1]*2 + 1
    # Initialize string maze
    maze_str = ''

    # CONVERT MAZE TO STRING
    # 1. Iterate over the rows
    for i in range(height):
        # 1.1 Handle first and last rows
        if i == 0 or i == height - 1:
            maze_str += wall*width + '\n'
        # 1.2 Handle even index rows (rows with no cells)
        elif i%2 == 0:
            # 1.2.1 Iterate over the columns
            for j in range(width):
                # 1.2.1.1 Handle the even columns - wall intersections are always walls
                if j%2 == 0:
                    maze_str += wall
                # 1.2.1.2 Handle odd columns - may be open or closed
                else:
                    x_idx = j//2
                    y_idx = i//2-1
                    box = maze[maze_map_index_from_coordinates(x_idx, y_idx)]
                    if box[1]: 
                        ch = wall
                    else: 
                        ch = space
                        # If the wall is open and surrounding cells are highlighted,
                        # highlight the space also
                        if (
                            (x_idx, y_idx) in highlighted_cells
                            and 
                            (x_idx, y_idx + 1) in highlighted_cells
                            ):
                            ch = highlight_color + space + bcolors.ENDC
                    maze_str += ch
            maze_str += '\n'
        # 1.3 Handle odd index rows (rows with cells)
        else:
            for j in range(width):
                if j%2 != 0:
                    ch = space
                    x_idx = j//2
                    y_idx = i//2                    
                    print((x_idx, y_idx),  highlighted_cells)
                    if (x_idx, y_idx) in highlighted_cells:
                        ch = highlight_color + ch + bcolors.ENDC
                    maze_str += ch
                elif j == 0 or j == width-1:
                    maze_str += wall
                else:
                    x_idx = j//2-1
                    y_idx = i//2
                    box = maze[maze_map_index_from_coordinates(x_idx, y_idx)]
                    if box[0]:
                        ch = wall
                    else:
                        ch = space
                        # If the wall is open and surrounding cells are highlighted,
                        # highlight the space also
                        if (
                            (x_idx, y_idx) in highlighted_cells
                            and 
                            (x_idx + 1, y_idx) in highlighted_cells
                            ):
                            ch = highlight_color + space + bcolors.ENDC
                    maze_str += ch
            maze_str += '\n'
    return maze_str

def main():
    check_initial_parameters()
    maze = generate_maze()
    print(maze_to_string(
        maze_map, 
        space='██', 
        color_walls=bcolors.OKBLUE, 
        highlighted_cells=[(0, 0),(0, 1),(0, 2),(5, 3),(2, 1),(2, 3),(2, 2),(5, 2),(4, 3),]
        ))



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
    


